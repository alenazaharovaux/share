# desk-research

A Claude Code skill that runs desk research on open data, from the question to the conclusions: scientific papers, reports, statistics, public registers, company websites and prices, job ads, reviews. Every statement in the result has a source, a date and a verbatim quote. A program checks each quote against the source, and a fresh session re-checks whatever the program could not confirm.

**This skill works only together with [verify-sources](../verify-sources/).** desk-research finds sources and collects quotes. verify-sources contains the program that opens every source and checks that the quote and each number are really there. Install both skills into the same skills folder.

## Two modes

| Mode | When | What you get |
|---|---|---|
| Quick reference | One question, such as "how big is the market for X" | `fakty.md`, `claims.json`, `verification.md`, `spravka.md` |
| Full desk | Several question blocks, or the result goes to a client | Source registers per block, fact files, `verification.md`, `review.md`, conclusions per block, summary with gaps |

In the full desk Claude stops twice and waits for you: after the research plan and after the source registers.

## Installation

Install both skills. Run the commands from the `skills` folder of this repository.

**macOS / Linux:**
```bash
cp -r desk-research ~/.claude/skills/desk-research
cp -r verify-sources ~/.claude/skills/verify-sources
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse desk-research $env:USERPROFILE\.claude\skills\desk-research
Copy-Item -Recurse verify-sources $env:USERPROFILE\.claude\skills\verify-sources
```

For Codex, copy both folders to `~/.agents/skills/`.

## First run

On the first run the skill asks four questions and saves the answers to `config.md` in its folder. Each question can be skipped.

| Question | Why | Example answer |
|---|---|---|
| Where are your projects? | The desk goes into a `desk/` folder inside the project | `~/Projects` |
| Where should it look for past desks? | So the same research is not done twice | `~/Projects, ~/Archive` |
| Is there a project card file to log the finished desk in? | One line about the desk goes into the card | `README.md` |
| Which search services are connected: Exa, Consensus, papers? | The skill picks tools per question block | `exa, papers` |

## Usage

- "desk research: what is known about the effect of remote work on turnover"
- "quick reference: market size of online language schools in Germany, 2024"
- "how do other companies publish their salary ranges, collect sources"
- "find studies about onboarding length and retention"
- "кабинетка по теме …"

## Dependencies

- **verify-sources** — required, from this repository.
- **Python 3.8+** — required. The scripts use only the standard library.
- **Internet access for scripts.** In Codex, enable it once in `~/.codex/config.toml`: `[sandbox_workspace_write]` → `network_access = true`.
- **Search services** — optional. [Exa](https://exa.ai) for web, reports and companies; [Consensus](https://consensus.app) for evidence-based science with meta-analysis filters; papers MCP for free search across OpenAlex, Semantic Scholar, Crossref, PubMed and arXiv. Without them the skill uses the agent's regular web search.

## Where the rules come from

The method file `references/method.md` cites its sources: PRISMA 2020 for the search trail, the Oxford CEBM levels of evidence, the AACODS checklist for grey literature, the OECD statistics quality framework, Wohlin on snowballing, Greenhalgh and Peacock on search methods. The verification rules come from the author's [KINEMETRIC experiment](https://kinemetric.vercel.app/): six models wrote a literature review, all 60 links were live, and one model invented all the content around them.

The skill and its texts are in Russian. Claude talks to you in your language.

By [Alena Zakharova](https://github.com/alenazaharovaux) · MIT

---

# desk-research (RU)

Навык Claude Code ведёт кабинетное исследование на открытых данных от вопроса до выводов. Он ищет научные статьи, отчёты, статистику, реестры, сайты и цены компаний, вакансии и отзывы. У каждого утверждения в результате есть источник, дата и дословная цитата. Программа проверяет каждую цитату по самому источнику, а новая сессия перепроверяет то, что программа подтвердить не смогла.

**Навык работает только вместе с [verify-sources](../verify-sources/).** desk-research ищет источники и собирает цитаты. В verify-sources лежит программа, которая открывает каждый источник и проверяет, что цитата и каждое число в нём действительно есть. Ставить нужно оба навыка в одну папку навыков.

## Два режима

| Режим | Когда | Что получится |
|---|---|---|
| Быстрая справка | Один вопрос, например «какой размер рынка X» | `fakty.md`, `claims.json`, `verification.md`, `spravka.md` |
| Полный деск | Несколько блоков вопросов или результат идёт заказчику | Реестры источников по блокам, файлы фактов, `verification.md`, `review.md`, выводы по блокам, итог со списком пробелов |

В полном деске Claude дважды останавливается и ждёт вашего «ок»: после плана поиска и после реестров источников.

## Установка

Поставьте оба навыка. Команды запускаются из папки `skills` этого репозитория.

**macOS / Linux:**
```bash
cp -r desk-research ~/.claude/skills/desk-research
cp -r verify-sources ~/.claude/skills/verify-sources
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse desk-research $env:USERPROFILE\.claude\skills\desk-research
Copy-Item -Recurse verify-sources $env:USERPROFILE\.claude\skills\verify-sources
```

Для Codex скопируйте обе папки в `~/.agents/skills/`.

## Первый запуск

При первом запуске навык задаёт четыре вопроса и записывает ответы в `config.md` в своей папке. Любой вопрос можно пропустить.

| Вопрос | Зачем | Пример ответа |
|---|---|---|
| В какой папке ваши проекты? | Деск кладётся в папку `desk/` внутри проекта | `~/Projects` |
| Где искать прошлые дески? | Чтобы не делать одно исследование дважды | `~/Projects, ~/Archive` |
| Есть ли у проекта файл-карточка для записи о деске? | В карточку добавится строка о сделанном деске | `README.md` |
| Какие поисковые сервисы подключены: Exa, Consensus, papers? | Навык подбирает инструменты под каждый блок вопросов | `exa, papers` |

## Как запускать

- «кабинетка: что известно про влияние удалёнки на текучесть»
- «быстрая справка: размер рынка онлайн-школ языков в Германии за 2024 год»
- «как другие компании публикуют вилки зарплат, собери источники»
- «найди исследования про длительность онбординга и удержание»
- «деск по теме …»

## Что нужно установить

- **verify-sources** — обязательно, из этого репозитория.
- **Python 3.8 или новее** — обязательно. Скрипты используют только стандартную библиотеку.
- **Интернет для скриптов.** В Codex его включают один раз в `~/.codex/config.toml`: `[sandbox_workspace_write]` → `network_access = true`.
- **Поисковые сервисы** — по желанию. [Exa](https://exa.ai) ищет по вебу, отчётам и компаниям. [Consensus](https://consensus.app) ищет по доказательной науке с фильтром по метаанализам. MCP-сервер papers бесплатно ищет по OpenAlex, Semantic Scholar, Crossref, PubMed и arXiv. Без них навык пользуется обычным веб-поиском агента.

## Откуда правила

Файл метода `references/method.md` ссылается на свои источники: PRISMA 2020 для поискового следа, уровни доказательности Оксфордского центра доказательной медицины, чек-лист AACODS для серой литературы, рамку качества статистики ОЭСР, работу Волина о снежном коме, Гринхал и Пикока о способах поиска. Правила проверки взяты из [эксперимента KINEMETRIC](https://kinemetric.vercel.app/) автора навыка: шесть моделей писали обзор литературы, все 60 ссылок оказались живыми, а одна модель выдумала всё содержание вокруг них.

Навык и его тексты на русском. С вами Claude говорит на вашем языке.

Автор — [Алёна Захарова](https://github.com/alenazaharovaux) · MIT
