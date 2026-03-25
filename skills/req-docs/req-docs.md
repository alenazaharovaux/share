---
name: req-docs
description: >
  Helps determine which requirement documents a project needs (PRD, BRD, FRD, MRD, SRD, TRD, QRD)
  and then writes them using templates. Two phases: advisor (recommend documents) and writer (create them).
  Use this skill whenever the user wants to write a PRD, BRD, FRD, MRD, SRD, TRD, QRD, or doesn't
  know which requirement document they need. Triggers on: "write a PRD", "I need a requirements doc",
  "which document should I write", "req docs", "requirement document", "напиши PRD",
  "нужен документ требований", "какой документ мне нужен", "создай спецификацию",
  "napisi PRD", "dokument zahteva", "koji dokument mi treba", "помоги с PRD", "write specs",
  "PRD for my project", "need a BRD", "create an FRD". Also triggers when user discusses
  product requirements, specs, or asks about document type differences in context of creating one.
  Even if the user asks for just one document type, use this skill — it validates the choice
  and may recommend additional documents the user hasn't considered.
---

# Req Docs — Requirements Document Advisor & Writer

A skill for determining which requirement documents a project needs and writing them. Works in two phases: advisor (recommend documents) → writer (create documents from templates).

Supports 7 document types: PRD, BRD, FRD, MRD, SRD, TRD, QRD with 13 template variations.

## Phase Auto-Detection

Before starting, determine which phase to enter:

1. Search for `**/req-docs-plan.md` in the project root and `docs/` directory (exact name, no fuzzy matching)
2. If found and has `pending` documents → start **Phase 2** (Writer), offer to write the next pending document
3. If not found → start **Phase 1** (Advisor)
4. If user explicitly names a document type ("write me a PRD") → confirm: "Are you sure you need specifically a PRD, or would you like me to help determine which documents your project needs?"

## Phase 1: Advisor

Goal: determine which documents the project needs, in what order.

### Step 1: Project Context

Read project files (README, package.json, CLAUDE.md, existing specs/docs). Understand what the product is, tech stack, stage, existing documents.

**Existing documents detection:** scan for files matching `*PRD*.md`, `*BRD*.md`, `*FRD*.md`, `*MRD*.md`, `*SRD*.md`, `*TRD*.md`, `*QRD*.md`, `*requirements*.md`, `*-spec.md`, `*specification*.md`. If found — read them, determine type and completeness. Report to user: "I found an existing PRD in `docs/prd.md`. I recommend complementing it with an FRD for the development team."

### Step 2: Clarifying Questions

Ask questions **one at a time**. Skip questions whose answers are obvious from context. Every question includes "Not sure / Not defined yet" as a valid option.

For newcomers: include a brief explanation of why each question matters.

1. **What product?** (skip if obvious from context)
2. **Stage?** Idea / Discovery / MVP / Growth / Scale / *Not sure yet*
3. **Document audience?** Investors / Product team / Developers / AI agent / Contractor / *Not sure*
4. **Methodology?** Waterfall / Agile / Hybrid / No formal process / *Not sure*
5. **Team size?** Solo / Startup (3-10) / Agile team (10-30) / Enterprise (50+) / *Not sure*
6. **Regulatory requirements?** Fintech, healthcare, defense, government — or none / *Not sure*
7. **Budget estimate?** Under $10K / $10K-100K / $100K-1M / Over $1M / *Not defined yet*

"Not sure" signals early stage → recommend lighter documents (MVP PRD, Lean BRD).

**Search triggers:** if the user names a specific domain (fintech, healthcare, defense, IoT) → offer to search for regulatory requirements that affect document structure. If competitors named → offer to search their approach. Use whatever search tools are available; if none, suggest specific things the user should research.

### Step 3: Decision Matrix

| Situation | Recommended Documents |
|-----------|----------------------|
| Idea + leadership audience | MRD |
| Investment justification | BRD |
| Product team, any scale | PRD |
| Technical spec for developers | FRD |
| Full system specification | SRD |
| Infrastructure/platform requirements | TRD |
| Formal quality standards | QRD |
| Regulated (fintech, healthcare) | PRD + FRD + SRD |
| Regulated + enterprise | BRD → PRD → FRD → SRD + TRD + QRD |
| Startup, quick validation | MVP PRD |
| AI agent (Cursor, Claude Code) | AI-Optimized PRD |
| Microservices / API product | PRD + API FRD |
| Infrastructure team documenting platform | TRD |
| Healthcare/regulated needing quality standards | QRD (alongside SRD) |
| Hardware product | PRD (Hardware) + TRD + QRD |

If PRD recommended → determine variation: Standard, One-Pager, MVP, Feature, Technical, AI-Optimized, Hardware, API, Agile.

### Step 4: Recommendation

Present to user:
- Which documents are needed and **why** (for newcomers: one-sentence explanation of each type)
- Recommended writing order (dependency chain: MRD → BRD → PRD → FRD → SRD, TRD and QRD parallel to SRD)
- What already exists and how new documents complement it
- **Confidence level:** if answers were clear → confident. If many "not sure" → honest: "I recommend starting with MVP PRD. If the project grows, come back for FRD and SRD."
- Ask for confirmation before proceeding

### Step 5: Save Plan

