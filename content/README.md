# Unified Engineering 0.1.0

One skills-only engineering plugin combining Ponytail's simplicity, Superpowers' development methods and Addy Osmani's specialist engineering expertise. This is an independent adaptation, not an official release or endorsement by those projects.

## Use it

Select the plugin/skill with ChatGPT's @ picker where available, or ask in ordinary language:

- “Use Unified Engineering to implement this change.”
- “Use Lite mode and fix this bug.”
- “Use Ultra mode, but follow this approved design.”
- “Review this diff only; do not edit files.”
- “Use the security skill to check this input boundary.”
- “Show Unified Engineering help.”

Relevant skills are eligible for native automatic discovery; the host decides when to invoke them. Do not expect every task to load a skill, and do not confuse a local file check with managed registry discovery. Manual invocation is the fallback. Claude slash commands printed by preserved Ponytail cards are historical usage examples, not a promise of an Android slash-command interface.

## Modes

| Mode | Behavior |
|---|---|
| Lite | Requested scope, minimal ceremony; name a smaller option when useful |
| Full (default) | Smallest complete solution; reuse first; proportionate verification |
| Ultra | Additionally challenge unjustified complexity once; respect informed choices |

All modes keep the same correctness, security, accessibility and evidence floor. Mode is not a testing-depth or agent-count setting. Simple tasks stay simple; high-risk work gets the checks its boundaries require.

“Workflow manual” and “specialists manual” suppress optional automatic expansion; an explicitly invoked skill still applies. “Stop unified engineering” suspends optional plugin guidance in this conversation. These preferences cannot override the host or disable another installed plugin.

Session choices take precedence over defaults. An existing project-root `.unified-engineering.json` may supply nonsecret preferences:

```json
{"mode":"full","workflow":"auto","specialists":"auto"}
```

Allowed values: mode=lite/full/ultra; workflow=auto/manual; specialists=auto/manual. The agent reads this as data when relevant; no background parser or global settings service runs. Write it only when asked to save project defaults. New conversations default to Full unless actual project/session context supplies another choice. No guaranteed cross-conversation or compaction persistence.

## What is included

28 entry points. Core: engineering, design, plan, implement, debug, test, review, simplify, ship, ponytail-audit. Specialists: api, browser, ci, migrate, docs, frontend, observe, performance, security, context, standards, sources. Explicit advanced/reporting: delegate, challenge, skill-authoring, workflow-diagnostics, ponytail-debt, ponytail-gain.

One workflow owns the task; specialists contribute relevant checks without restarting planning or review. Verification is a common completion contract and is also available through “engineering verify”. `ponytail-audit`, `ponytail-debt` and `ponytail-gain` retain their original skill-file bytes. Gain displays upstream Ponytail benchmark results, not measured performance of this plugin.

## Install and test on ChatGPT / Android

Use the single plugin upload ZIP, **unified-engineering-0.1.0.zip**. The separate **source ZIP is for maintenance**, not plugin upload. The upload ZIP has one plugin root, a portable manifest and one Codex compatibility overlay. It contains no marketplace catalog or nested original plugins.

Use the actual plugin upload/import flow available to your account. Android/account-specific plugin-management controls may vary; no CLI, Android terminal, Node installation or local MCP server is needed for the plugin's instruction-only core. If the upload is rejected, retain the exact error and archive version; do not turn this into a marketplace archive blindly.

Keep existing working plugins installed. For an uncontaminated standalone test, use an isolated account/workspace or another supported context where overlapping optional routers are not active. A new skill cannot suppress the original plugins' instructions. If that isolation is unavailable, mark results accordingly. Do not uninstall or replace anything until the new plugin passes target-runtime tests and the user explicitly requests replacement.

After upload, check:

1. The cloud registry lists all 28 skills and can read their packaged references.
2. A typo stays a direct edit; an approved plan is reused; review-only requests stay read-only.
3. A logic bug gets root-cause evidence and a meaningful regression check.
4. Lite security work still protects the boundary; Ultra respects settled requirements.
5. Explicit manual specialists work, while advanced skills do not auto-trigger.
6. A fresh session uses defaults; missing browser/agent tools produce honest limitations.
7. One nontrivial task completes in the actual Android Codex workflow.

Static archive/reference tests and offline text simulations are supplied in the source project. They do **not** prove uploader acceptance, native implicit routing, mobile UI behavior or external services. See the delivered validation report for what was actually run.

## No required hooks or services

No lifecycle hooks, statusline, hidden telemetry, task-cost webhook, transcript collector or persistent state service is included. Mode tracking happens through supported conversation/project inputs. Delegation and browser work use only real host tools when available and authorized. Optional project quality tools are not installed automatically. Desktop hook support elsewhere does not prove managed ChatGPT support.

## Licence and origin

MIT. Retain LICENSE, the three original notices in licenses/, ATTRIBUTION.md and SOURCES.json when redistributing. Sources are the user's supplied Ponytail 5.3.3, Superpowers 7.0.2 and Agent Skills 0.6.16 archives. The source map records archive hashes, original skill hashes, consolidation destinations and packaged reference adaptations. No upstream update is downloaded at runtime.
