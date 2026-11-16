---
name: design
description: "Use when a new feature or project has consequential unanswered requirements, when comparing implementation approaches, or when the user asks for a specification, idea refinement or an interview. Not for settled plans or mechanical edits."
---
# Design one coherent solution

{{POLICY}}

Read available requirements, project instructions and related code before asking anything. State the intended outcome and the uncertainty that would materially change it. Do not ask the user to repeat supplied context.

1. Establish who needs the outcome, what success means and which constraints matter. Ask one useful question at a time only where the answer changes the solution. Offer a reasonable assumption for reversible details when authorized.
2. Compare two or three viable approaches if there is a real choice. Recommend the least complex one that meets the need, explaining its trade-off. If there is one sensible approach, say so; do not invent alternatives.
3. Describe behavior, boundaries, affected components, data/API changes, acceptance criteria and verification. Reuse an existing specification or record only its delta. Use a short note for a small decision and a project-convention design document for substantial work.
4. Respect any requested approval boundary. Otherwise, clear authorized tasks can proceed without an extra process gate. Approval of an already presented design is not a reason to ask again. Do not begin implementation when the user explicitly requested design only.

Manual procedures: “interview me” explores missing intent; “refine this idea” explores variants before converging; “write a spec” captures testable behavior. They are procedures within this workflow, not three compulsory phases. Avoid numerical confidence claims and an extended interview for a complete brief.

For larger systems, identify independently testable capabilities, dependencies and deferred scope. Preserve necessary security/privacy/accessibility requirements. Hand the agreed outcome to `plan` only when decomposition would help; the design is not a transcript of implementation.

When business terms collide, use [shared vocabulary](references/domain-vocabulary.md)
to resolve the actual concepts against code. Read existing terms first; do not
create a glossary or ADR for an explanation-only request. A cheap prototype can
settle a concrete uncertainty when requested; it is not another compulsory phase.
