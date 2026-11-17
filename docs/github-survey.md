# GitHub top-25 skills/plugins survey for Unified Engineering

Historical research snapshot prepared before the 0.3.0 implementation. Its
no-change statements describe that research stage; see VALIDATION-0.3.md for
subsequent implementation evidence.

Counts checked: 2026-11-17T13:06:55.082245+00:00 (UTC). Research only; no plugin or repository changes.

## Recommendation

Keep the existing 30-skill architecture. The best additions are focused visual design critique, skill/plugin intake security checks, better evidence for requested security audits, and source-linked system diagrams. Improve existing entry points instead of bundling whole collections or installing another runtime.

Popularity is a discovery signal, not proof of quality or compatibility. The five original sources already supply a strong engineering core. Several useful specialist sources rank below the top 25 and still deserve consideration.

## Scope and evidence

Repositories shipping public user-facing Claude Code/Codex-compatible skills, generated skill workflows, or native plugins, including companion integrations for a larger product. Excludes link-only indexes, internal-only development skills, bare agent-persona lists, and host agent/model runtimes themselves. Stars belong to the entire repository, not an individual skill/plugin.

This is a broad ranking, so REA, Firecrawl, Graphify, browser-use, Orca, Paperclip and OpenDesign count because actual public skills/plugins exist, even though they are larger products. Their dependency-heavy adapters are labeled separately from portable instruction packs. Do not interpret their repository stars as stars or installations for the adapter alone.

Method: 16 GitHub repository searches, 596 unique candidates, then file-tree/README/root-license inspection for 145 repositories (candidates above 50,000 stars plus named seeds). Searches covered Claude/Codex skill and plugin names/descriptions, topics, marketplaces and README mentions, with up to the first 100 results per query sorted by stars. Sampled public skill definitions, native manifests, or actual skill-generator code were read for each ranked project. This is not a full security audit of every file.

The final counts come from GitHub REST repository metadata, refreshed for all 25 in a short retrieval window. Exact timestamps, counts, source tree SHAs, primary file paths, dependencies and assessments are in github-survey.json and github-survey.csv. Renamed repository URLs are deduplicated. The forrestchang Karpathy-inspired project currently resolves to multica-ai/andrej-karpathy-skills.

GitHub has no exhaustive official skills/plugins category. This is the highest-starred eligible set found by the documented search, not proof that every repository on GitHub was examined. Broad keyword searches can miss poorly indexed projects. Two excluded large host/app trees were truncated; every ranked source tree was complete.

