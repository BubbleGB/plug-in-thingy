import importlib.util
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock
import warnings
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / 'tools' / 'build.py'
spec = importlib.util.spec_from_file_location('plugin_build', SCRIPT)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / 'plugin'
        self.skill = self.root / 'skills' / 'sample'
        self.skill.mkdir(parents=True)
        self.manifest = {'name': 'sample-plugin', 'version': '0.1.0', 'description': 'Example skill plugin', 'license': 'MIT'}
        self.write_manifest()
        (self.root / 'LICENSE').write_text('MIT License\nExample copyright\n')
        self.body('Follow the task.\n')

    def write_manifest(self):
        (self.root / 'plugin.json').write_text(json.dumps(self.manifest))

    def body(self, text):
        (self.skill / 'SKILL.md').write_text('---\nname: sample\ndescription: Use when testing the package.\n---\n\n' + text)

    def test_valid_minimal_package(self):
        self.assertEqual(build.validate_package(self.root), [])

    def test_rejects_manifest_hooks(self):
        self.manifest['hooks'] = './hooks/hooks.json'
        self.write_manifest()
        self.assertTrue(any('hooks' in e for e in build.validate_package(self.root)))

    def test_rejects_nested_plugin_and_marketplace(self):
        (self.skill / 'plugin.json').write_text('{}')
        self.assertTrue(any('manifest' in e for e in build.validate_package(self.root)))
        (self.skill / 'marketplace.json').write_text('{}')
        self.assertTrue(any('marketplace' in e for e in build.validate_package(self.root)))

    def test_detects_frontmatter_mismatch(self):
        (self.skill / 'SKILL.md').write_text('---\nname: other\ndescription: Hello\n---\nBody\n')
        self.assertTrue(any('name' in e for e in build.validate_package(self.root)))

    def test_missing_reference_is_rejected(self):
        self.body('Read [checks](references/checks.md).\n')
        self.assertTrue(any('missing' in e for e in build.validate_package(self.root)))

    def test_reference_must_stay_in_skill_package(self):
        (self.root / 'check.md').write_text('# Check\n')
        self.body('Read [checks](../../check.md).\n')
        self.assertTrue(any('escapes skill' in e for e in build.validate_package(self.root)))

    def test_checks_nested_reference_and_anchor(self):
        refs = self.skill / 'references'
        refs.mkdir()
        (refs / 'check.md').write_text('# Checks\n\nSee [absent](missing.md).\n')
        self.body('Read [checks](references/check.md#nonexistent).\n')
        errors = build.validate_package(self.root)
        self.assertTrue(any('anchor' in e for e in errors))
        self.assertTrue(any('missing' in e for e in errors))

    def test_code_example_links_are_not_dependencies(self):
        self.body('```md\n[Example](does-not-exist.md)\n```\n')
        self.assertEqual(build.validate_package(self.root), [])

    def test_symlink_is_rejected(self):
        (self.skill / 'escape.md').symlink_to(self.base / 'outside.md')
        self.assertTrue(any('symlink' in e for e in build.validate_package(self.root)))

    def test_overlay_identity_must_match(self):
        overlay = self.root / '.codex-plugin'
        overlay.mkdir()
        (overlay / 'plugin.json').write_text(json.dumps({**self.manifest, 'version': '9.0.0', 'skills': './skills/'}))
        self.assertTrue(any('version' in e for e in build.validate_package(self.root)))

    def test_overlay_subtitle_limit(self):
        overlay = self.root / '.codex-plugin'
        overlay.mkdir()
        for subtitle, valid in [('A' * 30, True), ('A' * 31, False), (' ', False), ([], False)]:
            with self.subTest(subtitle=subtitle):
                (overlay / 'plugin.json').write_text(json.dumps({
                    **self.manifest, 'skills': './skills/',
                    'interface': {'shortDescription': subtitle},
                }))
                errors = build.validate_package(self.root)
                self.assertEqual(not errors, valid, errors)

    def test_deterministic_rootless_archive(self):
        a, b = self.base / 'a.zip', self.base / 'b.zip'
        self.assertEqual(build.write_archive(self.root, a), build.write_archive(self.root, b))
        with zipfile.ZipFile(a) as z:
            self.assertIn('plugin.json', z.namelist())
            self.assertIn('skills/sample/SKILL.md', z.namelist())
        self.assertEqual(build.validate_archive(a), [])

    def test_bad_build_does_not_replace_previous_archive(self):
        out = self.base / 'good.zip'
        build.write_archive(self.root, out)
        previous = out.read_bytes()
        self.body('Read [missing](references/no.md).\n')
        with self.assertRaises(ValueError):
            build.write_archive(self.root, out)
        self.assertEqual(out.read_bytes(), previous)

    def test_archive_traversal_and_duplicates_rejected(self):
        out = self.base / 'bad.zip'
        with zipfile.ZipFile(out, 'w') as z:
            z.writestr('../outside', 'bad')
        self.assertTrue(any('unsafe' in e for e in build.validate_archive(out)))
        with zipfile.ZipFile(out, 'w') as z:
            z.writestr('plugin.json', '{}')
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                z.writestr('plugin.json', '{}')
        self.assertTrue(any('duplicate' in e for e in build.validate_archive(out)))

    def test_archive_symlink_rejected(self):
        out = self.base / 'link.zip'
        with zipfile.ZipFile(out, 'w') as z:
            i = zipfile.ZipInfo('link')
            i.create_system = 3
            i.external_attr = 0o120777 << 16
            z.writestr(i, '../outside')
        self.assertTrue(any('symlink' in e for e in build.validate_archive(out)))

    def test_rejects_noncanonical_archive_paths_before_extraction(self):
        for alias in ('./plugin.json', 'skills//sample/SKILL.md'):
            with self.subTest(alias=alias):
                out = self.base / 'alias.zip'
                with zipfile.ZipFile(out, 'w') as z:
                    for file in self.root.rglob('*'):
                        if file.is_file():
                            z.write(file, file.relative_to(self.root).as_posix())
                    z.writestr(alias, (self.root / 'plugin.json').read_text())
                self.assertTrue(any('noncanonical' in e for e in build.validate_archive(out)))

    def test_invalid_yaml_description_does_not_replace_good_artifact(self):
        output = self.base / 'good.zip'
        build.write_archive(self.root, output)
        previous = output.read_bytes()
        for description in ("'Unclosed string", 'Use when: editing code', '[one, two]', '{a: b}', 'null', 'true', '123'):
            with self.subTest(description=description):
                (self.skill / 'SKILL.md').write_text('---\nname: sample\ndescription: ' + description + '\n---\nBody\n')
                with self.assertRaises(ValueError):
                    build.write_archive(self.root, output)
                self.assertEqual(previous, output.read_bytes())

    def test_frontmatter_supports_the_documented_string_subset(self):
        for description in ('"Use when: editing code"', "'Use when it''s needed'", '>\n  Use when editing\n  code with blocks.'):
            with self.subTest(description=description):
                (self.skill / 'SKILL.md').write_text('---\nname: sample\ndescription: ' + description + '\n---\nBody\n')
                self.assertEqual(build.validate_package(self.root), [])

    def test_nonobject_manifest_returns_actionable_errors(self):
        for value in ([], None, 'text'):
            with self.subTest(value=value):
                (self.root / 'plugin.json').write_text(json.dumps(value))
                self.assertTrue(any('object' in e for e in build.validate_package(self.root)))
        self.write_manifest()
        overlay = self.root / '.codex-plugin'
        overlay.mkdir()
        for value in ([], None):
            (overlay / 'plugin.json').write_text(json.dumps(value))
            self.assertTrue(any('object' in e for e in build.validate_package(self.root)))

    def test_invocation_metadata_rejects_malformed_or_nonboolean_policy(self):
        agents = self.skill / 'agents'
        agents.mkdir()
        for text in ('broken: [', 'policy:\n  allow_implicit_invocation: "false"\n',
                     'policy:\n  allow_implicit_invocation: false\n  allow_implicit_invocation: true\n'):
            with self.subTest(text=text):
                (agents / 'openai.yaml').write_text(text)
                self.assertTrue(any('metadata' in e for e in build.validate_package(self.root)))
        (agents / 'openai.yaml').unlink()
        (agents / 'openai.yaml').mkdir()
        self.assertTrue(any('metadata' in e for e in build.validate_package(self.root)))

    def test_manual_invocation_policy_must_match_source_map(self):
        (self.root / 'SOURCES.json').write_text(json.dumps({'skills': [{'name': 'sample', 'manual_only': True}]}))
        agents = self.skill / 'agents'
        agents.mkdir()
        policy = agents / 'openai.yaml'
        policy.write_text('policy:\n  allow_implicit_invocation: true\n')
        self.assertTrue(any('invocation policy' in e for e in build.validate_package(self.root)))
        policy.write_text('policy:\n  allow_implicit_invocation: false\n')
        self.assertEqual(build.validate_package(self.root), [])
        policy.unlink()
        self.assertTrue(any('invocation policy' in e for e in build.validate_package(self.root)))

    def test_skill_folder_without_entry_cannot_silently_disappear(self):
        (self.root / 'skills' / 'orphan').mkdir()
        self.assertTrue(any('SKILL.md' in e for e in build.validate_package(self.root)))

    def test_invalid_utf8_reference_returns_errors_and_preserves_archive(self):
        output = self.base / 'good.zip'
        build.write_archive(self.root, output)
        previous = output.read_bytes()
        reference = self.skill / 'references' / 'check.md'
        reference.parent.mkdir()
        reference.write_bytes(b'\xff')
        self.body('Read [checks](references/check.md#checks).\n')
        self.assertTrue(any('UTF-8' in e for e in build.validate_package(self.root)))
        with self.assertRaises(ValueError):
            build.write_archive(self.root, output)
        self.assertEqual(output.read_bytes(), previous)

    def test_assembly_preserves_sources_and_closes_all_references(self):
        target = self.base / 'assembled'
        build.assemble(target)
        self.assertEqual(build.validate_package(target), [])
        skill_names = {p.parent.name for p in (target / 'skills').glob('*/SKILL.md')}
        self.assertEqual(len(skill_names), 30)
        self.assertTrue({'architecture', 'prototype'} <= skill_names)
        self.assertEqual((target / 'licenses/matt-pocock-MIT.txt').read_bytes(),
                         (SCRIPT.parents[1] / 'inputs/matt-pocock/LICENSE').read_bytes())
        for name in ('ponytail-audit', 'ponytail-debt', 'ponytail-gain'):
            original = SCRIPT.parents[1] / 'inputs/ponytail/skills' / name / 'SKILL.md'
            self.assertEqual((target / 'skills' / name / 'SKILL.md').read_bytes(), original.read_bytes())
        sources = json.loads((target / 'SOURCES.json').read_text())
        originals = {p.relative_to(SCRIPT.parents[1] / 'inputs').as_posix()
                     for p in (SCRIPT.parents[1] / 'inputs').glob('*/skills/**/SKILL.md')}
        self.assertEqual(len(originals), 52)
        covered = {s['path'] for entry in sources['skills'] for s in entry['sources']}
        self.assertEqual(covered, originals)

    def test_refuses_to_assemble_over_existing_user_files(self):
        with self.assertRaises(ValueError):
            build.assemble(self.root)

    def test_local_references_have_verifiable_provenance(self):
        target = self.base / 'assembled'
        build.assemble(target)
        records = json.loads((target / 'SOURCES.json').read_text())['references']
        local = next((r for r in records if r.get('origin') == 'local'
                      and r['path'] == 'content/advanced-testing.md'), None)
        self.assertIsNotNone(local)
        source = SCRIPT.parents[1] / 'content/advanced-testing.md'
        expected = hashlib.sha256(source.read_bytes()).hexdigest()
        self.assertEqual(local['sha256'], expected)
        self.assertEqual(hashlib.sha256((target / local['destination']).read_bytes()).hexdigest(), expected)

    def test_local_reference_cannot_read_or_write_outside_its_declared_location(self):
        project = self.base / 'project'
        project.mkdir()
        shutil.copytree(SCRIPT.parents[1] / 'content', project / 'content')
        shutil.copyfile(SCRIPT.parents[1] / 'input-sources.json', project / 'input-sources.json')
        shutil.copytree(SCRIPT.parents[1] / 'inputs', project / 'inputs')
        outside = project / 'escape.md'
        outside.write_text('Outside the maintained reference directory.\n')
        (project / 'content/link.md').symlink_to(outside)
        catalog_path = project / 'content/catalog.json'
        catalog = json.loads(catalog_path.read_text())
        entry = next(e for e in catalog if e['name'] == 'frontend')
        for index, path in enumerate(('../escape.md', str(outside), 'link.md')):
            with self.subTest(path=path):
                entry['local_references'] = [path]
                catalog_path.write_text(json.dumps(catalog))
                with mock.patch.object(build, 'PROJECT', project):
                    with self.assertRaisesRegex(ValueError, 'local reference'):
                        build.assemble(self.base / ('assembly-' + str(index)))
                self.assertEqual(outside.read_text(), 'Outside the maintained reference directory.\n')


if __name__ == '__main__':
    unittest.main()
