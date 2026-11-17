# Use diagrams to answer a specific question

Choose a diagram only when it makes the requested explanation or assessment
clearer. A tiny inline flow needs no architecture project, renderer installation
or persistent artifact. Honor report-only and no-file requests. Reuse the
project's diagram conventions and the host's supported visualization tools.

## Select the useful view

| Question | Useful form |
|---|---|
| Which components exchange data, across which boundaries? | Architecture or data-flow view |
| In what order do calls, returns and failures occur? | Sequence view |
| Which choices, retries and terminal states exist? | Flow or state view |
| Which entities relate, and with what cardinality? | Entity/relationship view |
| When did events occur or where was time spent? | Timeline or measured trace |

Keep the scope to the question. Label edges with the important operation or data,
not just a vague relationship. Show meaningful branches, error paths and trust
boundaries. Use enough detail to support the conclusion; split views rather than
shrinking an entire repository into unreadable boxes.

## Tie factual edges to evidence

Trace the current implementation's entry point through callers, queues, workers,
storage and external boundaries as relevant. Link source locations or an adjacent
evidence key to the important nodes/edges. Record the source revision and material
local changes for a substantial repository map. Distinguish source-supported
structure, runtime observations, assumptions and proposed design.

A planning document's Redis box does not prove that Redis is deployed or used.
An import can suggest a dependency without proving a runtime call. Label a
proposal as proposed; omit unsupported factual edges or mark their uncertainty.
Use observed timestamps/durations only for measured events; label illustrative
timings clearly rather than deriving them from the layout.

## Deliver the smallest useful artifact

Use a small Mermaid diagram when sufficient, or an existing host visualization
for useful interaction. Use standalone HTML/SVG only when sharing/export or the
question justifies it. Do not impose a palette, graph engine or file hierarchy.
When an authorized file is requested, include its editable source where useful.

Check labels, direction, branches and source consistency. For interactive or
rendered artifacts, exercise available controls and inspect the actual output;
report rendering/runtime limits separately from source correctness. A diagram
explains evidence; it is not itself proof that the system ran successfully.
