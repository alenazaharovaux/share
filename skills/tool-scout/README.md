# Tool Scout

Find the right tools for your project tasks — services, MCP servers, AI models, no-code platforms, libraries, and APIs. Instead of building everything from scratch, discover what already exists. The skill searches for both established and brand-new tools, so you don't miss recent launches.

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

On first use, the skill will ask you two setup questions:

| Question | Why | Example answer |
|----------|-----|----------------|
| Which search tool do you have? | The skill needs web search to find tools. Exa MCP gives best results, but built-in WebSearch works too | `exa` |
| What language for results? | So the skill communicates in your language | `english` |

Settings are saved to `~/.claude/skills/tool-scout/config.md`. You can edit this file manually anytime.

### Search engine options

| Engine | Setup needed? | Quality | Notes |
|--------|--------------|---------|-------|
| **Exa MCP** (recommended) | Yes — [setup guide](https://docs.exa.ai/reference/mcp) | Best | Supports web search + code context search. Tested and verified |
| **WebSearch** | No — built into Claude Code | Good | No setup needed, works out of the box |
| **Other MCP** | Depends | Varies | Any MCP server that provides web search |

## Usage

Say any of these to Claude Code:

- "find tools for building a dashboard UI"
- "what's the best way to generate PDF reports?"
- "tool scout — I need to process images in bulk"
- "search for services that handle email automation"
- "how to build a real-time chat — what tools exist?"

### Two levels of depth

**Level 1 (default):** Quick scan — 2-4 search queries, results as a table in chat.

**Level 2 (on request):** Say "dig into [tool name]" to get a detailed report: pricing, pros/cons, alternatives, integration options.

## Example output

```
| Task         | Tool       | Type        | Maturity    | Why it fits              | Link          |
|--------------|------------|-------------|-------------|--------------------------|---------------|
| UI dashboard | v0.dev     | SaaS        | Established | React + shadcn/ui gen    | v0.dev        |
| UI dashboard | Pencil.dev | SaaS        | New         | Design + code from prompt| pencil.dev    |
| PDF reports  | WeasyPrint | Library     | Established | HTML to PDF, Python      | weasyprint.org|

Want to dig deeper into any of these? Say "dig into [name]".
```

---

# Tool Scout (RU)

Находит подходящие инструменты для задач проекта — сервисы, MCP-серверы, нейронки, no-code платформы, библиотеки и API. Вместо того чтобы писать всё с нуля, узнайте, что уже существует. Скилл ищет как устоявшиеся, так и совсем новые инструменты.

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

При первом использовании скилл задаст два вопроса:

| Вопрос | Зачем | Пример ответа |
|--------|-------|---------------|
| Какой поисковый инструмент доступен? | Скиллу нужен веб-поиск. Exa MCP даёт лучшие результаты, но встроенный WebSearch тоже работает | `exa` |
| На каком языке выдавать результаты? | Чтобы скилл общался на вашем языке | `русский` |

Настройки сохраняются в `~/.claude/skills/tool-scout/config.md`. Файл можно редактировать вручную.

### Варианты поискового движка

| Движок | Нужна настройка? | Качество | Заметки |
|--------|-----------------|----------|---------|
| **Exa MCP** (рекомендуется) | Да — [инструкция](https://docs.exa.ai/reference/mcp) | Лучшее | Веб-поиск + поиск по коду. Проверено и протестировано |
| **WebSearch** | Нет — встроен в Claude Code | Хорошее | Работает из коробки, без настройки |
| **Другой MCP** | Зависит от сервера | Разное | Любой MCP-сервер с веб-поиском |

## Использование

Скажите Claude Code любую из фраз:

- «посмотри инструменты для UI дашборда»
- «чем лучше генерировать PDF-отчёты?»
- «tool scout — нужно обрабатывать изображения пачками»
- «поищи сервисы для email-автоматизации»
- «как сделать чат в реальном времени — какие тулы есть?»

### Два уровня глубины

**Уровень 1 (по умолчанию):** Быстрый скан — 2-4 поисковых запроса, результат в виде таблицы.

**Уровень 2 (по запросу):** Скажите «копни [название]» для подробного отчёта: цены, плюсы/минусы, альтернативы, варианты интеграции.
