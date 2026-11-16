---
name: review
description: "Use when reviewing a diff, pull request or code change, or when responding to review feedback. Not for a whole-repository audit, implementation request or automatic repeated review of an unchanged diff."
---
# One evidence-backed review

{{POLICY}}

A review request is read-only unless fixes are also requested. Establish the target diff/range and intended behavior; read affected code, callers, tests and relevant constraints. For a whole-repository assessment use `ponytail-audit` instead.

Review tests and observable behavior, then correctness, security/data loss, expected load/concurrency, performance and unnecessary complexity. Check changed contracts against every caller. Judge trade-offs against the actual use and expected scale. Do not report style taste or speculative abstraction preferences as defects.

Every finding needs a concrete trigger, affected location, consequence and smallest useful fix. Verify that the flagged input/path/caller really exists. A documented shortcut is a finding only when requirements or expected load cross its limit. Deduplicate findings from specialists into one list:

- Must fix: wrong behavior, security, data loss or failure at expected load.
- Should fix: a meaningful missing test, maintainability fault or real slowdown.
- Optional: useful, lower-impact improvement with a stated benefit.

Explain findings in plain language; include a verdict and checks/areas not covered. No finding is better than invented concerns. Do not count the absence of an unavailable tool as a code bug.

For feedback reception, verify each suggestion against the contract and code before implementing. Resolve ambiguous feedback, explain incorrect recommendations with evidence and accept valid corrections without performative agreement. Keep review and fixes within the requested scope.

One consolidated pass per coherent change is the default. Re-review changed risk boundaries or unresolved substantive findings; do not re-run independent reviewers on an unchanged artifact. Fresh-context/external-model review belongs to explicitly requested `challenge` or `delegate` and requires real permitted tools.
