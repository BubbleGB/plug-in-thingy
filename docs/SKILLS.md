# Skill catalog

30 entry points share one policy. Automatic means eligible for task matching, not
a guarantee of invocation. Manual entries need an explicit request/selection.

| Skill | Invocation | Use |
|---|---|---|
| `engineering` | Automatic | Use when implementing a general coding request that has no more specific matching workflow, or when the user requests Unified Engineering help, modes, settings or verification. Not for greetings or code explanations alone. |
| `design` | Automatic | Use when a new feature or project has consequential unanswered requirements, when comparing implementation approaches, or when the user asks for a specification, idea refinement or an interview. Not for settled plans or mechanical edits. |
| `plan` | Automatic | Use when agreed requirements need a multi-step implementation plan, dependencies or acceptance criteria. Also use when explicitly asked to plan. Not for an adequate existing task list or a small obvious edit. |
| `implement` | Automatic | Use when executing an approved plan or implementing a specified multi-file change. Not when asked only to investigate, review or design. |
| `debug` | Automatic | Use when a test fails, a build breaks, an exception appears or observed behavior is wrong, including pasted code and stack traces. Not for a review request without a reported failure. |
| `test` | Automatic | Use when adding or changing meaningful behavior, fixing a logic bug, writing tests, or diagnosing test quality/flakiness. Not to impose unit tests on prose, generated output or purely mechanical edits. |
| `review` | Automatic | Use when reviewing a diff, pull request or code change, or when responding to review feedback. Not for a whole-repository audit, implementation request or automatic repeated review of an unchanged diff. |
| `ponytail-audit` | Automatic | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Ranked, each finding explained in plain English. One-shot report, changes nothing. Use for "audit this codebase", "review the whole repo", "find bloat", "what can I delete", /ponytail-audit. |
| `simplify` | Automatic | Use when asked to simplify, clean up or reduce nesting in working code without changing behavior, including pasted functions. Not for a performance complaint or feature redesign. |
| `ship` | Automatic | Use when preparing commits, changelogs, branches, pull requests, releases, deployment readiness or rollbacks. Not as an automatic deployment step after coding, and not for ordinary code review. |
| `api` | Automatic | Use when designing or changing an API, public interface, module boundary, REST/GraphQL contract, pagination or idempotency behavior. Not for every internal code edit. |
| `browser` | Automatic | Use when a browser application needs runtime, visual, accessibility, DOM, console, network or interaction verification. Not for server-only tasks or proof based solely on source inspection. |
| `ci` | Automatic | Use when creating, fixing or changing CI/CD pipelines, automated quality gates, build caches, deployment automation or CI failure reporting. Not to add CI to unrelated edits. |
| `migrate` | Automatic | Use when replacing or retiring an API, feature, dependency, data schema or system, especially when compatibility, staged migration or rollback matters. Not for incidental renaming. |
| `docs` | Automatic | Use when writing or repairing substantive documentation, API guides, architecture decisions, onboarding instructions or checks for documentation drift. Not as a prerequisite for a one-word typo. |
| `frontend` | Automatic | Use when building or changing user interfaces, components, state, layout, responsiveness or accessibility. Not for backend-only tasks or unrelated design-system setup. |
| `observe` | Automatic | Use when adding or repairing logs, metrics, tracing, alerts, correlation IDs or evidence of production behavior. Not to introduce a telemetry platform for an unrelated feature. |
| `performance` | Automatic | Use when investigating slowness, performance regressions, resource growth, expensive queries or a stated latency/load budget. Not for speculative optimization or general code simplification. |
| `security` | Automatic | Use when handling untrusted input, authentication, authorization, secrets, personal data, uploads, webhooks, dependency risk or an explicit security assessment. Not to start a separate workflow for every code edit. |
| `context` | Automatic | Use when preparing an agent handoff, recovering lost task context, repairing project instructions or diagnosing degraded outputs from missing/excess context. Not automatically at every session start. |
| `standards` | Automatic | Use when explicitly setting project quality standards, coverage/performance ratchets or checks against weakened tests and budgets. Also when a task is evading established checks. Not just because CONSTRAINTS.md is absent. |
| `sources` | Automatic | Use when version-sensitive or uncertain framework/library behavior needs authoritative documentation, or when the user explicitly requests source-verified guidance. Not to refetch familiar APIs for every local edit. |
| `delegate` | Manual | Use when the user explicitly asks for subagents, parallel agents or delegated execution. Not automatically for multiple files, independent tasks or an ordinary review. |
| `challenge` | Manual | Use when the user explicitly requests adversarial, fresh-context or skeptical review of an assumption, design or critical change. Not an automatic extra review on every decision. |
| `skill-authoring` | Manual | Use when explicitly creating, changing or evaluating reusable agent skills or their discovery metadata. Not as an automatic dependency of ordinary documentation work. |
| `workflow-diagnostics` | Manual | Use when the user explicitly asks why a skill session repeated work, missed activation, ignored a plan or consumed too much time/context, or requests a workflow bug report. Not automatic session monitoring. |
| `ponytail-debt` | Manual | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did ponytail defer", "list the shortcuts", /ponytail-debt. |
| `ponytail-gain` | Manual | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytail impact". |
| `architecture` | Automatic | Use when assessing module boundaries, unnecessary wrappers, interface complexity, testability or a requested architectural refactor. Not to redesign a codebase during an unrelated small edit. |
| `prototype` | Automatic | Use when asked for a throwaway demo, feasibility spike or UI/state-model experiment to answer a specific design question. Not for production implementation or an automatic stage before every feature. |

The installed 0.2.0 cloud package exposed 24 automatic entries while all 30
skills remained explicitly readable. Listing behavior and UI can differ by host.
See [validation](VALIDATION-0.3.md) for the exact evidence and remaining limits.

Full/Lite/Ultra change scope/complexity guidance, not the correctness floor.
Use “engineering help” for modes, “engineering verify” for evidence checks, and
ordinary task requests for relevant workflows. A review-only request stays read-only.

Version 0.3.0 keeps discovery descriptions and invocation policy unchanged.
Five conditional references enrich frontend, security, architecture, docs and
skill-authoring; no new top-level skill, router or automatic agent workflow is added.
