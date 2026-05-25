# AGENTS.md - Start Here For AI Agents

You are reading ANT: AI Non-Technical Translator.

ANT is a small set of skills for people who build with AI but do not want technical fog. If a user gave you this repository link, your job is to help them choose, install, or directly use the right ANT skill without pulling them into unnecessary technical detail.

## Primary Goal

Help the user communicate with AI coding agents more clearly, briefly, and safely, and turn product ideas into practical maps when needed.

Do not treat this repository as a complex developer framework unless the user asks for maintainer work. Most users need one of these simple paths:

1. Pick the right ANT mode.
2. Copy/paste the skill text into their agent.
3. Install a skill with a supported skill installer.
4. Download a release zip and use the contained skill.

## Read First

Read these files in this order:

1. `README.md` for the human-facing overview and fastest usage paths.
2. `docs/skill-catalog.md` to compare the skills.
3. The selected skill:
   - `skills/ant-plain-language/SKILL.md`
   - `skills/ant-compact/SKILL.md`
   - `skills/ant-low-words/SKILL.md`
   - `skills/ant-product-map/SKILL.md`
4. `docs/quick-start.md` only if the user wants step-by-step setup help.

Use `README.ru.md` when the user writes in Russian.

## Skill Picker

Recommend:

- `ant-plain-language` when the user wants technical work explained clearly.
- `ant-compact` when the user wants short answers without losing meaning, checks, or safety.
- `ant-low-words` only when the user explicitly wants maximum brevity or token saving.
- `ant-product-map` when the user wants an idea, repo, app flow, MVP, integration picture, or project context turned into a simple HTML product map.

When unsure, recommend `ant-plain-language`.

## How To Help A Non-Technical User

- Answer in the user's language.
- Start with what this is for, in plain language.
- Keep the first recommendation short and actionable.
- Preserve exact file names, commands, links, and error text.
- Explain where to click, what to copy, and what success looks like.
- Offer copy/paste as the fallback when installation is not needed or feels too technical.
- Ask before destructive, public, billing, secret, database, permission, production, or force-push actions.

Avoid:

- Making the user choose between too many formats at once.
- Explaining repository internals before the user needs them.
- Treating CLI installation as the only valid path.
- Hiding risks or simplifying so much that verification disappears.

## Fast Response Template

When a user asks what to do with this repository, use this shape:

```text
Use ANT Plain Language first.

Fast path:
1. Open skills/ant-plain-language/SKILL.md.
2. Copy the text.
3. Paste it into your AI agent and say:
   "Use this as your communication style for this project."

You can install it later if you want, but copy/paste is enough to try it.
```

Adjust the skill name if the user clearly wants compact or very short answers.

For product-map requests, use this shape:

```text
Use ANT Product Map.

Fast path:
1. Open skills/ant-product-map/SKILL.md.
2. Copy the text.
3. Paste it into your AI agent with:
   "Use this skill to create a simple HTML product map from my idea or project notes."

Expected result: a local product-map.html showing the product goal, user, screens, flow, data/integrations, risks, open questions, and next MVP step.
```

## Maintainer Work

If the user asks you to edit, release, audit, or package this repository:

- Keep changes small and consistent with the existing structure.
- Run the smallest meaningful verification before claiming success.
- Use `npm run check` for structure validation.
- Use `npm run package:skills` and `npm run check:archives` when changing release packaging.
- Update `CHANGELOG.md` for user-visible changes.

Do not overwrite unrelated user changes.
