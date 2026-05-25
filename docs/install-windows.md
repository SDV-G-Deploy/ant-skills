# Windows install notes

The recommended Windows path is the skills-compatible CLI:

```powershell
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
```

The local helper script, `tools/install-local.sh`, is Bash-first. Use it from Git Bash or WSL:

```bash
./tools/install-local.sh agents ant-plain-language
./tools/install-local.sh claude ant-compact
./tools/install-local.sh all ant-low-words
```

For manual install, copy the skill folder into a supported skill directory:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

Common destinations:

```text
%USERPROFILE%\.agents\skills\ant-plain-language
%USERPROFILE%\.agents\skills\ant-compact
%USERPROFILE%\.agents\skills\ant-low-words
.agents\skills\ant-plain-language
.agents\skills\ant-compact
.agents\skills\ant-low-words
```

For Claude Code on Windows, use the equivalent Claude skills or output-style folders for your installation. If the app does not expose a Windows skill folder, prefer the CLI install path or the prompt-only variants in `variants/prompt-only/`.
