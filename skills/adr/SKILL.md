---
name: adr
description: >
  Record architecture decisions in a project's ADR log. Creates the ADR file
  for new projects, appends new entries, and marks old decisions as superseded.
  Use this skill whenever an architectural or design decision is made during
  a session: choosing a technology, database schema, data format, API design,
  file structure, deployment strategy, or any choice that affects how the
  project is built. Also use at session end if any decisions were made.
  Triggers: "record ADR", "architecture decision", "log decision", "ADR",
  "запиши ADR", "зафиксируй решение", or when session-end checklist detects
  architectural decisions were made.
---

# ADR — Architecture Decision Record

You help the user document architectural decisions in their projects. Each decision
gets a structured entry that captures not just what was decided, but why — and what
was rejected. The rejected alternatives are the most valuable part: they prevent
revisiting dead ends months later.

## Step 0 — Configuration (First Run)

Read `config.md` from this skill's directory (`~/.claude/skills/adr/config.md`).

If it doesn't exist, ask these questions one at a time. Each is skippable — press
Enter to use the default or type "skip" to disable.

1. **Language:** "What language should ADR entries be written in?" (default: English)
2. **ADR location in repos:** "Where should the ADR file live inside git repositories?" (default: `docs/architecture-decisions.md`)
3. **Mirror location:** "Do you want a copy of ADR files in another folder (e.g., a notes app, Obsidian vault)? If so, what's the path?" (default: skip)
4. **Non-repo projects folder:** "Where do you keep projects that aren't git repos? ADR files for these will be created directly in the project folder." (default: skip)

Save answers to `config.md`:

```markdown
# ADR Skill Configuration

language: English
adr_path_in_repo: docs/architecture-decisions.md
mirror_location: skip
non_repo_projects: skip
```

On subsequent runs, read config silently and proceed.

## When to record a decision

Ask yourself: "Will I (or the user) remember why this choice was made in 6 months?"
If no — write an ADR entry.

**Record:**
- Technology/framework choices (Next.js over Remix, Supabase over Firebase)
- Data model design (per-test vs per-exercise progress, columns vs separate table)
- Architecture patterns (monolith vs microservices, SSR vs SSG)
- API/data format choices (JSON columns vs normalized tables, REST vs GraphQL)
- Deployment decisions (Vercel vs Render, monorepo vs multirepo)
- UX architecture (separate page vs tabs, translation strategy)

**Skip:**
- Variable naming, code formatting
- Which lint rule to enable
- Minor UI tweaks (button color, padding)

## Creating a new ADR file

If the project has no ADR file yet, create it with this header:

```markdown
# Architecture Decision Record (ADR)

Decision log for [project-name].

**Principles:**
- One entry per decision. Accepted entries are not edited (immutability).
- Revised decision → old one gets status `superseded by ADR-XXX`, new one references the old.

**Statuses:** `accepted` · `superseded by ADR-XXX`

---
```

Adapt the header language to match the `language` setting from config.

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
- **One-liner summary** (the blockquote after the title): always present. Fill in all five slots: context, problem, solution, goal, trade-off. This is the most scannable part of the file
- **Options table:** required when 2+ alternatives were considered. For binary decisions (do/don't do), write a short paragraph instead of a table
- **Language:** match the config's `language` setting
- **Date:** the date the decision was made, not the date it was recorded
- **Revisit if:** always present — every decision has conditions under which it should be reconsidered

## Superseding a decision

When a previous decision is reversed or replaced:

1. Update the old entry's status: `**Status:** superseded by ADR-NNN`
2. In the new entry's Context, reference the old one: "Replaces ADR-XXX because [reason]"
3. Do NOT edit the old entry's content — only the status line changes

## Session-end checklist

When the session is ending, review it for architectural decisions:

1. Were any technology choices made?
2. Were any data models designed or changed?
3. Were any structural/architectural patterns chosen?
4. Were any deployment or infrastructure decisions made?

If yes to any — append entries. If no — skip.

## Workflow

1. Identify the decision (from the session or from user's explicit request)
2. Read config to determine file locations
3. Find or create the ADR file for this project
4. Determine the next ADR number (read existing entries)
5. Write the entry using the format above
6. If `mirror_location` is configured — copy the updated file there
7. Confirm to the user what was recorded
