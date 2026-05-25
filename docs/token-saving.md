# ANT token-saving strategy

The goal of `ant-compact` and `ant-low-words` is not simply to write less. The goal is to preserve action, meaning, and safety with fewer words.

## What we save

1. **Output tokens** — words the agent writes to the user.
2. **Conversation history** — shorter replies pollute future context less.
3. **Human time** — users find the next step faster.

## What brevity alone does not solve

A terse style does not always cut total cost dramatically, because modern reasoning models may spend tokens on hidden reasoning, input context, files, logs, and tool outputs. ANT Low Words is useful, but it should not be marketed as a magical “-80% cost” without evals.

## Correct formula

```text
fewer words + same next action + same safety = good compression
fewer words - safety = bad compression
fewer words - clarity = bad compression
```

## Compress first

1. Greetings and praise.
2. Repeating the user's request.
3. Generic phrases.
4. Long theory.
5. Multiple options when one best option exists.
6. Technical appendix unless requested.

## Do not compress away

1. Commands.
2. Where to run the command.
3. What success looks like.
4. Risk warnings.
5. Uncertainty that changes the decision.
6. File names, variables, APIs, and error text.

## Future high-value feature

Add `ant-session-summary`:

- after a long session, the agent writes a compact summary;
- keeps decisions, changed files, commands, open questions;
- removes chatter;
- makes the next agent session cheaper and clearer.

This can help cost and context more than short answers alone.
