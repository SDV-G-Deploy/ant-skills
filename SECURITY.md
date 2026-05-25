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
