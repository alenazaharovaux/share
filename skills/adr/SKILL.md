---
name: adr
description: >
  Record architecture decisions in a project's ADR log. Creates the ADR file
  for new projects, appends new entries, and marks old decisions as superseded.
  Use this skill whenever an architectural or design decision is made during
  a session: choosing a technology, database schema, data format, API design,
  file structure, deployment strategy, or any choice that affects how the
  project is built. Also use at session end ("завершаем сессию") if any
  decisions were made. Triggers: "запиши ADR", "architecture decision",
  "запиши решение", "ADR", "зафиксируй решение", or when CLAUDE.md
  session-end checklist detects architectural decisions were made.
---

# ADR — Architecture Decision Record

You help the user document architectural decisions in their projects. Each decision
gets a structured entry that captures not just what was decided, but why — and what
was rejected. The rejected alternatives are the most valuable part: they capture *why*
something was rejected, so when conditions change, you can revisit the decision
intentionally — not repeat the same analysis from scratch.

## When to record a decision

Ask yourself: "Will I (or the user) remember why this choice was made in 6 months?"
If no — write an ADR entry.

Examples of decisions worth recording:
- Technology/framework choices (Next.js over Remix, Supabase over Firebase)
- Data model design (per-test vs per-exercise progress, columns vs separate table)
- Architecture patterns (monolith vs microservices, SSR vs SSG)
- API/data format choices (JSON columns vs normalized tables, REST vs GraphQL)
- Deployment decisions (Vercel vs Render, monorepo vs multirepo)
- UX architecture (separate page vs tabs, translation strategy)

Examples of decisions NOT worth recording:
- Variable naming, code formatting
- Which lint rule to enable
- Minor UI tweaks (button color, padding)

## Where the ADR file lives

**Projects with a git repo** (in `_repos/`):
- Primary: `docs/architecture-decisions.md` inside the repo
- Mirror copy: project folder in Obsidian Vault (for reading via Obsidian Sync)

**Projects without a git repo** (research projects like Motivity, Raiffeisen):
- Single location: project folder in Obsidian Vault

When creating the mirror copy, just copy the file — no symlinks, no fancy sync.
The repo version is the source of truth; the Obsidian copy is for convenience.

## Creating a new ADR file

If the project has no `docs/architecture-decisions.md` (or no ADR file in Obsidian
for non-git projects), create it with this header:

```markdown
# Architecture Decision Record (ADR)

Журнал архитектурных решений проекта [project-name].

**Принципы ведения:**
- Одна запись — одно решение. Принятые записи не редактируются (immutability).
- Пересмотренное решение → старое получает статус `superseded by ADR-XXX`, новое ссылается на старое.

**Статусы:** `accepted` · `superseded by ADR-XXX`

---
```

## Entry format

```markdown
## ADR-NNN: Short decision title

> In the context of [situation], facing [problem], we chose [solution],
> to achieve [goal], accepting [trade-off].

**Date:** YYYY-MM-DD
**Status:** accepted

**Context:** What motivates this decision? What problem or need triggered it?

**Options considered:**

| Option | Pros | Cons |
|--------|------|------|
| A. First option | ... | ... |
| **B. Chosen option ✅** | ... | ... |
| C. Third option | ... | ... |

**Decision:** What we chose and the key argument for it.

**Consequences:** What becomes easier? What becomes harder? What new decisions does this create?

**Revisit if:** Under what conditions should we reconsider this decision?
```

### Format rules

