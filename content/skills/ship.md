---
name: ship
description: "Use when preparing commits, changelogs, branches, pull requests, releases, deployment readiness or rollbacks. Not as an automatic deployment step after coding, and not for ordinary code review."
---
# Deliver with evidence and rollback

{{POLICY}}

Match the requested scope. A commit-message request produces a message; it does not authorize a commit or deployment. A release-readiness request assesses readiness. Execute remote writes, publishing, deployment or cleanup only within actual user authorization and host rules.

Inspect Git status, existing edits, branch/detached state and current isolation. Preserve unrelated work. Do not create another worktree when the managed environment already isolates the task. Use atomic commits when requested, with a subject stating the resulting behavior and a body explaining why. Do not blindly stage the whole workspace. Changelog/version changes follow project conventions.

Before a PR or release claim, verify the final state against relevant tests, build, lint, security and documentation requirements. Review unresolved findings. A green local suite is not evidence of a successful deployment. Describe changes and validation for someone who has not seen the conversation.

For actual launch planning, scope [readiness checks](references/launch-patterns.md) to the product: migration order, configuration/secrets, health checks, observability, staged rollout criteria and a tested rollback. Skip inapplicable infrastructure checks rather than invent services. Coordinate existing error budgets and feature flags instead of requiring new ones for every release.

When tools, credentials or branch operations are unavailable, return the prepared artifact/message and the exact remaining step; do not claim a push, PR or deploy occurred. Keep working files and current plugins for rollback. Never infer permission to delete a branch, worktree, old system or deployment because verification passed.
