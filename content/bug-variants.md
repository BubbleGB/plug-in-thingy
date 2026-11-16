# Find related occurrences of a known cause

Use this after understanding a concrete bug and within the authorized repository
scope. It is not a claim to have audited the whole system.

1. Identify the failure condition, missing invariant and trust boundary. Record
   the smallest known failing instance plus a nearby safe case if available.
2. Start with a search that actually finds the known instance. If already fixed,
   use its recorded diff or a fixture as the positive control; no matches in
   current code do not prove the pattern is calibrated.
3. Generalize names or API shapes one at a time. Read each candidate's callers,
   validation and control flow. Use rg first; use supported structural analyzers
   only when a text search cannot express the relevant behavior.
4. Separate confirmed variants from harmless text matches, public-resource paths,
   generated fixtures, and cases already protected by another guard. Similar
   spelling is not the same root cause.
5. Report concrete triggers and minimal fixes for real cases, plus search scope,
   excluded paths and unresolved uncertainty. Add regression coverage for a fixed
   cause as appropriate. Fixes outside the original scope need actual task
   authorization; a hunt/report request does not authorize edits.

Stop when further broadening produces noise without useful coverage. Do not
launch a recursive multi-agent audit, install analyzers, or claim all variants
are eliminated just because the search returned no additional matches.
