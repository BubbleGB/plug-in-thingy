---
name: standards
description: "Use when explicitly setting project quality standards, coverage/performance ratchets or checks against weakened tests and budgets. Also when a task is evading established checks. Not just because CONSTRAINTS.md is absent."
---
# Keep the project's quality bar honest

{{POLICY}}

Read existing project constraints, tools and baseline before proposing numbers. Do not weaken established tests, budgets or security checks to make a change pass. A missing standards document does not authorize installing a checker suite.

For requested setup, choose only dimensions the user/project needs. Measure the current baseline and agree on thresholds or a no-regression ratchet where useful. Record the rule, real command, scope, stage, owner and any time-limited exception in the existing convention or a concise CONSTRAINTS.md. Do not invent coverage from source inspection.

Use existing validators first. Fast checks belong near edits; expensive integration, mutation or browser checks belong at task boundaries or CI. A written rule is advisory until a real enforcing command/CI gate exists. No lifecycle hook or automatic post-edit runner is installed by this skill.

At review, inspect the diff for lowered thresholds, removed/skipped assertions, unimplemented stubs, new suppressions and unexplained exceptions. Distinguish a justified scoped exception from silently weakening the bar. A repository with known legacy failures needs an explicit baseline, not a false green claim.

Consult [ratchet and guard patterns](references/technical-details.md) and the [floor guard example](references/floor-guard.md). Treat examples as optional project integrations: review them and dependencies before execution, adapt to the actual stack and do not claim universal enforcement.
