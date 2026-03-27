# Req Docs — Requirements Document Advisor & Writer

A Claude Code skill that helps you figure out which requirement documents your project needs and then writes them for you. It covers seven document types (PRD, BRD, FRD, MRD, SRD, TRD, QRD) with 13 ready-to-use templates.

The skill works in two phases. First, it acts as an advisor: it reads your project, asks a few questions, and recommends which documents you need and in what order. Then it becomes a writer: it picks up a template, fills it with your project's context, and produces a draft you can review and refine.

You don't need to know what a PRD or BRD is — the skill explains everything along the way.

## Why this skill exists

Writing requirement documents is one of those tasks that seems straightforward until you sit down to do it. Which document type fits your situation? How detailed should it be? What sections should it include? Should you write one document or three?

This skill removes the guesswork. It asks the right questions, picks the right document types from a decision matrix, and writes structured drafts using professional templates. Whether you are a solo founder shipping an MVP or an enterprise team preparing for a regulated product launch, the skill adapts to your context.

## What's included

```
req-docs/
├── req-docs.md                          ← the skill (221 lines)
└── references/
    └── templates/                       ← 13 ready-to-use templates
        ├── prd-standard-template.md     ← Product Requirements Document
        ├── prd-mvp-template.md          ← Lean PRD for MVPs
        ├── prd-ai-optimized-template.md ← PRD for AI coding agents
        ├── brd-standard-template.md     ← Business Requirements Document
        ├── brd-lean-template.md         ← Lean BRD (5 sections)
        ├── frd-standard-template.md     ← Functional Requirements Document
        ├── frd-api-template.md          ← FRD for API products
        ├── mrd-standard-template.md     ← Market Requirements Document
        ├── mrd-startup-template.md      ← Lean MRD for startups
        ├── srd-standard-template.md     ← Software Requirements Document
        ├── srd-agile-template.md        ← Agile SRS (modular, per-feature)
        ├── trd-standard-template.md     ← Technical Requirements Document
        └── qrd-standard-template.md     ← Quality Requirements Document
```

The skill has no external dependencies, no config files, and no setup scripts — copy the folder and it works.

## Installation

**macOS / Linux:**
```bash
cp -r req-docs ~/.claude/skills/req-docs
```

**Windows:**
```powershell
Copy-Item -Recurse req-docs $env:USERPROFILE\.claude\skills\req-docs
```

## How it works

### Phase 1: Advisor (which documents do you need?)

When you invoke the skill, it starts by understanding your project:

1. **Reads your project files** — README, package.json, CLAUDE.md, existing specs. If you already have a PRD, the skill detects it and recommends complementary documents instead of duplicating.

2. **Asks clarifying questions** — one at a time, not all at once. Seven questions maximum: what you're building, the stage, the audience, team size, methodology, regulatory requirements, and budget. Every question includes a "not sure" option. For newcomers, each question comes with a brief explanation of why it matters.

3. **Recommends documents** — based on a decision matrix that maps your situation to the right document set. A solo founder building an MVP gets a single lightweight PRD. An enterprise team in healthcare gets BRD, PRD, FRD, SRD, TRD, and QRD. The skill explains why each document is recommended and proposes a writing order based on the dependency chain (MRD before BRD before PRD before FRD before SRD).

4. **Saves a plan** — the recommendation is saved to `docs/req-docs-plan.md` in your project. This file tracks which documents are pending and which are done.

### Phase 2: Writer (creating the documents)

Once the plan is agreed, the skill writes documents one at a time:

1. **Loads the right template** from its built-in collection (13 templates covering all seven types)
2. **Fills it with your project's context** — real data from your project files and your answers to the advisor's questions. Anything it doesn't know gets marked `[TBD]` with a note in the Open Questions section. The skill never invents metrics, competitor names, or market data.
3. **Runs a self-check** — verifies that required sections are filled, problem statements are based on facts, scope has both IN and OUT, and type-specific quality criteria are met (for example: FRD requirements have unique IDs, SRD non-functional requirements are quantified).
4. **Shows you the draft** — saves the document to a file, presents it, and asks what needs to change.
5. **Updates the plan** — marks the document as done and offers to write the next one.

### Multi-session support

You don't have to write all documents in one sitting. Write the BRD today, come back next week for the PRD. When you invoke the skill again, it finds the plan file and picks up where you left off. It even re-reads your project files in case things have changed.

### Cross-references

When you write multiple documents, the skill automatically adds cross-references between them. Your PRD will link to the BRD's business justification section. Your FRD will reference the PRD's requirements. This turns individual documents into a connected system.

## Document types at a glance

| Type | Full name | What it answers | Who reads it |
|------|-----------|----------------|-------------|
| **PRD** | Product Requirements Document | What are we building and why? | Product team, designers, developers |
| **BRD** | Business Requirements Document | Why should the business invest? | Executives, investors, sponsors |
| **FRD** | Functional Requirements Document | How should the system behave? | Developers, QA, architects |
| **MRD** | Market Requirements Document | What does the market need? | Marketing, product strategy |
| **SRD** | Software Requirements Document | What are the full technical specs? | Engineers, DevOps, architects |
| **TRD** | Technical Requirements Document | What infrastructure is needed? | DevOps, SRE, IT operations |
| **QRD** | Quality Requirements Document | How do we know it's good enough? | QA leads, project managers |

