---
name: simplify
description: "Use when asked to simplify, clean up or reduce nesting in working code without changing behavior, including pasted functions. Not for a performance complaint or feature redesign."
---
# Simplify without changing the contract

{{POLICY}}

Read callers, tests and the reason the code exists before deleting or merging it. Establish current behavior, including awkward edge cases users may depend on. Reuse existing project idioms; readability wins over a clever shorter expression.

Identify one concrete simplification: dead code verified across dynamic/config references, duplicate behavior, needless conversion, redundant state, unnecessary indirection or deeply nested control flow. Preserve validation, error handling, ordering, return types and accessibility behavior. Move behavior only with the tests and callers it needs.

Make a small behavior-preserving change and run existing meaningful tests. Add a regression check when behavior was unprotected or a tempting rewrite changes edge cases. If a proposed simplification would change behavior, surface that explicitly rather than call it equivalent.

Respect `simplify-ignore-start`/`simplify-ignore-end` markers and project-protected blocks. Inspect the diff to ensure their original content remains intact. The plugin does not hide these blocks, replace them with placeholders or guarantee enforcement through hooks.

Do not refactor adjacent systems or add a new abstraction just to make one function shorter. Split by responsibility, not a line-count quota. Report what became easier to understand and any material limits to equivalence checking.

See [language patterns](references/technical-details.md) for relevant examples. This skill retains Addy Osmani's acknowledgment of the [Anthropic Code Simplifier inspiration](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md).

Before removing an abstraction, ask whether its complexity would move back into
callers. Keep useful ownership, retry and consistency policy centralized. An
architectural assessment is a separate requested scope, not permission to expand
this cleanup into a codebase redesign.
