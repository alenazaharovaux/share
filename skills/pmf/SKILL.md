---
name: pmf
description: >
  Full product-market fit cycle for one product — from initial hypothesis to
  post-launch metrics. 10 stages: setup → hypothesis (7 dimensions) → market
  research → risk synthesis → DVF validation → interview prep → field → interview
  synthesis → MVP → metrics (Sean Ellis + retention + Levels of PMF) → iterate.
  Resumes between sessions based on the project folder state. Bilingual
  (English + Russian) — picks the language during first-run setup.
  TRIGGER on ANY:
  - "do PMF for [product]" / "I need product market fit for X" / "PMF [name]"
  - "start PMF cycle" / "I want to go through PMF" / "help me validate [idea]"
  - "continue PMF" / "continue PMF [name]"
  - "check PMF" / "what stage is my PMF at" / "show my PMF projects"
  - "is my product ready to launch"
  - "сделай PMF для [продукта]" / "нужен product market fit для X" / "PMF [имя]"
  - "запусти PMF цикл" / "хочу пройти PMF" / "помоги валидировать [идею]"
  - "продолжаем PMF" / "продолжай PMF [имя]"
  - "проверь PMF" / "на каком этапе у меня PMF" / "покажи мои PMF проекты"
  - "готов ли мой продукт к запуску"
  - User mentions a product and wants to validate it systematically
---

# PMF — Product-Market Fit Engine

This skill takes a product through the full product-market fit cycle. One skill = one orchestrator, not a bundle. All 10 stages live inside it. The skill figures out which stage the project is in and proposes the next step.

A PMF cycle takes months. The skill accepts that pace: it resumes between sessions, remembers where you left off, and does not rush.

---

## ⛔ Critical rules

1. **No subagents for research.** Stage 2 (market research) is done sequentially in the main session via Exa/WebSearch. The user sees every search and every result and can intervene. Researching analogs is substantive work, not "file lookup."

2. **The PMF projects folder is configurable.** Stored in `~/.claude/skills/pmf/config.md`. Default: `~/pmf-projects/`. The skill writes everything for a given product into `<projects_path>/<product-slug>/`. Not CWD, not somewhere else.

3. **Confidence can decrease.** That is normal. If the confidence in narrative-v2 is lower than v1 — the data is contradicting the hypothesis, and that is a useful signal, not a reason to inflate the number.

4. **Terminology: "assumption" (not "hypothesis") in Stage 4.** In stages 1–3 — "hypothesis." In stage 4 with DVF — only "assumption." This is methodologically important (David Bland).

5. **Tone is calm.** No exclamation marks, no dramatization. The user is doing PMF not to be cheered on, but to understand what works and what does not.

6. **Stages 6 (interviews) and 8 (MVP) are outside the skill.** The skill prepares the guide / gives metrics instructions, but does NOT try to "conduct interviews" or "launch an MVP." This is the user's work in the real world, weeks or months.

---

## Step 0 — Configuration (first run)

**On every trigger, before doing anything else, the skill reads its config:**

```
~/.claude/skills/pmf/config.md
```

**Expected format:**
```
language: en        # or "ru"
projects_path: ~/pmf-projects
```

### If config.md does not exist OR is missing values

Ask the user, **one question at a time**. Each question can be skipped (the default is used).

**Question 1 — Language:**
> "What language should we work in for this skill — English or Russian? (default: English)"
> 
> *English*: skill communicates in English, references loaded from `references/en/`.
> *Russian / Русский*: skill communicates in Russian, references loaded from `references/ru/`.

**Question 2 — Projects path:**
> "Where do you want PMF projects stored? (default: `~/pmf-projects/`)"
> 
> Examples:
> - `~/pmf-projects/` (default — home folder)
> - `~/Documents/PMF/`
> - `D:/Work/PMF/` (Windows)
> - `/Users/me/Projects/PMF/` (macOS)
> 
> The skill creates one subfolder per product inside this path.

**Save the config:**
After both answers (or skips → defaults), write `~/.claude/skills/pmf/config.md` with the chosen values. Confirm to the user: "Config saved. Default language is `<lang>`, projects folder is `<path>`. You can change this anytime by editing the file."

