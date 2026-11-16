---
name: migrate
description: "Use when replacing or retiring an API, feature, dependency, data schema or system, especially when compatibility, staged migration or rollback matters. Not for incidental renaming."
---
# Replace safely before removing

{{POLICY}}

Identify consumers, persisted data, version overlap and actual rollback constraints. Verify a replacement before retiring the working path. Do not treat a source search as proof that an external client no longer uses an API.

For production data changes, prefer expand/contract: add compatible structures, deploy code that supports both states, backfill with bounded/restartable work, observe migration, switch consumers, then remove obsolete structures only when authorized and proven unused. Consider read/write concurrency, retry/idempotency, partial failures and how newer data affects rollback.

For APIs/features, provide a clear replacement and transition boundary, with deprecation notices appropriate to the audience. Migrate thin slices and measure actual remaining use. Avoid permanent dual implementations and speculative adapters; document an exit criterion for necessary temporary compatibility code.

See [migration patterns](references/technical-details.md). Verify old/new paths, mixed-version operation, failure recovery and backup/restore assumptions as relevant. A migration script parsing successfully does not establish safe production execution. Keep destructive operations behind actual authorization; report what is prepared versus what has run.
