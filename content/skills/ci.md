---
name: ci
description: "Use when creating, fixing or changing CI/CD pipelines, automated quality gates, build caches, deployment automation or CI failure reporting. Not to add CI to unrelated edits."
---
# Automate the checks the project needs

{{POLICY}}

Inspect existing workflow files, package manager, lockfile, runner versions, secrets boundary and project commands. Reuse the pipeline and service already in place. Keep credential permissions and event triggers narrow, especially for contributions from forks.

Separate fast validation from expensive integration/security/browser checks. Preserve the committed authoritative lockfile and appropriate frozen installation mode. Do not enable unreviewed dependency scripts merely to make CI green. Cache by meaningful dependency/toolchain inputs, not broad mutable state; avoid cached credentials or artifacts from untrusted jobs crossing trust boundaries.

Make failures actionable: command, version/environment and useful redacted logs. Use independent jobs only where they do not share mutable state. Gate deployment on the intended checks and authorization; writing a pipeline does not authorize running a release.

See [pipeline patterns](references/technical-details.md). Adapt examples to the actual repository and current service schema; do not paste template versions or permissions blindly. Validate workflow syntax and affected commands locally when possible, then distinguish local validation from an observed hosted CI run. Keep rollback and environment configuration explicit for deployment changes.
