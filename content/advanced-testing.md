# Optional deeper test methods

These general engineering methods are independently worded for Unified
Engineering. Use them for a concrete coverage need with existing tools first;
they are not required phases or automatic dependency-installation requests.

## Property-based tests

Choose a rule the specification says must hold over a class of inputs. Generate
representative valid and invalid inputs, including boundary values; preserve the
smallest failing input and a reproducible seed. Good candidates include numeric
bounds, ordering laws, idempotent normalization and data-preserving codecs.

A property is not automatically an independent oracle. A serializer and parser
can share a bug; a round trip alone can miss lost information, canonicalization
or a pair that always returns a constant. Compare with hand-checked examples or
an independent specification/reference, and assert relevant information is
preserved. Do not derive expected values with the function under test. Make
preconditions explicit and avoid generators/filters that silently exclude the
interesting domain. A shrunk counterexample can reveal a wrong property as well
as a product bug; inspect both before changing code.

Use Hypothesis, fast-check or the project's installed equivalent when relevant.
If no library exists, explain the specific property and cost before adding a
dependency within authorized scope. A small deterministic boundary table may
already answer the question more cheaply.

## Mutation checks

For requested or justified deep test assessment, make controlled behavior changes
and check whether tests catch them. Work in an isolated temporary copy or an
existing mutation runner; never leave deliberate faults in user work. Bound the
target, time and compute. Document the baseline first so pre-existing failures
are not confused with detected mutations.

A surviving mutation may expose a missing assertion, unreachable code, a timeout
or equivalent behavior. Classify it before adding a test. Do not optimize a score
by silencing mutants, duplicating implementation logic or lowering the quality
bar. Mutations are unnecessary for prose/mechanical edits and do not establish
security or runtime correctness on their own.