## Usage examples

These phrases will trigger the skill:

- `"Write me a PRD for my project"`
- `"I need a requirements document but I'm not sure which one"`
- `"Which documents does this project need?"`
- `"req docs"`
- `"напиши PRD"` (Russian)
- `"нужен документ требований"` (Russian)
- `"napisi PRD"` (Serbian)

## Decision matrix

The skill uses this matrix to recommend documents based on your answers:

| Your situation | Recommended documents |
|---------------|----------------------|
| Early idea, pitching to leadership | MRD |
| Need funding approval | BRD |
| Product team, building features | PRD |
| Developers need technical spec | FRD |
| Full system specification needed | SRD |
| Infrastructure requirements | TRD |
| Quality standards for release | QRD |
| Startup, quick validation | MVP PRD |
| Writing for AI coding agents | AI-Optimized PRD |
| Regulated industry (fintech, healthcare) | PRD + FRD + SRD |
| Enterprise + regulated | BRD + PRD + FRD + SRD + TRD + QRD |

## PRD variations

The skill supports 9 PRD variations. Three have dedicated templates (Standard, MVP, AI-Optimized). Six others are created by adapting the Standard PRD template:

| Variation | Best for |
|-----------|---------|
| Standard | General-purpose, any product |
| MVP | Startups, quick validation, 2-4 pages |
| AI-Optimized | AI coding agents (Cursor, Claude Code) |
| One-Pager | Quick reference, single features |
| Feature | Individual feature within a larger product |
| Technical | Developer-audience, architecture focus |
| Hardware | Physical products with BOM and certifications |
| API | API-first products and microservices |
| Agile | Sprint-based teams, story points |

## Language support

The skill communicates in whatever language you use. Templates are in English (industry standard for requirement documents), but all content sections are written in your language. Section headers stay in English regardless of content language — this is a requirement-documents convention that helps with tool interoperability.

## Platform compatibility

This skill was designed to be portable:

- **Claude Code** — install to `~/.claude/skills/req-docs/` and invoke via Skill tool
- **Codex** — copy to your skills directory, use as a custom instruction
- **Cursor** — use as a `.cursorrules` or rule file
- **Any LLM tool** — the skill is plain markdown, no platform-specific dependencies

## Credits

