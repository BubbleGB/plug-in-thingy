# Make audit claims traceable

Use for requested security audits or a focused finding that needs a defensible
record. Ordinary security-sensitive implementation needs relevant checks, not a
new audit project. Stay read-only for a report-only request. Keep records inline
unless persistent artifacts are requested or already part of the authorized
deliverable.

## Fix the scope and evidence state

Identify the actual code revision or snapshot, relevant uncommitted changes,
target surfaces, assets and lower-trust principals. Map the boundary each check
must establish: who can act on which resource, through what input, and with what
authority. Review existing relevant evidence before repeating work. Changed
code or configuration can invalidate earlier conclusions.

For a broad audit, keep a small coverage table: surface/boundary, check performed,
observed result, evidence location and disposition. Distinguish inspected,
blocked, and deferred work. An inspected function is not necessarily a tested
boundary. Record important exclusions and the budget actually used; do not
inflate coverage with a count of files or searches.

## Separate observations from conclusions

Use these dispositions when reporting candidates:

| Disposition | Required basis |
|---|---|
| Confirmed | Current source trace and bounded decisive evidence establish the boundary failure, affected principal/resource and conditions. State exactly what that evidence proves. |
| Needs validation | A plausible source-grounded lead remains, but a specific prerequisite, configuration or runtime fact is missing. Name it and the smallest next check. |
| Rejected | Evidence disproves the candidate or the alleged security consequence. Keep the reason if it explains a disagreement or prior finding. |

A deterministic source proof may establish a defect without executing it; name
that basis. When the conclusion depends on runtime behavior, report the actual
observed result or retain the lead as needs validation. A test that is installed,
planned or copied from an example is not a result. Do not require a web endpoint
for a library, CLI, worker, mobile or infrastructure finding.

Assign vulnerability severity only after impact and conditions are established.
Do not give an unresolved deployment assumption a confident severity or promote
hardening advice into a vulnerability. A rejected hypothesis is not a low-severity
finding just to keep the report populated.

## Try to disprove the finding

Trace reachability, ownership and controls across the actual call path. Ask
whether a trusted value, public resource, fixture, existing authorization check
or deployment prerequisite changes the claim. Use synthetic local inputs and
the real resource contract where execution is authorized and contained. A request
for a source audit does not authorize probing deployed services or running an
untrusted target's install/build scripts with ambient credentials.

An independently requested reviewer must recheck the source and decisive evidence;
do not call a reread by the original investigator independent verification.
Use another agent only when explicitly authorized and actually available. Record
missing independent review instead of inventing it or launching a team by default.

## Finish proportionately

For each confirmed issue report the current source location, conditions,
principal/resource, trace, decisive evidence, bounded impact, smallest effective
fix and a meaningful regression check. Keep unresolved leads and their exact
blockers separate. Exclude secrets and unrelated user data from evidence.

If time or tools run out, report a partial audit: what was checked, blocked and
deferred, plus which conclusions remain supported. No confirmed issue in the
inspected scope is not proof of a clean repository. Revalidate materially changed
evidence before retaining a conclusion; do not silently reuse a stale report.
