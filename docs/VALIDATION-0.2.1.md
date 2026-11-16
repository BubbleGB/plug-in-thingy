# Unified Engineering 0.2.1: self-improvement evidence

The installed Unified Engineering review, test, debug, engineering and
skill-authoring guidance was used to improve the plugin's own release boundary.
No new skills, agents, dependencies, lifecycle hooks or services were added.

## Actual cloud checks on installed 0.2.0

The cloud registry listed 24 automatic skills. All 30 skills, including the six
manual-only entries, were directly readable by package/resource name. All 95
packaged Markdown bodies and references were fetched through the cloud skill API
and matched the 0.2.0 ZIP byte-for-byte. Full per-resource results and the matched
release hash are in CLOUD-SMOKE-0.2.json.

This verifies discovery/resource retrieval for that installed package. It does
not prove reliable implicit activation for every task, a manual @ picker UI,
standalone behavior with other routers disabled, Android device UI actions,
lifecycle hooks, or installation of this new patch. The current session still has
other plugins available. Version 0.2.1 is delivered separately for upload.

## Defects reproduced and fixed

1. A malformed agents/openai.yaml or a quoted boolean was previously accepted.
   The generated metadata subset is now validated; duplicate/unsupported fields,
   invalid values and non-file metadata paths are rejected. Effective invocation
   flags must agree with the source map, including omitted manual-only metadata.
2. A skill folder without SKILL.md was silently omitted. The inspector now
   reports it before packaging instead of losing the skill.
3. Invalid UTF-8 reference/anchor content raised an exception. It now produces a
   readable validation error and cannot replace an existing good ZIP.

All failures were recorded with regression tests before their fixes. The suite
now has 24 tests, all passing. The single consolidated review was a self-review
using the installed review guidance, not an independent reviewer. It checked the
changed validator, its callers, source-map policy and preserved archive output;
no additional substantiated issue remains from that pass.

The metadata parser is deliberately limited to this project's generated profile:
string interface fields and boolean invocation policy. It is not a complete YAML
or general OpenAI metadata schema validator. Optional metadata remains optional
for ordinary automatic skills; a source-map manual flag must remain enforced.

## Release checks

The 30-skill inventory, 52 selected source definitions, four original MIT notices
and three byte-preserved Ponytail skills are unchanged. Root/compatibility
manifest identity, required per-skill references, official portable manifest
schema and archive structure are checked. Final extracted-source tests/rebuild
results are delivered beside the ZIPs, with SHA-256 checksums.

Existing installations and 0.1.0/0.2.0 archives are retained. No application
repository was changed. Help now distinguishes manual-only list omissions from
missing content and distinguishes resource reading from actual invocation/UI
support. No universal runtime compatibility or token/cost savings is claimed.
