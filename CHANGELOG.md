# Changelog

## 0.4.2 - Public trust polish

- Added a README trust-and-safety section for public visitors and AI agents.
- Added a root `llms.txt` so agents given the repository link can quickly understand the project, skills, safe usage path, and release URL.
- Added a small Product Map example input and static HTML output.
- Updated release verification docs for the four-skill archive set and downloaded checksum validation.

## 0.4.1 - Product map flow polish

- Clarified copy/paste prompts and AI-agent flow for `ant-product-map` so it is presented as an HTML product-map artifact skill, not only as a communication style.

## 0.4.0 - Product maps

- Added `ant-product-map`, a new skill for turning ideas, repo context, app flows, MVP notes, or product discussions into simple evidence-based HTML product maps for non-technical builders.
- Added a bundled product-map HTML template and UI metadata for the new skill.
- Updated README, quick start, compatibility notes, catalog, installer whitelist, structure checks, and release archive validation for four skills.

## 0.3.6 - Pre-public hardening

- Added root `AGENTS.md` so AI agents given the repository link know how to help non-technical users choose, copy, install, or use ANT.
- Added pre-public repository hardening: CODEOWNERS, Dependabot for GitHub Actions, pinned CI actions, read-only workflow permissions, and stronger contribution/security guardrails.

## 0.3.5 - Human-first quick start

- Reworked README and README.ru around choosing, copying, and installing a skill quickly.
- Added docs/quick-start.md for copy/paste and CLI use.
- Moved maintainer/release details lower in the public entry flow.

## 0.3.4 - Install docs and release verification

- Added Windows/PowerShell install notes.
- Added release archive validation for expected files and unwanted build artifacts.
- Added SHA256 checksum generation for release archives.
- Added a cautious token-saving benchmark guide without percentage claims.
- Expanded CI to validate release archives after packaging.

## 0.3.3 - CI and skill metadata

- Added GitHub Actions CI for structure checks, Python syntax, JSON validation, shell syntax, lint, packaging, and install smoke tests.
- Added `agents/openai.yaml` metadata for each skill.
- Extended the structure checker to verify skill UI metadata.

## 0.3.2 - Installer safety and audit fixes

- Made `tools/install-local.sh` executable for documented `./tools/install-local.sh` usage.
- Added installer preflight so multi-target installs do not leave partial installs after a refusal.
- Applied the same refuse/backup behavior to Claude Output Style files.
- Tightened `ant-compact` triggers so explicit ANT Low Words requests route to `ant-low-words`.
- Added pasted-secret handling guidance and eval coverage.
- Replaced stale Russian README next-step guidance after public release.

## 0.3.1 — Public polish

- Polished public README install wording now that the repository is published.
- Softened public `ant-low-words` wording while keeping the explicit trigger phrase supported.
- Removed the internal release handoff document from the public repository.

## 0.3.0 — Compact modes

- Added `ant-compact` skill for short, plain-language technical answers.
- Added `ant-low-words` skill for ultra-compact, respectful token-saving answers.
- Added Claude Output Style variants for Compact and Low Words.
- Added Cursor and AGENTS.md snippets for compact modes.
- Added prompt-only Compact and Low Words variants in Russian and English.
- Added token-saving strategy docs and compact manual evals.
- Updated structure checker to validate all skills.

## 0.2.0 — MVP package

- Added main `ant-plain-language` skill.
- Added references: communication contract, risk gates, English/Russian glossaries, examples.
- Added Claude Output Style variant.
- Added Cursor rule variant.
- Added AGENTS.md snippet.
- Added Hermes and GitHub Copilot notes.
- Added prompt-only variants.
- Added manual evals and rubric.
- Added docs: product brief, launch plan, roadmap, tone guide, compatibility notes.
- Added helper scripts for maintainers.

## 0.1.0 — Initial starter

- First sketch of ANT as a plain-language skill.
