---
name: api
description: "Use when designing or changing an API, public interface, module boundary, REST/GraphQL contract, pagination or idempotency behavior. Not for every internal code edit."
---
# Stable contracts

{{POLICY}}

Work inside the active task, not a second planning lifecycle. Identify actual consumers and compatibility promises before changing a public interface. Make the input/output contract and failure semantics concrete before implementation; use existing project schemas/types where available.

Validate at trust boundaries, separate external inputs from trusted domain state, and return consistent errors without internal details. Check missing/empty/invalid values, authorization, retry behavior and the distinction between absent and explicitly null fields. Prefer backward-compatible additions when clients cannot change atomically; document breaking behavior and migration when required.

For pagination, define ordering and continuation under concurrent writes. For retried mutations, define idempotency scope, storage, duplicate/in-flight handling and failure recovery; a header alone does not make a write idempotent. Keep PATCH semantics explicit. Avoid exposing storage models or adding brand types/wrappers unless they prevent a concrete mistake.

Use [contract and API patterns](references/technical-details.md) only for the relevant interface. Verify representative consumers, error cases and compatibility, using integration/contract tests as appropriate. Report any untested external consumers instead of claiming universal compatibility.
