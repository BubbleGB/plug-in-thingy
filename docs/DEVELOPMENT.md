# Development

Python 3.10+ and Git are sufficient. Work in this repository; no application
checkout, cloud account, upstream installer or executable hook is needed.

```sh
python -m unittest discover -s tests -v
python tools/build.py
python tools/build.py --check dist/unified-engineering-0.3.0.zip
git diff --check
```

The version comes from `content/plugin.json`. Build output is generated and
ignored. Do not edit or commit an assembled ZIP. The plugin upload artifact
contains one root, never the authoring repository or a marketplace archive.

## Maintained source

| Path | Responsibility |
|---|---|
| content/common.md | Shared policy, inserted once into each adapted entry |
| content/skills/ | Canonical workflow/specialist bodies |
| content/catalog.json | Selected sources, reference sections and manual flags |
| content/preferences.md | Session/project preference contract |
| content/influences.json | Reviewed conceptual input not copied as source text |
| content/plugin.json and interface.json | Package identity and presentation |
| tools/build.py | Assembly, containment/reference checks and archive validation |

The assembler keeps references inside each owning skill package. Some shared
checklists are duplicated in the artifact but have one maintained upstream or
local source. Most skill text loads only when the host selects it; catalog size
is not a claim about per-task context cost.

## Upstream updates

`inputs/` is pinned evidence: three complete upstream regular-file snapshots and
selected Matt Pocock files. It is not an installed skill catalog. Its nested
AGENTS.md/CLAUDE.md files describe upstream contribution workflows, not this repo.
No upstream code runs during assembly.

Before updating an input, inspect the licence and actual changed guidance.
Record the version/repository and archive SHA-256 in `input-sources.json`, update
selection deliberately, and rerun the suite. Retain notices and source hashes.
The three Ponytail audit/debt/gain entry files are intentionally byte-preserved.
Do not silently replace them while changing unified policy.

## Verification layers

1. Unit/integration tests reject malformed inputs and exercise actual assembly.
2. ZIP inspection checks discovery structure, references and containment.
3. Offline model exercises explore description selection and instruction behavior.
4. Managed cloud checks establish actual listing/resource access for a version.
5. Device/client and standalone activation checks need the real target workflow.

Keep these results distinct. A package check or simulated response does not prove
Android UI support, implicit routing or a deployment. See the
[evidence index](README.md) for versioned results.

## Generated OpenAI metadata profile

The builder supports string interface fields and a boolean invocation policy.
It is intentionally not a general YAML/OpenAI schema parser. Six entries are
manual-only; effective flags must match SOURCES.json. Missing skill entries,
invalid encoding and malformed metadata are errors, not silently skipped content.

CI runs the same commands on Python 3.10 and 3.13. See
[CONTRIBUTING.md](../CONTRIBUTING.md) and [releasing](RELEASING.md).

## Local references and intake

Declare independently authored references in `content/catalog.json` using a
single Markdown filename from `content/`. The builder rejects path traversal,
absolute names, symlinks and nonregular files before copying. Each destination
is hashed in SOURCES.json with `origin: local` and a repository-relative source
path. Upstream reference paths continue to be relative to inputs/.

Before importing new instructions/scripts, use the package-intake method and
check exact file-specific notices. A static package check is not a malware scan.
The 0.3 behavior scenarios keep expected criteria out of model prompts. Fresh
paired model and managed-host trials are separate from the package suite; record
auth/tool blockers rather than treating saved scenarios as passing results.
