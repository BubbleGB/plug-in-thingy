# Contributing

Keep the plugin useful, small and testable. A new collection is not a reason to
install another router or duplicate a workflow.

## Before changing behavior

1. Describe the concrete problem and inspect the skill that owns it.
2. Prefer an existing entry point or focused reference over another top-level
   skill. Keep host/user/project precedence, read-only scope and approvals intact.
3. Add positive and negative behavior scenarios. Keep actual host tests distinct
   from offline model exercises. Never invent a failing baseline, benchmark gain
   or invocation guarantee.
4. Preserve notices and attribution. New upstream inputs need a repository,
   version, archive hash, applicable complete notice and deliberate source map.
   Do not relabel third-party material MIT.

## Where changes belong

- Shared policy: `content/common.md`, maintained once and inserted at build time.
- Skills: `content/skills/<name>.md`.
- Source/reference selection and manual flags: `content/catalog.json`.
- Presentation: `content/interface.json` and `content/plugin.json`.
- Validation: `tools/build.py` and meaningful regression tests in `tests/`.

Do not edit generated ZIPs or install every skill under `inputs/`. That directory
is provenance, not the active catalog. Upstream contributor/agent instructions
there are source evidence scoped to the respective upstream code. Do not execute
their installers, hooks or test suites as this project's setup.

## Verify

```sh
python -m unittest discover -s tests -v
python tools/build.py
python tools/build.py --check dist/unified-engineering-0.3.1.zip
git diff --check
```

Use the version in `content/plugin.json` if changed. New builder logic needs a
test that fails before the fix and passes afterward. Documentation needs relevant
command/link inspection, not artificial unit tests. See [development](docs/DEVELOPMENT.md)
and [releasing](docs/RELEASING.md).

Keep PRs focused. Explain the resulting behavior, why it matters, validation and
remaining limits. Do not weaken checks, drop provenance, commit secrets/generated
archives or modify unrelated applications to make a check pass.
