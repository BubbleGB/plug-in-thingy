---
name: implement
description: "Use when executing an approved plan or implementing a specified multi-file change. Not when asked only to investigate, review or design."
---
# Implement the smallest complete change

{{POLICY}}

Read the current task, actual workspace state and applicable design/plan. Preserve existing edits. Check whether the environment already supplies isolation before creating branches or worktrees. Do not modify unrelated repositories.

For each deliverable:

1. Trace affected callers and tests; find existing helpers, components and conventions. Reuse them before adding code, dependencies or abstraction.
2. Establish a meaningful behavior test first for new logic or a bug fix. Use the project's existing runner. Mechanical edits get an appropriate validator/inspection instead of a mirrored unit test.
3. Implement one complete vertical slice with needed validation and error handling. Preserve public contracts unless the task changes them. Safe defaults and rollback matter where data changes.
4. Run relevant verification and inspect results. Fix the root cause of failures; do not weaken tests or suppress checks to get green.
5. Update the existing task record and necessary documentation. Continue authorized work without repeated “shall I continue?” prompts. Record consequential deviations and their reason.

A deliberate shortcut is acceptable only within the requested requirements; record `shortcut: <known limit>, <when to upgrade>` where useful. Never label missing validation, data protection or unfinished requested behavior a shortcut.

Use one consolidated review for a coherent change when warranted by its size/risk. A new trust boundary needs specialist scrutiny, not multiple independent lifecycle chains. Delegation is an explicitly requested option through `delegate`, not the default implementation method.

Finish with evidence tied to the final state and remaining material limits. Preparing work does not itself authorize publishing, deployment, merges or deleting the workspace.
