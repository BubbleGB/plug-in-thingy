---
name: context
description: "Use when preparing an agent handoff, recovering lost task context, repairing project instructions or diagnosing degraded outputs from missing/excess context. Not automatically at every session start."
---
# Keep context relevant and restartable

{{POLICY}}

Establish the current objective, approved scope, repository state and missing evidence. Prefer a small set of relevant project rules, spec, current task, code paths and exact error output over loading a whole repository or every skill.

Resolve apparent conflicts using actual instruction precedence, not whichever text was read last. State material uncertainty; do not infer approval from an undocumented earlier session or an agent's guess. Preserve explicit recorded approvals and completed work rather than restarting the task after compaction.

For an authorized handoff, record: intended behavior, constraints and effective preferences; decisions/approvals with context; changes already made; verification command/result and code state; remaining tasks, blockers and risks. Read actual Git status and artifacts on resume. Do not invent transcript access or claim the handoff is permanently stored unless it was saved through a supported mechanism.

See [context selection patterns](references/technical-details.md). Use existing project rules files only when asked to create/update durable guidance. Never paste all original routers into AGENTS.md or create always-on startup machinery. Keep secrets, unrelated conversation and unnecessary tool output out of handoffs.

Link existing plans, decisions, commits and test logs instead of duplicating
them. Associate approvals with their exact scope and verification with its code
state; changed code makes older results stale. Include the next concrete action
and effective preferences. Save only to an authorized accessible location, and
do not promise another session can read temporary files or unavailable history.