### If config.md exists

Read it. Use those values for the rest of the session. **All references must be loaded from `references/<language>/...`.** All communication happens in the configured language.

---

## Step 1 — Auto-start (what the skill does first on every trigger after config)

### 1a. Read the listing of the projects folder

```
ls <projects_path>/
```

- Folder does not exist → create it (`mkdir`)
- Folder is empty → no active projects
- Subfolders exist → each = one active PMF project (product slug)

### 1b. Parse the user's intent

| Trigger phrase | Action |
|---------------|--------|
| "Do PMF for [new name]" / "new PMF for [X]" | Create project, go to Stage 0 (Setup) |
| "Do PMF" (no name) | Ask for product name and slug |
| "Continue PMF" (no name) | 0 projects → offer to create; 1 → continue; >1 → show list, ask which |
| "PMF [name]" / "continue PMF [name]" | Find project [name] in the listing, continue from its current stage. If not found — show what exists, offer to create |
| "What stage" / "show my PMF projects" / "PMF status" | Show table: project \| stage \| last updated \| next action. **Do not move forward**, wait for user choice |

### 1c. Determine the stage of the chosen project from folder contents

Check files in priority order (later stages first):

| File found | Stage |
|-------------|--------|
| `metrics-dashboard.md` | Stage 9 done (or Stage 10 if `iteration-changelog.md` exists) |
| `interview-synthesis.md` + `narrative-v3.md` | Stage 7 done → waiting for Stage 8 (MVP launch) or jump to Stage 9 |
| `interviews/notes/*.md` ≥ 1 file | Stage 6 (field in progress or done), ready for Stage 7 |
| `interview-guide.md` | Stage 5 done → waiting for Stage 6 (field) |
| `assumptions-map.md` | Stage 4 done, ready for Stage 5 |
| `risk-prioritization.md` + `narrative-v2.md` | Stage 3 done, ready for Stage 4 |
| `market-research.md` | Stage 2 done, ready for Stage 3 |
| `narrative-v1.md` | Stage 1 done, ready for Stage 2 |
| `00_setup.md` | Stage 0 done, ready for Stage 1 |
| Folder empty or just created | Stage 0 (setup needed) |

### 1d. Show status and ask for the next action

Output format:

```
📍 PMF project: <product-slug>
   Product type: <type> | Context: <org>
   Current stage: Stage N — <name>
   Ready artifacts: <list of .md files>
   Last updated: <file date>

Next step: Stage N+1 — <name>
   What it is: <one-line stage goal>
   Artifact: <filename>

Move on to Stage N+1? Or go back to stage X?
```

After the user agrees — move to the chosen stage.

---

## Step 2 — Setup (Stage 0)

**When it runs:** auto-start found an empty folder or an explicit "new PMF for X." If `00_setup.md` already exists in the folder — Stage 0 is skipped.

**Goal:** collect basic product and team context before working on the hypothesis. Short stage (10–20 minutes).

**What is collected:**
1. Product name and folder slug
2. Product type (B2C / B2B / Marketplace / DTC / Services / Internal / Other)
3. Organizational context (Zero-to-one / Established / Extension)
4. Team Pre-Flight Check (3 questions: Founder-Market Fit, Skill gaps, Conviction-flexibility) → risk flag

**Artifact:** `00_setup.md` in the project folder.

**The Pre-Flight Check happens HERE, not in Stage 1.** It is about the team, not the product. Stage 1 will read the finished results from `00_setup.md` and copy them into the narrative.

**Detailed logic, the `00_setup.md` template, quality gates, common pitfalls:** `references/<lang>/stage-0-setup.md`.

---

## Pipeline overview — 10 stages

