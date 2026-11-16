---
name: performance
description: "Use when investigating slowness, performance regressions, resource growth, expensive queries or a stated latency/load budget. Not for speculative optimization or general code simplification."
---
# Measure before optimizing

{{POLICY}}

Define the relevant workload, baseline and metric before changing code. Use representative data and concurrency, with enough repetition to distinguish a change from noise. Inspect the critical path rather than optimize the easiest visible function.

Profile where appropriate: browser rendering/bundle/network, request latency, database query plans/N+1 patterns, CPU, memory growth, I/O or shared resource contention. Name the bottleneck and a testable hypothesis. A microbenchmark improvement is not proof of end-to-end improvement.

Make one justified change, preserving correctness, invalidation, access control and failure handling. Caching and batching need explicit consistency/resource bounds; do not introduce them on speculation. Measure the same workload after the change. Keep the improvement when evidence supports it, otherwise revert or explain why results are inconclusive.

See [measurement and optimization](references/technical-details.md), [optimization examples](references/optimization-patterns.md) and [performance checklist](references/performance-checklist.md). Use only relevant sections. Add a durable budget/regression check when the project needs one; do not invent numeric targets. Report hardware/environment, workload and uncertainty, not an unsupported percentage.
