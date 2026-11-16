"""Build and inspect the instruction-only plugin. Python standard library only."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import shutil
import tempfile
import zipfile


PROJECT = Path(__file__).resolve().parents[1]
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
BLOCKED = {'hooks', 'userConfig', 'commands', 'agents', 'mcpServers', 'apps', 'dependencies', 'systemPromptPath'}


def unfenced(text):
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker[1][0]
            if fence is None:
                fence = char
            elif char == fence:
                fence = None
            lines.append('')
        else:
            lines.append('' if fence else line)
    return '\n'.join(lines)


def frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if not match:
        raise ValueError('missing YAML frontmatter')
    fields, current, block = {}, None, False
    for line in match[1].splitlines():
        field = re.match(r'^([a-z][a-z-]*):\s*(.*)$', line)
        if field:
            current, value = field.groups()
            if current in fields:
                raise ValueError('duplicate frontmatter field: ' + current)
            block = value in ('>', '|', '>-', '|-')
            if block:
                fields[current] = ''
            elif value.startswith('"'):
                fields[current] = json.loads(value)
                if not isinstance(fields[current], str):
                    raise ValueError('frontmatter fields must be strings')
            elif value.startswith("'"):
                if not re.fullmatch(r"'(?:[^']|'')*'", value):
                    raise ValueError('unbalanced single-quoted frontmatter string')
                fields[current] = value[1:-1].replace("''", "'")
            else:
                reserved = value[:1] in '[{!&*#?>|%@`' if value else False
                typed = value.lower() in ('null', '~', 'true', 'false', 'yes', 'no', 'on', 'off') or re.fullmatch(r'[-+]?(?:\d[\d_.]*(?:e[-+]?\d+)?|\.inf|\.nan)', value, re.I)
                if reserved or typed or re.search(r':(?:\s|$)', value) or value.startswith('- '):
                    raise ValueError('quote plain frontmatter values containing YAML type/collection syntax')
                fields[current] = value
        elif line[:1].isspace() and current and block:
            fields[current] += ' ' + line.strip()
        elif line.strip():
            raise ValueError('unsupported frontmatter line')
    return {k: v.strip() for k, v in fields.items()}


def links(text):
    return re.findall(r'\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', unfenced(text))


def slug(text):
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def anchors(text):
    result, counts = set(), {}
    for line in unfenced(text).splitlines():
        m = re.match(r'^#{1,6}\s+(.+?)(?:\s+#+)?$', line)
        if m:
            base = slug(m[1]); count = counts.get(base, 0)
            result.add(base if not count else f'{base}-{count}')
            counts[base] = count + 1
    return result


def validate_package(root):
    root = Path(root).resolve()
    errors = []
    files = list(root.rglob('*'))
    for file in files:
        rel = file.relative_to(root).as_posix()
        if file.is_symlink():
            errors.append('symlink forbidden: ' + rel)
        if file.name == 'marketplace.json':
            errors.append('marketplace forbidden: ' + rel)
        if file.name == 'plugin.json' and rel not in ('plugin.json', '.codex-plugin/plugin.json'):
            errors.append('nested manifest forbidden: ' + rel)
        if any(p in {'.git', '.claude-plugin', '__pycache__', 'hooks', 'node_modules'} for p in file.relative_to(root).parts):
            errors.append('unsupported package path: ' + rel)
    if errors:
        return errors
    try:
        manifest = json.loads((root / 'plugin.json').read_text())
        if not isinstance(manifest, dict):
            raise ValueError('plugin manifest must be a JSON object')
        for key in ('name', 'version', 'description', 'license'):
            if not isinstance(manifest.get(key), str) or not manifest[key].strip():
                errors.append('manifest missing ' + key)
        if not NAME.fullmatch(manifest.get('name', '')):
            errors.append('invalid plugin name')
        if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?', manifest.get('version', '')):
            errors.append('invalid plugin version')
        if BLOCKED & manifest.keys():
            errors.append('unsupported manifest fields: ' + ', '.join(sorted(BLOCKED & manifest.keys())))
        overlay_path = root / '.codex-plugin/plugin.json'
        if overlay_path.exists():
            overlay = json.loads(overlay_path.read_text())
            if not isinstance(overlay, dict):
                raise ValueError('Codex overlay must be a JSON object')
            for key in ('name', 'version', 'description', 'license'):
                if overlay.get(key) != manifest.get(key):
                    errors.append('overlay differs: ' + key)
            if overlay.get('skills') != './skills/':
                errors.append('overlay skills must be ./skills/')
            if BLOCKED & overlay.keys():
                errors.append('unsupported overlay fields: ' + ', '.join(sorted(BLOCKED & overlay.keys())))
        if 'extensions' in manifest:
            errors.append('inline extensions forbidden: use the single compatibility overlay')
    except (OSError, ValueError, TypeError) as exc:
        errors.append('invalid manifest: ' + str(exc))
    if not (root / 'LICENSE').is_file():
        errors.append('missing LICENSE')
    skill_root = root / 'skills'
    skills = sorted(skill_root.glob('*/SKILL.md'))
    if not skills:
        errors.append('no discoverable skills')
    for skill in skills:
        try:
            fields = frontmatter(skill.read_text())
            if fields.get('name') != skill.parent.name or not NAME.fullmatch(fields.get('name', '')):
                errors.append('skill name mismatch: ' + str(skill.relative_to(root)))
            if not fields.get('description') or len(fields['description']) > 1024:
                errors.append('invalid description: ' + skill.parent.name)
        except (ValueError, OSError) as exc:
            errors.append(f'invalid skill {skill.parent.name}: {exc}')
        for file in skill.parent.rglob('*.md'):
            for link in links(file.read_text()):
                if re.match(r'^[a-zA-Z][\w+.-]*:', link) or link.startswith('//'):
                    continue
                path, _, anchor = link.partition('#')
                target = (file.parent / path).resolve() if path else file.resolve()
                if not target.is_relative_to(skill.parent.resolve()):
                    errors.append(f'link escapes skill: {file.relative_to(root)} -> {link}')
                elif not target.is_file():
                    errors.append(f'missing reference: {file.relative_to(root)} -> {link}')
                elif anchor and target.suffix == '.md' and anchor not in anchors(target.read_text()):
                    errors.append(f'missing anchor: {file.relative_to(root)} -> {link}')
    return errors


def write_archive(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output.is_relative_to(root):
        raise ValueError('output must be outside package')
    errors = validate_package(root)
    if errors:
        raise ValueError('\n'.join(errors))
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix='.plugin-', suffix='.zip', dir=output.parent)
    os.close(handle)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for file in sorted(root.rglob('*')):
                if file.is_file():
                    entry = zipfile.ZipInfo(file.relative_to(root).as_posix(), (1980, 1, 1, 0, 0, 0))
                    entry.create_system = 3
                    entry.external_attr = 0o100644 << 16
                    entry.compress_type = zipfile.ZIP_DEFLATED
                    archive.writestr(entry, file.read_bytes(), compresslevel=9)
        errors = validate_archive(Path(temporary))
        if errors:
            raise ValueError('\n'.join(errors))
        os.replace(temporary, output)
    finally:
        Path(temporary).unlink(missing_ok=True)
    return hashlib.sha256(output.read_bytes()).hexdigest()


def validate_archive(path):
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                return ['duplicate archive entries']
            if sum(i.file_size for i in archive.infolist()) > 64 * 1024 * 1024:
                return ['archive exceeds 64 MiB inspection limit']
            for entry in archive.infolist():
                name = PurePosixPath(entry.filename)
                if name.is_absolute() or '..' in name.parts or '\\' in entry.filename or ':' in entry.filename or '\x00' in entry.filename:
                    return ['unsafe archive path: ' + entry.filename]
                canonical = name.as_posix() + ('/' if entry.is_dir() else '')
                if entry.filename != canonical:
                    return ['noncanonical archive path: ' + entry.filename]
                if stat.S_ISLNK(entry.external_attr >> 16):
                    return ['archive symlink: ' + entry.filename]
            with tempfile.TemporaryDirectory() as directory:
                archive.extractall(directory)
                return validate_package(Path(directory))
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        return ['invalid archive: ' + str(exc)]


def selected_sections(text, requested):
    """Copy complete level-two sections, ignoring headings inside examples."""
    lines = text.splitlines(keepends=True)
    boundaries, fence = [], None
    for index, line in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker[1][0]
            fence = char if fence is None else None if char == fence else fence
        elif fence is None and line.startswith('## '):
            boundaries.append((index, line[3:].strip()))
    found = {}
    for i, (start, heading) in enumerate(boundaries):
        end = boundaries[i + 1][0] if i + 1 < len(boundaries) else len(lines)
        found[heading] = ''.join(lines[start:end]).strip()
    missing = set(requested) - found.keys()
    if missing:
        raise ValueError('missing upstream sections: ' + ', '.join(sorted(missing)))
    return '\n\n'.join(found[heading] for heading in requested) + '\n'


def assemble(destination):
    destination = Path(destination)
    if destination.is_symlink() or (destination.exists() and any(destination.iterdir())):
        raise ValueError('refusing to assemble over existing files')
    destination.mkdir(parents=True, exist_ok=True)
    content, inputs = PROJECT / 'content', PROJECT / 'inputs'
    catalog = json.loads((content / 'catalog.json').read_text())
    manifest = json.loads((content / 'plugin.json').read_text())
    interface = json.loads((content / 'interface.json').read_text())
    sources = {'format': 1, 'archives': json.loads((PROJECT / 'input-sources.json').read_text()), 'influences': json.loads((content / 'influences.json').read_text()), 'skills': [], 'references': []}

    def output(path, text):
        file = destination / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding='utf-8')

    def record(source):
        file = inputs / source
        if not file.is_file() or file.is_symlink():
            raise ValueError('missing/nonregular upstream source: ' + source)
        return {'path': source, 'sha256': hashlib.sha256(file.read_bytes()).hexdigest()}

    output('plugin.json', json.dumps(manifest, indent=2) + '\n')
    overlay = {k: v for k, v in manifest.items() if k != '$schema'}
    overlay.update(skills='./skills/', interface=interface)
    output('.codex-plugin/plugin.json', json.dumps(overlay, indent=2) + '\n')
    output('README.md', (content / 'README.md').read_text())
    projects = [('ponytail', 'DietrichGebert', 2026), ('superpowers', 'Jesse Vincent', 2025), ('agent-skills', 'Addy Osmani', 2025), ('matt-pocock', 'Matt Pocock', 2026)]
    notices = []
    for project, author, year in projects:
        text = (inputs / project / 'LICENSE').read_text()
        output('licenses/' + project + '-MIT.txt', text)
        notices.append(f'Copyright (c) {year} {author}')
    license_text = (inputs / 'ponytail/LICENSE').read_text()
    output('LICENSE', license_text.replace('Copyright (c) 2026 DietrichGebert', '\n'.join(notices) + '\nCopyright (c) 2026 Unified Engineering contributors'))
    output('ATTRIBUTION.md', '# Attribution\n\nIndependent MIT-licensed adaptation. No upstream endorsement is implied.\n\n' + '\n'.join(f'- {p}: {a}; original complete notice in licenses/{p}-MIT.txt.' for p, a, _ in projects) + '\n\nPonytail provides the simplicity philosophy and reporting tools. Superpowers provides development workflow methods. Addy Osmani provides specialist engineering patterns and workflow refinements. Adapted skill bodies coordinate their overlapping guidance. SOURCES.json maps every canonical original skill to its unified destination and hashes each copied reference.\n\nThe simplification skill retains Addy Osmani\'s acknowledgment of Anthropic\'s Code Simplifier inspiration: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md . Third-party links do not imply copied code or endorsement.\n\nMatt Pocock contributes selected domain-modeling, interface-design, prototyping, handoff and retrospective methods. His original MIT notice is retained in licenses/matt-pocock-MIT.txt.\n\nThe forrestchang community collection inspired by Karpathy was reviewed as conceptual input for independently worded policy refinements. It is not authored by Karpathy; no source text from that collection is redistributed. See SOURCES.json influences for the reviewed archive hash and notice limitation.\n\nProperty-testing, mutation and related-bug guidance is independently written for this plugin. No Trail of Bits ShareAlike text or OpenAI/Vercel skill code is bundled.\n')

    common = (content / 'common.md').read_text().strip()
    preferences = (content / 'preferences.md').read_text()
    names = {entry['name'] for entry in catalog}
    if len(names) != len(catalog) or any(not NAME.fullmatch(name) for name in names):
        raise ValueError('canonical skill names must be unique kebab-case identifiers')
    catalog_note = '# Skill catalog\n\nOne workflow owns the task; specialists contribute checks. Names are manual invocation intents, not filesystem dependencies.\n\n' + '\n'.join(f'- `{e["name"]}`' + (' — explicit request only.' if e.get('manual') else ' — relevant task matching.') for e in catalog) + '\n\nUse Lite/Full/Ultra preferences without lowering correctness. Use @ selection where supported, or plain language. Native matching/manual-only enforcement must be tested in the target host.\n'
    for entry in catalog:
        name = entry['name']; skill_dir = Path('skills') / name
        source_records = [record(source) for source in entry['sources']]
        if entry.get('preserve'):
            original = inputs / entry['sources'][0]
            target = destination / skill_dir / 'SKILL.md'
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, target)
        else:
            body = (content / 'skills' / (name + '.md')).read_text()
            if body.count('{{POLICY}}') != 1:
                raise ValueError('missing/duplicate common policy token: ' + name)
            output(skill_dir / 'SKILL.md', body.replace('{{POLICY}}', common))
            output(skill_dir / 'references/preferences.md', preferences)
        metadata = frontmatter((destination / skill_dir / 'SKILL.md').read_text())
        short = metadata['description'][:64].rstrip()
        output(skill_dir / 'agents/openai.yaml', 'interface:\n  display_name: ' + json.dumps(name.replace('-', ' ').title()) + '\n  short_description: ' + json.dumps(short) + '\n  default_prompt: ' + json.dumps('Use the ' + name + ' skill for this task.') + '\npolicy:\n  allow_implicit_invocation: ' + ('false' if entry.get('manual') else 'true') + '\n')
        sources['skills'].append({'name': name, 'treatment': 'unchanged SKILL.md' if entry.get('preserve') else 'adapted and coordinated', 'manual_only': bool(entry.get('manual')), 'sources': source_records})
        if name == 'engineering':
            output(skill_dir / 'references/catalog.md', catalog_note)
        for local in entry.get('local_references', []):
            output(skill_dir / 'references' / local, (content / local).read_text())

        copied = {}
        def reference(source, target=None, sections=None):
            source_path = (inputs / source).resolve()
            if not source_path.is_relative_to(inputs.resolve()):
                raise ValueError('reference escaped input root')
            filename = target or source_path.name
            if '/' in filename or not filename.endswith('.md'):
                raise ValueError('invalid reference destination: ' + filename)
            if filename in copied:
                if copied[filename] != source:
                    raise ValueError('reference collision: ' + filename)
                return filename
            copied[filename] = source
            info = record(source)
            text = source_path.read_text()
            if sections:
                text = selected_sections(text, sections)
            # Localize real reference dependencies, including backticked paths.
            def local_link(match):
                link = match[1]
                path, sep, anchor = link.partition('#')
                if not path or re.match(r'^[a-zA-Z][\w+.-]*:', path) or path.startswith('//'):
                    return match[0]
                original = (source_path.parent / path).resolve()
                if not original.is_file():
                    raise ValueError(f'missing reference in {source}: {link}')
                if not original.is_relative_to(inputs.resolve()):
                    raise ValueError('upstream reference escapes inputs')
                new_name = reference(original.relative_to(inputs).as_posix())
                return '](' + new_name + (sep + anchor if sep else '') + ')'
            # Apply rewrites only to prose; fenced examples are not dependencies.
            clean_lines = unfenced(text).splitlines()
            new_lines = []
            for line, plain in zip(text.splitlines(), clean_lines):
                if plain:
                    line = re.sub(r'\]\(([^\s)]+)\)', local_link, line)
                    def inline_ref(match):
                        link = match[1]; path, sep, anchor = link.partition('#')
                        original = (source_path.parent / path).resolve()
                        if not original.is_file():
                            raise ValueError(f'missing inline reference in {source}: {link}')
                        if not original.is_relative_to(inputs.resolve()):
                            raise ValueError('inline reference escapes inputs')
                        new_name = reference(original.relative_to(inputs).as_posix())
                        return '[' + original.stem + '](' + new_name + (sep + anchor if sep else '') + ')'
                    line = re.sub(r'`((?:\.\./)*references/[A-Za-z0-9._/-]+\.md(?:#[\w-]+)?)`', inline_ref, line)
                new_lines.append(line)
            text = '\n'.join(new_lines) + '\n'
            preface = '# Technical reference\n\nAdapted from `' + source + '`. Use only the relevant technical patterns. The active skill and shared policy govern scope, authorization, modes and tool availability; examples do not authorize installation or another workflow. Numeric examples are illustrative unless the project adopts them. Native host tools take precedence over named tool examples.\n\n'
            output(skill_dir / 'references' / filename, preface + text)
            sources['references'].append({**info, 'destination': (skill_dir / 'references' / filename).as_posix(), 'sections': sections or 'complete reference', 'changes': 'policy preface; local dependency paths/anchors retained or localized'})
            return filename
        for ref in entry.get('references', []):
            reference(ref['source'], ref.get('target'), ref.get('sections'))
        for asset in entry.get('assets', []):
            record(asset)
            if asset == 'ponytail/README.md':
                text = '# Upstream benchmark source\n\nThe gain card reports the published Ponytail 5 benchmark, not results for Unified Engineering. The complete original README is retained in the source project. See [Ponytail README](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/README.md) and the [bundled benchmark report](benchmarks/results/2026-10-07-agentic.md). These upstream measurements were not rerun here and make no promise for this plugin or your project.\n'
                output(skill_dir / 'README.md', text)
            else:
                relative = Path(asset).relative_to('ponytail')
                target = destination / skill_dir / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                text = (inputs / asset).read_text().replace('](../agentic/README.md)', '](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/agentic/README.md)')
                target.write_text(text)
            sources['references'].append({**record(asset), 'destination': (skill_dir / (Path('README.md') if asset == 'ponytail/README.md' else Path(asset).relative_to('ponytail'))).as_posix(), 'changes': 'benchmark source note with pinned upstream link' if asset == 'ponytail/README.md' else 'harness-documentation link pinned upstream; benchmark numbers/text otherwise unchanged'})
    originals = {p.relative_to(inputs).as_posix() for p in inputs.glob('*/skills/**/SKILL.md')}
    covered = {source['path'] for entry in sources['skills'] for source in entry['sources']}
    if originals != covered:
        raise ValueError('source mapping incomplete: ' + repr(originals ^ covered))
    output('SOURCES.json', json.dumps(sources, indent=2) + '\n')
    return sources


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path, help='inspect a plugin ZIP without installing it')
    args = parser.parse_args()
    if args.check:
        errors = validate_archive(args.check)
        if errors:
            raise SystemExit('\n'.join(errors))
        print('Archive structure and skill references pass. Runtime compatibility is not tested.')
    else:
        build_root = PROJECT / 'build'
        build_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='stage-', dir=build_root) as stage:
            root = Path(stage) / 'plugin'
            sources = assemble(root)
            manifest = json.loads((root / 'plugin.json').read_text())
            output = PROJECT / 'dist' / f'{manifest["name"]}-{manifest["version"]}.zip'
            digest = write_archive(root, output)
        print(f'Archive: {output}\nSkills: {len(sources["skills"])}\nSHA-256: {digest}\nStructural checks pass; managed ChatGPT/Android compatibility still requires a real upload/session test.')


if __name__ == '__main__':
    main()