| # | Stage | Goal | Artifact |
|---|--------|------|----------|
| 0 | **Setup** | Product context (type, org, team) | `00_setup.md` |
| 1 | **Hypothesis** | Hypothesis across 7 dimensions + confidence scores | `narrative-v1.md` |
| 2 | **Market research** | Analogs (successes) + antilogs (failures) per dimension | `market-research.md` |
| 3 | **Synthesis** | Risk scoring + cross-fit + narrative V2 | `risk-prioritization.md`, `narrative-v2.md` |
| 4 | **Validate (DVF)** | 9 assumptions from the riskiest dimension + 2×2 map + experiment | `assumptions-map.md`, `experiment-brief.md` |
| 5 | **Interview prep** | Guide for in-depth interviews | `interview-guide.md` |
| 6 | **[Field]** | *Outside the skill. The user runs 15–20 interviews.* | `interviews/notes/*.md` |
| 7 | **Interview synthesis** | Patterns from notes → narrative V3 | `interview-synthesis.md`, `narrative-v3.md` |
| 8 | **[MVP launch]** | *Outside the skill. The user launches the MVP.* | — |
| 9 | **Metrics** | Sean Ellis + retention cohorts + Levels of PMF | `metrics-dashboard.md` |
| 10 | **Iterate** | Decision: continue / iterate / pivot | `iteration-changelog.md` |

For the stage-to-stage transition map, see `references/<lang>/pipeline-overview.md`.

---

## Step 3 — Hypothesis (Stage 1)

**Goal:** turn the product idea into a structured hypothesis across 7 PMF dimensions with honest confidence scores.

**7 dimensions** (detail — `references/<lang>/7-dimensions.md`):
1. Problem to Solve — outcome-motivation gap
2. Target Audience — 2-3 defining attributes, Now vs Future segments
3. Value Proposition — tagline + 3-5 benefits (not features)
4. Competitive Advantage — one of the 7 Powers (Helmer)
5. Growth Strategy — short-term traction (first 1K) ≠ long-term sustainable (100K+)
6. Business Model — equation, pricing, LTV, cost structure
7. Timing / Why Now — what changed, why now in particular

**Before dimensions:** Team Pre-Flight Check — 3 questions (`references/<lang>/stage-1-hypothesis.md`).

**After dimensions:** confidence assessment 1–10 for each + identification of the riskiest.

**Artifact:** `narrative-v1.md` from the template `references/<lang>/template-narrative.md` (structured) or `references/<lang>/template-narrative-prose.md` (prose, for stakeholders).

**Detailed stage logic:** `references/<lang>/stage-1-hypothesis.md`.

---

## Step 4 — Market Research (Stage 2)

**Goal:** find analogs (successful companies validating the dimension) and antilogs (known failures on the dimension) for each of the 7 dimensions.

**Method:** sequentially via `Exa` (preferred) or `WebSearch` (fallback). Per dimension — 3-5 analogs and 2-3 antilogs. Total ~14-21 searches.

**Adaptive threshold:**
- Mature markets (SaaS, e-commerce, marketplace): analog = $10M+ revenue
- Emerging markets (AI, web3, new categories): analog = $1M+ ARR or 10K+ active users

**⛔ Do NOT use the Agent tool / subagents.** Search is done by direct calls to `mcp__exa__web_search_exa` or `WebSearch` in the main session. This is a hard rule.

**Artifact:** `market-research.md` from the template `references/<lang>/template-market-research.md`.

**If context overflows:** split into 2 passes (dim 1-4 in one session, dim 5-7 in the next). This is normal for a months-long cycle.

**Detailed logic and search strategies per dimension:** `references/<lang>/stage-2-research.md`.

---

## Step 5 — Synthesis (Stage 3)

**Goal:** condense the research into risk-prioritization, identify the riskiest dimension, update the narrative to V2.

**Risk scoring formula:**
```
Risk Score = (10 - Evidence Score) × Failure Impact
```

**Failure Impact defaults** (can be recalibrated for the specific product):

| Dimension | Default Impact |
|-----------|---------------|
| Problem to Solve | 4 (Critical) |
| Target Audience | 3 (High) |
| Value Proposition | 2 (Medium) |
| Competitive Advantage | 2 (Medium) |
| Growth Strategy | 3 (High) |
| Business Model | 4 (Critical) |
| Timing / Why Now | 3 (High) |

