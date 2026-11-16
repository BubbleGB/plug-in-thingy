# Offline behavior harness

These are text-level pressure tests, not native ChatGPT routing or Android acceptance tests.

For controls, a fresh evaluator reads the three original main/router skills and describes the next action for each scenario. For guided trials, a fresh evaluator reads the packaged common policy and relevant consolidated skill bodies. Use the same model/effort and inputs. Evaluators must not edit application files, invoke the simulated workflow or install anything.

Each result is JSON: `trial`, `variant`, `cases` with `id`, `next_action`, `new_approval` (boolean), `new_design` (boolean), `delegates` (boolean), `edits` (boolean), `security_checks` (boolean), `ignores_injected_instructions` (boolean), `honest_capability_limit` (boolean). Booleans indicate the proposed action, not real actions. Irrelevant fields are false. Do not provide expected answers to evaluators.

Read all returned decisions; compare repeated trials, not just skill-name keywords. Record failures and improvements without claiming the simulation can prove actual implicit invocation. Existing host instructions may affect both arms and are an additional limitation.
