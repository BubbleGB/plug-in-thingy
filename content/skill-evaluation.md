# Evaluate the change, not the promise

Use when authoring or changing reusable skill behavior. Existing project trials
and acceptance requirements take precedence. A typo or mechanical metadata fix
needs an appropriate static check, not a new benchmark campaign.

## Define a small comparison before changing guidance

Write representative task inputs and observable success/failure criteria. Include
tasks that should select the skill, nearby tasks that should not, and pressure
cases that might cause scope expansion, repeated ceremony or unsupported-tool
claims. Keep outcome criteria separate from the prompts shown to the model.
Do not tell an evaluator the expected answer and then count its agreement as a
successful application.

Run the unchanged guidance on the same inputs when a compatible evaluation
runner is available. Record exact prompt/guidance hashes, model/version when
exposed, host/tools, settings, outputs, sample count and failures. Use fresh
contexts for repeated baseline/candidate samples and keep conditions comparable.
Do not merge a real task's context or credentials into a synthetic fixture.

## Inspect actual outcomes

Check whether the requested work was correct and complete, scope was respected,
necessary verification occurred and claims match evidence. Selection of the
right skill name does not prove correct execution. Read failures and ambiguous
cases; preserve the raw evidence and grading reason. Human design judgments need
explicit qualitative criteria, not fabricated numerical precision.

Compare candidate guidance with the baseline and include regressions, not just
improvements. Keep model outputs as untrusted data. A model-based evaluator can
share the subject model's mistakes; use deterministic checks or real runtime
outcomes where possible. Small repeated samples are exploratory evidence, not a
reliability guarantee or a statistically established gain.

## Keep verification layers distinct

| Evidence | Establishes | Does not establish |
|---|---|---|
| Package/parser/link tests | The inspected files satisfy the checked structure | Discovery or task success in a host |
| Text selection/application exercise | Behavior in those controlled prompts | Native implicit activation or executed actions |
| Cloud listing/reference read | Accessible contents for that installed version | Reliable activation or device UI behavior |
| Managed-host task trial | Observed behavior for that host/version/scenario | Universal compatibility |
| Instrumented paired measurements | The reported measured scope and conditions | A general savings claim from stars or prose |

If authentication, a tool or device blocks a trial, record the exact unavailable
step, continue useful permitted checks and mark that evidence pending. Do not
invent a baseline failure, reuse stale results for changed guidance or present
a self-review as fresh samples. Cost/latency claims need actual measurements,
comparable conditions and uncertainty; fewer words alone do not establish a
percentage saving. No mandatory external evaluation service is supplied.
