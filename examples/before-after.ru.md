# ANT примеры "до / после"

Эти примеры показывают разницу между обычным ответом AI-агента и тем же запросом со skill ANT.

Цель не в том, чтобы сделать ответ длиннее. Цель — сделать его понятнее, проверяемее и безопаснее.

## ant-plain-language

Ввод:

> Сборка упала. Что случилось?

Без ANT:

> TS types are wrong. Fix the props and rerun the build.

С ANT:

> Приложение не смогло подготовиться к запуску или публикации. Проблема в TypeScript-типах: одна часть кода ждёт данные одной формы, а другая передаёт их в другой форме. Я найду это несовпадение, поправлю тип или данные, потом снова запущу сборку. Всё хорошо, если сборка завершится без той же TypeScript-ошибки.

Что изменилось: человек понимает смысл ошибки, действие и проверку результата.

## ant-compact

Ввод:

> Почему сайт не стартует? Коротко.

Без ANT:

> Install deps and rerun.

С ANT:

> Смысл: проект не нашёл нужные библиотеки.
> Действие: в папке проекта запусти npm install, потом npm run dev.
> Проверка: сайт стартует без ошибки про missing package.

Что изменилось: ответ короткий, но не теряет смысл, действие и проверку.

## ant-low-words

Ввод:

> Максимально коротко. Почему dev падает?

Без ANT:

> It looks like the environment variable is missing, so you should configure your environment and try again.

С ANT:

> Причина: нет DATABASE_URL.
> Фикс: добавь в .env.
> Проверка: npm run dev без env-ошибки.

Что изменилось: меньше слов, но действие осталось точным.

## ant-product-map

Ввод:

> Хочу AI-помощника для ведущих локальных воркшопов. Он должен превращать идею воркшопа в outline лендинга и launch checklist. Про payments, login и database пока не уверен.

Без ANT:

> Можно сделать генератор лендингов с регистрацией, оплатой, шаблонами и базой данных. Начните с React app и добавьте authentication.

С ANT:

> Создай статичный product-map.html: цель продукта, пользователь, блоки, первый user flow, данные и интеграции, unknowns, risks, next MVP step. Payments, login, database и email пометь как unknown, а не придумывай. Следующий шаг: проверить outline на трёх ведущих воркшопов до постройки инфраструктуры.

Что изменилось: вместо выдуманного build plan появляется карта с фактами, неизвестным и маленьким следующим шагом.

## ant-research-run

Ввод:

> Исследуй, какие skills нужны non-technical AI builders. Глубоко.

Без ANT:

> Non-technical builders need prompt writing, debugging, deployment, security, product thinking, and testing skills.

С ANT:

> Сначала создай research brief: вопрос, решение, scope, out of scope, sources, artifact paths, pass list, stop conditions. Потом отдельно evidence, analysis, critique и synthesis. Не делай synthesis, пока нет evidence artifact. Если run упал по timeout, продолжай с последнего записанного artifact.

Что изменилось: глубокое исследование становится recoverable workflow, а не одним широким ответом.
