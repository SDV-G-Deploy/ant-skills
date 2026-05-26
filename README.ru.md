# ANT — AI Non-Technical Translator

ANT — это маленький набор готовых инструкций для AI-агентов, которые помогают строить проекты без технического тумана.

Дай ANT в Codex, Claude, Cursor, Hermes, OpenClaw, Copilot или другой coding agent, если хочешь, чтобы агент объяснял техническую работу понятно, безопасно и на твоём языке.

В ANT также есть artifact-skills: продуктовые HTML-карты и recoverable deep research.

## Выбери свой ANT

| Выбери | Когда подходит | Использовать |
|---|---|---|
| ANT Plain Language | “Объясни, что происходит, чтобы я понял.” | [открыть](skills/ant-plain-language/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-plain-language/SKILL.md) |
| ANT Compact | “Коротко, но без потери смысла.” | [открыть](skills/ant-compact/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-compact/SKILL.md) |
| ANT Low Words | “Максимально мало слов.” | [открыть](skills/ant-low-words/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-low-words/SKILL.md) |
| ANT Product Map | “Собери из идеи понятную HTML-карту продукта.” | [открыть](skills/ant-product-map/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-product-map/SKILL.md) |
| ANT Research Run | “Исследуй глубоко, но не теряй прогресс.” | [открыть](skills/ant-research-run/SKILL.md) / [raw](https://raw.githubusercontent.com/SDV-G-Deploy/ant-skills/main/skills/ant-research-run/SKILL.md) |

Если сомневаешься, начни с **ANT Plain Language**.

## Попробовать за 60 секунд

1. Открой [ANT Plain Language](skills/ant-plain-language/SKILL.md).
2. Скопируй весь текст.
3. Вставь его своему AI-агенту и напиши:

```text
Используй этот skill для этого проекта.
```

Если нужна не манера общения, а схема продукта, открой [ANT Product Map](skills/ant-product-map/SKILL.md) и напиши:

```text
Используй этот skill, чтобы сделать простую HTML-карту продукта из моей идеи или заметок по проекту.
```

Если нужна глубокая исследовательская задача, market/lookalike research или критика repo, открой [ANT Research Run](skills/ant-research-run/SKILL.md) и напиши:

```text
Используй этот skill, чтобы разбить исследование на brief, evidence pass, critique pass и synthesis gate.
```

## Доверие и безопасность перед установкой

- Каждый skill можно сначала прочитать: это обычный текст.
- ANT skills не просят API keys, пароли, tokens, биллинг или доступ к приватным аккаунтам.
- Release archives — это статические zip-файлы; checksums лежат в последнем GitHub Release.
- Не вставляй секреты, клиентские данные, private keys или production credentials в AI-агента, если не понимаешь риск.
- ANT просит агентов спрашивать подтверждение перед опасными действиями: удалить данные, публиковать, менять биллинг, секреты, базу, права, production или делать force push.
- Самый безопасный быстрый путь: сначала copy/paste, установка потом, если она реально нужна.

## Самый быстрый способ

### Вариант 1: скопировать и вставить

1. Открой один из skill-файлов выше.
2. Скопируй текст.
3. Вставь его агенту как инструкцию.

Можно написать:

```text
Используй этот skill для этого проекта.
```

Так можно пользоваться ANT даже в инструменте, где нет формальной установки skills.

Для ANT Product Map можно написать:

```text
Используй этот skill, чтобы сделать простую HTML-карту продукта из моей идеи или заметок по проекту.
```

### Вариант 2: установить через skills CLI

```bash
npx skills add SDV-G-Deploy/ant-skills --skill ant-plain-language
npx skills add SDV-G-Deploy/ant-skills --skill ant-compact
npx skills add SDV-G-Deploy/ant-skills --skill ant-low-words
npx skills add SDV-G-Deploy/ant-skills --skill ant-product-map
npx skills add SDV-G-Deploy/ant-skills --skill ant-research-run
```

### Вариант 3: скачать zip

Открой последний релиз:

https://github.com/SDV-G-Deploy/ant-skills/releases/latest

И скачай нужный файл:

```text
ant-plain-language.zip
ant-compact.zip
ant-low-words.zip
ant-product-map.zip
ant-research-run.zip
```

## Что меняет ANT

Без ANT:

> Run npm install, rebuild, then check the endpoint.

С ANT Plain Language:

> Проект не нашёл библиотеки, которые нужны ему для запуска. Открой терминал в папке проекта и выполни `npm install`. Эта команда скачает нужные библиотеки. Если всё хорошо, установка закончится без красных ошибок. После этого запусти проект снова.

С ANT Compact:

> Смысл: проект не нашёл библиотеку.  
> Действие: в папке проекта запусти `npm install`, потом `npm run dev`.  
> Проверка: сайт запускается без красной ошибки.

С ANT Low Words:

> Причина: нет `DATABASE_URL`.  
> Фикс: добавь его в `.env`.  
> Проверка: `npm run dev` без env-ошибки.

С ANT Product Map:

> Создаёт небольшой `product-map.html`: цель продукта, пользователь, экраны, flow, данные/интеграции, вопросы, риски и следующий MVP-шаг.

С ANT Research Run:

> Превращает широкий research-запрос в brief, evidence artifact, critique и synthesis gate, чтобы прогресс не терялся из-за timeout или контекстного лимита.

## Что ANT просит агента делать

- Отвечать на языке пользователя.
- Объяснять технические действия простыми словами.
- Разбивать большие исследования на evidence-артефакты до synthesis.
- Говорить, что изменилось и как это проверить.
- Не переводить точные команды, имена файлов и тексты ошибок.
- Спрашивать подтверждение перед опасными действиями: удалить данные, сделать force push, поменять секреты, биллинг, права доступа или деплой в production.
- Не выкидывать действие, проверку и безопасность ради краткости.

ANT — это не “упрощение для глупых”. Это слой коммуникации: сначала смысл, потом действия, потом проверка, а технические детали — отдельно и по делу.

## Ещё помощь

- [Быстрый старт](docs/quick-start.md)
- [Каталог skills](docs/skill-catalog.md)
- [Примеры до/после](examples/before-after.ru.md)
- [Product Map example input](examples/product-map-input.md)
- [Product Map example output](examples/product-map-output.html)
- [Research Run example](skills/ant-research-run/references/public-example.md)
- [English README](README.md)
- [Windows install notes](docs/install-windows.md)

## Для мейнтейнеров и продвинутых пользователей

В репозитории также есть инфраструктура качества и релизов:

```text
skills/                  # основные Agent Skill папки
variants/                # Claude, Cursor, AGENTS.md, Copilot, Hermes, prompt-only варианты
docs/                    # режимы, установка, проверка релизов, token-saving notes
evals/                   # ручные evals и rubric
tools/                   # packaging, lint, archive checks, local install helper
.github/                 # CI, issue templates, PR template
```

Полезные maintainer docs:

- [Release verification](docs/release-verification.md)
- [Token-saving benchmark guide](docs/token-saving-benchmarks.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Лицензия

MIT. Можно использовать, форкать, переводить и адаптировать.
