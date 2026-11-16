# Validation status — 0.1.0

Date: 2026-11-16. This is a locally validated test release, not a claim of managed
ChatGPT/Android runtime certification.

## Passed

- 20 Python standard-library unit/integration tests, including real assembly,
  deterministic rootless ZIP output, source coverage and preserved source bytes.
- Rejection fixtures for traversal, symlinks, raw/normalized duplicate paths,
  broken references/anchors, nested plugins/marketplaces, hook declarations,
  identity mismatch, malformed YAML and non-object JSON.
- A rejected build leaves the previous good archive byte-for-byte unchanged.
- All 28 canonical skills and optional invocation metadata are present; six
  advanced/reporting entries are marked manual-only.
- All 46 original skills mapped; every recorded source/reference hash matches;
  the three original MIT notices and Ponytail audit/debt/gain skill files match.
- All required linked Markdown references resolve inside their own skill
  packages after extraction. No raw original router is installed alongside the
  consolidated workflows.
- Portable manifest validated against the live official schema at
  https://agent-plugins.org/schemas/1.0.0/plugin.schema.json using an already
  available jsonschema validator. Schema SHA-256:
  `0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883`.
  The build itself requires no jsonschema dependency. Codex overlay fields were
  checked against the documented/previously used compatibility layout; actual
  uploader acceptance is still pending.
- Five control and five guided offline behavior trials, eight scenarios each.
  Raw results and limitations are in tests/results and docs/BEHAVIOR.md.
- One offline description-selection exercise matched all 28 intended entry
  points and selected no skill for four negative examples (32/32). All six
  manual entries had explicit named requests. This is model-assisted catalog
  checking, not the actual native skill router.
- Fresh independent release review; all three demonstrated validator defects
  reproduced by regression fixtures and fixed. See REVIEW.md.
- The downloadable source bundle was extracted into a clean temporary folder:
  all 20 tests passed there, and its build reproduced the delivered plugin ZIP
  byte-for-byte. The extracted CLI also inspected the delivery ZIP successfully.
  Raw extracted-source test output is in FINAL-TEST-OUTPUT.txt.

## Required target-runtime acceptance

Not performed: plugin uploader/import acceptance, cloud-registry listing and
reference reads for this new plugin, implicit activation, manual-only policy
enforcement, Android UI/device use, real end-to-end coding with only this plugin,
cross-session persistence, or external service/browser integrations. No upload
or installation API for this custom artifact was exposed in this session.

The plugin cannot suppress separately installed Ponytail/Superpowers rules.
Keep them installed, and test the new ZIP in an appropriately isolated supported
context. If isolation is unavailable, disclose contamination. Only replace old
plugins after an actual standalone acceptance pass and explicit user instruction.

No executable lifecycle hooks, hidden telemetry or required background service
are shipped. No token/cost/time improvement is claimed for this integration.

See content/README.md for Android invocation and the minimal acceptance checklist.
Release SHA-256 checksums are supplied beside the delivered archives.
