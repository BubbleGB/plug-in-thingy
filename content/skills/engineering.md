---
name: engineering
description: "Use when implementing a general coding request that has no more specific matching workflow, or when the user requests Unified Engineering help, modes, settings or verification. Not for greetings or code explanations alone."
---
# Unified Engineering

{{POLICY}}

## Choose the smallest sufficient workflow

Read the request and affected code first. Match the actual intent, not every possible phase:

- Mechanical typo, rename or known configuration correction: make the requested edit and inspect/validate it directly. No design document, unit-test ritual or review fan-out.
- Material uncertainty about what to build: use `design`; a substantial agreed change may need `plan`. An adequate existing design/plan is input, not something to recreate.
- Approved implementation: work in small slices using `implement`; substantive logic and bug fixes use `test`.
- Unexpected failure: `debug`. Review/audit requests stay read-only unless fixes are requested.
- Add relevant domain expertise such as `security`, `api` or `frontend` only for a concrete boundary. Do not load the whole catalog.

One workflow owns the task. Specialists contribute checks; they do not restart its lifecycle. Do not invoke the original Ponytail, Superpowers or Addy routers as prerequisites.

## Completion contract

Before claiming success, identify the evidence required, run appropriate checks, read the complete result and compare against the actual acceptance criteria. Match evidence to the final code/configuration state. Reuse an observed valid run for that unchanged state; rerun when changes or uncertainty invalidate it. Report an unavailable/failing check by name. A passing lint is not a passing runtime test. A delegate's claim is not independently verified evidence.

Manual verification is accessible through “engineering verify”. A verification-only request authorizes checks and reporting, not repairs. End with the concrete result and any material limitation, without invented savings or boilerplate disclaimers.

For help, give the relevant entry from [the catalog](references/catalog.md), the three modes and the @/plain-language invocation options. For original benchmark results use `ponytail-gain`; for deliberate shortcut comments use `ponytail-debt`.

Some hosts omit manual-only skills from automatic listings. Distinguish that
from missing content: use supported explicit selection or package/resource
reading before reporting a catalog skill unavailable. File access alone does
not prove an @ picker entry or automatic invocation works.

For an explicitly requested assessment of module shape, use `architecture`.
For an explicitly requested throwaway experiment, use `prototype`; neither is a
prerequisite for routine implementation. When asked to explain more simply,
state the outcome, the minimum useful context and the next action in plain
language. Do not start a coding workflow or create a teaching workspace.
