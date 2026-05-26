# ANT before / after examples

These examples show the practical difference between a normal AI-agent answer and the same task handled with an ANT skill.

A good example should make the improvement visible: clearer meaning, fewer words, safer scope, a real artifact, or recoverable progress.

## ant-plain-language

Input:

> The build failed. What happened?

Without ANT:

> TS2322 in src/App.tsx. Prop type mismatch. Fix the component props and rerun tsc.

With ANT:

> The app failed while checking whether the code is internally consistent. One component expects data in one shape, but another part of the app sends it in a different shape. I will fix the mismatch in src/App.tsx, then run the type check again. It worked if the same TS2322 error is gone.

Difference: the technical error is still accurate, but the user now understands what it means, where the fix is, and how it will be checked.

## ant-compact

Input:

> Why is the site not starting? Keep it short.

Without ANT:

> It is probably a dependency issue. You should reinstall everything and try running the development server again, then see if the same error appears.

With ANT:

- Meaning: required libraries are missing.
- Action: run npm install, then npm run dev.
- Check: the site starts without the missing-package error.

Difference: the answer is shorter and more actionable: meaning, action, check.

## ant-low-words

Input:

> Max short. Why does dev fail?

Without ANT:

> It looks like the environment variable is missing, so you should configure your environment and try again.

With ANT:

- Missing DATABASE_URL.
- Add to .env.
- Rerun npm run dev.

Difference: the output becomes a tiny operational note, not a sentence trying to sound helpful.

## ant-product-map

Input:

> I want an AI helper for local workshop hosts. It should turn a rough workshop idea into a landing page outline and launch checklist. I am not sure about payments, login, or database.

Without ANT:

> Build a React app with signup, payments, templates, dashboard, database, and email automation. Start by choosing an auth provider.

With ANT:

> Create product-map.html with: product goal, primary user, core blocks, first user flow, data/integrations, unknowns, risks, and next MVP step. Mark payments, login, database, and email as unknown. Next step: test the outline with three workshop hosts before building infrastructure.

Difference: the agent stops inventing a full product and creates a map that separates facts, assumptions, unknowns, risks, and the next smallest test.

## ant-research-run

Input:

> Research what skills non-technical AI builders need. Go deep.

Without ANT:

> Non-technical builders need prompt writing, debugging, deployment, security, product thinking, and testing skills.

With ANT:

- Artifact 1: research brief.
- Artifact 2: evidence matrix.
- Artifact 3: critique.
- Artifact 4: synthesis.
- Rule: no synthesis before evidence; resume from the latest artifact after timeout.

Difference: deep research becomes a recoverable workflow with named artifacts instead of one broad answer.
