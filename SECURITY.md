# Security policy

ANT is primarily an instruction pack, not a code execution tool. Still, it includes safety guidance because AI agents often work with files, production systems, credentials, and user data.

## Report a concern

Open an issue if ANT encourages or fails to prevent risky behavior, such as:

- deleting data without confirmation;
- exposing API keys or secrets;
- deploying to production without confirmation;
- weakening authentication or permissions;
- suggesting dangerous shell commands without warning;
- making private data public.

## Safety principle

ANT should always pause before actions that affect real users, money, production, security, privacy, or irreversible data changes.

## Public repository rules

ANT is meant to be copied into AI agents. Public contributions must therefore stay inspectable and conservative.

Do not add:

- `curl | sh` or similar one-line remote execution install flows;
- telemetry, tracking, analytics, or background network calls;
- prompts that ask users to paste secrets, API keys, tokens, private URLs, or credentials;
- instructions that tell agents to skip confirmation for destructive, billing, permission, production, secret, or data actions;
- hidden or obfuscated code paths in release tooling.

Preferred patterns:

- readable Markdown instructions;
- explicit copy/paste paths users can inspect;
- whitelisted local installer targets;
- checks that validate release archives before publishing.
