---
name: test
description: "Use when adding or changing meaningful behavior, fixing a logic bug, writing tests, or diagnosing test quality/flakiness. Not to impose unit tests on prose, generated output or purely mechanical edits."
---
# Prove behavior with meaningful tests

{{POLICY}}

Detect the stack, existing runner, test conventions and actual project command. Use what is installed. Identify the observable failure a proposed test must catch before writing it.

For new substantive behavior or logic fixes:

1. Write a small behavioral test, using realistic boundary inputs and existing fixtures. A bug test reproduces the reported defect.
2. Run it before the implementation. Confirm it fails for the missing behavior, not a typo, broken setup or unrelated error. A passing baseline test does not demonstrate a regression.
3. Make the minimum complete change that passes it. Refactor only while evidence stays green.
4. Check adjacent behavior and relevant project gates. Use the full suite when required by project rules or needed to establish integration; state any broader check not run. Reuse valid results for unchanged state rather than repeating the same expensive suite without a reason.

Prefer real implementations and assertions on outcomes. Mock only real external boundaries with understood side effects. Do not test mock call choreography or create production flags solely for a test. Keep test helpers in test utilities, names descriptive and assertions specific. Cover empty/error/permission/race cases where the boundary makes them real.

For behavior-preserving refactors, establish existing behavior before changing it. For docs/configuration/mechanical changes, use inspection, parsing, schema validation, build or a focused smoke check as appropriate; do not invent logic tests just to satisfy ceremony. Never delete user work to recreate a test-first sequence.

Consult [test quality](references/writing-good-tests.md) and [testing patterns](references/testing-patterns.md) for relevant cases. UI claims need an actual browser/runtime check when available; otherwise report that limit. Never disable tests or lower thresholds to claim success.
