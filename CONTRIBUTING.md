# Contributing to ANT

Thanks for helping make AI agents easier to understand.

## Good first contributions

- Add a before/after example.
- Add glossary entries in your language.
- Improve an installation guide.
- Add eval prompts for a technical situation that agents explain badly.
- Report where ANT makes answers too long or too vague.

## Contribution principles

1. Keep language respectful. Non-technical does not mean less intelligent.
2. Do not remove accuracy to make an answer feel simpler.
3. Explain important risks clearly.
4. Prefer examples from real builder workflows: errors, commands, deployments, auth, databases, Git, hosting.
5. Keep the core skill compact enough to load easily.
6. Do not add telemetry, secret collection, external install scripts, `curl | sh` flows, or instructions that bypass user confirmation.
7. Keep copy/paste usage safe: users should be able to inspect skill text before giving it to an agent.

## Pull request checklist

- [ ] The change improves clarity, safety, or portability.
- [ ] New jargon is explained or avoided.
- [ ] Risky actions are handled with confirmation gates.
- [ ] Examples include a “good” response and optionally a “bad” response.
- [ ] The change does not make the main `SKILL.md` unnecessarily long.
- [ ] The change does not introduce unsafe installer behavior, hidden network calls, telemetry, or requests for secrets.

## Style

Use simple English in shared docs. For localized docs, write naturally in that language rather than translating word-for-word.