**Cross-fit analysis** (mandatory):
- **Channel-Model Fit** — does the growth channel fit the business model? (example conflict: enterprise sales + freemium pricing)
- **Model-Market Fit** — does the business model fit the target audience? (example conflict: subscription for an audience that does not pay for software)

**Artifacts:**
- `risk-prioritization.md` (from the template `references/<lang>/template-risk-prioritization.md`)
- `narrative-v2.md` (an update of V1 based on research data, with an explicit version history changelog)

**Decision tree after synthesis:**
- Overall confidence > 7 + a riskiest dimension exists → Stage 4 (validate the riskiest) or jump to Stage 5 (interviews)
- Overall confidence 4–7 → Stage 4 is mandatory
- Overall confidence < 4 → return to Stage 1 (rethink hypothesis) or do more research

**Detailed logic:** `references/<lang>/stage-3-synthesis.md`.

---

## Step 6 — Validate / DVF (Stage 4)

**Goal:** take the riskiest dimension, decompose it into 9 assumptions across DVF (Desirability × Viability × Feasibility), prioritize via a 2×2 (importance × evidence), and design an experiment for the riskiest assumption.

**DVF categories** (detail — `references/<lang>/dvf-framework.md`):
- **Desirability** — does the user need this? (only user needs, nothing about money or technical feasibility)
- **Viability** — is this profitable for the business? (everything financial — pricing, unit economics, LTV, CAC, costs)
- **Feasibility** — can we build it? (operational + technical + regulatory)

**Assumption format:** "I believe..." 9 of them (3 per category).

**Regulatory sub-check:** if product type = AI / fintech / healthtech → automatically add 1-2 regulatory assumptions to Feasibility.

**2×2 map:** importance (high/low) × evidence (strong/weak). The riskiest = high importance + weak evidence.

**Experiment brief** for the risk-assumption:
- Assumption verbatim
- What learning?
- Experiment type (one of the standards: Customer Interview, Smoke Test, Concierge, Survey, Prototype, Landing Page)
- How to run (3 steps)
- How to measure (success + failure signals, concrete thresholds)
- Estimated effort
- Remaining uncertainty

**Artifacts:**
- `assumptions-map.md` (9 assumptions + 2×2)
- `experiment-brief.md` (for the risk-assumption)

**Detailed logic:** `references/<lang>/stage-4-validate.md`.

---

## Step 7 — Interview Prep (Stage 5)

**Goal:** prepare the guide for in-depth interviews on the 2-3 riskiest dimensions from risk-prioritization.

**Guide structure:**
1. Introduction script (greeting, purpose, consent, recording)
2. Screening questions (2-3 questions to check audience fit)
3. Thematic blocks: 5-7 open questions per risk-dimension
4. Closing (thanks, next steps, incentive)

**Question rules:**
- Open, not leading
- About past behavior, not hypothetical futures
- About concrete situations, not general opinions
- Coverage matrix: every question maps to a dimension and assumption

**Quantity:** at least 15-20 interviews, saturation usually at 12-20.

**Artifacts:**
- `interview-guide.md`
- `interviews/note-template.md` (template for one note for the user)

**Detailed logic:** `references/<lang>/stage-5-interview-prep.md`.

---

## Step 8 — Field Interviews (outside the skill)

This is a **waiting state**. When resumed at this stage, the skill says:

```
📍 Stage 6 — field (interviews)
   Guide ready: interview-guide.md
   Notes collected: <count> in interviews/notes/

What's new? Ready to move to synthesis (Stage 7)?
- How many interviews have you done in total?
- Are there obvious patterns already?
- When are you planning to finish the field?
```

The skill **does not try to conduct interviews**. It only prepares and then processes the results.

With ≥ 1 note in `interviews/notes/` — moving to Stage 7 is possible (though 15+ is optimal).

---

## Step 9 — Interview Synthesis (Stage 7)

**Goal:** read all interview notes, extract patterns per dimension, update confidence scores, evolve the narrative to V3.

