---
name: ant-product-map
description: Product-map skill for AI agents helping non-technical builders turn an idea, repo, feature brief, messy notes, or product discussion into a simple evidence-based HTML product map. Use when the user asks for a product map, HTML scheme, HTML schema, visual project map, app map, startup idea map, MVP map, user-flow map, service/integration map, or a clear non-technical overview of what a product is, who it serves, what screens/flows/data/integrations exist, what is unknown, and what to do next.
---

# ANT Product Map

Use this skill to turn scattered product context into a simple map a non-technical builder can inspect, share, and hand to another agent or developer.

The default output is a single static product-map.html file. Keep it readable, local, and evidence-based.

For a quick before/after demonstration, see references/before-after.md.

## Core Rules

1. Answer in the user's language.
2. Start from the user's goal, not from architecture.
3. Separate facts from assumptions. Mark unknowns explicitly.
4. Use simple labels: product, user, screens, flow, data, integrations, risks, next step.
5. Prefer a compact HTML map over a long Markdown report when the user wants a scheme/map.
6. Do not invent services, screens, payments, databases, or business logic that are not in evidence.
7. Keep the map useful for humans first and agents second.
8. Ask before publishing, deploying, overwriting an existing file, or using private/secret data.

## Workflow

1. Gather only enough context to map the product:
   - user notes or prompt;
   - README/docs if a repo exists;
   - package/app routes if relevant;
   - existing screenshots or HTML only when needed.
2. Extract the product shape:
   - what it is;
   - who it is for;
   - main promise;
   - key screens or states;
   - main user flow;
   - data and integrations;
   - unclear decisions.
3. Create a small HTML map with sections the user can scan.
4. Add short status labels:
   - known for evidence-backed facts;
   - assumption for likely but unconfirmed items;
   - unknown for missing decisions;
   - risk for safety, privacy, billing, legal, production, or trust issues.
5. End with a small next-step block: 3-5 practical actions.

## Output Contract

When writing a map file, produce one self-contained HTML file:

- no external JavaScript;
- no external CSS;
- no external fonts or analytics;
- no trackers, forms, cookies, or network calls;
- no private tokens, secrets, internal URLs, or credentials;
- semantic HTML with inline CSS;
- responsive layout that works on mobile and desktop;
- clear visual hierarchy without decorative clutter.

Default file names:

- product-map.html for a standalone project;
- docs/maps/<product-slug>.html when the repo already has docs/maps;
- ask before overwriting an existing map.

## HTML Map Rules

Use the bundled reference template as a shape guide when useful: references/product-map-template.html.

The map should include:

1. Header: product name, one-line plain-language description, status/date if known.
2. Who It Is For: primary user, their problem, what success looks like.
3. Product Blocks: core screens, features, or modules; each block gets a simple status label.
4. User Flow: 4-8 steps from entry to outcome.
5. Data And Integrations: accounts, payments, APIs, storage, email, AI, analytics, hosting; mark unknowns instead of guessing.
6. Risks And Open Questions: privacy, payments, production, security, unclear scope, missing owner decisions.
7. Next MVP Step: the smallest useful next action.

## Safety Gates

Pause and ask for confirmation before:

- publishing or deploying the HTML map;
- exposing private project details publicly;
- including secrets, tokens, private URLs, customer data, or personal data;
- changing production systems, DNS, billing, auth, permissions, or databases;
- overwriting an existing map or docs file.

If the source contains secrets, do not repeat them. Say they may be exposed and recommend rotation/revocation.

## Response Shape

After creating or updating a map, report briefly:

    Готово: создала product map.
    Файл: docs/maps/product-name.html
    Что внутри: цель продукта, пользователь, основные блоки, user flow, данные/интеграции, риски и вопросы, следующий MVP-шаг.
    Проверка: открой файл в браузере и посмотри, понятно ли за 30 секунд, что это за продукт и что делать дальше.

Use the same shape in the user's language. In English:

    Done: created the product map.
    File: docs/maps/product-name.html
    Inside: product goal, user, main blocks, user flow, data/integrations, risks and questions, next MVP step.
    Check: open the file in a browser and see whether the product is understandable within 30 seconds.

Keep the explanation short unless the user asks for a deeper audit.

## Quality Bar

A good ANT product map makes the product easier to discuss within 30 seconds.

It should not look like a pitch deck, a landing page, or a full technical architecture diagram. It should be a practical working map for a builder.
