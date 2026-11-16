# Shared domain vocabulary

Use this when meaning is genuinely ambiguous, not as setup for every repository.
Read an existing glossary or context map first. Compare terms with behavior in
the code and ask about consequential disagreement: a paying organization and a
login identity may both be called Account but have different rights/lifecycles.
Do not invent the business answer or mass-rename code during the discussion.

Propose one precise term per concept within the relevant context, with concrete
examples and important distinctions. Respect different meanings in separate
bounded contexts when deliberate. Keep general programming definitions and
implementation decisions out of a business glossary.

Capture resolved terms in an existing appropriate artifact only when writing is
authorized. Otherwise include the proposed entries in the report. A glossary is
created lazily; an explanation-only request should not create files. Use the
[glossary example](GLOSSARY-FORMAT.md) as a format option, not a required layout.

Record a design decision when its trade-off is lasting and would surprise a
future maintainer, not for every naming choice. The [short ADR example](ADR-FORMAT.md)
can help when no house format exists. Never rewrite a settled glossary/decision
just to adopt vocabulary from an imported skill.

Adapted from Matt Pocock's domain-modeling method; the source notice and hashes
are included in the package. The active workflow controls scope and approval.