**Process:**
1. Read **all** notes from `interviews/notes/` (not in a batch — one at a time, to avoid mixing respondents)
2. For each dimension extract: pattern (what they say) + supporting evidence (how many respondents confirm) + key quotes (2-3 verbatim) + confidence change
3. Cross-dimensional insights (patterns spanning several dimensions)
4. Surprises (findings that contradict the hypothesis)
5. Updated risk assessment table (pre vs post)
6. Recommended next steps (build MVP / more validation / pivot)

**Artifacts:**
- `interview-synthesis.md` (from the template `references/<lang>/template-interview-synthesis.md`)
- `narrative-v3.md` (an update of V2 based on field data)

**Loop detection:** if confidence dropped between V2 and V3 → flag + recommendation (return to Stage 4 for deeper validation, or to Stage 1 to revisit the hypothesis).

**Detailed logic:** `references/<lang>/stage-7-interview-synthesis.md`.

---

## Step 10 — MVP Launch (outside the skill)

A waiting state. The skill says:

```
📍 Stage 8 — MVP launch
   narrative-v3 is ready, the hypothesis is validated.

When you are ready:
- Launch the MVP to a minimally viable audience
- Collect the first ~40 active users
- Come back for Stage 9 (metrics)

What do you want to discuss about the launch?
```

The skill is only useful here as a sounding board — it does not try to "launch the MVP."

---

## Step 11 — Metrics (Stage 9)

**Goal:** set up post-launch PMF measurement through 3 instruments.

**Sean Ellis Survey** (`references/<lang>/sean-ellis-survey.md`):
- Question: "How would you feel if you could no longer use [product]?"
- Options: Very disappointed / Somewhat disappointed / Not disappointed / N/A
- Threshold: ≥ 40% Very disappointed = PMF
- Minimum 40 responses
- Distribute only to active users (not the newsletter list)
- The skill generates the question text + distribution instructions, **does not collect data itself**

**Retention Cohorts:**
- Cohort table (week 1, 2, 3, 4, 5...) × percentage of returning users
- PMF signal: the curve flattens, does not drop to zero
- Table template

**First Round Levels of PMF** (`references/<lang>/levels-of-pmf.md`):
- Level 1: Nascent (early signals)
- Level 2: Developing (some signals, but not stable)
- Level 3: Strong (stable retention + WOM growth)
- Level 4: Extreme (mega-signals — non-linear growth, hype)
- Each level has its own signals across satisfaction / demand / efficiency

**Artifact:** `metrics-dashboard.md` (from the template `references/<lang>/template-metrics-dashboard.md`)

**Flow:** the skill creates the template → the user collects data over weeks → comes back → the skill interprets and recommends Stage 10.

**Detailed logic:** `references/<lang>/stage-9-metrics.md`.

---

## Step 12 — Iterate (Stage 10)

**Goal:** based on the metrics, make a decision and lock it in.

