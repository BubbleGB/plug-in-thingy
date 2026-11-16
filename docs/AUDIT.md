> Historical research/design baseline. The user subsequently approved implementation in conversation; status lines below reflect the proposal stage.

# Unified Agent Skills: upstream audit

Date: 2026-11-16. Scope: source structure, instructions, activation, dependencies, licensing, packaging and managed ChatGPT/Codex compatibility. This is an audit, not an implementation or an assertion that a unified plugin works.

The repositories were cloned for inspection under `/workspace/unified-skills-audit/upstream/`. No existing project checkout or installed plugin was changed. No upstream hook, installer, plugin packaging script or model evaluation runner was executed.

## 1. Reproducible source baseline

| Project | Version in manifest | Audited commit | Root skill definitions |
|---|---|---|---:|
| [Ponytail](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) | 5.3.3 | `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` | 6 |
| [Superpowers](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7) | 7.0.2 | `22f0b463e7a5e579904dd6211a520321035526f7` | 15 |
| [Agent Skills](https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563) | 0.6.16 | `39b723ceebf81474d0557c1fecd01eddab585563` | 25 |

Ponytail also contains six generated OpenClaw copies; they are not six additional capabilities. The integration inventory is therefore 46 canonical upstream skill definitions, not 52. Their `SKILL.md` files alone total approximately 79,000 whitespace-delimited words, excluding supporting references. That is package content, not the amount automatically loaded into a prompt: hosts use progressive disclosure.

All three expose `name` and `description` in YAML frontmatter and have `.codex-plugin/plugin.json`. The only literal skill-name collision across their canonical directories is `test-driven-development`, present in Superpowers and Agent Skills. Semantic overlap is much wider.

## 2. Ponytail

**Structure.** Six canonical skills, multiple harness manifests and adapters, Gemini commands, hooks, benchmarks and tests. Root `plugin.json` contains only the name. The Codex manifest points to `./skills/` and `./hooks/claude-codex-hooks.json`; the Claude manifest additionally declares Band functionality and installation configuration.

**Useful behavior.** Reuse existing code and dependencies, prefer platform features, finish the whole requested change, avoid speculative abstraction, preserve security/error handling/accessibility, test meaningful new logic, and identify deliberate limits with `shortcut:` comments. Read-only audit/review skills demand concrete failure cases and connected-code inspection. Debt and benchmark reporting are separate one-shot tools.

**Activation.** The main skill's description matches coding tasks broadly. Its body retains the selected mode within the session. Executable hooks separately inject instructions on SessionStart, propagate them on SubagentStart, and track commands on UserPromptSubmit. Configuration uses environment variables and a local config file. This local mechanism is different from the cloud registry exposing the skill body.

**Dependencies and effects.** The instruction skills do not require npm installation. Hook paths use Node and filesystem state; activation may invoke a repository map. Statusline scripts and Band have additional host integration. Band can maintain a local task ledger and optionally send task data to a configured webhook. These features must not be carried into a managed package as implied background services.

**Portability issues.** Help currently includes Claude installation/update commands, statusline/Band instructions and machine-local mode configuration. Gain reports upstream benchmark averages, not measurements of this integration or the user's repository. Its cited benchmark source must be retained if the skill is shipped. The raw upstream root manifest is not a sufficient specification for a new portable package.

Evidence: [Codex manifest](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/.codex-plugin/plugin.json), [skills](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills), [hooks](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks).

## 3. Superpowers

**Structure.** Fifteen skills plus templates, references, debugging helpers, plan-execution shell helpers, an optional brainstorming web server, lifecycle bootstrap scripts, many harness integrations and tests. There is no portable root `plugin.json` at this revision; the Codex manifest supplies its plugin entry point.

**Useful behavior.** Clarify consequential ambiguity, plan work in verifiable slices, investigate root causes before fixes, use test-first development, verify claims from evidence, handle review feedback critically, isolate work when appropriate, and manage delegation and branch completion.

**Activation.** `using-superpowers` says to load relevant skills before responding, using a very broad 1% applicability threshold. Other supported hosts inject this bootstrap with a SessionStart hook. Significantly, the audited **Codex manifest has `"hooks": {}`**. Its packaging script deliberately excludes top-level hooks. The skill registry is therefore a separate and important activation path.

**Workflow cost.** The current brainstorming skill allows quick, clear tasks to proceed and permits a single-message design when only one sensible approach exists. It still has explicit design/approval gates for larger work. Test-driven development is strict, with exceptions requiring a conversation. Plan execution and subagent execution carry task briefs, ledgers, helper scripts and reviews; they must not both own the same task. Workflow diagnostics can require seven analysts. These are useful options, expensive universal defaults.

