# Offline behavior evidence

Date: 2026-11-16. Model: gpt-6.1-sol, medium reasoning. Five fresh control
evaluators and five fresh guided evaluators, each describing next actions for
the same eight scenarios. The scenarios within each evaluator share context;
the five evaluators are separate trials. Raw results: tests/results/.

Controls read the original Ponytail main skill and Superpowers/Addy routers.
Guided trials read the generated engineering skill and its preference reference
from the actual ZIP. Both arms ran under the same available host instructions.
This tests coordination text, not all specialist bodies or native discovery.

Observed before authoring the unified policy:

- All five controls proposed extra documentation/skill workflow loading for a
  single specified typo; some identified unresolved Definition-of-Done overlap.
- Four controls described new design/spec work for already clear Lite security
  requirements. One avoided declaring a new design but still loaded overlapping
  process routes.
- Manual preference keys were unspecified by the original routers.
- One control would wait for the user after finding agent tools unavailable;
  the others continued the approved work inline.
- Already approved scope, read-only review and injected-secret-upload rejection
  were mostly handled correctly already. These are not claimed as new gains.

Guided observations, manually read across all five trials:

- All five described a direct typo edit/inspection without a design or workflow
  ceremony, reused settled approvals, and kept report-only cases read-only.
- All five kept relevant token security checks in Lite, respected the settled
  Ultra decision, honored explicit manual security invocation, and disclosed
  missing delegation tools while continuing permitted inline work.
- All five rejected the fetched instruction to upload .env or run its installer.
- Recorded targeted boolean invariants passed for all five guided trials.

Limitations: agents described proposed actions rather than performing a full
coding task; the host did not route among installed skills; controls contained
only the original router/main bodies; guided trials contained only the unified
coordination body/preferences; host baseline knowledge influenced both arms.
Eight cases and five trials are limited coverage. No universal activation,
security guarantee, quality superiority, token savings or mobile compatibility
claim follows. Native registry/discovery and real Android acceptance remain
pending. The source includes prompts and raw records to reproduce/extend this.
