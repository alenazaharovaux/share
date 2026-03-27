# Tool Scout

Find the right tools for your project tasks — services, MCP servers, AI models, no-code platforms, libraries, and APIs. The skill searches across five sources (web, GitHub, MCP catalogs, awesome-lists, and package registries) so you don't have to figure out where to look. It covers both established and recently launched tools.

## What's new in v2

- **GitHub search** via `gh` CLI — finds repos by stars, searches code in `modelcontextprotocol/servers`
- **MCP catalog search** — queries smithery.ai and the official MCP servers list
- **Awesome-lists** — finds `awesome-*` repos, reads their READMEs, extracts tools
- **Adaptive source selection** — picks which sources to query based on task type (SaaS → web only; MCP server → web + GitHub + catalogs; unclear → all sources)
- **Signals column** — GitHub stars and archived status right in the results table
- **Deduplication** — a tool found in three sources appears once, with aggregated signals
- **Trivial task detection** — if the task is three lines of code, the skill says so instead of running a full search
- **Graceful fallback** — works without `gh` CLI by using web search with `site:github.com`

## Installation

**macOS / Linux:**
```bash
cp -r tool-scout ~/.claude/skills/tool-scout
```

**Windows:**
```powershell
Copy-Item -Recurse tool-scout $env:USERPROFILE\.claude\skills\tool-scout
```

## First Run

On first use, the skill runs a short setup:

| Question | Why | Example answer |
|----------|-----|----------------|
| Which search tool do you have? | The skill needs web search. Exa MCP gives the best results, but built-in WebSearch works too | `exa` |
| GitHub CLI available? | Auto-detected via `gh --version`. Enables direct repo search and star counts | (automatic) |
| What language for results? | So the skill communicates in your language | `english` |

Settings are saved to `~/.claude/skills/tool-scout/config.md`.

### Search engine options

| Engine | Setup needed? | Quality | Notes |
|--------|--------------|---------|-------|
| **Exa MCP** (recommended) | Yes — [setup guide](https://docs.exa.ai/reference/mcp) | Best | Web search + code context search |
| **WebSearch** | No — built into Claude Code | Good | Works out of the box |
| **Other MCP** | Depends | Varies | Any MCP server that provides web search |

### GitHub CLI (optional but recommended)

If `gh` is installed and authenticated, the skill uses it for precise searches (`gh search repos --sort=stars`). Without it, GitHub search falls back to web queries with `site:github.com` — functional but less precise.

Install: [cli.github.com](https://cli.github.com/)

## Usage

Say any of these to Claude Code:

- "find tools for building a dashboard UI"
- "is there an MCP server for Google Sheets?"
- "tool scout — I need to process images in bulk"
- "find a library for PDF generation in Python"
- "what tools exist for email automation?"

### Two levels of depth

**Level 1 (default):** Adaptive search across relevant sources, results as a table with signals.

**Level 2 (on request):** Say "dig into [tool name]" or ask about a specific source ("any awesome-lists for this?", "what about MCP servers?") for a detailed report with pricing, pros/cons, alternatives, and download counts.

## Example output

```
| Task         | Tool          | Type       | Maturity    | Signals        | Why it fits              | Link            |
|--------------|---------------|------------|-------------|----------------|--------------------------|-----------------|
| Email API    | Resend        | API/SaaS   | New         | ★114, 4 sources| Modern DX, free 3K/mo    | resend.com      |
| Email API    | SendGrid      | API/SaaS   | Established | ★1625          | Most popular, templates  | sendgrid.com    |
| Slack bot    | slack-mcp     | MCP server | New         | ★340           | Connect to Claude Code   | github.com/...  |

Want to dig deeper? Say "dig into [name]".
Or ask about a specific source: "any MCP servers for this?", "any awesome-lists?"

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
```

---

# Tool Scout (RU)

Находит подходящие инструменты для задач проекта — сервисы, MCP-серверы, нейронки, no-code платформы, библиотеки и API. Скилл ищет по пяти источникам (веб, GitHub, каталоги MCP, awesome-списки и пакетные реестры), чтобы вам не приходилось гадать, где искать. Покрывает как устоявшиеся, так и недавно запущенные инструменты.

## Что нового в v2

- **Поиск по GitHub** через `gh` CLI — находит репозитории по звёздам, ищет код в `modelcontextprotocol/servers`
- **Каталоги MCP** — запросы к smithery.ai и официальному списку MCP-серверов
- **Awesome-списки** — находит `awesome-*` репозитории, читает README, извлекает инструменты
- **Адаптивный выбор источников** — подбирает источники по типу задачи (SaaS → только веб; MCP-сервер → веб + GitHub + каталоги; неясно → все источники)
- **Колонка «Сигналы»** — звёзды GitHub и статус архивации прямо в таблице результатов
- **Дедупликация** — инструмент, найденный в трёх источниках, появляется один раз с агрегированными сигналами
- **Детекция тривиальных задач** — если задача решается тремя строками кода, скилл скажет об этом вместо полного поиска
- **Graceful fallback** — работает без `gh` CLI через веб-поиск с `site:github.com`

## Установка

**macOS / Linux:**
```bash
cp -r tool-scout ~/.claude/skills/tool-scout
```

**Windows:**
```powershell
Copy-Item -Recurse tool-scout $env:USERPROFILE\.claude\skills\tool-scout
```

## Первый запуск

При первом использовании скилл проведёт короткую настройку:

| Вопрос | Зачем | Пример ответа |
|--------|-------|---------------|
| Какой поисковый инструмент доступен? | Скиллу нужен веб-поиск. Exa MCP даёт лучшие результаты, но встроенный WebSearch тоже работает | `exa` |
| GitHub CLI доступен? | Определяется автоматически через `gh --version`. Позволяет искать репозитории напрямую | (автоматически) |
| На каком языке выдавать результаты? | Чтобы скилл общался на вашем языке | `русский` |

Настройки сохраняются в `~/.claude/skills/tool-scout/config.md`.

### Варианты поискового движка

| Движок | Нужна настройка? | Качество | Заметки |
|--------|-----------------|----------|---------|
| **Exa MCP** (рекомендуется) | Да — [инструкция](https://docs.exa.ai/reference/mcp) | Лучшее | Веб-поиск + поиск по коду |
| **WebSearch** | Нет — встроен в Claude Code | Хорошее | Работает из коробки |
| **Другой MCP** | Зависит от сервера | Разное | Любой MCP-сервер с веб-поиском |

### GitHub CLI (опционально, но рекомендуется)

Если `gh` установлен и авторизован, скилл использует его для точного поиска (`gh search repos --sort=stars`). Без него поиск по GitHub идёт через веб-запросы с `site:github.com` — работает, но менее точно.

Установить: [cli.github.com](https://cli.github.com/)

## Использование

Скажите Claude Code любую из фраз:

- «посмотри инструменты для UI дашборда»
- «есть MCP-сервер для Google Sheets?»
- «tool scout — нужно обрабатывать изображения пачками»
- «найди библиотеку для генерации PDF на Python»
- «какие тулы есть для email-автоматизации?»

### Два уровня глубины

**Уровень 1 (по умолчанию):** Адаптивный поиск по релевантным источникам, результат в виде таблицы с сигналами.

**Уровень 2 (по запросу):** Скажите «копни [название]» или спросите по конкретному источнику («а есть awesome-списки?», «а MCP-серверы?») для подробного отчёта с ценами, плюсами/минусами, альтернативами и статистикой скачиваний.

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
