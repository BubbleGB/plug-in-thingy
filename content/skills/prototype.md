---
name: prototype
description: "Use when asked for a throwaway demo, feasibility spike or UI/state-model experiment to answer a specific design question. Not for production implementation or an automatic stage before every feature."
---
# Prototype to settle one question

{{POLICY}}

Name the uncertainty and the observation that would answer it before writing
code. A state/logic question needs visible transitions and inspectable state;
a visual question needs a few meaningfully different arrangements. Do not build
both unless the task needs both.

Choose the smallest runnable artifact: a single HTML file, a focused local script
or an existing project route. Reuse the stack without adding a package/service
for the demo. Mark files and output as prototype work. Use synthetic in-memory
data by default; production credentials or database URLs are not permission to
connect. Keep existing application code and user data intact.

Exercise the specific success and failure paths that decide the question. Expose
relevant state and assumptions instead of hiding them behind polish. A throwaway
demo may use smoke/manual checks instead of a production test suite, but required
data protection, validation at real boundaries and honest reporting still apply.

If a browser/runtime is missing, provide the artifact and run instructions and
state exactly what was not observed. Creating HTML does not prove interaction,
accessibility, hosting or device compatibility. Do not invent a preview URL.

Record the answer, evidence and remaining uncertainty. Keep, discard or turn the
demo into production only within actual user scope; do not auto-commit a throwaway
branch or promote unverified code. Transfer the learned requirement to the
existing design, not a new parallel specification.
