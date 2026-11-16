---
name: delegate
description: "Use when the user explicitly asks for subagents, parallel agents or delegated execution. Not automatically for multiple files, independent tasks or an ordinary review."
---
# Delegate only when it helps and is supported

{{POLICY}}

Inspect actual host agent tools, schemas, model choices and restrictions. A CLI binary, configuration example or skill description does not prove a delegation capability exists. If unsupported, state the limitation and continue authorized work inline unless the user made delegation a binding requirement. Never fabricate agent output or silently start an external model/service.

Choose independent, bounded tasks without overlapping writes or sequential dependencies. Shared filesystem changes are visible to other agents: assign file ownership, share interface contracts and integrate deliberately. One implementer per coherent deliverable is enough; do not add a reviewer per trivial task.

Give each delegate the requested outcome, exact scope/files, effective mode, relevant project constraints, interfaces, available evidence and completion criteria. Use only supported context/model options. Avoid copying the whole conversation when a focused brief suffices. A child should report blockers and evidence, not recursively spawn another team unless explicitly permitted.

Work on independent tasks locally while agents run. Prefer event-driven notifications and bounded waits over rapid polling; use the host's timing constraints. Reuse the existing agent for substantive fixes instead of relaunching it with the same context.

Integrate and inspect actual changes, verify contracts and test the combined result. A delegate's success report is evidence to check, not a passing build. Use one consolidated review when warranted. Report actual delegation and any fallback, with no invented cost or capability guarantees.