After confirmation, write `docs/req-docs-plan.md`:

```markdown
# Required Documents — [Project Name]

## Context
- Product: [description from Step 1-2]
- Stage: [stage]
- Team: [size, methodology]
- Audience: [who the documents are for]
- Regulatory: [requirements or none]
- Save path: [to be set in Phase 2]

## Documents
1. **[TYPE]** ([Variation]) — pending
2. **[TYPE]** ([Variation]) — pending

## Order Rationale
[Why this order — dependency chain explanation]

## Existing Documents
- [path] — [type, completeness assessment]
```

Then transition to Phase 2 or ask if the user wants to continue later.

## Phase 2: Writer

Goal: write documents one at a time using templates + project context.

### Entry

1. Read `docs/req-docs-plan.md`
2. **Re-read project files** — context may have changed since Phase 1
3. Find first document with status `pending`
4. Offer: "Next document is [TYPE]. Start?" (user can pick a different one)
5. On first document: ask save path. Default `docs/`. If the project has a different convention, suggest that. Store path in plan file for subsequent documents.

### Writing Process (per document)

**Step 1: Load template.** Read the corresponding template from `references/templates/`. Templates available:

| Template | File |
|----------|------|
| PRD Standard | `prd-standard-template.md` |
| PRD MVP | `prd-mvp-template.md` |
| PRD AI-Optimized | `prd-ai-optimized-template.md` |
| BRD Standard | `brd-standard-template.md` |
| BRD Lean | `brd-lean-template.md` |
| FRD Standard | `frd-standard-template.md` |
| FRD API | `frd-api-template.md` |
| MRD Standard | `mrd-standard-template.md` |
| MRD Startup | `mrd-startup-template.md` |
| SRD Standard | `srd-standard-template.md` |
| SRD Agile | `srd-agile-template.md` |
| TRD Standard | `trd-standard-template.md` |
| QRD Standard | `qrd-standard-template.md` |

For PRD variations without a dedicated template (One-Pager, Feature, Technical, Hardware, API, Agile), adapt the Standard PRD template:

| Variation | Remove | Add |
|-----------|--------|-----|
| One-Pager | Wireframes, Technical Approach, Timeline | (condense to 1 page) |
| Feature | Market context | Feature dependencies, rollback plan |
| Technical | Market context, personas | Architecture, API specs, data models |
| Hardware | — | BOM, certifications, manufacturing |
| API | Personas, wireframes | Endpoints, schemas, rate limits (merge with API FRD) |
| Agile | Timeline, formal sign-off | Sprint mapping, story points |

**Step 2: Fill with context.** Use project context (freshly scanned) + advisor answers (from plan file).

Rules:
- Fill sections with real data from context where possible
- Where data is missing → write `[TBD]` and add to Open Questions section
- **Never invent** metrics, numbers, competitor names — only what is known
- Generate user stories independently but mark: "Requires validation with team"
- Prioritize requirements (P0/P1/P2) based on context but suggest review
- Add **cross-references** to already-written documents: `See [Type] §[Section] (path/to/file.md)`

**Step 3: Targeted questions.** If key sections critically lack data → ask the user (max 3-4 questions). If user doesn't know → leave TBD, don't block the process.

**Step 4: Self-check.**

Generic checks:
- All required sections filled or marked TBD
- Problem Statement based on facts, not assumptions
- Scope contains both IN and OUT
- Success Metrics specific and measurable (or TBD)
- No duplication with existing project documents
- No invented data
- Cross-references correct
- Document length within range (MVP PRD: 2-4 pages, Standard PRD: 5-15, BRD: 5-20, FRD: 10-50, SRD: 10-50, TRD: 5-15, QRD: 5-10)

Type-specific checks:

| Type | Checks |
|------|--------|
| PRD | User stories "As a [role]..." format, Scope has IN/OUT, SMART metrics |
| BRD | Problem cites data not opinions, cost-benefit present or TBD, ROI justified |
| FRD | Unique IDs (FR-001), "shall/should" language, error states described |
| MRD | TAM/SAM/SOM present or TBD, user segments specific |
| SRD | NFRs quantified (ms, %, count), architecture not empty, data model described |
| TRD | Software versions specified, licenses noted, capacity planning |
| QRD | Blocking/advisory split, each attribute has measurement method |

**Step 5: Present to user.** Write document to file, show, ask:
- What needs to change?
- Which TBDs can we fill now?
- Is the document ready?

**Step 6: Update plan.** Mark document as `done` in plan, record file path. Offer: "Next document is [TYPE]. Continue now or come back later?"

## Error Handling

- **Malformed plan file:** offer to re-run Phase 1 and rebuild
- **Pending document whose file already exists:** ask overwrite or skip
- **All documents done:** congratulate, offer to review the full set or add new documents
- **Stale context:** on Phase 2 re-entry, if project files changed significantly since plan was created → warn user, offer to re-run advisor

## Language

Determined by user's language. If unclear, ask. Templates are in English (industry standard for requirement documents). Content sections are written in the user's language. Section headers remain in English (e.g., "## Problem Statement") regardless of content language.

## What This Skill Does NOT Do

- Does not replace user/market research
- Does not generate wireframes or mockups
- Does not make decisions for the user — proposes and explains
- Does not invent data — uses what is known, marks the rest as TBD
