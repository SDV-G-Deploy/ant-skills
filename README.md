# ANT — AI Non-Technical Translator

ANT is a small set of ready-to-use AI agent instructions for people who build with AI but do not want technical fog.

Give ANT to Codex, Claude, Cursor, Hermes, OpenClaw, Copilot, or another coding agent when you want it to explain technical work clearly, safely, and in your language.

## Pick Your ANT

| Choose this | When you want | Use it |
|---|---|---|
| ANT Plain Language | “Explain what is happening so I understand it.” | [open](skills/ant-plain-language/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-plain-language/SKILL.md) |
| ANT Compact | “Keep it short, but do not lose the point.” | [open](skills/ant-compact/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-compact/SKILL.md) |
| ANT Low Words | “Use as few words as possible.” | [open](skills/ant-low-words/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-low-words/SKILL.md) |

Not sure? Start with **ANT Plain Language**.

## Fastest Way To Use It

### Option 1: Copy and paste

1. Open one of the three skill files above.
2. Copy the text.
3. Paste it into your agent as an instruction.

You can say:

```text
Use this as your communication style for this project.
```

This works even if your tool does not support formal skill installation.

### Option 2: Install with the skills CLI

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
```

### Option 3: Download a zip

Download the latest release:

https://github.com/SDV-G-Deploy/ant-skills/releases/latest

Then use one of these files:

```text
ant-plain-language.zip
ant-compact.zip
ant-low-words.zip
```

## What ANT Changes

Without ANT:

> Run npm install, rebuild, then check the endpoint.

With ANT Plain Language:

> The project is missing some libraries it needs before it can run. Open the terminal in the project folder and run `npm install`. This downloads the required libraries. When it finishes without red error messages, run the app again.

With ANT Compact:

> Meaning: the project cannot find a library.  
> Action: in the project folder, run `npm install`, then `npm run dev`.  
> Check: the site starts without the red error.

With ANT Low Words:

> Cause: missing `DATABASE_URL`.  
> Fix: add it to `.env`.  
> Check: `npm run dev` has no env error.

## What ANT Tells Agents To Do

- Answer in the user's language.
- Explain technical work before using technical jargon.
- Say what changed and how to check it.
- Keep exact commands, file names, and error text unchanged.
- Ask before risky actions like deleting data, force pushing, changing secrets, billing, permissions, or deploying to production.
- Keep short answers useful: action, verification, and safety must stay.

ANT is not “dumbing down” technical work. It is a communication layer: plain language first, exact technical details when needed, safe steps always.

## More Help

- [Quick start](docs/quick-start.md)
- [Skill catalog](docs/skill-catalog.md)
- [Before/after examples](examples/before-after.en.md)
- [Russian README](README.ru.md)
- [Windows install notes](docs/install-windows.md)

## For Maintainers And Advanced Users

The repository also includes release and quality infrastructure:

```text
skills/                  # canonical Agent Skill folders
variants/                # Claude, Cursor, AGENTS.md, Copilot, Hermes, prompt-only variants
docs/                    # modes, install notes, release verification, token-saving notes
evals/                   # manual evals and rubric
tools/                   # packaging, lint, archive checks, local install helper
.github/                 # CI, issue templates, PR template
```

Useful maintainer docs:

- [Release verification](docs/release-verification.md)
- [Token-saving benchmark guide](docs/token-saving-benchmarks.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## License

MIT. Use, fork, translate, and adapt freely.

