# ANT — Accessible Non-Technical Translator

ANT Skills — это бесплатный open-source skill pack для AI-агентов. Он даёт агентам три режима коммуникации: понятный обычный язык, короткий режим и ультракороткий low-words режим.

**Короткое описание:** Plain-language режимы для AI coding agents: clear, compact, low-words.

**Слоган:** ANT helps AI agents build with you, not talk over you.  
По-русски: **ANT помогает AI-агентам строить вместе с человеком, а не говорить поверх него.**

ANT подходит для non-technical builders: фаундеров, продактов, дизайнеров, маркетологов, студентов, начинающих разработчиков и всех, кто строит сайты, ботов, приложения, автоматизации или внутренние инструменты через AI.

Важно: ANT — это не “упрощение для глупых”. Это слой коммуникации. Сначала смысл, потом действия, потом проверка, а технические детали — отдельно и по делу.

## Что меняет ANT

После установки агент должен:

- отвечать на языке пользователя;
- объяснять технические действия простыми словами;
- переводить или пояснять англоязычные термины при первом появлении;
- не писать “просто запусти”, “очевидно”, “тривиально”;
- объяснять команды: где их запускать, зачем, какая точная команда, как понять, что всё прошло хорошо;
- после изменений в коде говорить, что изменилось и как это проверить;
- просить подтверждение перед опасными действиями: удалить данные, сделать force push, поменять секреты, биллинг, права доступа, деплой в production;
- выносить глубокую технику в блок “Техническое приложение”.

## Режимы

ANT теперь можно использовать в трёх режимах:

| Режим | Для чего | Типичный размер |
|---|---|---|
| `ant-plain-language` | понятные объяснения для non-technical builders | средний |
| `ant-compact` | коротко, но всё ещё понятно | 60–160 слов |
| `ant-low-words` | максимальная экономия слов / очень кратко, но уважительно | 20–80 слов |

Ключевая идея: **не просто меньше слов, а меньше слов без потери действия, проверки и безопасности.**

Подробнее: [docs/ant-modes.ru.md](docs/ant-modes.ru.md) и [docs/token-saving.ru.md](docs/token-saving.ru.md).

## Что внутри

```text
skills/ant-plain-language/SKILL.md             # основной portable Agent Skill
skills/ant-compact/SKILL.md                    # краткий режим
skills/ant-low-words/SKILL.md                  # ultra-compact режим
skills/ant-plain-language/references/          # словари, risk gates, правила коммуникации
variants/claude-output-style/                  # always-on стили для Claude Code
variants/cursor-rules/                         # правила для Cursor
variants/agents-md/                            # вставки для AGENTS.md / инструкций проекта
variants/github-copilot/README.md              # заметки для GitHub Copilot / VS Code
variants/hermes/README.md                      # заметки для Hermes Agent
variants/prompt-only/                          # промпты для ручной вставки
evals/                                          # ручные тесты качества
tools/                                          # маленькие скрипты для мейнтейнеров
docs/                                           # режимы, token-saving, совместимость, strategy docs
```

## Быстрая установка