- **Numbering:** sequential `ADR-001`, `ADR-002`, etc. within each project
- **One-liner summary** (the blockquote): always present. Fill in all five slots: context, problem, solution, goal, trade-off. This is the most scannable part of the file
- **Options table:** required when 2+ alternatives were considered. For binary decisions (do/don't do), write a short paragraph instead of a table
- **Language:** match the project's language. Russian for Russian projects, English for English ones. The one-liner summary is always in the project's language
- **Date:** the date the decision was made, not the date it was recorded
- **Revisit if:** always present — every decision has conditions under which it should be reconsidered

## Superseding a decision

When a previous decision is reversed or replaced:

1. Update the old entry's status: `**Status:** superseded by ADR-NNN`
2. In the new entry's Context, reference the old one: "Replaces ADR-XXX because [reason]"
3. Do NOT edit the old entry's content — only the status line changes

## Retroactive Mode — first-time detection

When the ADR skill is invoked and **no ADR file exists** for the current project:

1. Check `~/.claude/history.jsonl` for entries where the `project` field matches the current working directory
2. Branch on what you find:

**No history found** → new project, create empty ADR file normally and proceed.

**History found** → ask:

> "Вижу, проект уже ведётся, но ADR-документа пока нет. Запустить ретроспективу — восстановить историю решений из прошлых сессий?"
> `[да / нет, создай пустой файл]`

**If "да"** → first show a preview by scanning history for decision signals:
- Count total messages and sessions for this project
- Scan for signals: technology names, "использу", "выбра", "переход", "решили", "мигрир", "давай будем", "оставим", framework/library names
- Show: *"Нашла X сообщений в Y сессиях (с [earliest date] по сегодня). По первичному сканированию — около N потенциальных архитектурных решений."*

Then offer mode choice:

> **Черновики** *(рекомендую для проектов старше месяца)* — Claude составляет ADR-заготовки на основе истории, ты проверяешь и дополняешь вручную. ~5–10 минут твоего времени.
>
> **Интерактивный** *(тщательно, но долго)* — обсуждаем каждое найденное решение, задаю уточняющие вопросы там, где в промптах не хватает контекста. Для ~10 решений — ориентировочно 30–60 минут диалога.
>
> **Не сейчас** — создать пустой ADR-файл, вернуться к ретроспективе позже.

**"Не сейчас" trigger**: the phrase "запусти ретроспективу ADR" (or "run ADR retrospective") should invoke retroactive mode at any time, even if an ADR file already exists.

### Draft mode execution

Scan all project messages in history.jsonl. For each identified decision signal, generate a full ADR entry using the standard format. Be transparent about uncertainty:
- If rationale is unclear from the prompt alone → write "Context: восстановлено из истории, возможны неточности — уточни"
- If alternatives aren't known → omit the options table, write a short paragraph instead
- Mark each draft entry with `**Status:** draft (needs review)` instead of `accepted`

After writing all drafts, tell the user: *"Записала N черновиков. Проверь каждый — особенно раздел 'Options considered', там мало данных из истории. Когда подтвердишь запись — смени статус на `accepted`."*

### Interactive mode execution

For each detected decision signal (grouped by session):
1. Show the relevant prompt(s) that triggered the signal
2. Ask: *"Здесь похоже принималось решение о [X]. Что именно решили и почему?"*
3. Ask follow-up if needed: *"Какие альтернативы рассматривали?"*
4. Write the ADR entry immediately after getting enough context
5. Continue to next signal

At the start of interactive mode, warn: *"Нашла ~N решений. Это займёт примерно [N×3–5] минут. Можно остановиться в любой момент фразой 'стоп, дальше сам' — допишу оставшиеся в режиме черновиков."*

## Session-end checklist

When "завершаем сессию" is triggered, review the session for architectural decisions:

1. Were any technology choices made?
2. Were any data models designed or changed?
3. Were any structural/architectural patterns chosen?
4. Were any deployment or infrastructure decisions made?

If yes to any — call this skill and append entries. If no — skip.

## Workflow

1. Identify the decision (from the session or from user's explicit request)
2. Find or create the ADR file for this project
3. Determine the next ADR number
4. Write the entry using the format above
5. If the project has a git repo AND an Obsidian folder — copy the updated file to both locations
6. Confirm to the user what was recorded