**Dependencies and portability.** Core guidance is Markdown. Optional helpers use Bash/Git and common shell tools; the brainstorming companion uses Node; graph rendering needs Node and Graphviz. Delegation needs real host tools and allowed models. Git workflows need a writable checkout and must account for managed/detached workspaces. Claude/Codex adapter examples are not authoritative schemas for this session: the actual host tools win.

**Packaging finding.** `scripts/package-codex-plugin.sh` makes a rootless single archive and omits source-only content. However, it requires a prior official package to seed `skills/*/agents/openai.yaml`, and those metadata files are absent from this checkout. Reusing this script unchanged would introduce an avoidable external build prerequisite. Optional UI metadata should be authored and validated for the unified project instead.

Evidence: [Codex manifest](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/.codex-plugin/plugin.json), [packaging script](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/scripts/package-codex-plugin.sh), [skills](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7/skills).

## 4. Addy Osmani's Agent Skills

**Structure.** Twenty-five skills, seven shared root checklists, some skill-local references, four reviewer/test/security/performance personas, nine Claude commands and Gemini command equivalents, optional hooks, validation scripts and evaluation fixtures. Portable root and Codex manifests identify version 0.6.16.

**General workflows.** Specification, idea refinement, interviewing, planning, incremental implementation, testing, debugging, review and simplification substantially overlap the other projects. `using-agent-skills` is a second workflow router and can describe a sixteen-stage feature lifecycle.

**Specialist value.** API contracts, accessible frontend engineering, browser testing, CI/CD, security and privacy, performance, migration/deprecation, observability, documentation/ADRs, source-verified engineering, context management, project constraints and adversarial review provide substantial additional coverage. Constraint management includes checking that agents have not weakened tests, budgets or suppression rules to make checks pass.

**Activation.** Descriptions support native matching. Crucially, `docs/codex-setup.md` explicitly warns against preloading `using-agent-skills` into always-on context because it stacks a meta-router over Codex's native routing. Its standalone SessionStart script is deliberately not wired by either plugin. Repository `AGENTS.md` is explicitly scoped to contributors working on this repository, not a reusable global rules file.

**Dependencies and effects.** Most skills are instructions. Browser testing explicitly requires Chrome DevTools MCP, whose availability is not established merely by having some other browser tool. The idea helper creates a directory with Bash. The quality-gate helper uses Node. Standards can install tools such as scanners, coverage tooling, Lighthouse and axe according to selected dimensions; these are optional project integrations, not core plugin dependencies. Personas and Claude command declarations are not a portable managed ChatGPT interface.

**References matter.** Many skills reach shared checklists with `../../references/...`. These paths resolve in the complete repository. That does not establish that a cloud registry exposing one skill package can read a sibling or repository-root file. Dependency closure must be repackaged and tested per skill, rather than copying only `SKILL.md`.

**Hooks.** Optional source-document caching intercepts WebFetch and revalidates with HTTP validators. Simplification protection can temporarily replace protected code blocks with placeholders and later restore them. Neither is appropriate to emulate as an invisible lifecycle service in the managed plugin. Preserve the intent through explicit source verification and instructions respecting protected blocks, while documenting the loss of deterministic interception/filtering.

**Adversarial review.** Doubt-driven development uses fresh-context review, bounded cycles and a mandatory offer of cross-model escalation in interactive sessions. This must be adapted for the unified cost policy rather than becoming an automatic extra review of every decision.

