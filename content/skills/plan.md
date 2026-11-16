---
name: plan
description: "Use when agreed requirements need a multi-step implementation plan, dependencies or acceptance criteria. Also use when explicitly asked to plan. Not for an adequate existing task list or a small obvious edit."
---
# Plan verifiable slices

{{POLICY}}

Read the agreed design and relevant code. Check existing plans and open tasks before writing another. If the plan already specifies adequate steps, use or update it rather than duplicate it.

Map affected callers, tests, exports, fixtures, configuration and data boundaries. Follow project structure. Order work by actual dependencies and uncertainty; aim for small deliverables that can be verified independently. Fold scaffolding and documentation into the deliverable they support.

For each task record:

- The observable outcome and files/components affected.
- Interfaces consumed/produced where tasks meet.
- Acceptance criteria, relevant error cases and verification commands.
- Prerequisites and any material risk/rollback requirement.

Tests describe behavior rather than duplicate an anticipated implementation. Do not fill the plan with complete function bodies, repetitive review ceremonies or mandatory commits for every step. Flag unavailable tools and uncertain commands instead of inventing them.

Use the project's existing plan/task convention, otherwise a single document under `docs/engineering/` for substantial work. Never overwrite another incomplete plan or manipulate an external tracker without authorization. A small plan may remain in conversation.

Present the plan when requested or when consequential choices require review. If the user already authorized execution and delegated routine decisions, continue into `implement`; do not add another approval solely because a planning step occurred. A planning-only request ends with the plan.
