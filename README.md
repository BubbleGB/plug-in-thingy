# Unified Engineering

**Simple solutions. Sound workflows. Focused expertise.**

[![CI](https://github.com/BubbleGB/plug-in-thingy/actions/workflows/ci.yml/badge.svg)](https://github.com/BubbleGB/plug-in-thingy/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](docs/DEVELOPMENT.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An instruction-only ChatGPT/Codex plugin with **30 coordinated engineering
skills**. It combines Ponytail's simplicity, Superpowers' workflow methods,
Addy Osmani's specialist guidance and selected Matt Pocock techniques, with
independently worded refinements informed by the Karpathy-inspired community
guidelines.

One workflow owns the task. Specialists add the checks that matter. Clear tasks
stay small; consequential changes get proportionate planning and verification.

**[Download releases](https://github.com/BubbleGB/plug-in-thingy/releases)** ·
**[Skill catalog](docs/SKILLS.md)** · **[Development](docs/DEVELOPMENT.md)** ·
**[Changelog](CHANGELOG.md)**

## Install and use

1. Use the delivered **`unified-engineering-0.3.0.zip`**, or build it from
   source using the commands below. Published artifacts, when available, appear
   on the repository releases page. Source ZIPs and GitHub's automatic source
   downloads are for development, not plugin upload.
2. Import the plugin ZIP through the supported plugin flow available to your
   ChatGPT account. Management controls may vary by account/client.
3. Select the plugin/skill where supported, or ask in ordinary language:

   > Use Unified Engineering to fix this bug.
   >
   > Review this diff only; do not edit files.
   >
   > Use Lite mode and implement the approved plan.

Keep existing working plugins until the replacement passes your actual workflow.
Other installed routers can still affect behavior; this plugin cannot disable
them. No Android terminal, executable hooks, MCP server or background service is
required. Code/browser work still needs appropriate host tools.

## What it does

| Area | Examples |
|---|---|
| Design and delivery | Clarify consequential ambiguity, plan slices, implement approved work, prepare releases |
| Debugging and quality | Root-cause investigation, behavior tests, reviews, simplification, whole-repo audits |
| Specialist engineering | APIs, frontend, security, performance, migrations, CI, observability, documentation |
| Focused experiments | Module/interface assessment and question-driven throwaway prototypes |
| Explicit advanced tools | Delegation, adversarial review, skill authoring, workflow diagnosis, debt and benchmark reports |

See the [complete catalog](docs/SKILLS.md). Some hosts list only the 24 automatic
entries; the six manual-only skills can require explicit selection or resource
reading. Automatic matching is host/model behavior, not a guaranteed event hook.

## Three modes, one quality floor

| Mode | Behavior |
|---|---|
| **Lite** | Requested scope with minimal ceremony |
| **Full** (default) | Smallest complete solution; reuse first; proportionate checks |
| **Ultra** | Also challenge unjustified complexity once, then respect the informed choice |

All modes retain correctness, security, accessibility and honest evidence.
Session settings include `workflow=manual` and `specialists=manual`. An existing
project-root `.unified-engineering.json` can provide defaults:

```json
{"mode":"full","workflow":"auto","specialists":"auto"}
```

Session instructions take precedence. No global persistence or automatic
installation is promised. See [end-user instructions](content/README.md).

## Build from source

Requires Python 3.10+ and Git. No pip/npm install is needed.

```sh
python -m unittest discover -s tests -v
python tools/build.py
python tools/build.py --check dist/unified-engineering-0.3.0.zip
```

The build produces one rootless plugin ZIP with a portable manifest, Codex
compatibility overlay, self-contained references and retained notices. It runs
no upstream installers or hooks. Builds are deterministic on the same Python/
zlib implementation; failed validation preserves the previous good ZIP.

## Verification and limits

- **27 package/security tests** cover assembly, source mapping, invocation
  metadata, broken references, unsafe ZIP paths and failure behavior.
- In a managed ChatGPT session, installed **0.2.0** exposed 24 automatic skills;
  all 30 skills and **95 Markdown documents** matched the release exactly.
- **0.2.1** adds stricter metadata, missing-entry and UTF-8 checks. Its source
  archive was rebuilt into a byte-identical plugin ZIP.

These checks do not establish universal implicit activation, Android UI controls,
standalone behavior with other routers disabled, or installation of a new ZIP.
Version **0.3.0** adds focused visual review, audit evidence, skill/plugin intake,
source-linked diagrams and evaluation guidance through five conditional references.
It records local reference hashes and rejects unsafe reference paths and oversized
listing subtitles. No new runtime dependency or top-level skill is added.

Read the [current validation report](docs/VALIDATION-0.3.md) and
[evidence index](docs/README.md). Ponytail benchmark figures describe upstream
Ponytail, not measured savings from this plugin.

## Project layout

```text
content/         Maintained policy, skill bodies, reference selections and metadata
inputs/          Pinned upstream source evidence; never installed wholesale
tools/build.py   Standard-library assembler, inspector and ZIP builder
tests/           Regression tests and recorded offline behavior exercises
docs/            Maintainer guides, decisions and versioned evidence
dist/            Generated archives; ignored by Git, attached to releases
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing skills or source inputs.
Coding-agent instructions are in [AGENTS.md](AGENTS.md).

## License and attribution

MIT; retain [LICENSE](LICENSE), [ATTRIBUTION.md](ATTRIBUTION.md) and all original
notices. The built package retains four complete MIT notices and records 52
selected source definitions and hashes in SOURCES.json. The Karpathy-inspired
community source is conceptual input only; no text from it is redistributed.
New specialist references are independently authored, with reviewed conceptual
sources pinned in `content/influences.json`; no additional upstream text,
scripts, hooks or assets are redistributed. No Trail of Bits ShareAlike,
OpenAI Apache or Vercel skill content is bundled.
This is an independent adaptation and implies no upstream endorsement.
