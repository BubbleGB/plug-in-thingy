# Unified Engineering 0.3.1 evidence

Local refinement release, 17 November 2026. The user reports updating to 0.3.
We used the installed skill-authoring, intake, evaluation and review guidance to
refine the plugin. Version 0.3.1 itself has not been installed or tested in the
managed host here; an update ZIP does not install itself.

## Actual installed v0.3 check

Ten sampled resources were read through the managed cloud skill API: five skill
bodies and five new 0.3 references. All ten matched the delivered 0.3.0 ZIP byte
for byte. Exact resource paths and SHA-256 values are in CLOUD-SMOKE-0.3.json.
This establishes sampled cloud availability/content, not all resource access,
native routing reliability or Android UI behavior.

## Reproduced defects and refinements

Four new tests were written against 0.3.0 before the fixes. They failed the
intended nine subcases:

1. A local reference could collide with an upstream or generated filename, or be
   listed twice. Existing content was silently replaced or duplicated in the map.
2. Two selections from the same upstream file could claim the same destination
   while the second selection was silently dropped.
3. Changing a recorded reference was accepted and could replace an existing good
   archive. Both legacy verbatim local hashes and adapted packaged hashes were
   ignored by the inspector.
4. Malformed or escaping source-map reference records were ignored.

Assembly now rejects collisions and inconsistent selections. SOURCES.json keeps
original source hashes and adds packaged hashes for the final reference bytes.
Inspection validates reference paths/records and verifies recorded packaged
checksums plus legacy local hashes. A failed check preserves an existing good ZIP.
Older upstream records without packaged hashes remain readable; their original
source hash is not mistaken for the adapted file checksum. Checksums establish
consistency, not a publisher signature or absence of malicious instructions.

Engineering help gains a self-contained add-on/source inventory. It distinguishes
four adapted source collections, Karpathy-inspired principles, ten conceptual
influences, separately configured host tools and installed-versus-source versions.
No new skill, external runtime, hook, scanner or source import is added. Two
prospective help cases extend the earlier scenario file to 16 cases; they are not
reported as fresh model trials. The listing also now credits Matt Pocock.

## Verification

- All 31 package tests pass, including the four reproduced regressions.
- Build, ZIP inspection, reference checks, archive CRC and source mapping pass.
- The previous 0.3.0 archive is still inspectable by the updated checker.
- The four original MIT notices, mapping of 52 upstream definitions and the three
  byte-preserved Ponytail skill files remain intact. No pinned input changed.
- There are still 30 skills, 24 eligible automatic entries and six manual-only
  entries. Names, discovery descriptions and invocation policy are unchanged.
- Official portable manifest validation and independent YAML parsing are separate
  optional checks; they do not add a build dependency.
- A clean source export/rebuild and its checksums are recorded with delivered
  artifacts. GitHub CI/release workflow results apply to their tested commit,
  not arbitrary later changes.

One consolidated self-review checked the code, callers, tests, source inventory,
reference ownership and evidence claims. It is not an independent review. The
earlier CLI authentication failure still limits fresh baseline/candidate model
comparisons; historical model results are not reused as proof of this change.

Use the GitHub release's SHA256SUMS.txt and the delivered verification record for
the exact final artifact hashes. Installed 0.3.0 evidence does not prove 0.3.1
installation, outcomes, token savings or Android acceptance. Keep the old working
ZIP until the new upload passes the actual account/device workflow.
