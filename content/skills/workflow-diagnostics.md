---
name: workflow-diagnostics
description: "Use when the user explicitly asks why a skill session repeated work, missed activation, ignored a plan or consumed too much time/context, or requests a workflow bug report. Not automatic session monitoring."
---
# Diagnose observed workflow behavior

{{POLICY}}

Identify the actual symptom and useful session/turn range from the user's evidence before searching. Use only accessible transcripts, task artifacts and tool results. Managed cloud history may not exist on disk; do not trawl unrelated caches or imply unavailable access.

Build a small timeline: user instruction, selected skill/reference, action, result and unnecessary repetition or missed requirement. Separate elapsed time, agent execution time, token counts and estimates. Every number needs an observed source; do not fabricate billing or savings from prose length.

Compare against the effective task and policy, including existing approvals, capability restrictions and external failures. Distinguish discovery failure from adherence failure and content conflict. An unavailable tool is not proof that the skill was never loaded. Read only the evidence needed for the issue; no mandatory seven-analyst fan-out.

Report concrete findings with file/line or turn/tool references, likely cause, uncertainty and a bounded correction. If evidence is missing, state what cannot be established and the smallest next test.

Prepare an upstream bug-report draft only when requested. Redact secrets, personal data and unrelated content. Do not upload transcripts, publish an issue or send a message without explicit authorization for the exact action. No hidden session collection or telemetry is supplied.

For a requested retrospective, recommend improvements to navigation, existing
check commands, misleading instructions and unnecessarily costly tool use. Check
whether a guardrail already exists before proposing another. Mechanical mistakes
may deserve an existing linter/CI check; judgment calls may deserve a concise
rule. A report-only retrospective does not authorize installing tools, editing
global instructions or creating hooks.
