# Unified Engineering 0.2 implementation plan

User instruction: “do whats best”, following the five-source recommendations.
Use inline implementation with one fresh final review. Preserve working 0.1.0,
installed plugins, application repositories and the no-runtime-claims boundary.

## Scope and choices

- Keep the shared policy and 28 existing skills. Add two distinct jobs:
  architecture assessment and focused throwaway prototyping.
- Merge Matt Pocock's domain vocabulary, design/testability, handoff,
  retrospective and plain-language ideas into the relevant existing workflows.
- Add independently worded general guidance for property tests, optional mutation
  checks and finding related occurrences of a known bug. No Trail of Bits text
  is imported or relicensed; link external reading separately.
- Karpathy community collection informs independently phrased scope/verification
  refinements. No source text is copied while its complete notice is unresolved.
- Add real CI-log procedure using available host capabilities, with no required
  CLI installation. Keep stack-specific external bundles out of the core release.
- Copy only selected Matt source files for reproducibility, preserve its full MIT
  notice and source hashes; support their nested skill layout in coverage checks.

## Review focus

New skills must not impose architecture refactors/prototypes on routine edits;
glossaries/handoffs/retrospectives must not write files unless in scope; generated
tests must assert independent properties; bug searches must distinguish a match
from a real defect; all new source/reference paths must stay self-contained.

## Tasks

- [x] 1. Add failing release tests: 30 entries including architecture/prototype,
  Matt notice/source preservation, nested source-map coverage. Extract selected
  regular Matt source files; extend assembler source/notice handling minimally.
- [x] 2. Refine common/existing skills and add two focused skills plus technical
  references. Add holdout application/discovery prompts; test against prior
  guidance and revised guidance without claiming native routing evidence.
- [x] 3. Independent review, required fixes, full checks, clean source ZIP rebuild,
  updated validation notes and release archives. Keep 0.1.0 intact; no installs.
