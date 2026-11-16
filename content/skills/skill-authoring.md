---
name: skill-authoring
description: "Use when explicitly creating, changing or evaluating reusable agent skills or their discovery metadata. Not as an automatic dependency of ordinary documentation work."
---
# Author skills against observed failures

{{POLICY}}

Identify the recurring engineering problem and existing overlapping guidance before adding a skill. Prefer a useful existing entry point or focused reference over another router. Keep deterministic checks in tooling; reserve instructions for judgment.

Write positive/negative discovery cases and representative application/pressure scenarios first. Record baseline behavior without the proposed guidance; do not invent failures. Preserve successful behavior rather than add instructions for a problem the control does not show. For behavior-shaping wording, use repeated fresh samples and inspect every claimed failure.

Write concise frontmatter naming when the skill applies and when it does not. The body states the procedure, evidence/exit criteria and material exceptions. Keep heavy technical references separate, self-contained in the skill package and attributed. Do not rely on executable hooks, another host's tool names or an inaccessible filesystem path.

Repeat the same scenarios with the guidance. Inspect actual actions, not just whether the agent says it used a skill. Close demonstrated loopholes, then verify affected positive and negative cases. Distinguish static lint, offline simulation, host discovery and real runtime tests; one does not prove the others.

Consult [discovery principles](references/discovery.md) for useful naming and progressive disclosure. Its authoring advice is technical reference subordinate to the shared policy: do not import its sample cross-skill dependencies or require every micro-test in unrelated work. Ship a clear compatibility statement and preserve original notices.
