# ANT before / after examples

These examples show the practical difference between a normal AI-agent answer and the same task handled with an ANT skill.

The goal is not to make the answer longer. The goal is to make it easier to understand, verify, continue, or trust.

## ant-plain-language

User input:

> The build failed. What happened?

Without ANT:

> TS types are wrong. Fix the props and rerun the build.

With ANT:

> The app failed while preparing itself to run or publish. The problem is in TypeScript types: the code says one piece of data should have a certain shape, but another part sends it in a different shape. I will find the mismatch, fix the type or the data shape, then run the build again. It worked if the build finishes without the same TypeScript error.

What changed: the user learns what the error means, what will be changed, and how success will be checked.

## ant-compact

User input:

> Why is the site not starting? Keep it short.

Without ANT:

> Install deps and rerun.

With ANT:

> Meaning: the project cannot find required libraries.
> Action: in the project folder, run npm install, then npm run dev.
> Check: the site starts without the missing-package error.

What changed: the answer stays short but keeps meaning, action, and verification.

## ant-low-words

User input:

> Max short. Why does dev fail?

Without ANT:

> It looks like the environment variable is missing, so you should configure your environment and try again.

With ANT:

> Cause: missing DATABASE_URL.
> Fix: add it to .env.
> Check: npm run dev has no env error.

What changed: fewer words, same operational value.

## ant-product-map

User input:

> I want an AI helper for local workshop hosts. It should turn a rough workshop idea into a landing page outline and launch checklist. I am not sure about payments, login, or database.

Without ANT:

> You could build a landing page generator with signup, payments, templates, and a database. Start with a React app and add authentication.

With ANT:

> Create a static product-map.html with: product goal, primary user, core blocks, first user flow, data and integrations, unknowns, risks, and next MVP step. Mark payments, login, database, and email as unknown instead of assuming them. Recommend testing the outline with three workshop hosts before building infrastructure.

What changed: the output becomes a map with facts, assumptions, unknowns, and a small next step instead of an invented build plan.

## ant-research-run

User input:

> Research what skills non-technical AI builders need. Go deep.

Without ANT:

> Non-technical builders need prompt writing, debugging, deployment, security, product thinking, and testing skills.

With ANT:

> First create a research brief: question, decision supported, scope, out of scope, sources, artifact paths, pass list, and stop conditions. Then run evidence, analysis, critique, and synthesis as separate artifacts. Do not synthesize until the evidence artifact exists. If a run times out, resume from the latest written artifact.

What changed: deep research becomes recoverable work, not one broad answer that can be lost or overconfident.
