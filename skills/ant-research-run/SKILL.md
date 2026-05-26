---
name: ant-research-run
description: Break deep AI research into recoverable, evidence-based passes. Use when a user asks for deep research, market/lookalike research, repo critique, roadmap research, multi-source investigation, or any long AI-agent research that may hit timeouts, context limits, or produce weak final-only summaries.
version: 0.5.0
license: MIT
tags:
  - research
  - deep-research
  - agent-workflow
  - checkpoints
  - non-technical
  - artifact
---

# ANT Research Run

You help a builder run deep AI research without losing progress.

ANT Research Run means: split the work, write artifacts early, checkpoint progress, synthesize only after evidence exists.

Plain version: when a research task is too big for one AI answer, turn it into small passes that each leave a useful artifact behind.

## When To Use

Use this skill when the user asks for:

- deep research;
- lookalike or competitor research;
- repo/product critique;
- roadmap research;
- best-practice research;
- multi-agent or multi-pass investigation;
- long research that should be saved as files;
- a research workflow that must survive timeouts or context limits.

Do not use it for a simple factual lookup.

## Core Rule

The final chat answer is not the deliverable.

The deliverable is a small set of Markdown artifacts that can be inspected, continued, and synthesized.

If the tool cannot write files, produce one complete Markdown artifact in chat at a time. Tell the user which artifact it is and wait before moving to the next one.

Use clear artifact headers so the user can copy each artifact into a file later.

## Workflow

### 1. Create The Research Brief

Define:

- question;
- decision this research supports;
- scope;
- out of scope;
- known sources;
- artifact paths;
- pass list;
- stop conditions.

If key context is missing, make a reasonable assumption and mark it, unless the missing decision is risky or impossible to recover.

If the request asks for everything, narrow it to the first decision and first evidence pass. Say what is deferred.

### 2. Split Into Passes

Default pass sequence:

1. brief - define the research contract.
2. evidence - collect sources, examples, files, and observations.
3. analysis - extract patterns and implications.
4. critique - attack weak claims and assumptions.
5. synthesis - turn findings into decisions and next actions.

Use fewer passes for smaller work. Do not combine evidence and synthesis for broad research.

### 3. Write Artifacts Early

Every long pass must create or update its Markdown artifact within the first 3-5 minutes.

Default artifact names:

- research-brief.md
- research-evidence.md
- research-critique.md
- research-synthesis.md

If the project has a docs/research folder, prefer dated names there, such as 2026-05-26-topic-evidence.md.

Required sections:

- status;
- scope;
- source/evidence table;
- findings;
- confidence and gaps;
- checkpoint log.

### 4. Use A Ledger

For multi-pass work, maintain a ledger:

| Pass | Status | Artifact | Notes |
| --- | --- | --- | --- |
| evidence | useful / partial / failed | path | ... |
| critique | useful / partial / failed | path | ... |
| synthesis | ready / blocked | path | ... |

### 5. Recover From The Latest Artifact

If a run times out or fails:

1. Inspect the artifact.
2. Mark whether it is useful, partial, stub, or failed.
3. Continue from that artifact with a narrower pass.
4. Do not restart from the original broad prompt unless no artifact exists.

### 6. Synthesize Only After Evidence

Before synthesis, check:

- Is there a source/evidence table?
- Are findings prioritized?
- Are confidence and gaps explicit?
- Are weak claims challenged?

If not, run a completion pass first.

## Artifact Templates

### Research Brief

- Question:
- Decision this supports:
- Audience:
- Scope:
- Out of scope:
- Known sources:
- Artifact paths:
- Passes:
- Stop conditions:

### Evidence Table

| Source | Type | Why inspected | Useful finding | Implication | Confidence |
| --- | --- | --- | --- | --- | --- |

For market or current-events research, add a Date / Freshness column.

If a source fetch fails, is sparse, or looks weak, keep it in the table only when useful and mark confidence as Low. Do not pretend weak evidence is strong.

### Critique Table

| Severity | Claim / assumption | Evidence | Risk | Recommended correction |
| --- | --- | --- | --- | --- |

### Checkpoint Log

00:03 - Created artifact and source plan.
00:08 - Inspected first source group.
00:14 - Added evidence table.
00:20 - Prioritized findings and marked gaps.

## Output Shape For The User

Keep chat updates short:

Status:
- Evidence: useful / partial / failed - path
- Critique: useful / partial / failed - path
- Synthesis: ready / blocked

Next:
- ...

Do not paste long reports into chat unless the user asks.

## Tiny Example

Bad request:

Research competitors and tell me what to build.

Better research run:

1. Brief: define the decision and scope.
2. Evidence: collect 15 comparable products in a table.
3. Analysis: find repeated patterns.
4. Critique: challenge weak assumptions.
5. Synthesis: recommend the next 3 product moves.

For a complete public-facing example, read references/public-example.md when preparing docs, release notes, or a user-facing explanation of this skill.

## Safety And Quality

Ask before external/public actions such as publishing, posting, emailing, deploying, billing, changing permissions, or exposing private data.

Do not claim research is complete when artifacts are weak. Say exactly what is useful, partial, or blocked.

## Final Check

Before finishing, verify:

- artifacts exist;
- source/evidence table exists;
- findings are prioritized;
- gaps are marked;
- synthesis is based on evidence, not vibe;
- the user knows the next action.
