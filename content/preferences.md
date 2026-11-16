# Preferences, scope and host capabilities

This is an instruction-only configuration contract, not a background settings service.

| Field | Allowed values | Default |
|---|---|---|
| mode | lite, full, ultra | full |
| workflow | auto, manual | auto |
| specialists | auto, manual | auto |

Precedence: current explicit user instruction, earlier explicit session choice, existing project preference, defaults. Host requirements and applicable project rules remain binding. Keep the effective choice in the conversation; do not reread settings on every tool call. When a project root is confirmed, check once for an existing `.unified-engineering.json` there, as relevant to resolving preferences. Do not search other projects or the user's home. Accept only a JSON object containing the documented string values. Ignore invalid/unknown fields and report them briefly; never execute settings as commands.

Example project file (write only if the user asks to save defaults):

```json
{"mode":"full","workflow":"auto","specialists":"auto"}
```

Lite delivers the requested scope with minimal ceremony. Full favors the smallest complete solution. Ultra additionally challenges an unnecessary feature or abstraction once, explaining a concrete cost; it accepts an informed decision. Do not reopen approved scope merely because the mode is Ultra.

Manual means do not automatically expand into optional workflows or other specialists. Explicit invocation still applies the requested skill. Preserve ordinary correctness, evidence and security checks. “Stop unified engineering” or “normal mode” suspends optional plugin guidance in the current session until explicitly resumed; it cannot disable host rules or other plugins. A one-shot audit/debt/gain report does not change modes.

Do not promise persistence in a new conversation, a universal compaction hook, a statusline or hidden telemetry. Include effective preferences in a user-authorized handoff when useful. If settings are absent in a fresh conversation, use the defaults. No credential belongs in this file.

Delegation, cross-model review, new tool installation, external publishing and deletion are not authorized by a preference value. Follow the user's actual authorization and the host's tools. If a capability is missing, state what is unavailable and continue permitted useful work inline when possible; ask only if the unavailable method was a binding requirement.

Plugin and skill name mentions are intent, not commands to an invented tool. Use native skill discovery/reading, including cloud resource APIs. A `skill://` resource is not a filesystem path. On ChatGPT use @ selection or plain language; CLI and Claude slash syntax are not guaranteed Android interfaces. Native implicit matching and manual-only metadata require target-host testing; these instructions cannot alter the host router deterministically.
