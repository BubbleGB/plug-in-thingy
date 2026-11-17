---
name: architecture
description: "Use when assessing module boundaries, unnecessary wrappers, interface complexity, testability or a requested architectural refactor. Not to redesign a codebase during an unrelated small edit."
---
# Assess interfaces by the work they save

{{POLICY}}

Begin with the requested scope and actual pain: a change scattered across callers,
a contract that is hard to use correctly, duplicated policy or tests coupled to
private details. An assessment is read-only unless implementation is requested.

Trace a representative use through callers, interfaces, dependencies and tests.
Include invariants, ordering, failures, configuration and performance in the
interface's real cost, not just its type signature. Ask what complexity would
reappear at callers if an abstraction vanished. A facade that centralizes
authorization, retries or consistency can earn its place even when it looks thin.
Do not delete wrappers solely by line count or class count.

Find the smallest change that improves locality and reduces what callers must
know. Preserve trust boundaries, error handling and required compatibility. A
testable seam may be justified by a real external boundary; do not manufacture
multiple implementations just to satisfy an architectural slogan. Keep useful
project vocabulary rather than forcing a new naming system.

For each candidate, show concrete evidence, affected consumers, expected benefit,
cost and a verification/migration path. Compare alternatives only where they
would change the decision. Recommend no refactor when the benefit is speculative.

Use [module design patterns](references/module-design.md) selectively. Public
behavior and failure cases remain the test surface. Do not automatically remove
old tests: establish that meaningful coverage survives before changing them.
Keep the result in the existing design/review workflow without restarting it.

When a diagram clarifies the requested assessment, use
[system diagrams](references/system-diagrams.md). Trace important edges to the
current code, distinguish proposals and runtime observations, and choose a small
inline view when sufficient. Do not install a graph engine or write artifacts
for a report-only request.
