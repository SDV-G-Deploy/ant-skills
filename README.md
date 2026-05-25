# ANT — Accessible Non-Technical Translator

ANT Skills is an open, free skill pack for AI coding agents. It gives agents three communication modes: plain-language, compact, and low-words.

**Short description:** Plain-language modes for AI coding agents: clear, compact, low-words.

**Tagline:** ANT helps AI agents build with you, not talk over you.

ANT is for non-technical and mixed-technical builders: founders, creators, product people, designers, marketers, students, junior developers, and anyone using agents such as Codex, Claude Code, Cursor, Hermes Agent, Copilot, Windsurf, Cline, OpenCode, or similar tools.

ANT is not “dumbing down” technical work. It is a communication layer: plain-language first, exact technical details when needed, and safe step-by-step guidance.

## Modes

ANT ships as a small mode family:

| Mode | Use case | Typical size |
|---|---|---|
| `ant-plain-language` | clear explanations for non-technical builders | medium |
| `ant-compact` | short but still understandable | 60–160 words |
| `ant-low-words` | maximum word saving / terse but respectful | 20–80 words |

The goal is not just fewer words. The goal is **fewer words without losing action, verification, or safety**.

See [docs/ant-modes.md](docs/ant-modes.md), [docs/token-saving.md](docs/token-saving.md), [docs/ant-modes.ru.md](docs/ant-modes.ru.md), and [docs/token-saving.ru.md](docs/token-saving.ru.md).

## What ANT changes

When an AI agent uses ANT, it should:

- answer in the user’s language;
- explain technical work before using technical jargon;
- translate or define English technical terms the first time they appear;
- avoid phrases like “just run”, “obviously”, “trivial”, and unexplained acronyms;
- explain terminal commands with where to run them, why they are needed, the exact command, and what success looks like;
- summarize code changes in terms of user-visible impact;
- ask for confirmation before risky actions like deleting data, force pushing, changing secrets, billing, permissions, or deploying to production;
- keep deep implementation details in an optional “Technical appendix”.

## What is inside

```text
skills/ant-plain-language/SKILL.md             # main portable Agent Skill
skills/ant-compact/SKILL.md                    # compact mode
skills/ant-low-words/SKILL.md                  # ultra-compact mode
skills/ant-plain-language/references/          # glossaries, risk gates, communication contract
variants/claude-output-style/ANT.md            # always-on style for Claude Code
variants/claude-output-style/ANT-Compact.md    # compact output style
variants/claude-output-style/ANT-Low-Words.md  # ultra-compact output style
variants/cursor-rules/                         # Cursor rules
variants/agents-md/                            # AGENTS.md snippets
variants/github-copilot/README.md              # GitHub Copilot / VS Code notes
variants/hermes/README.md                      # Hermes Agent notes
variants/prompt-only/                          # copy-paste prompts for tools without skills
evals/                                          # manual evals and rubric
tools/                                          # helper scripts for maintainers
docs/                                           # modes, token-saving notes, compatibility, strategy docs
```

## Quick install

Use a skills-compatible installer:

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
```

Replace `SDV-G-Deploy/ant-skills` if you are installing from a fork.

## Local helper install

For local testing from this repository:

```bash
./tools/install-local.sh agents ant-plain-language
./tools/install-local.sh claude ant-compact
./tools/install-local.sh all ant-low-words
```

If a skill already exists at the target path, the installer stops instead of overwriting it. Add `--force` to replace it; the previous folder will be moved to a timestamped backup first.

On Windows, use the skills-compatible CLI or follow [docs/install-windows.md](docs/install-windows.md). The helper script is Bash-first and is best used from Git Bash, WSL, Linux, or macOS.

## Manual install

### Generic Agent Skills / Codex-style layout

Copy the folder you want:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

to a matching skill location, for example:

```text
~/.agents/skills/ant-plain-language
~/.agents/skills/ant-compact
~/.agents/skills/ant-low-words
.agents/skills/ant-plain-language
.agents/skills/ant-compact
.agents/skills/ant-low-words
```

Use the user-level path for personal use. Use the project-level path when you want the project team to share the same communication behavior.

### Claude Code Skill

Copy the skill folders you want to:

```text
~/.claude/skills/ant-plain-language
~/.claude/skills/ant-compact
~/.claude/skills/ant-low-words
```

For always-on communication styles in Claude Code, also copy:

```text
variants/claude-output-style/ANT.md
variants/claude-output-style/ANT-Compact.md
variants/claude-output-style/ANT-Low-Words.md
```

to:

```text
~/.claude/output-styles/
```

Then choose the output style you want.

### Cursor

Copy the rule you want to:

```text
.cursor/rules/ant-plain-language.mdc
.cursor/rules/ant-compact.mdc
.cursor/rules/ant-low-words.mdc
```

### Hermes Agent

Copy the skill folder you want to:

```text
~/.hermes/skills/ant-plain-language
~/.hermes/skills/ant-compact
~/.hermes/skills/ant-low-words
```

### VS Code / GitHub Copilot

Copy the skill folder to a supported skill location such as:

```text
.github/skills/ant-plain-language
.github/skills/ant-compact
.github/skills/ant-low-words
.agents/skills/ant-plain-language
.agents/skills/ant-compact
.agents/skills/ant-low-words
~/.copilot/skills/ant-plain-language
~/.copilot/skills/ant-compact
~/.copilot/skills/ant-low-words
~/.agents/skills/ant-plain-language
~/.agents/skills/ant-compact
~/.agents/skills/ant-low-words
```

## Examples

Before ANT:

> Run npm install, rebuild, then check the endpoint.

After ANT Plain:

> The project is missing some libraries it needs before it can run. Open the terminal in the project folder and run `npm install`. This downloads the required libraries. When it finishes without red error messages, run the app again.

ANT Compact:

> Meaning: the project cannot find a library.  
> Action: in the project folder, run `npm install`, then `npm run dev`.  
> Check: the site starts without the red error.

ANT Low Words:

> Cause: missing `DATABASE_URL`.  
> Fix: add it to `.env`.  
> Check: `npm run dev` has no env error.

## Recommended names

Use `ant-plain-language`, `ant-compact`, and `ant-low-words`, not just `ant`. “ANT” is good as a brand, but `ant` alone can be confused with Ant Design and other developer tooling.

Possible expansions:

- **Accessible Non-Technical Translator**
- **AI Non-Technical Translator**
- **Agent Non-Technical Translator**

## Project principles

1. Plain language is not less accurate.
2. Non-technical does not mean less intelligent.
3. Agents should explain consequences, not only commands.
4. Safety beats speed for destructive or irreversible actions.
5. Technical details are welcome, but they should not be the first wall the user hits.
6. Fewer words are good only when action, verification, and safety remain intact.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The easiest contribution is a before/after example, a glossary entry in another language, or a compact-mode eval case.

For release archive verification, see [docs/release-verification.md](docs/release-verification.md). For cautious token-saving measurement, see [docs/token-saving-benchmarks.md](docs/token-saving-benchmarks.md).

## License

MIT. Use, fork, translate, and adapt freely.