Templates are based on the [TheHuman2AI](https://thehuman2ai.com) requirements documents knowledge base — a free, multilingual resource covering all major requirement document types with guides, templates, and AI prompts.
[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

## License

MIT

---

# Req Docs — Советник и генератор документов требований

Скилл для Claude Code, который помогает определить, какие документы требований нужны вашему проекту, а затем пишет их за вас. Поддерживает семь типов документов (PRD, BRD, FRD, MRD, SRD, TRD, QRD) с 13 готовыми шаблонами.

Скилл работает в двух фазах. Сначала как советник: читает ваш проект, задаёт несколько вопросов и рекомендует, какие документы нужны и в каком порядке их писать. Затем как генератор: берёт шаблон, заполняет его контекстом вашего проекта и создаёт черновик, который вы можете просмотреть и доработать.

Не нужно знать, что такое PRD или BRD — скилл объясняет всё по ходу работы.

## Зачем этот скилл

Написание документов требований кажется простой задачей, пока не сядешь за неё. Какой тип документа подходит? Насколько детальным он должен быть? Какие секции включить? Нужен один документ или три?

Этот скилл убирает догадки. Задаёт правильные вопросы, подбирает нужные типы документов по матрице решений и пишет структурированные черновики по профессиональным шаблонам. Подходит и для соло-основателя, запускающего MVP, и для корпоративной команды, готовящей документацию для регулируемого продукта.

## Что в комплекте

```
req-docs/
├── req-docs.md                          ← скилл (221 строка)
└── references/
    └── templates/                       ← 13 готовых шаблонов
        ├── prd-standard-template.md     ← Product Requirements Document
        ├── prd-mvp-template.md          ← Лёгкий PRD для MVP
        ├── prd-ai-optimized-template.md ← PRD для AI-агентов
        ├── brd-standard-template.md     ← Business Requirements Document
        ├── brd-lean-template.md         ← Lean BRD (5 секций)
        ├── frd-standard-template.md     ← Functional Requirements Document
        ├── frd-api-template.md          ← FRD для API-продуктов
        ├── mrd-standard-template.md     ← Market Requirements Document
        ├── mrd-startup-template.md      ← Lean MRD для стартапов
        ├── srd-standard-template.md     ← Software Requirements Document
        ├── srd-agile-template.md        ← Agile SRS (модульный)
        ├── trd-standard-template.md     ← Technical Requirements Document
        └── qrd-standard-template.md     ← Quality Requirements Document
```

Скилл не требует внешних зависимостей, конфигурационных файлов или скриптов установки — скопируйте папку, и он работает.

## Установка

**macOS / Linux:**
```bash
cp -r req-docs ~/.claude/skills/req-docs
```

**Windows:**
```powershell
Copy-Item -Recurse req-docs $env:USERPROFILE\.claude\skills\req-docs
```

## Как это работает

### Фаза 1: Советник (какие документы нужны?)

При вызове скилл начинает с изучения вашего проекта:

1. **Читает файлы проекта** — README, package.json, CLAUDE.md, существующие спецификации. Если PRD уже есть, скилл определяет это и рекомендует дополняющие документы, а не дублирует.

2. **Задаёт уточняющие вопросы** — по одному, не все сразу. Максимум семь вопросов: что строите, стадия, аудитория, размер команды, методология, регуляторика и бюджет. Каждый вопрос включает вариант «не уверен(а)». Для новичков каждый вопрос сопровождается кратким объяснением, зачем он нужен.

3. **Рекомендует документы** — по матрице решений, которая соотносит вашу ситуацию с нужным набором документов. Соло-основатель с MVP получает один лёгкий PRD. Корпоративная команда в здравоохранении — BRD, PRD, FRD, SRD, TRD и QRD. Скилл объясняет, зачем каждый документ, и предлагает порядок написания по цепочке зависимостей (MRD → BRD → PRD → FRD → SRD).

4. **Сохраняет план** — рекомендация записывается в `docs/req-docs-plan.md` в вашем проекте. Этот файл отслеживает, какие документы ожидают написания, а какие готовы.

### Фаза 2: Генератор (создание документов)

После согласования плана скилл пишет документы по одному:

1. **Загружает нужный шаблон** из встроенной коллекции (13 шаблонов для всех семи типов)
2. **Заполняет контекстом проекта** — реальные данные из файлов проекта и ответов на вопросы советника. Что не знает — помечает `[TBD]` с пометкой в разделе Open Questions. Скилл никогда не выдумывает метрики, названия конкурентов или рыночные данные.
3. **Проводит самопроверку** — проверяет заполнение обязательных секций, соответствие фактам, наличие IN и OUT в скоупе, а также типоспецифичные критерии качества (например: у требований FRD есть уникальные ID, нефункциональные требования SRD квантифицированы).
4. **Показывает черновик** — сохраняет документ в файл, показывает вам и спрашивает, что нужно изменить.
5. **Обновляет план** — отмечает документ как готовый и предлагает написать следующий.

### Мультисессионная работа

Не обязательно писать все документы за один раз. Напишите BRD сегодня, вернитесь через неделю за PRD. При повторном вызове скилл находит файл плана и продолжает с того места, где вы остановились. При этом заново читает файлы проекта на случай, если что-то изменилось.

### Перекрёстные ссылки

При написании нескольких документов скилл автоматически добавляет перекрёстные ссылки между ними. PRD ссылается на секцию бизнес-обоснования в BRD. FRD ссылается на требования PRD. Отдельные документы превращаются в связанную систему.

## Типы документов

| Тип | Полное название | На какой вопрос отвечает | Кто читает |
|-----|----------------|------------------------|-----------|
| **PRD** | Product Requirements Document | Что мы строим и зачем? | Продуктовая команда, дизайнеры, разработчики |
| **BRD** | Business Requirements Document | Зачем бизнесу инвестировать? | Руководство, инвесторы, спонсоры |
| **FRD** | Functional Requirements Document | Как система должна себя вести? | Разработчики, QA, архитекторы |
| **MRD** | Market Requirements Document | Что нужно рынку? | Маркетинг, продуктовая стратегия |
| **SRD** | Software Requirements Document | Каковы полные технические спецификации? | Инженеры, DevOps, архитекторы |
| **TRD** | Technical Requirements Document | Какая инфраструктура нужна? | DevOps, SRE, IT-операции |
| **QRD** | Quality Requirements Document | Как понять, что продукт достаточно хорош? | QA-лиды, проектные менеджеры |

## Примеры вызова

Эти фразы активируют скилл:

- `"Write me a PRD for my project"`
- `"I need a requirements document but I'm not sure which one"`
- `"req docs"`
- `"напиши PRD"`
- `"нужен документ требований"`
- `"какой документ мне нужен"`
- `"napisi PRD"` (сербский)

## Совместимость с платформами

Скилл разработан для портативности:

- **Claude Code** — установите в `~/.claude/skills/req-docs/` и вызывайте через Skill tool
- **Codex** — скопируйте в директорию скиллов, используйте как custom instruction
- **Cursor** — используйте как `.cursorrules` или rule file
- **Любой LLM-инструмент** — скилл написан на чистом markdown без привязки к платформе

## Благодарности

Шаблоны основаны на базе знаний [TheHuman2AI](https://thehuman2ai.com) — бесплатном мультиязычном ресурсе, покрывающем все основные типы документов требований с гайдами, шаблонами и AI-промптами.
[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
## Лицензия

MIT
