# ANT for Hermes Agent

Hermes Agent uses skills as on-demand knowledge documents and keeps user skills under:

```text
~/.hermes/skills/
```

To install ANT manually, copy the skill folders you want:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

to:

```text
~/.hermes/skills/ant-plain-language
~/.hermes/skills/ant-compact
~/.hermes/skills/ant-low-words
```

Recommended first test prompts:

```text
Use ant-plain-language. Explain this error in Russian: Cannot find module react
```

```text
Use ant-compact. Коротко объясни ошибку Cannot find module vite.
```

```text
Use ant-low-words. Очень коротко: что делать с missing DATABASE_URL?
```