Evidence: [Codex setup](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/docs/codex-setup.md), [skills](https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563/skills), [references](https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563/references), [optional hooks](https://github.com/addyosmani/agent-skills/tree/39b723ceebf81474d0557c1fecd01eddab585563/hooks).

## 5. Instruction conflicts and proposed resolution

| Conflict | Actual overlap | Resolution proposed in architecture |
|---|---|---|
| Multiple routers | Superpowers bootstrap, Addy bootstrap, broad Ponytail activation | Native host discovery; one common engineering policy; no stacked startup bootstraps |
| Scope and clarification | Ponytail's smallest complete solution; multiple interview/spec/design paths | One design workflow when material uncertainty exists; respect already-decided scope |
| Testing | Ponytail exempts trivial edits; both other projects broadly require TDD | One test workflow; regression test first for logic bugs, meaningful checks for new behavior, proportionate verification for mechanical edits |
| Planning artifacts | Superpowers dated documents/ledgers; Addy SPEC/tasks/todo conventions | Reuse project conventions; one spec and one task list; no duplicate plans |
| Review | Ponytail review, Addy multi-axis review, Superpowers request/receive/final reviews, doubt cycles | One review owner; specialists contribute findings to it; independent review is deliberate, bounded and capability-gated |
| Delegation | Parallel dispatch, per-task implementers/reviewers, personas, cross-model tools | Inline default; delegate only when requested and permitted; no invented tools/models |
| Context | Both bootstraps plus generic startup/context skills | Load only the workflow and references needed; no always-on multi-router prompt |
| Authorization | Optional skill rules can ask again for already-authorized actions | Host rules and explicit user instructions control; no extra permission invented by plugin preferences |
| Shipping | Branch finish/cleanup, git workflow, deployment and rollout | One delivery workflow; preparing a release does not itself authorize deployment or deletion |
| Persistence | Hook flag files/config, Claude userConfig, cloud conversations | Session inputs first; optional project preferences; no promised global cloud persistence |

The unified policy cannot override host/system/developer rules or suppress another installed plugin's instructions. During testing, unrelated installed routers can still influence the session. Isolation is a test-environment requirement, not something a new skill can enforce against other plugins.

## 6. Licensing and provenance

All three root licenses are MIT:

- Ponytail: `Copyright (c) 2026 DietrichGebert`.
- Superpowers: `Copyright (c) 2025 Jesse Vincent`.
- Agent Skills: `Copyright (c) 2025 Addy Osmani`.

MIT permits modification and redistribution while retaining the copyright and permission notices in copies or substantial portions. The future package should retain all three complete license texts, a human-readable attribution file, and a source map recording repository, commit, original paths and modifications. The unified license must not replace those notices or imply upstream endorsement.

Preserve embedded acknowledgments too: for example, Addy's simplification skill credits Anthropic's Code Simplifier. Before copying auxiliary reference text, assets or helpers, check their own notices and provenance rather than assuming the repository's root license settles every embedded third-party item. Prefer original unified branding and omit unused assets. No secondary license file was found in the inspected checkout trees; that is not a legal clearance of every external link.

## 7. Platform evidence

Official documentation was fetched directly after Parallel Research required authentication and Parallel Fetch hit its anonymous rate limit. The Help Center page returned HTTP 403, so its content was not used as verification. Local text extracts of the three successfully fetched developer pages are in `evidence/`.

- [Package your plugin](https://developers.openai.com/plugins/build/plugins): new portable packages use root `plugin.json`; `skills/` is discovered by convention. `.codex-plugin/plugin.json` remains a compatibility fallback. `extensions.com.openai`, when present as an object, replaces rather than merges the fallback's OpenAI-specific settings. Hooks are supported for manually installed Codex desktop plugins; hook-containing packages are ineligible for the public directory.
- [Build skills](https://developers.openai.com/codex/build-skills): ChatGPT supports explicit `@` skill selection and implicit description matching. `agents/openai.yaml` is optional metadata; `allow_implicit_invocation` is documented. Same-name skills are not automatically merged. Metadata/policy behavior must still be checked on the target managed surface.
- [Submit a Claude plugin](https://developers.openai.com/plugins/guides/submit-claude-plugin): convert reusable commands/personas into skills, remove lifecycle hooks for public submission, and replace Claude userConfig. Required cross-conversation hosted preferences call for an MCP service; task-local inputs can remain skills-only. Its direct Claude-import archive route is distinct from authoring a portable OpenAI package.

The current cloud skill registry was enumerated through both pages: six Ponytail skills and fifteen Superpowers skills are present; no Agent Skills entry was listed. This confirms discovery in this session, not the installed plugins' exact upstream revisions or universal future availability. A Superpowers packaged reference was also readable through `skills.read`, demonstrating a working cloud reference mechanism for that package.

The handoff reports an earlier successful Ponytail upload. Its exact ZIP is not available here for byte-for-byte comparison. There has been no new unified upload, no managed activation evaluation, no Android-device interaction and no lifecycle hook execution verification. Account/Android plugin management UI availability remains a target-runtime question.

## 8. Checks actually run

| Check | Observed result | Scope limit |
|---|---|---|
| Canonical skill scan | 46 definitions; name/description present; names match folders; no scan failures | Lightweight static checks, not a complete YAML/schema validator |
| Manifest JSON parse | 14 inspected manifests/catalogs parse | Parsing is not uploader schema acceptance |
| Cross-project name scan | Two `test-driven-development` definitions | Semantic conflicts need the content audit above |
| Addy `node scripts/validate-skills.js` | 25 skills + 4 personas; 0 errors, 0 warnings | Upstream anatomy checks, not ChatGPT behavior |
| Addy `node scripts/validate-reference-links.js` | 25 skills checked; 0 errors | Repository reference paths/anchors, not cloud package closure |
| Git status | All three audit checkouts clean | No claim about an unrelated repository |
| Cloud registry listing | Ponytail 6, Superpowers 15; no Addy entries listed | Availability in this session only |

No unified plugin has been created. Its future archive, discovery, automatic activation, mode handling and mobile use require the staged acceptance tests in [ARCHITECTURE.md](ARCHITECTURE.md).
