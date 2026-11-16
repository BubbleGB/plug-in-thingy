---
name: docs
description: "Use when writing or repairing substantive documentation, API guides, architecture decisions, onboarding instructions or checks for documentation drift. Not as a prerequisite for a one-word typo."
---
# Document behavior and decisions accurately

{{POLICY}}

Read the implementation and existing documentation conventions. State what the system actually does, who the instructions serve and the command/path/version that can substantiate them. Do not turn plans into claims of shipped behavior.

Use a decision record when an architectural choice has lasting consequences, alternatives or a non-obvious constraint. Record context, decision, trade-offs and status succinctly. Follow existing locations/naming; do not create a second documentation hierarchy for the plugin.

For user/API instructions, include useful inputs, output/error behavior and prerequisites. Verify commands, links, examples and version-specific claims. Avoid comments that merely narrate code; document reasons and known limits. Keep sensitive information out of examples.

For drift, map changed public behavior/configuration to its documentation and identify stale or conflicting instructions. Add a lightweight existing CI check only when requested or necessary for this scope, not a new doc framework. See [documentation patterns](references/technical-details.md).

Finish with the concrete documentation change and what was checked. An ADR, README or generated API reference is not runtime evidence by itself. Plain explanations need no development lifecycle or edits unless requested.

For domain terminology, apply [shared vocabulary](references/domain-vocabulary.md).
Record the resolved meaning, not a pile of implementation notes. Keep existing
context boundaries and useful project terms; a naming discussion alone does not
authorize a code rename or new persistent documents.
