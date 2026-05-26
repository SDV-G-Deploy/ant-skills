# ANT Research Run Public Example

This example shows how the skill changes a broad research request into a recoverable research run.

## Example Input

    Research the market for AI tools for non-technical founders.
    Find competitors, best practices, pricing, workflows, risks, and tell me what product I should build.

## Why This Input Is Risky

The request is too broad for one reliable AI answer.

If handled as one run, the result will likely be:

- shallow;
- hard to verify;
- missing sources;
- too big for chat;
- fragile if the run times out.

## Better ANT Research Run Response

    # Research Brief

    Question:
    What should we learn first about AI tools for non-technical founders before deciding what product to build?

    Decision this supports:
    Choose the next product direction or feature area.

    Audience:
    Non-technical founders and builders using AI tools to create apps, automations, content, or internal tools.

    Scope for first pass:
    - 15-20 comparable tools or workflows;
    - user jobs they support;
    - onboarding patterns;
    - trust/safety patterns;
    - pricing and packaging notes when visible.

    Out of scope for first pass:
    - full market sizing;
    - final product recommendation;
    - financial model;
    - legal/compliance review;
    - implementation plan.

    Artifacts:
    - research-brief.md
    - research-evidence.md
    - research-critique.md
    - research-synthesis.md

    Passes:
    1. Evidence pass: collect source matrix.
    2. Analysis pass: find repeated patterns.
    3. Critique pass: challenge weak assumptions.
    4. Synthesis pass: recommend 3 possible product moves.

    Stop conditions:
    - at least 15 sources inspected;
    - every major conclusion has evidence;
    - weak or failed sources are marked Low confidence;
    - synthesis waits until evidence and critique exist.

## First Evidence Artifact Shape

    # Research Evidence

    Status:
    First pass.

    Scope:
    Comparable AI tools and workflows for non-technical founders.

    | Source | Type | User | Useful finding | Implication | Confidence |
    | --- | --- | --- | --- | --- | --- |
    | Tool A | AI app builder | Founder | Onboarding starts from a plain-language idea. | ANT should support idea-to-brief flow. | Medium |
    | Tool B | Automation builder | Operations user | Uses templates for common workflows. | ANT may need workflow templates later. | Medium |
    | Tool C | Coding agent docs | Builder/developer | Strong emphasis on project instructions and validation. | ANT task briefs should include checks. | High |

    Findings:
    1. Non-technical users need help turning intent into structured tasks.
    2. Trust depends on clear scope, checks, and risk warnings.
    3. The strongest tools show a first useful output quickly.

    Gaps:
    - Pricing needs a separate pass.
    - No final product recommendation yet.
    - More sources needed before synthesis.

    Checkpoint log:
    00:03 - Created artifact and source plan.
    00:10 - Added first source group.
    00:18 - Marked early patterns and gaps.

## Short User Update

    Status:
    - Brief: done.
    - Evidence: started as research-evidence.md.
    - Synthesis: blocked until evidence and critique exist.

    Next:
    - collect the 15-20 source matrix, then run pattern analysis.

## What The Skill Prevented

It did not try to answer everything at once.

It turned one vague deep-research request into:

- a decision-focused brief;
- a bounded first pass;
- explicit deferred topics;
- evidence artifacts;
- a synthesis gate.
