---
name: observe
description: "Use when adding or repairing logs, metrics, tracing, alerts, correlation IDs or evidence of production behavior. Not to introduce a telemetry platform for an unrelated feature."
---
# Make important behavior observable

{{POLICY}}

Define the operational question before adding signals: did the request work, where did latency go, which entry point caused the job, or which failure requires action? Reuse existing logging/metrics/tracing conventions and backend.

Use structured logs with useful context and severity. Carry correlation and entry-point metadata across HTTP/queue/worker boundaries rather than guessing attribution from a related field. Redact secrets and sensitive data at collection; avoid unbounded labels and excessive payload logging.

Choose metrics for rates, errors, duration and saturation as relevant. Keep cardinality bounded. Sample traces and instrument real boundaries; do not make one log statement stand in for an operational contract. Alerts need an actionable condition, owner/runbook and threshold appropriate to expected traffic, not notification on every exception.

See [instrumentation patterns](references/technical-details.md) and [signal checklist](references/observability-checklist.md). Verify the telemetry itself with a successful and failing flow: fields, correlation, export and alert behavior. Distinguish instrumented code from a signal actually observed in the target system. No automatic external telemetry or webhook is supplied by this plugin.
