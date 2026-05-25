# Compatibility notes

ANT is designed around the portable Agent Skills pattern: a folder containing `SKILL.md` with at least `name` and `description` metadata, plus optional references and assets.

## Skills

```text
skills/ant-plain-language/SKILL.md
skills/ant-compact/SKILL.md
skills/ant-low-words/SKILL.md
skills/ant-product-map/SKILL.md
```

Use these for skills-compatible agents.

## Always-on variants

Some tools are better served by always-on instructions rather than on-demand skills.

- Claude Code: use `variants/claude-output-style/ANT.md`, `ANT-Compact.md`, or `ANT-Low-Words.md`.
- Cursor: use files in `variants/cursor-rules/`.
- Generic project instructions: use snippets in `variants/agents-md/`.

## Why both skill and style/rules?

A skill is best when the agent can activate it for relevant tasks. A style or rule is best when you want the communication behavior to apply to every technical answer.

For ANT, both are useful:

- `SKILL.md` makes it portable and installable.
- Output style / rules make it reliable as a default communication layer.

## Which mode should be installed?

- Install `ant-plain-language` for most non-technical users.
- Install `ant-compact` when the user often asks for short answers.
- Install `ant-low-words` only when token-saving is more important than teaching.
- Install `ant-product-map` when the user wants product ideas, app flows, or repo context turned into a simple HTML map.

All modes keep safety warnings.
