# ANT — AI Non-Technical Translator

ANT is a small set of ready-to-use AI agent instructions for people who build with AI but do not want technical fog.

Give ANT to Codex, Claude, Cursor, Hermes, OpenClaw, Copilot, or another coding agent when you want it to explain technical work clearly, safely, and in your language.

ANT also includes artifact skills for product maps and recoverable deep research.

## Pick Your ANT

| Choose this | When you want | Use it | Example |
|---|---|---|---|
| ANT Plain Language | “Explain what is happening so I understand it.” | [open](skills/ant-plain-language/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-plain-language/SKILL.md) | [before/after](skills/ant-plain-language/references/before-after.md) |
| ANT Compact | “Keep it short, but do not lose the point.” | [open](skills/ant-compact/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-compact/SKILL.md) | [before/after](skills/ant-compact/references/before-after.md) |
| ANT Low Words | “Use as few words as possible.” | [open](skills/ant-low-words/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-low-words/SKILL.md) | [before/after](skills/ant-low-words/references/before-after.md) |
| ANT Product Map | “Turn this idea into a clear HTML product map.” | [open](skills/ant-product-map/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-product-map/SKILL.md) | [before/after](skills/ant-product-map/references/before-after.md) |
| ANT Research Run | “Research deeply without losing progress.” | [open](skills/ant-research-run/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-research-run/SKILL.md) | [before/after](skills/ant-research-run/references/before-after.md) |

Not sure? Start with **ANT Plain Language**.

## Try It In 60 Seconds

1. Open [ANT Plain Language](skills/ant-plain-language/SKILL.md).
2. Copy the full text.
3. Paste it into your AI agent and say:

```text
Use this skill for this project.
```

If you want a product scheme instead of a communication style, use [ANT Product Map](skills/ant-product-map/SKILL.md) and say:

```text
Use this skill to create a simple HTML product map from my idea or project notes.
```

If the task is deep research, market/lookalike research, or repo critique, use [ANT Research Run](skills/ant-research-run/SKILL.md) and say:

```text
Use this skill to split this research into a brief, evidence pass, critique pass, and synthesis gate.
```

## Trust And Safety Before Install

- You can inspect every skill before using it. They are plain text.
- ANT skills do not ask for API keys, passwords, tokens, billing access, or private account access.
- ANT release archives are static zip files with checksums in the latest GitHub Release.
- Do not paste secrets, customer data, private keys, or production credentials into an AI agent unless you understand the risk.
- ANT tells agents to ask before destructive, public, billing, secret, database, permission, production, or force-push actions.
- The fastest safe path is copy/paste first, installation later if you actually need it.

## Fastest Way To Use It

### Option 1: Copy and paste

1. Open one of the skill files above.
2. Copy the text.
3. Paste it into your agent as an instruction.

You can say:

```text
Use this skill for this project.
```

This works even if your tool does not support formal skill installation.

For ANT Product Map, you can say:

```text
Use this skill to create a simple HTML product map from my idea or project notes.
```

### Option 2: Install with the skills CLI

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
npx skills add SDV-G-Deploy/ant-skills --skill ant-product-map
npx skills add SDV-G-Deploy/ant-skills --skill ant-research-run
```

### Option 3: Download a zip

Download the latest release:

https://github.com/SDV-G-Deploy/ant-skills/releases/latest

Then use one of these files:

```text
ant-plain-language.zip
ant-compact.zip
ant-low-words.zip
ant-product-map.zip
ant-research-run.zip
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

With ANT Product Map:

> Creates a small `product-map.html` that shows the product goal, user, screens, flow, data/integrations, open questions, risks, and next MVP step.

With ANT Research Run:

> Turns a broad research request into a brief, evidence artifact, critique, and synthesis gate so progress survives timeouts and context limits.

## What ANT Tells Agents To Do

- Answer in the user's language.
- Explain technical work before using technical jargon.
- Split broad research into evidence-producing artifacts before synthesis.
- Say what changed and how to check it.
- Keep exact commands, file names, and error text unchanged.
- Ask before risky actions like deleting data, force pushing, changing secrets, billing, permissions, or deploying to production.
- Keep short answers useful: action, verification, and safety must stay.

ANT is not “dumbing down” technical work. It is a communication layer: plain language first, exact technical details when needed, safe steps always.

## More Help

- [Quick start](docs/quick-start.md)
- [Skill catalog](docs/skill-catalog.md)
- [Before/after examples](examples/before-after.en.md)
- [Product Map example input](examples/product-map-input.md)
- [Product Map example output](examples/product-map-output.html)
- [Research Run example](skills/ant-research-run/references/public-example.md)
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
