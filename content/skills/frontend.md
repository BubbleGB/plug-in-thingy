---
name: frontend
description: "Use when building or changing user interfaces, components, state, layout, responsiveness or accessibility. Not for backend-only tasks or unrelated design-system setup."
---
# Interfaces that work for their users

{{POLICY}}

Start with the user's intended action, reference/design system and existing house components. Use the project's framework and styling conventions; do not add a UI library for a few elements or impose a new visual language.

Keep component and state responsibilities clear. Store only necessary state, derive values where possible, and handle async errors, races and loading consistently. Include meaningful loading, empty, error and success states. Preserve form values and focus through transitions.

Use semantic controls, labels, keyboard navigation, visible focus and appropriate screen-reader announcements. Verify color contrast and reduced-motion behavior where relevant. ARIA supplements semantics; it does not replace native elements. Check narrow/wide layouts and realistic long/empty content, not only the happy screenshot.

Consult [UI patterns](references/technical-details.md) and [accessibility checks](references/accessibility-checklist.md) selectively. Verify with the project's available runtime/browser tools. Code inspection, a build and a screenshot prove different things; report actual coverage. Do not assert WCAG compliance or mobile-device testing from a lint pass or resized desktop alone.

For visual creation or polish, use the focused [visual review](references/visual-review.md):
hierarchy and content first, existing design tokens, translated/RTL stress cases
and purposeful motion with interruption/reduced-motion behavior. Keep checks
proportionate; this does not start another design workflow or impose a new style.