Cross-checks used the [public plugin index](https://github.com/quemsah/awesome-claude-plugins), [skill collections directory](https://github.com/zhuyansen/awesome-claude-code-skills-collections), [Codex skills directory](https://github.com/zhuyansen/awesome-codex-skills), and public web search. Their cached counts, safety grades and compatibility labels were not accepted as evidence. Source inspection mattered: REA has actual native Claude and Codex manifests, not just internal development skills.

## Top 25 by repository stars

| Rank | Repository | Stars | What it provides | Recommendation |
|---:|---|---:|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | 465,366 | Reverse engineering of shipped binaries, packages and runtime behavior. | Optional integration |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 326,410 | Domain language, module boundaries, prototypes and handoffs. | Already integrated |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | 318,982 | Planning, debugging, tests and development workflow. | Already integrated |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 305,025 | Agent configuration security scanning; a large engineering and learning catalog. | Selective addition |
| 5 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 233,892 | Assumptions, small changes, simplicity and verifiable goals. | Already integrated |
| 6 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 202,499 | Application web-data integration: search, scraping, extraction and browser interaction. | Optional integration |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | 196,439 | Skill authoring/evaluation, design and document tooling. | Selective addition |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 192,578 | Small complete solutions plus audit/debt/gain reports. | Already integrated |
| 9 | [f/prompts.chat](https://github.com/f/prompts.chat) | 177,724 | Prompt/skill discovery and retrieval through a real Claude plugin. | Keep external |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 150,707 | Concrete typography, palettes, layout, design-system and stack references. | Selective addition |
| 11 | [github/spec-kit](https://github.com/github/spec-kit) | 150,205 | Structured specifications, process templates and generated agent skills. | Selective method only |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 149,335 | Persistent source/document knowledge graphs with traceable edges and query/explain tools. | Optional integration |
| 13 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 144,927 | An examples repository that also distributes public installable skills. | Selective methods only |
| 14 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 144,142 | A public agent skill driving end-to-end video creation. | Keep separate |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | 141,870 | Browser QA, release and evidence-oriented engineering roles. | Selective method only |
| 16 | [stablyai/orca](https://github.com/stablyai/orca) | 127,372 | Agent worktrees, terminals, browser and orchestration exposed through public skills. | Optional separate workbench |
| 17 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 121,285 | Browser access for agents through public skills, CLI and supported browser connections. | Optional integration |
| 18 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 120,923 | Concise output and a larger compression/proxy ecosystem. | Mostly overlap |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 118,522 | Engineering specialists and workflow refinements. | Already integrated |
| 20 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 117,848 | Persistent observations and retrieval across sessions. | Optional external integration |
| 21 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 117,379 | Art direction, real content/assets and browser-backed design critique. | Selective addition |
| 22 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 114,475 | Native Claude/Codex plugins for durable task delegation and team results. | Optional external integration |
| 23 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 112,581 | Read-only access to social/web content when existing tools cannot retrieve it. | Optional integration |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 111,823 | Design critique, hierarchy, typography, polish and resilient UI states. | High-priority addition |
| 25 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 108,046 | A native Claude plugin exposing a design app with skills and design systems. | Optional separate design platform |

## What to add, in order


### 1. Focused visual design critique — high value

Sources: Impeccable, UI UX Pro Max, Taste Skill and selected Front-End-Checklist rules. Existing frontend covers semantics, state and accessibility but has little concrete visual critique. Add a short reference covering audience/task, hierarchy, type scale, spacing, coherent design tokens, realistic copy, overflow, i18n and focused rendered checks. Integrate under frontend/browser; no extra top-level design router. Preserve the existing design system. Add Emil-style interruption, exit and reduced-motion guidance only for motion work.

Acceptance: compare the current guidance with the proposed reference on a bland landing page, dense settings form and multilingual narrow layout. Verify visible outcomes using available browser tooling. Include negative cases for backend-only tasks and a request to preserve an established brand. Do not claim this improves design until the trials show it.

### 2. Security-audit evidence — high value

Source: Cloudflare security-audit-skill. Existing security covers trust boundaries, dependencies and related defects. The useful extension is an explicit coverage/status record for requested audits, tied to the current source revision. Separate a confirmed boundary failure from a blocked lead or rejected hypothesis; include an exact reproducible observation and impact. Keep a small focused review small.

Integrate into security with an optional deep-audit reference. Leave the preserved Ponytail audit file unchanged. Do not import automatic multi-agent orchestration or the upstream full workflow as a claim about our runtime. Independent verification is valuable when agents are explicitly authorized and available; a same-agent reread is not equivalent.

Acceptance: include an apparently dangerous but unreachable path, a real cross-owner access bug, a source-only lead needing runtime evidence and an interrupted audit. Reports must not give false confirmations, confuse blocked with covered, or claim complete coverage after a partial pass.

### 3. Skill/plugin intake review — high value for this project

Source: ECC security-scan/AgentShield. Existing build.py already validates archive structure, references, source mappings and notices; this is an extension of those controls. Before importing a new skill, record its source revision, license, scripts, permissions, network destinations, secret handling and host assumptions. Inspect prompt text as executable influence, not trusted policy. Keep deterministic schema/path checks in tooling.

Integrate into skill-authoring/security and the existing package review, not a new always-on agent. AgentShield or another scanner can be an explicit optional integration; do not install it silently, assume it detects every attack, or treat a scan pass as proof a package is safe.

Acceptance: use harmless synthetic fixtures containing a policy-override instruction, unexpected network upload, secret-bearing config, unsafe hook interpolation and a benign documented URL. Findings need evidence and context; avoid rejecting every useful network-capable plugin.

### 4. Source-linked diagrams — useful on demand

Sources: Archify and Diagram Design. Improve architecture/docs with diagram-type selection, concrete source locations for edges, uncertainty labels, error paths and an explicit observed/proposed distinction. Prefer one diagram that answers a question to a whole-codebase graph. Existing visualization tools can provide rendering; do not bundle a new graph service or require HTML for a small Mermaid diagram.

Acceptance: trace a real request path and one failure branch from code. Every factual edge must be supported; a proposed component must be labeled as proposed. A synthetic timeline must not be described as measured. A diagram is not runtime evidence.

### 5. Operationalize existing skill evaluation — useful maintenance

Source: Anthropic skill-creator. Unified Engineering already has baseline/pressure/discovery experiments and a skill-authoring procedure. Improve their repeatability and target-host coverage rather than claim evaluation is missing. Track positive/negative routing, task outcome, needless ceremony and unsupported-tool claims against a pinned plugin version; use repeated fresh samples. Token/latency claims need actual instrumentation and uncertainty.

Acceptance: rerun representative routing and application scenarios on the final archive in managed ChatGPT, including Android use. Local packaging tests and offline model simulations are useful distinct evidence, not substitutes for host acceptance.


## Evidence and assessment for each ranked project

### 1. morluto/rea

**Optional integration.** Reverse engineering of shipped binaries, packages and runtime behavior.

A legitimate Claude Code/Codex plugin: both native manifests and a public workflow skill are present. Keep it as an optional tool integration for explicitly requested artifact/runtime analysis, not a dependency of ordinary source-code architecture work. Reuse its distinction between direct evidence, inference and unknowns.

Licensing: MIT. Requirements/limits: Node MCP runtime; native analysis may require Hopper, Ghidra, IDA or Kuna and additional platform support. The skill itself explicitly says loading it does not install/register the runtime.

Inspected source tree: `a88c0a55544e16a710ddaad2feb5a2c6e7011f4e`.

- [.claude-plugin/plugin.json](https://github.com/morluto/rea/blob/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e/.claude-plugin/plugin.json)
- [.codex-plugin/plugin.json](https://github.com/morluto/rea/blob/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e/.codex-plugin/plugin.json)
- [.cursor-plugin/skills/reverse-engineer-anything/SKILL.md](https://github.com/morluto/rea/blob/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e/.cursor-plugin/skills/reverse-engineer-anything/SKILL.md)

### 2. mattpocock/skills

**Already integrated.** Domain language, module boundaries, prototypes and handoffs.

Keep the selected methods already integrated. Its current tree contains additional material, but a larger catalog is not a reason to restore setup interviews or another general router.

Licensing: MIT. Requirements/limits: Markdown methods; some upstream workflows assume setup scripts and host-specific commands.

Inspected source tree: `5863806dd4e15c63174bee4e7515a4256792ecfa`.

- [skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md)
- [skills/engineering/domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md)

### 3. obra/superpowers

**Already integrated.** Planning, debugging, tests and development workflow.

Keep the coordinated workflow backbone. Do not reintroduce mandatory discovery/planning/review cycles on every small task or unconditional delegation.

Licensing: MIT. Requirements/limits: Instruction methods are portable; upstream hooks and exact host tools are separate capabilities.

Inspected source tree: `22f0b463e7a5e579904dd6211a520321035526f7`.

- [skills/using-superpowers/SKILL.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md)
- [skills/verification-before-completion/SKILL.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md)

### 4. affaan-m/ECC

**Selective addition.** Agent configuration security scanning; a large engineering and learning catalog.

Adapt the threat checklist for skill/plugin intake: instruction files, permissions, hooks, MCP definitions, secrets and install-time commands. Its security-scan delegates to AgentShield; that scanner is an additional dependency, not a capability supplied by Markdown. Do not import automatic instinct learning.

Licensing: MIT root; inspect embedded notices. Requirements/limits: AgentShield is a separate npm tool. Continuous-learning-v2 requires observation hooks, background analysis and persistent storage.

Inspected source tree: `3f14a103a8694e51c1df9a806217a6d0b5f7a6f7`.

- [skills/security-scan/SKILL.md](https://github.com/affaan-m/ECC/blob/3f14a103a8694e51c1df9a806217a6d0b5f7a6f7/skills/security-scan/SKILL.md)
- [skills/continuous-learning-v2/SKILL.md](https://github.com/affaan-m/ECC/blob/3f14a103a8694e51c1df9a806217a6d0b5f7a6f7/skills/continuous-learning-v2/SKILL.md)

### 5. multica-ai/andrej-karpathy-skills

**Already integrated.** Assumptions, small changes, simplicity and verifiable goals.

No second coding philosophy. These principles already inform the shared policy. The original forrestchang URL resolves to this repository; count it once. This is community work inspired by Karpathy, not a Karpathy-authored package.

Licensing: MIT declared; complete notice unresolved. Requirements/limits: Instruction-only core. No root LICENSE was present in the inspected tree; do not copy text until notice requirements are resolved.

Inspected source tree: `2c606141936f1eeef17fa3043a72095b4765b9c2`.

- [skills/karpathy-guidelines/SKILL.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md)

### 6. firecrawl/firecrawl

**Optional integration.** Application web-data integration: search, scraping, extraction and browser interaction.

Useful when a project actually selects Firecrawl. Do not import its broad activation rule that steers any app-level web-data request to Firecrawl or make an API provider mandatory. Existing sources/api/security workflows already supply the general method.

Licensing: AGPL-3.0 host; sampled build skill declares ISC. Requirements/limits: FIRECRAWL_API_KEY and SDK/cloud or configured self-hosted service. Apply exact file-specific terms; do not relabel the entire upstream repository MIT.

Inspected source tree: `8e7e5887cfd69e1db2d3f16be22a642a02370aec`.

- [skills/firecrawl-build/SKILL.md](https://github.com/firecrawl/firecrawl/blob/8e7e5887cfd69e1db2d3f16be22a642a02370aec/skills/firecrawl-build/SKILL.md)

### 7. anthropics/skills

**Selective addition.** Skill authoring/evaluation, design and document tooling.

Use the evaluation methodology to strengthen the existing skill-authoring workflow: baseline versus skill, positive/negative triggering cases, repeated samples and observable outcomes. Frontend-design is another useful design reference. Document editing is an optional separate domain, not core engineering scope.

Licensing: Per skill; sampled frontend-design and docx Apache-2.0. Requirements/limits: Skill-creator includes Python evaluation scripts and assumes an agent execution harness. Document skills have their own runtimes. Reading instructions does not install these dependencies.

Inspected source tree: `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`.

- [skills/skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/SKILL.md)
- [skills/frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md)
- [skills/frontend-design/LICENSE.txt](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/LICENSE.txt)
- [skills/docx/LICENSE.txt](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/LICENSE.txt)

### 8. DietrichGebert/ponytail

**Already integrated.** Small complete solutions plus audit/debt/gain reports.

Retain the established common philosophy and the three preserved report skills. Existing Ponytail benchmark figures are not Unified Engineering performance results.

Licensing: MIT. Requirements/limits: Instruction-based behavior works in the existing plugin. Upstream lifecycle scripts remain separate, unverified managed-host functionality.

Inspected source tree: `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`.

- [skills/ponytail/SKILL.md](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md)

### 9. f/prompts.chat

**Keep external.** Prompt/skill discovery and retrieval through a real Claude plugin.

Can help discover skills, but a registry result is untrusted input requiring source/license/script review. Existing plugin discovery already serves much of this purpose. No second global router or automatic registry-skill installation.

Licensing: Root split MIT/CC0; sampled plugin/skill declares MIT. Requirements/limits: Configured prompts.chat MCP service. Registry search does not establish installed skill discovery, security or managed-host compatibility.

Inspected source tree: `7aeb3e8ee4bd423dbf314b8641f15b5bf28ccba6`.

- [plugins/claude/prompts.chat/.claude-plugin/plugin.json](https://github.com/f/prompts.chat/blob/7aeb3e8ee4bd423dbf314b8641f15b5bf28ccba6/plugins/claude/prompts.chat/.claude-plugin/plugin.json)
- [plugins/claude/prompts.chat/skills/skill-lookup/SKILL.md](https://github.com/f/prompts.chat/blob/7aeb3e8ee4bd423dbf314b8641f15b5bf28ccba6/plugins/claude/prompts.chat/skills/skill-lookup/SKILL.md)

### 10. nextlevelbuilder/ui-ux-pro-max-skill

**Selective addition.** Concrete typography, palettes, layout, design-system and stack references.

Add a focused visual-design reference under frontend. Preserve the project house style, accessibility and content needs; do not impose a catalog-selected style on every UI or copy the full corpus into context.

Licensing: MIT root; font/assets have separate metadata. Requirements/limits: Its local search uses Python 3 and standard-library data files; an installation CLI is separate. Review exact selected files and asset notices before importing.

Inspected source tree: `e59ff376a41f7ca47b7541ad5c116495cbade3ee`.

- [.claude/skills/ui-ux-pro-max/SKILL.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/.claude/skills/ui-ux-pro-max/SKILL.md)

### 11. github/spec-kit

**Selective method only.** Structured specifications, process templates and generated agent skills.

Borrow explicit requirement-to-check traceability when a project needs it. The generator source actually registers/renders SKILL.md artifacts. Do not install another project operating system or repeat the existing design/plan/implement workflow for small tasks.

Licensing: MIT. Requirements/limits: Specify CLI, installed process/preset templates and project-generated artifacts. A skill generator is labeled separately from a ready-made instruction pack.

Inspected source tree: `e210504aa09c9273a38bba665b12b8088468c96f`.

- [src/specify_cli/presets/_manager_skills.py](https://github.com/github/spec-kit/blob/e210504aa09c9273a38bba665b12b8088468c96f/src/specify_cli/presets/_manager_skills.py)

### 12. Graphify-Labs/graphify

**Optional integration.** Persistent source/document knowledge graphs with traceable edges and query/explain tools.

Useful on a large repository with repeated navigation needs. Prefer focused tracing first. Its broad any-codebase-question trigger and full scan should not become default policy. The public Codex adapter is real; lowercase skill.md is not evidence of invalidity or insecurity.

Licensing: Apache-2.0 root; additional notices present. Requirements/limits: Python CLI/package, parsing/rendering dependencies and generated graph artifacts. Semantic/enrichment paths must distinguish inferred edges from deterministic source links.

Inspected source tree: `480b61ed91cbc08177dc2c60caa9ffd6c9b95749`.

- [graphify/skill.md](https://github.com/Graphify-Labs/graphify/blob/480b61ed91cbc08177dc2c60caa9ffd6c9b95749/graphify/skill.md)
- [graphify/skill-codex.md](https://github.com/Graphify-Labs/graphify/blob/480b61ed91cbc08177dc2c60caa9ffd6c9b95749/graphify/skill-codex.md)

### 13. Shubhamsaboo/awesome-llm-apps

**Selective methods only.** An examples repository that also distributes public installable skills.

Do not count it as a link-only awesome list: its agent_skills directory contains executable instructions. Commit archaeology and dependency reasoning may inform context/debug references. Reject automatic multi-model fan-out as default behavior; the sampled orchestrator calls external CLIs/APIs and includes bypass-permission flags.

Licensing: Apache-2.0. Requirements/limits: Varies by skill. Sampled orchestration requires shell/jq and external model CLIs or API keys. None were invoked. Model orchestration is not supplied by copying the prose.

Inspected source tree: `4f40918e7f6fb90db5d736f77e91c9a80800dd7e`.

- [agent_skills/advisor-orchestrator-worker/SKILL.md](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/4f40918e7f6fb90db5d736f77e91c9a80800dd7e/agent_skills/advisor-orchestrator-worker/SKILL.md)
- [agent_skills/commit-archaeologist/SKILL.md](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/4f40918e7f6fb90db5d736f77e91c9a80800dd7e/agent_skills/commit-archaeologist/SKILL.md)

### 14. harry0703/MoneyPrinterTurbo

**Keep separate.** A public agent skill driving end-to-end video creation.

Useful as a separate video-production capability, not an engineering-quality workflow. Do not adopt automatic install/config actions, fixed Chinese portrait defaults or provider choices in a general coding plugin.

Licensing: MIT. Requirements/limits: Sampled skill supports macOS/Windows, uses uv and its adjacent Python helper, and needs configured model/media providers and rendering dependencies. Managed Linux/Android compatibility not established.

Inspected source tree: `92e0f9a55b91e353565015aab74b7c50cc28f148`.

- [docs/skill/SKILL.md](https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/docs/skill/SKILL.md)

### 15. garrytan/gstack

**Selective method only.** Browser QA, release and evidence-oriented engineering roles.

Borrow scoped QA charters and reproducible evidence, which extend existing browser/test/ship skills. The complete generated workflows are too operationally coupled and repetitive for this plugin.

Licensing: MIT. Requirements/limits: Bun/Git and built browser/runtime helpers; transcripts, telemetry/config and host-specific commands appear in workflows. Sampled review requires Agent dispatches. No blanket import.

Inspected source tree: `e8c8625bd65fdcc0f0650f982830649d326c4bf4`.

- [qa/SKILL.md](https://github.com/garrytan/gstack/blob/e8c8625bd65fdcc0f0650f982830649d326c4bf4/qa/SKILL.md)
- [review/SKILL.md](https://github.com/garrytan/gstack/blob/e8c8625bd65fdcc0f0650f982830649d326c4bf4/review/SKILL.md)

### 16. stablyai/orca

**Optional separate workbench.** Agent worktrees, terminals, browser and orchestration exposed through public skills.

Useful for someone who chooses the Orca environment. Keep its runtime-specific management outside the core; current native worktree and delegation workflows should use actual host tools. Do not replace the user Android ChatGPT workflow to obtain it.

Licensing: MIT. Requirements/limits: Orca executable and its version-matched guide/runtime. The public orca-cli skill is a discovery stub, not an independent implementation.

Inspected source tree: `787138074a5c2a67782caaa1dd91c1a07b2b2839`.

- [skills/orca-cli/SKILL.md](https://github.com/stablyai/orca/blob/787138074a5c2a67782caaa1dd91c1a07b2b2839/skills/orca-cli/SKILL.md)

### 17. browser-use/browser-use

**Optional integration.** Browser access for agents through public skills, CLI and supported browser connections.

Useful when no suitable browser tool is available and this integration is explicitly chosen. Existing browser/frontend/testing methods already cover the general checks. Do not impose its CLI over a supported native browser or reuse unrelated logged-in sessions.

Licensing: MIT. Requirements/limits: browser-use CLI/Python package and a browser/CDP connection; hosted paths add cloud service configuration. No new browser runtime or package was installed.

Inspected source tree: `197972b206d3a6ec9fb30afcf76149c07fb8ee61`.

- [skills/browser-use/SKILL.md](https://github.com/browser-use/browser-use/blob/197972b206d3a6ec9fb30afcf76149c07fb8ee61/skills/browser-use/SKILL.md)

### 18. JuliusBrussee/caveman

**Mostly overlap.** Concise output and a larger compression/proxy ecosystem.

Keep answer-first, clear writing. Do not adopt a caveman persona, persistent extra voice mode or token/cost savings claims. Lite already reduces ceremony without dropping technical substance.

Licensing: Apache-2.0 current root; components/history need notice review. Requirements/limits: The voice skill is text; automatic modes, compression, proxy and statistics are separate runtime capabilities.

Inspected source tree: `9b243662ff98d392bc0a95b865a554583d71be75`.

- [skills/caveman/SKILL.md](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman/SKILL.md)

### 19. addyosmani/agent-skills

**Already integrated.** Engineering specialists and workflow refinements.

Continue using the integrated specialists rather than loading a second duplicate collection. Only consider an upstream delta when it fixes a demonstrated gap.

Licensing: MIT. Requirements/limits: Many methods portable; scripts, named tools, browser runners and stack-specific examples require capability checks.

Inspected source tree: `39b723ceebf81474d0557c1fecd01eddab585563`.

- [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/api-and-interface-design/SKILL.md)

### 20. thedotmack/claude-mem

**Optional external integration.** Persistent observations and retrieval across sessions.

Useful only as an explicitly configured external memory integration. Prefer existing scoped handoffs in the core. Do not promise capture or future-session recall from a skill alone.

Licensing: Apache-2.0 current root. Requirements/limits: Node/Bun worker, SQLite and optional vector-search tooling; capture hooks/adapters and durable storage. README states anonymous analytics are enabled by default and cloud sync is opt-in.

Inspected source tree: `3d1aa47ec6406c88a76bf9289c4a4248282303e6`.

- [plugin/skills/mem-search/SKILL.md](https://github.com/thedotmack/claude-mem/blob/3d1aa47ec6406c88a76bf9289c4a4248282303e6/plugin/skills/mem-search/SKILL.md)

### 21. Leonxlnx/taste-skill

**Selective addition.** Art direction, real content/assets and browser-backed design critique.

Reuse content-specific design critique under frontend. Do not adopt rigid one-section-per-screen, mandatory effects, startup gates or automatic image acquisition as universal policy.

Licensing: MIT. Requirements/limits: Current SKILL.md embeds a Stop hook and references Node gate scripts and browser evidence. Text adaptation must not claim these gates ran.

Inspected source tree: `f6b76575f949707b4e3c37cd86cb44b0b98643e8`.

- [skills/taste-skill/SKILL.md](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md)

### 22. paperclipai/paperclip

**Optional external integration.** Native Claude/Codex plugins for durable task delegation and team results.

Good ideas: stable task IDs, idempotent request IDs, inspect uncertain outcomes before retry, and distinguish submitted/running/complete. General API/observability/delegation methods overlap; the persistent autonomous-team platform is not appropriate as a core dependency.

Licensing: MIT. Requirements/limits: Connected Paperclip person/company, configured agents and service execution capacity/budget. Its plugin creates real external work; requires an actual delegation request.

Inspected source tree: `ca34aca77750a143dfc637c96769d64f9b14cbdb`.

- [integrations/assistant-plugins/claude/paperclip/.claude-plugin/plugin.json](https://github.com/paperclipai/paperclip/blob/ca34aca77750a143dfc637c96769d64f9b14cbdb/integrations/assistant-plugins/claude/paperclip/.claude-plugin/plugin.json)
- [integrations/assistant-plugins/openai/paperclip/skills/delegate-work/SKILL.md](https://github.com/paperclipai/paperclip/blob/ca34aca77750a143dfc637c96769d64f9b14cbdb/integrations/assistant-plugins/openai/paperclip/skills/delegate-work/SKILL.md)

### 23. Panniantong/Agent-Reach

**Optional integration.** Read-only access to social/web content when existing tools cannot retrieve it.

Useful fallback for a concrete missing source, not a reason to install channels or request login every time a site is named. Existing public fetch/search/connected apps stay first. Preserve distinctions between a page shell, full text, comments and transcripts.

Licensing: MIT. Requirements/limits: agent-reach CLI plus channel-specific backends, sessions or dependencies. The sampled skill explicitly prefers built-in tools and does not authorize installation merely from a URL mention.

Inspected source tree: `c70ae6da5d39bc90e09ad2ae0575ccc89f31e284`.

- [agent_reach/skill/SKILL.md](https://github.com/Panniantong/Agent-Reach/blob/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284/agent_reach/skill/SKILL.md)

### 24. pbakaus/impeccable

**High-priority addition.** Design critique, hierarchy, typography, polish and resilient UI states.

Best source for a concise, task-relevant visual critique procedure. Integrate with frontend and browser; avoid another router, 24 new top-level commands or automatic design/config files.

Licensing: Apache-2.0. Requirements/limits: Text references are portable. Current workflow also uses helper scripts, optional live mode and design hooks; these are not automatically available in managed ChatGPT.

Inspected source tree: `d41d9860b0094dcb68030657da63461212835aaa`.

- [.devin/skills/impeccable/SKILL.md](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/.devin/skills/impeccable/SKILL.md)

### 25. nexu-io/open-design

**Optional separate design platform.** A native Claude plugin exposing a design app with skills and design systems.

Real companion plugin, not merely internal development skills. Useful if the user chooses that design platform; do not bundle its daemon, 139-skill surface or many design systems into this engineering core. Use a few portable visual-critique principles instead.

Licensing: Apache-2.0. Requirements/limits: Sampled plugin explicitly requires the od daemon on PATH and stdio MCP. A large application/catalog is separate from instruction-only frontend guidance.

Inspected source tree: `f2ecaa3f88e1eba001379ea845e7b7754310ea6d`.

- [plugins/open-design/.claude-plugin/plugin.json](https://github.com/nexu-io/open-design/blob/f2ecaa3f88e1eba001379ea845e7b7754310ea6d/plugins/open-design/.claude-plugin/plugin.json)

## Additional useful projects below this broad cutoff

These were also inspected. Their absence from the top 25 is a consequence of repository star counts, not a finding that they are less valuable. In particular, Cloudflare is one of the strongest sources for a targeted improvement.

### tt-a1i/archify — 97,339 stars when checked

**Selective addition.** Source-backed architecture, sequence, lifecycle and data-flow diagrams.

Add diagram selection, evidence anchoring and uncertainty handling to architecture/docs. Keep rendering optional; use native visualization or simple Mermaid where sufficient.

Licensing: Apache-2.0. Requirements/limits: Full package uses Node validators/renderers and optional local preview/export. README describes an opt-out update-manifest check. No renderer was executed here.

Inspected source tree: `44781293f38728baf04dbad33ce1a0cef8c39cca`.

- [archify/SKILL.md](https://github.com/tt-a1i/archify/blob/44781293f38728baf04dbad33ce1a0cef8c39cca/archify/SKILL.md)

### Egonex-AI/Understand-Anything — 92,953 stars when checked

**Optional external integration.** Codebase knowledge graphs and guided architectural exploration.

Useful for large repositories when a maintained graph tool is already available. Start with targeted code tracing and a small source-linked map; avoid installing a graph database/dashboard or scanning every file for ordinary tasks.

Licensing: MIT. Requirements/limits: Sampled analysis requires building its Node package (Node >=22 and pnpm >=10), language parsing and an agent pipeline; dashboard requirements differ. Auto-update is a separate opt-in feature.

Inspected source tree: `b861852dda79273bd9d2e01c3160d42e2df510d2`.

- [understand-anything-plugin/skills/understand/SKILL.md](https://github.com/Egonex-AI/Understand-Anything/blob/b861852dda79273bd9d2e01c3160d42e2df510d2/understand-anything-plugin/skills/understand/SKILL.md)

### career-ops-hq/career-ops — 83,212 stars when checked

**Keep separate.** Job-search, resume, offer and interview workflows.

Legitimate skills/plugin distribution, but not an engineering quality capability. Keep outside this plugin and avoid collecting career data as part of coding work.

Licensing: MIT. Requirements/limits: Node project and multiple workflow files; some PDF/browser paths add Playwright tooling. A standalone SKILL.md is not the full application.

Inspected source tree: `0ad9049f726105894bc9e85843ab7f510646baf0`.

- [.agents/skills/career-ops/SKILL.md](https://github.com/career-ops-hq/career-ops/blob/0ad9049f726105894bc9e85843ab7f510646baf0/.agents/skills/career-ops/SKILL.md)

### ComposioHQ/awesome-claude-skills — 79,697 stars when checked

**Selective reference only.** A real skill collection plus service integrations and an index.

Do not import hundreds of automation adapters or a second integration layer. Its MCP builder can inform an optional api/security reference for tool contracts, only when relevant; host plugin-creator already covers much of this. Browser testing overlaps existing skills.

Licensing: README Apache-2.0; per-skill licenses vary. Requirements/limits: Automation depends on configured external services/accounts/tools. Some helper skills assume Python/Playwright. Unlike link-only awesome lists, this tree actually contains distributable skills.

Inspected source tree: `be2a406907dbc61b73e6827ded415c96139d13a2`.

- [mcp-builder/SKILL.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/mcp-builder/SKILL.md)
- [webapp-testing/SKILL.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/webapp-testing/SKILL.md)

### thedaviddias/Front-End-Checklist — 74,761 stars when checked

**Selective addition.** Priority-ranked frontend checks, including accessibility, privacy and internationalization.

Use a small relevant checklist under frontend/browser, especially text expansion, RTL and overflow. Do not make hundreds of rules mandatory on every UI change or copy blanket stack/legal assumptions.

Licensing: MIT. Requirements/limits: Local skill/reference content and plugin files exist; its online/MCP modes are separate services. The sampled manifest lists 386 rules; file/mirror counts are not unique skill counts.

Inspected source tree: `e8d14d049010e2ce25afcd5e8609dfcbbe63e47e`.

- [plugins/front-end-checklist/.claude-plugin/plugin.json](https://github.com/thedaviddias/Front-End-Checklist/blob/e8d14d049010e2ce25afcd5e8609dfcbbe63e47e/plugins/front-end-checklist/.claude-plugin/plugin.json)

### cloudflare/security-audit-skill — 74,394 stars when checked

**High-priority addition.** Coverage-led auditing, disprovable findings, evidence and explicit validation status.

Extend security with a bounded audit evidence procedure: trust-boundary inventory, covered/blocked/deferred units, confirmed/needs-validation/rejected records, exact source revision and reproducible observations. Preserve the distinction between an unverified lead and a finding.

Licensing: MIT. Requirements/limits: Full upstream workflow requires parallel independent agents, Node validators and an OS-enforced execution sandbox. Adapt the method without claiming its full six-phase protocol ran or launching agents automatically.

Inspected source tree: `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.

- [skills/security-audit/SKILL.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md)
- [skills/security-audit/VALIDATION-AND-REPORTING.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md)

### blader/humanizer — 70,162 stars when checked

**Small optional refinement.** Plain prose with fewer generic writing patterns.

Useful for docs/help, but most overlaps the existing concise style. Preserve technical precision, uncertainty and the user voice. Never promise to evade AI detectors or fabricate personal experience.

Licensing: MIT. Requirements/limits: Core skill is instruction text; lengthy style rules should not become global coding policy.

Inspected source tree: `b48c832f0f809c1b5658edbb838c2521b72f2413`.

- [SKILL.md](https://github.com/blader/humanizer/blob/b48c832f0f809c1b5658edbb838c2521b72f2413/SKILL.md)

### mvanhorn/last30days-skill — 68,590 stars when checked

**Optional external integration.** Recent multi-source research and source-health diagnosis.

Useful for product/ecosystem research, less useful for routine implementation. Existing sources plus available research tools should remain the default. An engine-backed invocation must not be represented as completed if only web search ran.

Licensing: MIT. Requirements/limits: Current skill requires its Python 3.12+ engine, Node helpers and source configuration; API credentials are optional per provider and a keyless floor exists. Coverage varies by available source.

Inspected source tree: `9cee9178210ee8492fac558df89855ef334adbcc`.

- [skills/last30days/SKILL.md](https://github.com/mvanhorn/last30days-skill/blob/9cee9178210ee8492fac558df89855ef334adbcc/skills/last30days/SKILL.md)

### cathrynlavery/diagram-design — 67,790 stars when checked

**Selective addition.** Clear editorial diagrams and matching diagram form to the question.

Combine a few readability checks with Archify-inspired source evidence under architecture/docs: label edges, show failure paths, keep density useful and separate observed from proposed structure. Do not impose its palette, setup gate, HTML-only output or blanket rejection of Mermaid.

Licensing: MIT. Requirements/limits: Self-contained HTML/SVG artifacts and bundled references. Source is currently version 2.6; exact current diagram-type counts differ from cached descriptions.

Inspected source tree: `f6db0decea96de66b901331a0f79a8d4b147ebae`.

- [skills/diagram-design/SKILL.md](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/skills/diagram-design/SKILL.md)

### ayghri/i-have-adhd — 61,448 stars when checked

**Optional style refinement.** Answer-first, actionable and scannable output.

Offer a plain concise-output preference if requested. Do not infer a diagnosis, activate a medical label, repeat state unnecessarily or invent time estimates. Existing help and Lite behavior cover most of the value.

Licensing: MIT. Requirements/limits: Instruction-only core, manual-invocation metadata. Session persistence is a behavioral request, not a host settings service.

Inspected source tree: `1ecea1993b7fce257ffbd686c070948b5e07eda6`.

- [skills/i-have-adhd/SKILL.md](https://github.com/ayghri/i-have-adhd/blob/1ecea1993b7fce257ffbd686c070948b5e07eda6/skills/i-have-adhd/SKILL.md)

### coreyhaines31/marketingskills — 60,934 stars when checked

**Keep separate.** SEO, analytics, conversion and product-marketing workflows.

Some technical SEO may be useful when explicitly requested for public websites. Keep marketing strategy, advertising and growth automation outside a general engineering core.

Licensing: MIT. Requirements/limits: Mostly instruction/reference workflows; measurement and actions depend on actual analytics/site/account access.

Inspected source tree: `1f837447b20bb6f0e72d87b80ece1c221c362c7d`.

- [skills/seo-audit/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/seo-audit/SKILL.md)

### emilkowalski/skills — 57,643 stars when checked

**Selective addition.** Purposeful interaction motion, interruption behavior, reduced motion and web/mobile distinctions.

Add a small motion reference under frontend when animation is requested: decide whether it helps, handle interruption/exit and respect reduced motion. Load React Native/Expo guidance only for matching projects. Do not add animation by default.

Licensing: MIT. Requirements/limits: Stack-specific examples; Expo version matching and real-device checks are separate from desktop web testing. Upstream conversational persona/opening requirements are not needed.

Inspected source tree: `64eb3deb9a5fbfa041faf783e0bc3fd635872e9c`.

- [skills/animate/SKILL.md](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/animate/SKILL.md)
- [skills/animate-expo/SKILL.md](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/animate-expo/SKILL.md)

## Exclusions, alternative scopes and maintenance notes

- Host agents/model runtimes such as openclaw, Hermes, Claude Code itself and Pi are outside this ranking. Their bundled/internal developer skills are not a reason to count the entire host as a skill pack.
- Bare agent-role collections, such as msitarzewski/agency-agents, are useful adjacent material but are not the requested SKILL.md/native Claude/Codex plugin category.
- Link-only directories such as VoltAgent/awesome-agent-skills and hesreallyhim/awesome-claude-code help discovery but do not supply a local skill collection. Conversely, Composio and awesome-llm-apps actually contain public skill definitions and are not excluded just because awesome appears in their names.
- cc-switch and model routers without a public skill/native plugin are adjacent desktop/CLI utilities. RTK is a real hook/CLI output optimizer, but its internal development skills and host hooks are not a native Claude/Codex plugin or public reusable SKILL.md package in the inspected tree. It is a separate optional integration, not command interception supplied by skill text.
- GSD old home gsd-build/get-shit-done is archived and its current README points to open-gsd/gsd-core. The new repository had 11,632 stars when checked separately. Do not combine their totals or claim the old home is current.
- A narrower list containing only instruction-first skill packs would rank differently; this report deliberately includes the genuine public plugin/skill adapters of larger applications so they are not silently omitted. Individual adapter popularity cannot be extracted from aggregate repository stars.

## Other specialist sources worth retaining

- [openai/skills](https://github.com/openai/skills), 28,786 stars in the candidate snapshot: official Codex examples, including gh-fix-ci. The relevant actual-log CI investigation method is already represented in this plugin. Per-skill terms and actual authenticated tooling still matter.
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), 34,276 stars: conditional React/Next.js performance references. Match the real stack/version and preserve applicable notices before copying.
- [trailofbits/skills](https://github.com/trailofbits/skills), 8,244 stars: security and deeper testing expertise. Root CC BY-SA 4.0 means copied/adapted text cannot simply be relabeled MIT. Existing property-testing/mutation/related-bug guidance was independently written.
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), 47,531 stars: genuine vendor collection and useful plugin examples. Claude-native packaging/hooks do not prove managed ChatGPT support.
- [MemPalace/mempalace](https://github.com/MemPalace/mempalace), 60,590 stars: actual public skills around a Python memory engine. Optional external integration requiring storage/MCP/capture configuration, not a text-only cross-session memory upgrade.

## Licensing, runtime compatibility and what changed

MIT/Apache-2.0 candidates still require notices and correct attribution. Repository-level license detection is not sufficient. Anthropic uses per-skill notices; sampled frontend-design and docx both currently say Apache-2.0. Composio explicitly warns individual skills may differ. Firecrawl host code is AGPL-3.0 while the sampled build skill declares ISC, requiring exact-file review. prompts.chat has separate MIT/CC0 scope. The Karpathy-inspired source declares MIT but lacked a complete root notice in the inspected tree; no source text from it is currently redistributed by Unified Engineering. This research is not full redistribution clearance.

No newly fetched installer, helper script, hook or plugin was executed. No new plugin was installed, removed, replaced or runtime-tested. No source text was copied into the released plugin. No Unified Engineering file, Git branch or remote was changed. The report/data live in the separate research workspace. Existing plugin runtime evidence does not establish compatibility of these candidates.

A skill can guide on-demand actions, choose references and prepare explicit handoffs through available tools. It cannot create lifecycle events, intercept commands, run a persistent worker or access future-session transcripts merely by describing those capabilities. Keep those integrations optional until independently verified in the target managed environment.

Recommended implementation scope: strengthen existing frontend, security and skill-authoring references first; add optional diagram/motion guidance and repeatable evaluations next. Keep Lite/Full/Ultra quality floors and current routing. These are proposed improvements, not measured outcomes or an implemented release.
