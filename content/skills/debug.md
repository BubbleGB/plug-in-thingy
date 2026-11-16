---
name: debug
description: "Use when a test fails, a build breaks, an exception appears or observed behavior is wrong, including pasted code and stack traces. Not for a review request without a reported failure."
---
# Find the root cause

{{POLICY}}

An investigation-only request remains read-only. With permission to fix, follow the same evidence path before editing:

1. Read the exact error, expected behavior and recent change. Reproduce with the smallest existing command/input. If reproduction is unavailable, distinguish observations from hypotheses.
2. Trace values across the real failing path, including callers, configuration and external boundaries. Compare a working neighboring case. Add temporary targeted instrumentation only where it can discriminate causes; do not log secrets.
3. State one falsifiable hypothesis and test it. Change one relevant variable at a time. A failing build or import may be an environment issue; check versions/configuration before rewriting business logic.
4. Before the fix, capture the regression in a focused test that fails for the reported reason. Correct the shared cause once and inspect all callers affected by changed behavior.
5. Run the reproduction and appropriate integration/project checks. Remove temporary instrumentation and report the root cause, fix and evidence.

Repeated failed fixes indicate a wrong model of the problem. Re-read the evidence and architecture rather than stack guesses. If the problem is intermittent, bound observation and record timing/load conditions; do not use arbitrary sleeps as proof of correctness.

Consult [root-cause tracing](references/root-cause-tracing.md) or [defense in depth](references/defense-in-depth.md) only when relevant. For test pollution, narrow the order-dependent input before adding retries. “Could not reproduce” is a valid result with documented inputs and limits; it is not proof of a fix.

When the task asks whether the same cause occurs elsewhere, use
[related-bug searches](references/bug-variants.md). Calibrate on a known failing
instance and inspect candidate guards/callers. A text match is not a confirmed
bug, and an empty search is not proof that every variant is gone.