**Decision tree:**
- Sean Ellis ≥ 40% + retention flattens + Level 3+ → **PMF achieved**, move to scale (outside this skill's scope)
- Sean Ellis 25-40% + retention partly flattens + Level 2 → **iterate** (return to Stage 4 for the risk-assumption or Stage 7 for a new interview cycle)
- Sean Ellis < 25% + retention falling + Level 1 → **pivot** (return to Stage 1, rethink the failed dimension)

**Artifact:** `iteration-changelog.md` — what changes, why, which stage we return to.

After the changelog is written, auto-start will determine the stage again from the new artifacts.

---

## Cross-stage rules

**Narrative versioning:**
- V1 (after Stage 1) — initial hypothesis
- V2 (after Stage 3) — after market research, updated based on analogs/antilogs
- V3 (after Stage 7) — after interview synthesis, updated based on field data
- Each version is its own file, does not overwrite the previous one
- Each new version has a "Version History" section with a changelog (what changed vs the previous version)

**Confidence can decrease.** Do not inflate. If the data contradicts the hypothesis — note it honestly.

**Loop detection:** if the confidence on some dimension dropped in the new version → flag. Possible actions: more validation, return to research, or pivot.

**Going back.** The user can say "go back to stage X" at any time — the skill switches. Old artifacts are not deleted. Example: after Stage 4 you decide more research is needed → return to Stage 2 → new `market-research-v2.md` (not overwrite).

**Between sessions:** the PMF cycle is months. On every resume the skill re-reads auto-start and does not trust "memory" of the previous session.

---

## Quality gates (general for the pipeline)

Before moving to the next stage, verify:

- [ ] All 7 dimensions covered (no "we forgot Timing")
- [ ] Confidence scores recorded for every dimension
- [ ] Riskiest dimension explicitly identified
- [ ] Cross-fit analysis (Channel-Model + Model-Market) done in Stage 3
- [ ] DVF assumptions = 9 (3 per category) in Stage 4
- [ ] Interview guide contains no leading questions in Stage 5
- [ ] Coverage matrix covers all 2-3 risk-dimensions in Stage 5
- [ ] Sean Ellis survey collected on at least 40 responses in Stage 9
- [ ] Retention analyzed by cohorts, not by overall average, in Stage 9
- [ ] Decisions in Stage 10 are based on all three instruments at once (not just Sean Ellis)

---

## Common pitfalls

| Mistake | How to avoid |
|--------|--------------|
| Solution-framed problem ("our product gives X") | Problem = what the user is trying to achieve, what gets in the way. Do not mention the product. |
| Audience too broad ("all women") | 2-3 defining attributes. Now segment vs Future segments. |
| Features instead of benefits in value prop | Benefit first (what the user gets), then how (the feature) |
| Overconfidence in V1 | At stage 1, confidence is usually 4-6/10. 9-10 in V1 is a red flag. |
| Missing "why now" | Timing is not "we feel the time has come." It is a concrete change in technology, behavior, or regulation. |
| 7 dimensions = "let's do well" | The goal is to find WEAK spots, not validate everything. The riskiest dimension matters more than the rest. |
| Wanting to jump straight to Stage 9 | Without Stages 1-7, metrics mean nothing. Sean Ellis on a random audience gives a random result. |
| Comparing with old analogs without context | An analog from 2010 ≠ market 2026. Account for what changed. |
| Sean Ellis on fewer than 40 responses | Statistically meaningless. Wait. |
| Sean Ellis on a newsletter list, not active users | Active = actually used the product ≥ 1 time in the last 2 weeks. |

---

## Reference files

All references live under `references/<lang>/...`, where `<lang>` is `en` or `ru` (chosen at first run, stored in config).

**Pipeline map:**
- `pipeline-overview.md` — state machine, transitions between stages

**Stage logic (read on the corresponding stage):**
- `stage-0-setup.md`
- `stage-1-hypothesis.md`
- `stage-2-research.md`
- `stage-3-synthesis.md`
- `stage-4-validate.md`
- `stage-5-interview-prep.md`
- `stage-7-interview-synthesis.md`
- `stage-9-metrics.md`

**Methodology (read when needed — reference manuals):**
- `7-dimensions.md` — full description of the 7 PMF dimensions + what good looks like
- `7-powers.md` — Hamilton Helmer competitive advantage
- `dvf-framework.md` — David Bland Desirability/Viability/Feasibility
- `sean-ellis-survey.md` — 40% threshold, distribution
- `levels-of-pmf.md` — First Round 4 levels
- `narrative-writing-guide.md` — how to make problem visceral

**Artifact templates** (load at the relevant stage):
- `template-narrative.md` — structured narrative with 7 dimensions + validation table
- `template-narrative-prose.md` — prose for stakeholders
- `template-market-research.md` — market research synthesis
- `template-risk-prioritization.md` — risk scoring + cross-fit
- `template-interview-guide.md` — interview guide
- `template-interview-synthesis.md` — interview synthesis
- `template-metrics-dashboard.md` — metrics dashboard
- `template-interview-note.md` — one interview note

---

## Methodology sources

- **gnurio/pmf-plugin** — structural pipeline pattern (10 stages)
- **Marty Cagan** — *Empowered*, product discovery
- **David Bland** — *Testing Business Ideas* (DVF framework)
- **Hamilton Helmer** — *7 Powers* (competitive advantage)
- **Sean Ellis** — PMF survey (40% threshold)
- **First Round Capital** — Levels of PMF
- **Bill Gross** — TED talk on timing as the key startup-success factor
