# Independent release review and fixes

Read-only whole-project review by a fresh gpt-6-astra reviewer, high reasoning,
against the approved architecture and initial implementation commit `ce323e7`.

Confirmed strengths: complete 46-to-28 source mapping, matching source/reference
hashes and MIT notices, unchanged Ponytail audit/debt/gain, all six intended
manual-only metadata entries, self-contained references and atomic output
replacement. Canonical policy adequately subordinates imported technical advice.

Findings and disposition:

1. Important: equivalent ZIP paths such as `plugin.json` and `./plugin.json`
   bypassed exact-name duplicate detection. Added a regression fixture including
   repeated slashes; observed failure; reject all noncanonical entry paths
   before extraction. Targeted archive tests pass.
2. Important: malformed/non-string YAML descriptions could pass the constrained
   parser. Added invalid quoting, colon, collection and typed-scalar fixtures;
   observed failures; enforce a string-only subset with balanced single/double
   quoting and supported block scalars. Valid quoted/block cases still pass.
   Invalid packaging preserves the existing good artifact.
3. Reviewer labeled Minor: JSON array/null manifests produced AttributeError.
   Treated as a release validation issue worth fixing because users need an
   actionable error for a rejected upload. Root and overlay regression fixtures
   failed first, then passed after explicit object-type validation.

Full suite after fixes: 20 tests, 0 failures/errors. No reviewer findings remain
deferred. Fixes affect validation only; the tested skill bodies/preferences are
unchanged. No repeated independent review was run on the same content.

The reviewer expressly did not certify uploader acceptance, registry discovery,
manual-only enforcement, Android operation, every specialist's adherence, or
every external technical example/API claim. Those limits remain part of the
release statement, not implicitly waived.
