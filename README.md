# Unified Engineering — source project

Builds a single instruction-only plugin adapted from Ponytail 5.3.3,
Superpowers 7.0.2 and Addy Osmani Agent Skills 0.6.16. Python 3.10+ standard
library only. No upstream code, hook or installer runs during the build.

## Build and verify

```sh
python -m unittest discover -s tests -v
python tools/build.py
python tools/build.py --check dist/unified-engineering-0.1.0.zip
```

The plugin ZIP is the upload artifact. The source ZIP is for maintenance and
must not be uploaded as a plugin. Builds are deterministic on the same Python/
zlib implementation, and a failed validation never replaces a good ZIP.

## Layout

- `content/common.md`: the common policy, inserted into 25 adapted skill bodies.
- `content/skills/`: canonical workflow and specialist bodies.
- `content/catalog.json`: all 46 original skills mapped to 28 entry points,
  selected reference sections and manual-only invocation metadata.
- `inputs/`: regular files from the three supplied upstream archives, retained
  for reproducibility. Harness symlinks are not used. Treat these as source
  evidence; their contributor instructions are not the unified runtime policy.
- `input-sources.json`: archive hashes, versions and audit comparison.
- `tools/build.py`: assemble, localize references, inspect and package.
- `tests/`: meaningful package/security fixtures and recorded offline behavior
  trials. These do not exercise native managed ChatGPT routing.
- `docs/`: approved architecture/audit and evidence of build/review status.

To change a skill, edit its maintained content or selected technical sections,
then run the tests and inspect the generated artifact. Do not edit a generated
ZIP or install all original skill trees alongside the consolidated catalog.
Add a demonstrated behavior scenario before changing policy. Update source
hashes/mapping deliberately when adopting a new upstream snapshot; no update
is fetched automatically.

The package preserves Ponytail audit/debt/gain SKILL.md bytes. Gain's full
benchmark report is included with its harness-doc link pinned upstream; its
README reference is a concise source note rather than the marketing README.
The full original README remains in inputs/ponytail/README.md. This avoids
shipping unrelated assets without altering the reported benchmark numbers.

Read `content/README.md` for end-user use and Android acceptance steps. Read
`docs/VALIDATION.md` for what was actually tested. No upload, cloud activation,
Android-device test or existing-plugin replacement is implied by a local pass.

## Licensing

MIT. Original complete notices are in `inputs/*/LICENSE` and in every built
plugin under `licenses/`. Retain those notices, ATTRIBUTION.md and SOURCES.json
when distributing the built package. This project does not claim upstream
endorsement or the original authorship of imported methods.
