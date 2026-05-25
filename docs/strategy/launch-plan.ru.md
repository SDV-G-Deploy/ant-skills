# План запуска ANT

## Шаг 1 — GitHub repo

Рекомендуемое имя:

```text
ant-skills
```

Описание репозитория:

```text
Plain-language communication skill for AI coding agents. Helps non-technical builders understand code, errors, commands, deployments, and risks.
```

Topics:

```text
agent-skills, ai-agents, codex, claude-code, cursor, hermes-agent, github-copilot, non-technical, plain-language, vibe-coding
```

## Шаг 2 — Первая версия

Положи в репозиторий содержимое этого ZIP. Первый тег:

```text
v0.2.0
```

Почему не `v1.0.0`: нужно собрать обратную связь от реальных пользователей и проверить, как skill активируется в разных агентах.

## Шаг 3 — README и демо

В README нужны три вещи сразу сверху:

1. Кому это нужно.
2. Один пример “до / после”.
3. Команда установки.

Хороший демо-пост:

```text
I made ANT — a free open-source skill that makes AI coding agents explain technical work in plain language.

Before:
“Just install deps and rerun build.”

After:
“The project is missing libraries it needs. Open the terminal in the project folder and run npm install…”

For non-technical builders, founders, designers, PMs, students, and anyone vibe-coding with agents.
```

## Шаг 4 — Первые площадки

Где можно опубликовать:

- GitHub;
- X / Twitter;
- LinkedIn;
- Reddit: r/ClaudeAI, r/ChatGPTCoding, r/vibecoding, r/cursor;
- Product Hunt позже, когда будут отзывы;
- русскоязычные Telegram/VC/Хабр посты;
- discussions/communities вокруг Claude Code, Codex, Cursor, Hermes.

## Шаг 5 — Сбор обратной связи

Проси пользователей присылать:

- ответы “до / после”;
- непонятные термины;
- ошибки, где агент всё равно говорит слишком технически;
- ситуации, где агент не спросил подтверждение перед опасным действием;
- языки, на которые нужен словарь.

## Шаг 6 — v0.3.0

Следующая версия может добавить:

- испанский словарь;
- португальский словарь;
- французский словарь;
- больше примеров для деплоя, auth, базы данных, Git;
- отдельный `ant-debug-translator` skill;
- отдельный `ant-founder-brief` skill;
- автоматический eval runner.

## Шаг 7 — v1.0.0

Версия 1.0.0 уместна, когда:

- есть 20–30 реальных примеров “до / после”;
- skill проверен минимум в Codex, Claude Code, Cursor и Hermes;
- есть понятные installation guides;
- нет частых жалоб, что ответы стали слишком длинными;
- risk gates реально срабатывают.
