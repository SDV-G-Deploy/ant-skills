# ANT примеры до / после

Эти примеры показывают разницу между обычным ответом AI-агента и тем же запросом со skill ANT.

Хороший пример должен делать улучшение видимым: понятнее смысл, меньше слов, безопаснее scope, есть артефакт или прогресс можно восстановить.

## ant-plain-language

Ввод:

> Сборка упала. Что случилось?

Без ANT:

> TS2322 in src/App.tsx. Prop type mismatch. Fix the component props and rerun tsc.

С ANT:

> Приложение упало на проверке внутренней согласованности кода. Один компонент ждёт данные одной формы, а другая часть приложения передаёт их в другой форме. Я поправлю несовпадение в src/App.tsx и снова запущу проверку типов. Всё хорошо, если ошибка TS2322 исчезла.

Разница: техническая точность осталась, но человек понимает смысл ошибки, место фикса и проверку.

## ant-compact

Ввод:

> Почему сайт не стартует? Коротко.

Без ANT:

> Похоже, проблема с зависимостями. Нужно всё переустановить, снова запустить dev server и посмотреть, повторится ли ошибка.

С ANT:

- Смысл: не хватает библиотек.
- Действие: npm install, потом npm run dev.
- Проверка: сайт стартует без missing-package ошибки.

Разница: ответ короче и практичнее: смысл, действие, проверка.

## ant-low-words

Ввод:

> Максимально коротко. Почему dev падает?

Без ANT:

> It looks like the environment variable is missing, so you should configure your environment and try again.

С ANT:

- Нет DATABASE_URL.
- Добавь в .env.
- Повтори npm run dev.

Разница: вместо вежливой фразы получается короткая рабочая записка.

## ant-product-map

Ввод:

> Хочу AI-помощника для ведущих локальных воркшопов. Он должен превращать идею воркшопа в outline лендинга и launch checklist. Про payments, login и database пока не уверен.

Без ANT:

> Сделайте React app с регистрацией, оплатой, шаблонами, dashboard, базой данных и email automation. Начните с выбора auth provider.

С ANT:

> Создай product-map.html: цель продукта, пользователь, блоки, первый user flow, данные/интеграции, unknowns, risks, next MVP step. Payments, login, database и email пометь как unknown. Следующий шаг: проверить outline на трёх ведущих воркшопов до постройки инфраструктуры.

Разница: агент не выдумывает большой продукт, а создаёт карту с фактами, неизвестным, рисками и маленькой проверкой.

## ant-research-run

Ввод:

> Исследуй, какие skills нужны non-technical AI builders. Глубоко.

Без ANT:

> Non-technical builders need prompt writing, debugging, deployment, security, product thinking, and testing skills.

С ANT:

- Artifact 1: research brief.
- Artifact 2: evidence matrix.
- Artifact 3: critique.
- Artifact 4: synthesis.
- Правило: не делать synthesis до evidence; после timeout продолжать с последнего artifact.

Разница: глубокое исследование становится восстанавливаемым workflow с артефактами, а не одним широким ответом.
