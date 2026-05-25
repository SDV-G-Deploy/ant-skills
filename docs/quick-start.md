# Quick start

ANT can be used in two ways:

1. Copy a skill into your agent as plain text.
2. Install a skill with a skills-compatible installer.

If you are not sure what to choose, use `ant-plain-language`.

## Choose

| Need | Skill |
|---|---|
| You want clear explanations for technical work | `ant-plain-language` |
| You want shorter answers that still keep the next step and safety | `ant-compact` |
| You want the fewest useful words | `ant-low-words` |
| You want an HTML map of a product idea or repo | `ant-product-map` |

## Copy/paste use

Open one skill file:

- [ANT Plain Language](../skills/ant-plain-language/SKILL.md)
- [ANT Compact](../skills/ant-compact/SKILL.md)
- [ANT Low Words](../skills/ant-low-words/SKILL.md)
- [ANT Product Map](../skills/ant-product-map/SKILL.md)

Copy the full text and paste it into your agent with:

```text
Use this skill for this project.
```

This works for tools that do not support formal skill installation.

For `ant-product-map`, use:

```text
Use this skill to create a simple HTML product map from my idea or project notes.
```

## CLI install

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
npx skills add SDV-G-Deploy/ant-skills --skill ant-product-map
```

## Download

Go to:

https://github.com/SDV-G-Deploy/ant-skills/releases/latest

Download one archive:

```text
ant-plain-language.zip
ant-compact.zip
ant-low-words.zip
ant-product-map.zip
```

## Check that it worked

Ask your agent a technical question. A good ANT-style answer should:

- explain the practical meaning first;
- give a concrete next action;
- say how to check success;
- warn before risky or destructive actions.
