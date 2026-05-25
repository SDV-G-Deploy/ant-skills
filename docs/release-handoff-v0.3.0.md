# ANT Skills v0.3.0 release handoff

Date: 2026-05-25

Repository: https://github.com/SDV-G-Deploy/ant-skills
Release: https://github.com/SDV-G-Deploy/ant-skills/releases/tag/v0.3.0

## Current state

`ant-skills` is a public open-source Agent Skills repository for AI coding-agent communication modes.

Published skills:

- `ant-plain-language`: explains technical work in clear human language for non-technical and mixed-technical builders.
- `ant-compact`: short technical help that keeps meaning, next action, verification, and safety.
- `ant-low-words`: ultra-compact mode for repeated coding updates and maximum word saving.

The initial public release is `v0.3.0`. Release archives are attached for direct/manual install:

- `ant-plain-language.zip`
- `ant-compact.zip`
- `ant-low-words.zip`

## Repository layout

```text
skills/                  # canonical Agent Skill folders
variants/                # Claude, Cursor, AGENTS.md, Copilot, Hermes, prompt-only variants
docs/                    # mode docs, token-saving notes, compatibility, strategy notes
docs/strategy/           # product/launch strategy docs kept separate from core install docs
evals/                   # manual evals and test prompts
examples/                # before/after examples
tools/                   # helper checks, packaging, local install
.github/                 # issue and PR templates
```

## Verification already run

Before publishing and release creation:

- `python3 tools/check_skill_structure.py` -> PASS
- `python3 -m py_compile tools/*.py` -> OK
- `python3 -m json.tool package.json` -> OK
- `bash -n tools/install-local.sh` -> OK
- Quick secret-pattern scan for obvious live keys -> no findings
- Release archives regenerated via `python3 tools/package_skills.py` and inspected

GitHub state after release:

- Public repository: yes
- Main branch pushed: yes
- Tag pushed: `v0.3.0`
- GitHub Release created: yes
- Release assets: 3 skill zip archives

## Important implementation notes

- `tools/install-local.sh` was changed before publication so it no longer silently removes an existing installed skill. It now refuses to overwrite unless `--force` is passed, and with `--force` it moves the previous folder to a timestamped backup.
- `dist/` was removed from source before the initial commit. Release zip files are generated from source and attached to GitHub Releases instead of being kept in the repo.
- Strategy documents from the source material were moved into `docs/strategy/` to keep public install docs separate from product-roadmap thinking.
- `package.json` remains `private: true`; this is intentional for GitHub-only release. Revisit only if npm publishing becomes a goal.

## Known follow-up review targets

Ask an independent reviewer to check:

1. Skill trigger descriptions: are the three skills distinct enough for an agent to choose correctly?
2. Safety gates: do compact and low-words preserve destructive/production/security warnings clearly enough?
3. README clarity: does a new user understand which skill to install first?
4. Installer behavior: is `--force` backup handling clear and safe?
5. Release packaging: are the zip archives minimal and installable?
6. Public posture: any wording that sounds condescending, too broad, or overclaims token savings?
7. Privacy/security: any examples that look like real secrets or encourage copying sensitive values?

## Suggested codex_alt_high prompt

```text
Audit https://github.com/SDV-G-Deploy/ant-skills as an open-source Agent Skills repo.

Focus on public-readiness, skill quality, security/privacy, install docs, release packaging, and whether the three skills are cleanly separated.

Do not make changes. Produce findings with severity, file/line references, and concrete fixes. Check the v0.3.0 release assets too if possible.
```

## Next likely work

- Run independent `codex_alt_high` audit.
- Apply any public-readiness fixes.
- Consider whether to add `agents/openai.yaml` metadata per skill in a future release.
- Start a separate `ant-map` repository only after combining `ant.map` branding with Product X-Ray evidence rigor.
