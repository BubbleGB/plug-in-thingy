# Review the interface against its purpose

Use for requested UI creation, critique or polish. This is a conditional reference,
not permission to restyle a product during an unrelated edit. Keep the existing
brand, component library and user-approved direction. Backend work needs none of
this procedure.

## Establish the visual job

Identify the audience, main action and surface: a marketing page can invite
exploration; a billing form must make choices and consequences easy to scan.
Use real product language and representative content. Fix competing emphasis,
unclear grouping and missing states before adding decoration. A screenshot that
looks attractive is not evidence that the task can be completed.

Choose a few deliberate improvements: a legible type scale, consistent spacing,
alignment and clear emphasis for the primary action. Reuse existing tokens.
Explain how each change helps the task. Do not generate a fresh design system,
install fonts/libraries or demand a brand interview for a local adjustment.
Distinguish visual judgment from measured accessibility or performance results.

## Check content that stresses the layout

- Use real long labels, empty results, validation messages and loading states.
  Keep meaningful actions reachable when content grows or the keyboard opens.
- Check narrow/wide layouts, text zoom and translated strings. Where RTL is in
  scope, inspect logical spacing/alignment, reading order, mixed-direction text,
  icons with directional meaning, and keyboard/focus order. Do not mirror every
  icon or force all text into one direction.
- Keep contrast, visible focus, semantic controls and error recovery intact.
  A compact control must still be operable; truncation must not hide critical
  amounts, consequences or the only way to identify an item.
- Check the rendered result with available host tools, then exercise the main
  interaction and a relevant failure. Group visible fixes into a useful pass;
  avoid restarting review or taking a screenshot after every small edit.

## Motion only when it communicates something

First decide whether motion improves feedback, continuity or orientation. Use
the existing stack and simplest supported transition. Specify initial, active,
interrupted, replaced, dismissed and unmounted behavior where those states can
occur. A toast entering while dismissed must not reappear after its exit.

Honor reduced-motion preferences and keep the state change understandable
without movement. Choose properties, curves and duration for the interaction;
do not apply a universal spring or timing constant. Check interruption, rapid
repetition and cleanup with the project's actual runtime. React Native/Expo
threading and gestures require matching platform guidance and device evidence;
a desktop viewport is not a mobile-device test.

## Report what changed and what was observed

Name the affected surface, intended improvement, content/viewport/flow checked,
and remaining uncertainty. If rendering is unavailable, make useful source-level
changes within scope and say visual/interaction verification is pending. Do not
claim a style gate, browser test, compliance score or design preference was
measured when it was not.
