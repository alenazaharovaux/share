# ADR — Architecture Decision Record

A Claude Code skill that logs architectural decisions as you work. Every time you choose a technology, design a database schema, pick a deployment strategy, or make any structural choice — this skill captures *what* you decided, *why*, and *what you rejected*.

The rejected alternatives are the most valuable part. Six months later, they prevent you (or your AI assistant) from revisiting dead ends.

## Who is this for?

**Solo developers and small teams.** The format is lightweight: one Markdown file per project, ~1 minute per entry, no tooling required. It works particularly well with AI coding assistants — Claude Code uses your ADR log as context to make better suggestions and avoid proposing approaches you already rejected.

> For larger teams that need governance, SWOT analysis, stakeholder tracking, and CI integration, see the comprehensive [Architecture Decision Record guide](https://github.com/joelparkerhenderson/architecture-decision-record) by Joel Parker Henderson — it includes 10 templates ranging from minimal to enterprise-grade.

## Installation

**macOS / Linux:**
```bash
cp -r adr ~/.claude/skills/adr
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse adr $env:USERPROFILE\.claude\skills\adr
```

## First run

On first use, the skill asks a few setup questions:

| Question | Why | Example |
|----------|-----|---------|
| Language for entries | Match your project's language | `English`, `Russian`, `Serbian` |
| ADR file path in repos | Where to create the file inside git projects | `docs/architecture-decisions.md` |
| Mirror location | Optional copy for a notes app (Obsidian, Notion export, etc.) | `/path/to/vault/project/` or `skip` |
| Non-repo projects folder | For projects without git — ADR goes directly in the folder | `/path/to/projects/` or `skip` |

All questions are skippable. Settings are saved to `~/.claude/skills/adr/config.md`.

## What an entry looks like

```markdown
## ADR-003: Translations — column suffixes _sr/_ru/_en

> In the context of a trilingual education platform, facing the need for
> inline translations, we chose column suffixes per language, to keep queries
> simple and avoid JOINs, accepting that adding a 4th language requires a migration.

**Date:** 2026-03-09
**Status:** accepted

**Context:** The platform runs in Serbian, with Russian and English translations
for a child adapting to a new school system. Translation is supplementary, not a replacement.

**Options considered:**

| Option | Pros | Cons |
|--------|------|------|
| A. Translations table (key-value) | Unlimited languages | Complex JOINs, slower reads |
| **B. Column suffixes _ru/_en ✅** | Simple queries, single row | Fixed language set, wider tables |

**Decision:** B. Three languages are fixed. A fourth is unlikely.

**Consequences:**
- Each translatable field has 3 versions: `field_sr`, `field_ru`, `field_en`
- TranslationToggle component shows buttons only if translation exists
- Translation expands alongside Serbian text, not instead of it

**Revisit if:** A 4th language is needed or languages must be added without migration.
```

## Trigger phrases

The skill activates when you say:

| English | Russian |
|---------|---------|
| "Record this as an ADR" | "Запиши ADR" |
| "Log this architecture decision" | "Зафиксируй решение" |
| "ADR" | "Запиши решение" |
| "We just made a design choice, let's document it" | "Это архитектурное решение, запиши" |

It also runs automatically at session end if architectural decisions were made during the session (requires a one-line addition to your CLAUDE.md — see below).

## Recommended CLAUDE.md addition

To make the skill run automatically at session end, add this to your global `~/.claude/CLAUDE.md`:

```markdown
## Session end checklist
- ADR check: review the session — were any architectural/technical decisions made?
  If yes → call the `adr` skill and append entries. If no → skip.
```

## Key principles

- **Immutability:** accepted entries are never edited. If a decision is reversed, the old entry gets `superseded by ADR-NNN` status, and a new entry explains why.
- **The 6-month test:** "Will I remember why this choice was made in 6 months?" If not — write it down.
- **Alternatives are mandatory:** an ADR without rejected options is just a note. The table of what you *didn't* choose is what makes it valuable.
- **One file per project:** no folder of numbered files. One `architecture-decisions.md` with sequential `ADR-001`, `ADR-002`, etc.

## Credits

Format inspired by [Michael Nygard's ADR template](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) and the [Alexandrian pattern](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/locales/en/templates/decision-record-template-for-alexandrian-pattern) (one-liner summary). Research and best practices from [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record).

By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT).

---

# ADR — Журнал архитектурных решений

Скилл для Claude Code, который фиксирует архитектурные решения по ходу работы. Каждый раз, когда вы выбираете технологию, проектируете схему БД, определяете стратегию деплоя или принимаете любое структурное решение — скилл записывает *что* решили, *почему* и *что отвергли*.

Отвергнутые альтернативы — самая ценная часть записи. Через полгода они не дадут вам (или вашему AI-ассистенту) предлагать подходы, которые уже были отвергнуты.

## Для кого

**Соло-разработчики и небольшие команды.** Формат лёгкий: один Markdown-файл на проект, ~1 минута на запись, никаких дополнительных инструментов. Особенно хорошо работает с AI-ассистентами — Claude Code использует ваш ADR как контекст и не предлагает подходы, которые вы уже отвергли.

> Для больших команд, которым нужны governance, SWOT-анализ, трекинг стейкхолдеров и интеграция с CI — смотрите полный [гайд по Architecture Decision Records](https://github.com/joelparkerhenderson/architecture-decision-record) от Joel Parker Henderson. Там 10 шаблонов от минимального до корпоративного.

## Установка

**macOS / Linux:**
```bash
cp -r adr ~/.claude/skills/adr
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse adr $env:USERPROFILE\.claude\skills\adr
```

## Первый запуск

При первом использовании скилл задаёт несколько вопросов:

| Вопрос | Зачем | Пример |
|--------|-------|--------|
| Язык записей | Соответствие языку проекта | `English`, `Russian`, `Serbian` |
| Путь к ADR в репозиториях | Где создавать файл внутри git-проектов | `docs/architecture-decisions.md` |
| Зеркальная копия | Копия для заметочника (Obsidian, Notion и др.) | `/path/to/vault/project/` или `skip` |
| Папка проектов без git | Для проектов без репозитория — ADR пишется прямо в папку | `/path/to/projects/` или `skip` |

Все вопросы можно пропустить. Настройки сохраняются в `~/.claude/skills/adr/config.md`.

## Как выглядит запись

```markdown
## ADR-003: Переводы — колонки _sr/_ru/_en

> В контексте трёхъязычной образовательной платформы, столкнувшись с необходимостью
> встроенных переводов, выбрали суффиксы колонок по языкам, чтобы запросы оставались
> простыми без JOIN-ов, принимая что добавление 4-го языка потребует миграции.

**Дата:** 2026-03-09
**Статус:** accepted

**Контекст:** Платформа работает на сербском, с переводами на русский и английский.
Перевод — вспомогательный, не замена.

**Варианты:**

| Вариант | Плюсы | Минусы |
|---------|-------|--------|
| A. Таблица translations (key-value) | Неограниченное число языков | Сложные JOIN-ы |
| **B. Колонки _ru/_en ✅** | Простые запросы, одна строка | Фиксированный набор языков |

**Решение:** B. Три языка фиксированы. Четвёртый маловероятен.

**Последствия:**
- Каждое переводимое поле имеет 3 версии: `field_sr`, `field_ru`, `field_en`
- TranslationToggle показывает кнопки только если перевод существует

**Пересмотреть если:** понадобится 4+ языка или динамическое добавление языков.
```

## Триггеры

| English | Русский |
|---------|---------|
| "Record this as an ADR" | "Запиши ADR" |
| "Log this architecture decision" | "Зафиксируй решение" |
| "ADR" | "Запиши решение" |
| "We just made a design choice" | "Это архитектурное решение, запиши" |

Также запускается автоматически при завершении сессии, если были архитектурные решения (нужна одна строка в CLAUDE.md — см. выше в английской секции).

## Ключевые принципы

- **Иммутабельность:** принятые записи не редактируются. Пересмотр = новая запись со ссылкой на старую.
- **Тест 6 месяцев:** «Вспомню ли я через полгода, почему так решили?» Если нет — записывай.
- **Альтернативы обязательны:** ADR без отвергнутых вариантов — просто заметка. Таблица того, что *не* выбрали, делает запись ценной.
- **Один файл на проект:** не папка пронумерованных файлов, а один `architecture-decisions.md`.

## Авторство

Формат вдохновлён [шаблоном ADR Майкла Найгарда](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) и [Alexandrian pattern](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/locales/en/templates/decision-record-template-for-alexandrian-pattern) (однострочное резюме). Исследование и лучшие практики из [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record).

Автор: [Alena Zakharova](https://github.com/alenazaharovaux) (MIT).