Через skills-compatible CLI:

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
```

`SDV-G-Deploy/ant-skills` нужно заменить, если устанавливаешь из форка.

## Локальная установка через helper

Для теста из папки репозитория:

```bash
./tools/install-local.sh agents ant-plain-language
./tools/install-local.sh claude ant-compact
./tools/install-local.sh all ant-low-words
```

Если skill уже есть в целевом месте, installer остановится и не перезапишет его молча. Чтобы заменить существующую папку, добавь `--force`; старая версия будет перенесена в timestamped backup.

## Ручная установка

### Codex / generic Agent Skills

Скопируй нужную папку:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

в соответствующее место:

```text
~/.agents/skills/ant-plain-language
~/.agents/skills/ant-compact
~/.agents/skills/ant-low-words
.agents/skills/ant-plain-language
.agents/skills/ant-compact
.agents/skills/ant-low-words
```

Пути с `~` — личная установка. Пути внутри проекта — установка для конкретного репозитория или команды.

### Claude Code

Скопируй нужные папки:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

сюда:

```text
~/.claude/skills/ant-plain-language
~/.claude/skills/ant-compact
~/.claude/skills/ant-low-words
```

Если хочется, чтобы стиль был включён почти всегда, дополнительно скопируй:

```text
variants/claude-output-style/ANT.md
variants/claude-output-style/ANT-Compact.md
variants/claude-output-style/ANT-Low-Words.md
```

сюда:

```text
~/.claude/output-styles/
```

После этого выбери нужный стиль в Claude Code.

### Cursor

Скопируй нужное правило:

```text
variants/cursor-rules/ant-plain-language.mdc
variants/cursor-rules/ant-compact.mdc
variants/cursor-rules/ant-low-words.mdc
```

сюда:

```text
.cursor/rules/ant-plain-language.mdc
.cursor/rules/ant-compact.mdc
.cursor/rules/ant-low-words.mdc
```

Это хороший вариант, если ANT должен применяться ко всем ответам внутри проекта.

### Hermes Agent

Скопируй нужный skill:

```text
skills/ant-plain-language
skills/ant-compact
skills/ant-low-words
```

сюда:

```text
~/.hermes/skills/ant-plain-language
~/.hermes/skills/ant-compact
~/.hermes/skills/ant-low-words
```

### VS Code / GitHub Copilot

Скопируй skill в один из поддерживаемых путей:

```text
.github/skills/ant-plain-language
.github/skills/ant-compact
.github/skills/ant-low-words
.agents/skills/ant-plain-language
.agents/skills/ant-compact
.agents/skills/ant-low-words
~/.copilot/skills/ant-plain-language
~/.copilot/skills/ant-compact
~/.copilot/skills/ant-low-words
~/.agents/skills/ant-plain-language
~/.agents/skills/ant-compact
~/.agents/skills/ant-low-words
```

## Пример “до / после”

До ANT:

> Run npm install, rebuild, then check the endpoint.

После ANT:

> Проект не нашёл библиотеки, которые нужны ему для запуска. Открой терминал в папке проекта и выполни `npm install`. Эта команда скачает нужные библиотеки. Если всё хорошо, установка закончится без красных ошибок. После этого запусти проект снова. Если ошибка останется — пришли новый текст ошибки, и я переведу её на нормальный язык.


## Пример ANT Compact

Обычный ответ:

> You need to install the missing dependency and then restart the development server.

ANT Compact:

> Смысл: проект не нашёл библиотеку.  
> Действие: в папке проекта запусти `npm install`, потом `npm run dev`.  
> Проверка: сайт запускается без красной ошибки.

## Пример ANT Low Words

> Причина: нет `DATABASE_URL`.  
> Фикс: добавь его в `.env`.  
> Проверка: `npm run dev` без env-ошибки.

## Почему лучше технические имена `ant-plain-language`, `ant-compact`, `ant-low-words`

ANT / муравей — хорошее название для бренда. Но пакеты лучше назвать `ant-plain-language`, `ant-compact`, `ant-low-words`, потому что просто `ant` легко спутать с Ant Design и другими developer-инструментами.

Расшифровки:

- **Accessible Non-Technical Translator**
- **AI Non-Technical Translator**
- **Agent Non-Technical Translator**

## Принципы проекта

1. Простой язык не значит неточный язык.
2. Non-technical не значит “менее умный”.
3. Агент должен объяснять последствия, а не только команды.
4. Перед опасными действиями нужна пауза и подтверждение.
5. Технические детали нужны, но они не должны быть первой стеной на пути пользователя.

## Что делать дальше

Смотри [docs/strategy/launch-plan.ru.md](docs/strategy/launch-plan.ru.md). Там есть короткий план: как назвать репозиторий, что выложить, как собрать первые примеры и как проверить, что skill реально делает ответы понятнее.

## Лицензия

MIT. Можно использовать, форкать, переводить и адаптировать.
