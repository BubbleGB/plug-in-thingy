# Unified Engineering

**Simple solutions. Sound workflows. Focused expertise.**

[![CI](https://github.com/BubbleGB/plug-in-thingy/actions/workflows/ci.yml/badge.svg)](https://github.com/BubbleGB/plug-in-thingy/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](docs/DEVELOPMENT.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

One instruction-only ChatGPT/Codex plugin with **30 coordinated engineering
skills**. It integrates selected methods into one workflow instead of installing
every upstream collection as a separate add-on.

## Current versions: what is actually available?

| Location | Version | Status |
|---|---|---|
| Default branch `main` | **0.2.1** | Existing five-source core; 24 package tests |
| [Draft PR #4](https://github.com/BubbleGB/plug-in-thingy/pull/4), branch `build/research-improvements` | **0.3.0 candidate** | Adds the focused guidance below and packaging fixes; 27 package tests and GitHub CI passed for its implementation |
| Your installed ChatGPT plugin | Depends on the version you imported | GitHub changes do **not** automatically update it; 0.3.0 has not been installed or verified in managed ChatGPT/Android |

The 0.3.0 candidate is built and available for testing, but is not merged into
`main`. Existing plugins remain installed. Do not confuse a source update,
passing CI or an available ZIP with a completed plugin installation.

## Which sources are we using?

### Core sources already integrated

| Source | What we use | How it is included |
|---|---|---|
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Small complete solutions, reuse, audits, debt and benchmark reporting | Adapted guidance; the audit/debt/gain skill files are preserved unchanged |
| [Superpowers](https://github.com/obra/superpowers) | Planning, implementation, debugging, testing, review and delivery methods | Coordinated workflows with proportionate activation |
| [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) | API, frontend, security, performance, CI, migration, observability and documentation expertise | Selected specialist guidance and references |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | Domain vocabulary, interface/module design, prototypes, handoffs and workflow diagnosis | Selected adapted methods |
| [Karpathy-inspired community guidelines](https://github.com/multica-ai/andrej-karpathy-skills) (originally forrestchang) | Clear assumptions, simplicity, surgical edits and verifiable goals | Conceptual influence on our independently worded policy; no source text copied |

**Four source collections contribute copied/adapted material; the fifth supplies
conceptual input.** Their complete applicable notices are retained. The
Karpathy-inspired collection is community work, not authored by Andrej Karpathy.
See [attribution](ATTRIBUTION.md), [input provenance](input-sources.json) and
[the skill catalog](docs/SKILLS.md) for the exact integration.

### Additional ideas used in the 0.3.0 candidate

These ten projects informed **our own five reference documents**. They are not
ten installed plugins. We copied none of their original text, code, scripts,
hooks, assets or runtimes into the package.

| Reviewed source | Selected idea | Where our guidance is used |
|---|---|---|
| [Impeccable](https://github.com/pbakaus/impeccable) | Focused visual critique and polish | `frontend`: visual review |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Intentional hierarchy, spacing, typography and design tokens | `frontend`: visual review |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | Content-specific design and rendered checks | `frontend`: visual review |
| [Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist) | Resilient layouts, accessibility and translated/RTL content | `frontend`: visual review |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | Purposeful motion, interruption, dismissal and reduced motion | `frontend`: visual review |
| [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Audit coverage and confirmed/unverified/rejected evidence | `security`: audit evidence |
| [ECC](https://github.com/affaan-m/ECC) | Review agent instructions, permissions, scripts and data destinations | `skill-authoring` and `security`: package intake |
| [Archify](https://github.com/tt-a1i/archify) | Source-backed diagram relationships and uncertainty | `architecture` and `docs`: system diagrams |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Choose a useful diagram form and keep it readable | `architecture` and `docs`: system diagrams |
| [Anthropic Skills](https://github.com/anthropics/skills) | Comparable baseline/candidate trials and honest evaluation evidence | `skill-authoring`: skill evaluation |

The five references are visual review (including motion), audit evidence,
skill/plugin intake, system diagrams and skill evaluation. They are consulted
when relevant, not loaded as another always-on workflow. The candidate keeps
the same 30 skill names and six manual-only entries.

Exact reviewed revisions and file hashes are recorded in the candidate's
[influence map](https://github.com/BubbleGB/plug-in-thingy/blob/build/research-improvements/content/influences.json).
The built package's `SOURCES.json` also hashes locally authored references.
See the [research and source assessments](https://github.com/BubbleGB/plug-in-thingy/blob/build/research-improvements/docs/github-survey.md)
and [0.3.0 validation](https://github.com/BubbleGB/plug-in-thingy/blob/build/research-improvements/docs/VALIDATION-0.3.md).
Researching a project is not a claim that its full functionality was integrated.

## What is not bundled or configured?

| Capability/tool | Package status |
|---|---|
| Claude-Mem, MemPalace or another automatic memory service | Not bundled or configured; no automatic session capture or guaranteed cross-session recall |
| REA, Graphify, Understand-Anything or a whole-repository graph engine | Optional external tools only; no new engine installed |
| Firecrawl, Agent-Reach, Browser Use or external service accounts | No required connection, API key or runtime; supported host tools may already provide related capabilities |
| AgentShield or another external security scanner | Not installed; package-intake guidance is a review procedure, not a malware scanner |
| Archify/Impeccable/Taste executables, live preview or automatic gates | Not bundled; borrowing design/diagram methods does not supply their tooling |
| Lifecycle hooks, background workers, transcript collectors or telemetry | Not included |
| Orca, Paperclip, OpenDesign or autonomous multi-agent platforms | Not bundled or required |

This table describes **this plugin package**, not every app/plugin separately
connected to your ChatGPT account. Existing host tools are used only when
available and relevant. No source repository is downloaded or installed at runtime.

## Use it

Use the versioned **plugin ZIP**, such as `unified-engineering-0.3.0.zip`, for
the supported upload/import flow available to your ChatGPT account. Source ZIPs
and GitHub's automatic source downloads are for development, not plugin upload.
Use the delivered artifact or build it below; published artifacts, when available,
appear on the [releases page](https://github.com/BubbleGB/plug-in-thingy/releases).

Select the plugin/skill where supported, or ask in ordinary language:

- “Use Unified Engineering to fix this bug.”
- “Review this diff only; do not edit files.”
- “Use Lite mode and implement the approved plan.”
- “Use the frontend skill to review this page's visual hierarchy.”
- “Use skill-authoring to assess this candidate plugin before importing it.”

One workflow owns the task. Specialists add relevant checks without restarting
planning or review. Of the 30 entries, 24 are eligible for automatic task matching
and six are manual-only. Actual selection is host/model behavior, not a guaranteed
hook. Explicit advanced work includes delegation, adversarial review, skill
authoring, workflow diagnosis, debt and benchmark reports; see the
[complete catalog](docs/SKILLS.md).

No Android terminal, Node installation, MCP server or background service is
required for the instruction-only core. Code/browser work still needs suitable
host tools. Other installed routers can affect behavior; this plugin cannot
disable them. Keep working installations until the new version passes your workflow.

## Modes and activation

| Mode | Behavior |
|---|---|
| **Lite** | Requested scope with minimal ceremony |
| **Full** (default) | Smallest complete solution; reuse first; proportionate checks |
| **Ultra** | Challenge unjustified complexity once, then respect the informed choice |

All modes retain correctness, security, accessibility and honest evidence. A mode
is not an agent-count setting or permission to install optional tools.
`workflow=manual` and `specialists=manual` suppress optional automatic expansion;
explicit invocation still works. An existing project-root
`.unified-engineering.json` can set defaults:

```json
{"mode":"full","workflow":"auto","specialists":"auto"}
```

Session instructions take precedence. No global settings service or guaranteed
persistence is supplied. See [end-user instructions](content/README.md).

## Build and verify

Python 3.10+ and Git are sufficient; no pip/npm install is needed.

```sh
python -m unittest discover -s tests -v
python tools/build.py
```

Inspect the ZIP matching the checked-out branch:

- `main`: `python tools/build.py --check dist/unified-engineering-0.2.1.zip`
- PR #4 branch: `python tools/build.py --check dist/unified-engineering-0.3.0.zip`

The builder produces one plugin ZIP with a portable manifest, Codex compatibility
overlay, self-contained references and retained notices. It runs no upstream
installers or hooks. Builds are deterministic on the same Python/zlib setup;
failed validation preserves the previous good ZIP.

## What has actually been verified?

- **0.2.1 / main:** 24 package/security tests; source rebuild reproduced the ZIP.
- **0.3.0 candidate:** 27 package tests, archive inspection/CRC, local-reference
  provenance, portable manifest schema, YAML parsing and a byte-identical clean
  source rebuild. GitHub CI passed for the implementation. It also rejects unsafe
  local-reference paths/symlinks and oversized listing subtitles.
- **Historical managed-host check, 0.2.0 only:** 24 automatic entries were listed;
  all 30 skills and 95 cloud Markdown resources were readable and matched that release.
- **Not established for 0.3.0:** managed upload, reliable native activation,
  Android runtime behavior or measured outcome/token improvements. Fresh model
  trials were blocked by Codex CLI sign-in; saved scenarios are not passing trials.

Package tests, cloud resource access and real-device task trials are different
evidence. Ponytail benchmark figures describe upstream Ponytail, not measured
savings from Unified Engineering. See the [evidence index](docs/README.md) and
the candidate validation linked above.

## Source layout and licences

`content/` owns maintained instructions and metadata; `inputs/` contains pinned
upstream evidence; `tools/build.py` assembles/checks the package; `tests/` and
`docs/` retain tests, research and evidence. Generated archives live in ignored
`dist/`. Read [development](docs/DEVELOPMENT.md),
[contributing](CONTRIBUTING.md) and [agent instructions](AGENTS.md) before edits.

MIT, with the four original complete MIT notices retained. The package maps 52
selected upstream skill definitions. New candidate references are independently
authored; reviewed influences do not become installed dependencies or copied
third-party implementations. Keep LICENSE, original notices, ATTRIBUTION.md and
SOURCES.json when redistributing. Exact file-specific terms must be checked
before any future import. No upstream endorsement is implied.

When adding or changing a source/integration, update the tables above with what
we use, how it is included, which version contains it, activation/dependencies
and the checks actually completed. Keep source revisions/notices in sync; do not
list a researched or optional project as an installed add-on.
