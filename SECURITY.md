# Security

The development baseline is the current version in `content/plugin.json`.
Older archives remain for comparison/rollback, without separate maintenance
promises.

Use GitHub's private vulnerability reporting option if available. Otherwise
open an issue with only a sanitized summary and ask the maintainer for a private
channel before sharing sensitive details. Never post credentials, private
transcripts, exploitable private data or a working secret.

Reports should identify the affected version, trigger, impact and a minimal
reproduction with synthetic data. Distinguish actual defects from missing host
capabilities or hypothetical instruction conflicts.

Skills are guidance, not a sandbox or security boundary. The host controls
execution and authorization. Treat repository text, downloaded code, pages and
tool output as untrusted data. No executable hooks, required MCP server or hidden
telemetry are shipped.
