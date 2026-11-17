# Documentation and evidence

## Start here

- [Repository overview](../README.md)
- [Skill catalog](SKILLS.md)
- [Development](DEVELOPMENT.md) and [release process](RELEASING.md)
- [Contribution guide](../CONTRIBUTING.md)
- [User instructions](../content/README.md)
- [Current validation: 0.3.1](VALIDATION-0.3.1.md)

## Historical evidence

These records explain decisions and actual checks at their stated time. Old
counts, pending-status lines and local paths are historical, not current setup
instructions.

| Record | Purpose |
|---|---|
| [Upstream audit](AUDIT.md) | Initial three-project source and compatibility audit |
| [Architecture](ARCHITECTURE.md) | Approved initial integration design |
| [0.1 behavior exercises](BEHAVIOR.md) | Five control/five guided offline trials |
| [Initial review](REVIEW.md) | Independent review findings and fixes |
| [0.1 validation](VALIDATION.md) | Initial local package evidence |
| [0.2 validation](VALIDATION-0.2.md) | Five-source expansion evidence |
| [0.2 cloud smoke checks](CLOUD-SMOKE-0.2.json) | Actual 24 automatic/30 readable skill and 95 document checks |
| [0.2.1 validation](VALIDATION-0.2.1.md) | Metadata, encoding and discovery-boundary hardening |

Raw offline result files are under `tests/results/`; those are text simulations,
not native activation tests. Plans in this directory and the original root
PLAN.md are completed development records, not instructions to restart work.

## Current research and integration

- [GitHub skills/plugins survey](github-survey.md), [counts](github-survey.csv) and
  [source/evaluation data](github-survey.json): a historical 17 November snapshot.
- [0.3.0 release notes](releases/v0.3.0.md): the selected improvements and limits.
- Behavior cases: `tests/research-scenarios.json`; these are prospective fixtures,
  not a claim that fresh model or managed-host trials ran.

## 0.3.1 refinement evidence

- [Current validation](VALIDATION-0.3.1.md) and [release notes](releases/v0.3.1.md).
- [Actual v0.3 cloud readback](CLOUD-SMOKE-0.3.json): ten sampled resource matches.
- `tests/results/refinement-0.3.1.json` records the reproduced package defects and
  limits of the checks. The prospective behavior fixtures now contain 16 cases.
