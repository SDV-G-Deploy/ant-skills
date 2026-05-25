# Token-saving benchmark guide

ANT Compact and ANT Low Words should be measured carefully. Do not claim a fixed cost reduction such as “80% cheaper” unless a real benchmark supports it.

## What to measure

Measure at least three things separately:

1. Output words or tokens.
2. Whether the answer still includes the next action.
3. Whether the answer still includes verification and safety warnings.

Shorter is only better when action, verification, and safety remain intact.

## Suggested manual benchmark

Use the prompts in `evals/test-prompts.jsonl`.

For each prompt, collect three answers:

1. Normal assistant answer.
2. `ant-compact` answer.
3. `ant-low-words` answer.

For each answer, record:

```text
prompt_id:
mode:
word_count:
has_next_action: yes/no
has_success_check: yes/no
has_safety_warning: yes/no/not-needed
notes:
```

Use `tools/ant_word_budget.py` for a simple word count:

```bash
python3 tools/ant_word_budget.py --max 160 sample-answer.txt
```

## Reporting

Report ranges, not universal promises. Good wording:

> In this small eval set, ANT Compact reduced output words while preserving required checks.

Avoid:

> ANT always cuts token cost by a fixed percentage.
