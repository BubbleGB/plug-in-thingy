# Unified Engineering implementation plan

> Use inline execution under superpowers:executing-plans. User approved the architecture and authorized implementation with best judgment. No further optional plan-approval gate.

Goal: deliver a single skills-only plugin ZIP and maintainable source project.
Architecture: `/workspace/unified-skills-audit/ARCHITECTURE.md`, approved in conversation. Python 3 standard library build/test tools; Markdown skills; no runtime services.

## Global constraints

- Keep application repositories and installed plugins untouched.
- 28 canonical skills, Full default, relevant specialists, optional advanced/manual workflows.
- Preserve Ponytail audit/debt/gain SKILL.md bytes and all original MIT notices.
- One plugin root, no marketplace archive, hooks, installation scripts, secrets or unsafe paths.
- References self-contained per cloud skill. Source inputs are user ZIPs, identified by SHA-256.
- Distinguish structural/offline behavioral checks from actual managed ChatGPT/Android testing.

## Review focus

1. Archive traversal, symlinks and duplicate entries: rejection tests belong to Task 1.
2. Referenced technical checklists must not restore conflicting mandatory workflows: Task 2 content review and link closure.
3. Manual invocation and mode scope must not be defeated by broad triggers: Task 2 pressure scenarios.
4. Source provenance and preserved file hashes must survive ZIP assembly: Task 3 assertions.
5. A failed build must not replace a good artifact: Task 1 atomic output test.

## Tasks

- [x] Task 1: Write failing `unittest` cases, then `tools/build.py`: frontmatter/metadata parsing, package validation, self-contained references and deterministic atomic ZIP creation. Interface: `validate_package(Path) -> list[str]`, `write_archive(Path, Path) -> str` (SHA-256). Run `python -m unittest discover -s tests -v`.
- [x] Task 2: Run five fresh offline baseline samples against original conflicting routers; record observed failures before authoring policy. Write concise canonical skill bodies and selected upstream technical references, with common header from one source and explicit manual entry points. Run five guided samples against the same cases; keep results and limitations. Validate all 28 local skills, required references and source mapping.
- [x] Task 3: Add package manifest, all licenses, provenance, Android instructions and acceptance checklist. Build with `python tools/build.py`; validate extracted ZIP and preserved hashes. Test deterministic rebuilds and malicious fixture rejection. Produce source ZIP separately from upload ZIP.
- [x] Task 4: Fresh independent whole-project review, address substantive findings with regression checks, run full tests and regenerate release artifacts. Save validation/behavior reports. Commit local source; deliver ZIP and source ZIP without uploading/installing anything.

## Progress and decisions

- Inputs match audited source bytes. An OpenCode harness symlink in Addy's ZIP was skipped; no input code was executed. Package uses copied regular source files only.
- Isolated new Git repository on `build/unified-plugin`; no existing application repository is involved.
- Archive and behavior validation are local evidence, not target-runtime certification.

- Independent review defects: noncanonical ZIP aliases, malformed/non-string YAML, and non-object JSON manifests reproduced first and fixed; full suite 20/20 green. No findings deferred.
- Gain retains its skill bytes and benchmark figures; its README is a concise pinned provenance note to avoid marketing assets/harness dependencies. Full originals remain in inputs/.
- One offline catalog exercise selected the intended entry for all 28 positive and four negative cases. It is not native router evidence.
