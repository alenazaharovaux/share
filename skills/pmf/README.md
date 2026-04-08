# PMF — Product-Market Fit Engine

A Claude Code skill that walks one product through a full product-market fit cycle, from the first sketch of the hypothesis to post-launch metrics. Ten stages, three narrative versions, two languages, one continuous loop.

A PMF cycle takes months. The skill returns to the same questions in different forms — first as guesses, then as research findings, then as user quotes, then as post-launch metrics. It is built for that pace: it remembers where you stopped, resumes between sessions, does not rush you. A week on the hypothesis, three weeks on market research, six weeks of interviews, a two-month pause, return with metrics — that is a normal sequence. On every run the skill reads the project folder, identifies the stage, and proposes the next reasonable step.

> **🧪 Beta — feedback wanted.** The skill is being shaken down on real products. The pipeline holds end to end, but every product is its own animal — there will be places where the skill works well, places where it is awkward, and places where it is plain wrong. If you try it, tell us what worked, what broke, and what felt off. Open an issue or drop a note in the share repo. The first 5–10 outside users are the most valuable feedback the skill can get.

---

## Table of contents

- [What this skill is](#what-this-skill-is)
- [Who it's for](#who-its-for)
- [What's inside](#whats-inside)
- [Installation](#installation)
- [First run — configuration](#first-run--configuration)
- [How it works](#how-it-works)
- [The 10 stages in depth](#the-10-stages-in-depth)
- [The 7 dimensions](#the-7-dimensions)
- [Cross-stage rules](#cross-stage-rules)
- [Methodology sources](#methodology-sources)
- [Trigger phrases](#trigger-phrases)
- [Dependencies](#dependencies)
- [FAQ](#faq)
- [Limitations](#limitations)
- [How to give feedback](#how-to-give-feedback)
- [Русская версия](#русская-версия)

---

## What this skill is

The PMF skill is one orchestrator, not a bundle. One entry point: you say something like "let's do PMF for my new product", and the skill takes you through the whole cycle. No sub-skills to remember, no manual switching. All ten stages live inside it. Each stage reads the artifacts of the previous stages and writes its own.

The project folder is the state. The skill checks which files exist in the folder and derives the current stage from them. No database, no JSON state file, no hidden bookkeeping. Delete a file and the matching stage becomes undone. Copy the folder and you have a full snapshot of the project. The whole system is files in a folder: easy to inspect by hand, edit by hand, share with a teammate, commit to git.

Three principles hold the skill together.

**Calm tone.** No exclamation marks, no drama. You are doing PMF to find out what works and what does not, not to get cheered on. The skill is a quiet collaborator, not a coach.

**Confidence is allowed to drop.** If new data contradicts the hypothesis, the skill lowers the confidence score and says so, rather than papering over it. A V2 narrative with lower confidence than V1 is a sign the cycle is doing its job. The whole pipeline is built on the idea that "I know less than I thought" is a productive finding.

**The skill does not pretend to do field work.** Two stages — Stage 6 (field interviews) and Stage 8 (MVP launch) — are explicitly outside the skill. It prepares the interview guide and waits. It writes the metrics dashboard template and waits. It never simulates user data, never invents respondent quotes, never pretends to "run the MVP for you." Real-world work stays outside the skill.

---

## Who it's for

The skill drives one product through a full PMF cycle under one person in charge — whoever sits in Claude Code and works with the artifacts. Company size does not enter into it. It works the same for:

- a solo founder with an idea;
- a product manager in a small team;
- a product manager in a large company, responsible for one product or one product line;
- a researcher running a discovery project;
- a team where one person runs the cycle and the rest read the files and discuss the results.

Artifacts live in a folder as plain markdown files. Commit them to git and your colleagues read the same versions you do. Collaboration is built this way, not through built-in review workflows.

The skill does **not** cover:
- Built-in collaboration. No approval flows, no in-artifact comments, no roles, no notifications. If your company needs that, use the skill as the lead's tool and run review outside it.
- Portfolio analysis. Five products mean five separate folders with no links between them. A cross-product view has to be assembled by hand.
- Replacing an existing corporate PMF process. The skill is opinionated: Cagan, Bland, Helmer, Sean Ellis, First Round. If the methodology cannot bend, the skill will clash with it.
- MVP launch and task management. The skill produces content artifacts; it does not replace Jira or Linear.
- Investor pitch decks. The narrative inside is a working hypothesis, not sales copy for a fundraising deck.
- Real interviews. You run them. The skill makes the conversation sharper: a better guide, a better synthesis.

---

## What's inside

```
pmf/
├── SKILL.md                                  ← the skill itself (English entry point)
├── README.md                                 ← this file
├── config.md                                 ← user configuration (language, projects path)
└── references/
    ├── en/                                   ← 23 English reference files
    │   ├── pipeline-overview.md              ← state machine, transitions between stages
    │   ├── stage-0-setup.md                  ← detailed Stage 0 logic
    │   ├── stage-1-hypothesis.md             ← detailed Stage 1 logic
    │   ├── stage-2-research.md               ← detailed Stage 2 logic
    │   ├── stage-3-synthesis.md              ← detailed Stage 3 logic
    │   ├── stage-4-validate.md               ← detailed Stage 4 logic
    │   ├── stage-5-interview-prep.md         ← detailed Stage 5 logic
    │   ├── stage-7-interview-synthesis.md    ← detailed Stage 7 logic
    │   ├── stage-9-metrics.md                ← detailed Stage 9 logic
    │   ├── 7-dimensions.md                   ← the 7 PMF dimensions in full
    │   ├── 7-powers.md                       ← Hamilton Helmer's competitive moats
    │   ├── dvf-framework.md                  ← David Bland's Desirability/Viability/Feasibility
    │   ├── sean-ellis-survey.md              ← the 40% benchmark, full distribution rules
    │   ├── levels-of-pmf.md                  ← First Round 4-level ladder
    │   ├── narrative-writing-guide.md        ← how to write the central narrative
    │   ├── template-narrative.md             ← structured narrative template
    │   ├── template-narrative-prose.md       ← prose narrative template (for stakeholders)
    │   ├── template-market-research.md       ← market research output template
    │   ├── template-risk-prioritization.md   ← risk scoring template
    │   ├── template-interview-guide.md       ← interview guide template
    │   ├── template-interview-note.md        ← single interview note template
    │   ├── template-interview-synthesis.md   ← interview synthesis template
    │   └── template-metrics-dashboard.md     ← metrics dashboard template
    └── ru/                                   ← 23 Russian reference files
        └── ... (same set, in Russian)
```

The skill itself is about 480 lines in `SKILL.md`. References are loaded on demand — only when you reach a stage that needs them. This keeps the active context small even though the full methodology is over 250K characters.

The references split into three groups:

**Stage logic** (9 files: pipeline-overview + 8 stages). These are the operational manuals for each stage — what reads what, what writes what, the quality gates, the common pitfalls. Loaded when you enter the corresponding stage.

**Methodology** (6 files: 7-dimensions, 7-powers, dvf-framework, sean-ellis-survey, levels-of-pmf, narrative-writing-guide). These are reference manuals for the underlying frameworks. Loaded when needed — for example, `7-powers.md` is read inside Stage 1 when you reach the Competitive Advantage dimension.

**Templates** (8 files: narrative × 2, market research, risk prioritization, interview guide, interview note, interview synthesis, metrics dashboard). These are the actual fill-in-the-blanks templates the skill copies into your project folder. Each one is paired with its stage.

---

## Installation

**macOS / Linux:**
```bash
cp -r pmf ~/.claude/skills/pmf
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse pmf $env:USERPROFILE\.claude\skills\pmf
```

After this you can invoke the skill from any Claude Code session — it is global, not per-project.

---

## First run — configuration

The first time you trigger the skill, it asks you two questions and saves your answers in `~/.claude/skills/pmf/config.md`. Both questions can be skipped — the skill will use defaults.

| Question | Why it's asked | Default |
|---|---|---|
| **What language should we work in — English or Russian?** | The skill is fully bilingual. Each language has its own set of references in `references/en/` or `references/ru/`. The skill also speaks to you in the chosen language for the rest of the cycle. | `en` (English) |
| **Where should PMF projects be stored?** | Each product becomes a subfolder. The default keeps everything in your home directory; you can point it at any folder you like — Documents, an Obsidian vault, an external drive, anywhere. | `~/pmf-projects/` |

After both answers, the skill writes the config and confirms. You can change either value at any time by editing `~/.claude/skills/pmf/config.md` directly. If you delete the file, the skill will recreate it on the next run by asking again.

The config file looks like this:
```
language: en
projects_path: ~/pmf-projects
```

That's it. No environment variables, no JSON, no install scripts.

---

## How it works

On trigger the skill reads the config first (or asks the setup questions if there is no config yet). Then it lists the projects folder and looks at what is there. Three scenarios.

1. **Starting a brand-new product.** The skill creates a subfolder, runs Stage 0 (setup), and walks you through the basics: name, slug, product type, organizational context, team pre-flight check. 10–20 minutes. Output: `00_setup.md`.

2. **Continuing an existing product.** The skill finds your subfolder, looks at the files inside, and figures out the current stage by file presence. If `narrative-v1.md` exists but `market-research.md` does not, you are between Stage 1 and Stage 2. The skill says exactly that and asks what to do next.

3. **Several products in flight.** The skill lists them with current stage and last-modified date and asks which one you want to work on. It does not guess.

After that the skill proposes the next reasonable step and waits for confirmation. You can always override: "go back to Stage 2", "let me redo the narrative", "skip Stage 4 for this dimension" — and the skill switches. Old artifacts are never deleted. Redo Stage 2 and you get `market-research-v2.md`, not an overwrite.

The whole machine runs on file presence. No separate state, no in-memory cache. Every session is a fresh read of the folder. It sounds slow, and that is exactly what lets the skill survive months between sessions.

---

## The 10 stages in depth

The pipeline is one happy path with explicit non-linear escapes. Here is what each stage does.

### Stage 0 — Setup

A short stage to gather basic context before you touch the hypothesis. Three things are collected: product type (B2C / B2B / Marketplace / DTC / Services / Internal / Other), organizational context (Zero-to-one / Established / Extension), and a team Pre-Flight Check (3 questions: founder-market fit, skill gaps, conviction-flexibility).

Why these three? Because they shape every later stage. A B2B product needs to be analyzed twice — once for the buyer, once for the user. A zero-to-one product cannot lean on existing channels. A team with no founder-market fit needs partners, and that affects the risk map. Skipping Stage 0 to "save time" usually costs hours of confusion in Stage 1.

**Output:** `00_setup.md`

### Stage 1 — Hypothesis

The first version of the central narrative. The skill walks you through 7 PMF dimensions, asking guided questions, applying validation rules, and recording confidence scores for each.

The output is `narrative-v1.md` — a structured document with one section per dimension, a confidence table, and an explicit "riskiest dimension" mark. Confidence scores in V1 are usually 4–6 out of 10 for most dimensions. If you find yourself writing 9–10 in V1, that is a sign of overconfidence and the skill will push back.

For B2B and Marketplace products, the skill goes through the dimensions twice — once per role. Decision Makers and End Users have different problems and different value props. The chicken-and-egg side of marketplaces is called out explicitly in Growth Strategy.

You can pick between two output formats — structured (better for internal tracking) or prose (better for stakeholders). V1 is usually structured only.

**Output:** `narrative-v1.md`

### Stage 2 — Market Research

The skill leaves the team's heads and searches the world for evidence. The goal: for each of the 7 dimensions, find **analogs** (companies that successfully validated this dimension under real conditions) and **antilogs** (known failures that show what breaks on this dimension).

The method is sequential web search via Exa (preferred) or WebSearch (fallback). 14–21 searches total, 2–3 per dimension. **Subagents are explicitly forbidden** here. Researching analogs is content work, not file lookup, and the user must see every search and every result to intervene. The skill adapts the "what counts as an analog" threshold to the market type: $10M+ for mature markets, $1M+ ARR for emerging ones.

The output is written to `market-research.md` after each dimension, not held in memory until the end. If the context starts overflowing, the skill splits the work into two passes (dimensions 1–4 in one session, 5–7 in the next). This is normal for a months-long cycle.

Stage 2 ends with a short preview of which dimensions look risky after the research, and a recommendation for Stage 3.

**Output:** `market-research.md`

### Stage 3 — Synthesis

The skill takes the V1 narrative and the market research and produces three things: a numerical risk score per dimension, a cross-fit analysis, and an updated narrative (V2).

**Risk scoring** uses the formula `Risk Score = (10 - Evidence Score) × Failure Impact`. Evidence Score is how strongly the data supports the dimension (1–10). Failure Impact is how catastrophic it would be if this dimension turned out to be wrong (1–4, with sensible defaults — Problem and Business Model are 4, Audience and Growth are 3, Value Prop and Power are 2). The default impacts can be recalibrated for the specific product.

**Cross-fit analysis** is two mandatory consistency checks: Channel-Model Fit (does the growth channel work with the business model?) and Model-Market Fit (does the business model work for the audience?). These often hide fatal conflicts that scoring alone misses.

**V2 narrative** is a separate file from V1, with a Version History changelog. If a dimension's confidence dropped, V2 says so explicitly. If a dimension was pivoted or reset, the skill marks it. Confidence is allowed to go down.

Stage 3 ends with a decision tree: high overall confidence + a clear riskiest dimension → go to Stage 4 to validate it. Mid confidence → Stage 4 is mandatory. Low confidence → return to Stage 1 or Stage 2. Cross-fit conflicts → return to Stage 1 to rethink the conflicting pieces.

**Outputs:** `risk-prioritization.md`, `narrative-v2.md`

### Stage 4 — Validate (DVF)

The riskiest dimension from Stage 3 gets unfolded into 9 testable assumptions across DVF — David Bland's Desirability × Viability × Feasibility framework. Three assumptions per category, no exceptions. Desirability is *only* about user needs (no money, no tech). Viability is *only* about money. Feasibility is operational + technical + regulatory.

The skill is strict about terminology here. In stages 1–3 it uses "hypothesis." In Stage 4 it switches to "assumption." Bland's framework is built around assumptions being concrete, testable "I believe..." statements, and mixing the two terms causes confusion down the line.

After the 9 assumptions are written, the skill places them on a 2×2 of importance × evidence. The Critical quadrant — high importance, weak evidence — is what gets tested first. The skill then designs an experiment for the riskiest assumption from this quadrant, using one of 6 standard experiment types: Customer Interview, Smoke Test, Concierge, Survey, Prototype, Landing Page. **Custom experiment types are forbidden** — "mini-pilot" and "discovery sprint" are vague and the skill will refuse to invent new ones. If nothing fits, the assumption gets reframed.

The experiment brief includes concrete success and failure thresholds (not "lots of sign-ups" but "≥3% landing → trial sign-up"), estimated effort, and a note on what the experiment will *not* show.

For AI / fintech / healthtech products, regulatory assumptions automatically replace one or two operational/technical ones in Feasibility.

**Outputs:** `assumptions-map.md`, `experiment-brief.md`

### Stage 5 — Interview Prep

Based on the 2–3 riskiest dimensions from Stage 3, the skill builds an interview guide with five thematic blocks. Each block has 5–7 open questions. The questions follow strict rules: no leading, no hypothetical futures, no opinions about what people might do — only past behavior, only concrete situations.

The guide is structured: introduction script, screening questions (2–3, behavioral not demographic), thematic blocks per risk-dimension, closing with a referral request. Every question is mapped to a dimension and an assumption in a coverage matrix, so by the end of the interview cycle every Critical-quadrant assumption from Stage 4 has at least one question pointed at it.

The skill recommends 15 interviews as a minimum, 20–30 as the sweet spot. It also creates a `note-template.md` — the structured format the user copies for each interview in the field.

**Outputs:** `interview-guide.md`, `interviews/note-template.md`, empty `interviews/notes/` folder

### Stage 6 — Field Interviews (outside the skill)

This is a **waiting state**. The skill cannot conduct interviews. It can only prepare the guide and then process the notes. When you resume the skill on this stage, it tells you the guide is ready, asks how many interviews you've done, and waits.

The user does the field work over weeks or months. Each interview becomes a note in `interviews/notes/`, written in the structured format from the template. With at least one note in the folder the skill will let you move to Stage 7, but 15+ is the recommended minimum for meaningful synthesis.

### Stage 7 — Interview Synthesis

The skill reads all the interview notes — **one at a time**, not batched, to avoid averaging out the patterns — and extracts findings per dimension. For each dimension it produces: pattern (what they say), supporting evidence count (N out of M respondents), 2–3 verbatim key quotes, confidence change (V2 → V3), and an update type (Validated / Refinement / Pivot / Reset).

It also pulls out **cross-dimensional insights** (patterns that span multiple dimensions) and **surprises** (findings that contradict the hypothesis). Surprises are often the most valuable findings in the whole cycle. If you find none, the skill flags possible confirmation bias and asks you to re-read the notes.

The result is `interview-synthesis.md` and a third version of the narrative — `narrative-v3.md`. V3 is rewritten in user language, with direct quotes, narrower personas, and updated risks. If confidence dropped on any dimension between V2 and V3, the skill flags it and recommends what to do next: more validation, return to research, or a pivot.

**Outputs:** `interview-synthesis.md`, `narrative-v3.md`

### Stage 8 — MVP Launch (outside the skill)

Another waiting state. The narrative is validated as far as words allow. Next you build something and put it in front of real users. When you resume the skill on this stage, it confirms the narrative is ready and reminds you to come back for Stage 9 once you have around 40 active users.

During this stage the skill can work as a sounding board — discussing scope, MVP features, target audience for the launch — but it will not launch the product for you.

### Stage 9 — Metrics

Post-launch measurement, set up through three instruments used together:

**Sean Ellis 40% Survey.** One question — *"How would you feel if you could no longer use [product]?"* — with four answer options. The threshold is ≥40% "Very disappointed" (excluding N/A) = PMF. Minimum 40 responses, distributed only to active users (not the newsletter list, not cherry-picked top customers). The skill generates the question text and the distribution instructions but does NOT collect data itself.

**Retention Cohorts.** A cohort table (signup week × percent of users returning in week 1, 2, 3, 4, 8, 12), with the definition of "active" calibrated to the product type. PMF signal: the curve flattens at a healthy level, instead of falling to zero. Strong PMF threshold is >40% for consumer, >60% for B2B, >25% for high-frequency. The skill creates the table template and the data-collection instructions.

**First Round Levels of PMF.** A 4-level ladder — Nascent / Developing / Strong / Extreme — assessed across three dimensions (Satisfaction, Demand, Efficiency). The overall level is the *minimum* of the three, not the average. A team cannot be Strong on Satisfaction and Nascent on Efficiency at the same time — that mismatch is the bottleneck.

Stage 9 unfolds across three phases: a setup phase where the dashboard template is created, a collection phase of 4–12 weeks where the user gathers the data on their own, and an interpretation phase where the user returns with the filled dashboard and the skill recommends what to do in Stage 10.

**Output:** `metrics-dashboard.md`

### Stage 10 — Iterate

Based on the metrics, decide what's next:

- **Sean Ellis ≥40% + retention flatten + Level 3+** → PMF achieved. The skill steps out — scaling is outside its scope.
- **Sean Ellis 25–40% + partial retention flatten + Level 2** → Iterate. Return to Stage 4 (validate the next risk-assumption) or Stage 7 (a new round of interviews focused on the "Somewhat disappointed" segment).
- **Sean Ellis <25% + falling retention + Level 1** → Pivot. Return to Stage 1 with explicit reasoning about which dimension failed.

The output is `iteration-changelog.md`. After it's written, the skill's auto-start will read the folder again and propose the next stage based on the new state. The cycle continues.

**Output:** `iteration-changelog.md`

---

## The 7 dimensions

Every stage of the pipeline circles back to these 7 dimensions. They are not independent — strong hypotheses show how they reinforce each other. The skill loads the full description from `references/<lang>/7-dimensions.md` when you reach Stage 1, but here is the short version:

| # | Dimension | The question | Watch out for |
|---|---|---|---|
| 1 | **Problem to Solve** | What outcome are users trying to achieve, and what is in the way? | Solution-framed problems ("they don't have our tool"). Abstract problems ("they want efficiency"). |
| 2 | **Target Audience** | Who exactly, and why them now (vs. who later)? | Demographic-only personas. "All small businesses." Now segment = future segment. |
| 3 | **Value Proposition** | What single benefit, in their words, hits hardest? | Features instead of benefits. Generic claims. Multiple competing taglines. |
| 4 | **Competitive Advantage** | Which of Helmer's 7 Powers is your long-term moat? | "Best team", "first to market", "unique tech" — none of those are Powers. |
| 5 | **Growth Strategy** | How do you get the first 1K, and how do you get to 100K? | Same channel for both horizons. "We'll go viral" with no mechanism. |
| 6 | **Business Model** | What is the equation, and is it consistent with audience and channel? | "There will be ads / freemium / premium" with no numbers. Pricing copied from a competitor. |
| 7 | **Timing / Why Now** | What concrete shift made this possible/needed in the last 1–3 years? | "We feel the time has come." "AI hype." Vague "the market is ready." |

The 8th half-dimension, Defensibility / Power, is treated as part of Competitive Advantage but is checked separately during Stage 1 and again in Stage 9 once metrics are in.

---

## Cross-stage rules

A few rules cut across the whole pipeline. Boring but load-bearing.

**Narrative versioning.** V1, V2, and V3 are **separate files**, never overwrites. Each new version has a Version History section explaining what changed and why. The diff between V1 and V3 is often the most useful artifact of the whole cycle.

**Confidence can decrease.** If the data contradicts the hypothesis, the skill lowers the confidence score and says so. A V3 with lower confidence than V2 is a sign the cycle is working. Inflating numbers to feel better is the most common failure mode in self-driven PMF work, and the skill is built to push back against it.

**Loop detection.** If the same dimension's confidence keeps dropping across versions, the skill flags a possible loop and recommends one of three actions: more validation, return to research, or a pivot. It will not let you run an infinite cycle of "interviews → small refinement → more interviews" without surfacing the pattern.

**Going back is a first-class operation.** You can say "go back to Stage 2" at any time and the skill switches. Old artifacts are not deleted. Redo Stage 2 and you get `market-research-v2.md` next to the original. The folder grows over time.

**Between sessions, the skill re-reads everything.** It does not trust memory of "what we did last time." On every resume, auto-start scans the folder fresh and derives the state. This is what lets a months-long cycle survive across many short sessions.

**No subagents for content work.** Stage 2 (research) and Stage 7 (synthesis) are done in the main session, not delegated. Research is content work — the user must see every search and every quote to intervene. Synthesis requires reading interview notes one at a time in isolation, and a subagent would average the patterns. This is a hard rule.

**The skill never invents data.** It will not simulate interview quotes, will not generate fake metrics, will not assume "let's say Sean Ellis is 47%." Where data is missing, the skill says "no data yet" and asks the user to collect it.

---

## Methodology sources

The skill builds on several established frameworks. If you have time to read one thing from each, here is where to start.

- **Marty Cagan — *Empowered* and *Inspired*.** The 7-dimensions decomposition (with Timing as a 7th) draws on Cagan's product discovery work. His insistence that problem must be framed independently of the solution shows up in Stage 1's validation rules.

- **David Bland & Alex Osterwalder — *Testing Business Ideas* (2019, Strategyzer).** The DVF framework, the 9 assumptions, the 2×2 of importance × evidence, and the 6 standard experiment types in Stage 4 all come from this book. Bland's strictness about "assumption" vs "hypothesis" is preserved.

- **Hamilton Helmer — *7 Powers: The Foundations of Business Strategy*.** The competitive advantage dimension uses Helmer's seven powers (Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power) as the only acceptable answers. "We have a great team" is not on the list, and the skill will say so.

- **Sean Ellis — the 40% survey.** Published in 2009 as a response to "how do we know if we have PMF?" The 40% threshold is empirical, not theoretical — Ellis collected data from ~100 startups he consulted and found that those at ≥40% "Very disappointed" could scale via paid marketing with positive economics.

- **First Round Capital — *The Levels of Product/Market Fit (& What to Focus on at Each)*.** Todd Jackson, Brian Rothenberg, Carolyn Stein. The 4-level ladder — Nascent / Developing / Strong / Extreme — and the 3-dimensional assessment grid (Satisfaction × Demand × Efficiency) come from this First Round Review piece.

- **Bill Gross — TED talk on the #1 factor in startup success.** After analyzing 200+ companies, Gross found that timing was the strongest predictor of startup success — more important than team, idea, business model, or funding. This is why Timing / Why Now is one of the seven, treated with the same weight as Problem and Audience.

- **Rahul Vohra — *How Superhuman Built an Engine to Find Product/Market Fit*.** Published on First Round Review. Extends the Sean Ellis approach into a full process — segment the "Very disappointed" group, identify what they value, rebuild around them, repeat. This loop shape is what Stage 9 ↔ Stage 10 implements.

- **gnurio/pmf-plugin.** The structural pattern of breaking the cycle into ~10 sequential stages with auto-detection from folder state borrows from this plugin's pipeline. The dimensions, methodologies and quality gates inside are different, but the orchestration shape owes it a debt.

---

## Trigger phrases

The skill fires on natural language in either English or Russian. Anything in this rough shape will work.

**English:**
- "do PMF for [product name]"
- "I need product market fit for X"
- "PMF [name]"
- "start a PMF cycle"
- "I want to go through PMF"
- "help me validate [idea]"
- "continue PMF" / "continue PMF [name]"
- "what stage is my PMF at"
- "show my PMF projects"
- "is my product ready to launch"

**Russian:**
- «сделай PMF для [продукта]»
- «нужен product market fit для X»
- «PMF [имя]»
- «запусти PMF цикл»
- «хочу пройти PMF»
- «помоги валидировать [идею]»
- «продолжаем PMF»
- «продолжай PMF [имя]»
- «проверь PMF»
- «на каком этапе у меня PMF»
- «покажи мои PMF проекты»
- «готов ли мой продукт к запуску»

The skill also tries to catch any message where you mention a product and want to validate it systematically, even if you don't say "PMF" by name.

---

## Dependencies

**Required:**
- Claude Code (this is a Claude Code skill)
- WebSearch (built into Claude Code)

**Optional but recommended:**
- **Exa MCP** for Stage 2 market research. The skill prefers `mcp__exa__web_search_exa` because Exa's semantic search is significantly better for finding analogs and antilogs by problem description, not just keyword. If Exa isn't installed, the skill falls back to WebSearch automatically — Stage 2 still works, the searches are just more keyword-driven.

To install Exa MCP, see the [Exa MCP server docs](https://github.com/exa-labs/exa-mcp-server). If you don't want to set it up, you can ignore this entirely — the skill will simply use WebSearch.

**Not required:**
- No Python libraries
- No external APIs other than the search ones above
- No database
- No login or API keys to anything

---

## FAQ

**Q: How long does a PMF cycle take with this skill?**

A full cycle (Stage 0 through Stage 10) is months, not days. Realistic ranges: Stage 0 is 10–20 minutes. Stage 1 is 1–3 sessions of an hour each. Stage 2 (research) is 1–2 days of focused work. Stage 3 (synthesis) is half a day. Stage 4 (DVF) is half a day for the assumptions plus however long the experiment takes. Stage 5 (interview prep) is half a day. Stage 6 (field interviews) is **weeks** — 15–25 interviews, scheduled and conducted by the user. Stage 7 (synthesis) is half a day to a day. Stage 8 (MVP launch) is **weeks to months**. Stage 9 (metrics) needs at least 4 weeks of data collection. Stage 10 is one session. The skill fits that pace and resumes between sessions.

**Q: Can I skip a stage?**

You can, but the skill will warn you. Some skips are reasonable — for example, skipping Stage 4 if your Stage 3 confidence is high and the riskiest dimension is best validated through interviews directly. Other skips are warning signs — wanting to jump straight to Stage 9 (metrics) usually means you're hoping the numbers will tell you what the hypothesis won't. Sean Ellis on a random audience gives a random result; the earlier stages exist to make the metric meaningful.

**Q: What if my product is multi-sided (marketplace) or has multiple personas (B2B)?**

The skill handles this in Stage 1 with multi-role processing. For B2B you go through the 7 dimensions twice — once for Decision Makers (who pays), once for End Users (who uses). For marketplaces you go through them twice — once for each side, with the chicken-and-egg problem flagged in Growth Strategy. Both roles end up in the same `narrative-v1.md` as separate sections.

**Q: I already have a product in production. Can I start in the middle?**

Yes. You can create the project folder, drop your existing data into the relevant artifact files (e.g. an existing pitch deck → `narrative-v1.md`), and the skill will detect the stage and propose where to go next. There is nothing magical about starting at Stage 0; the auto-start treats whichever artifacts exist as the current state.

**Q: My team uses a different terminology — can I rename things?**

The skill is opinionated about a few terms because they have methodological weight: "assumption" vs "hypothesis" in Stage 4 (Bland's distinction matters), and the 4 Sean Ellis answer options must be in the original wording. Outside of those, you can rename anything you like in your own narrative — the templates are just suggestions.

**Q: Is this a replacement for talking to users?**

No. Stage 6 explicitly cannot be done by the skill. The whole pipeline is built around the assumption that you talk to real humans, and the skill's job is to make the conversations more useful (better guide, better synthesis) and the surrounding structure (hypothesis, research, risk scoring, metrics) more honest.

**Q: What if I don't know whether my product is B2C or B2B?**

Stage 0 has a tiebreaker question for this: who actually pays — the end user or their company? That's the type. If neither is clear, the product probably isn't ready for PMF analysis yet — you may need to pick a target first.

**Q: Will the skill commit my project files to git?**

No. The skill creates files in your projects folder and that's it. Whether you commit them, share them, or back them up is your choice. Many users keep their PMF projects in an Obsidian vault that syncs separately, others put them in a private git repo, others keep them local.

---

## Limitations

The honest list, from the team that built it:

1. **The skill is opinionated.** It enforces specific frameworks (Cagan's 7 dimensions, Bland's DVF, Helmer's 7 Powers, Sean Ellis 40%, First Round Levels). If you prefer a different methodology — Lean Startup canvas, Jobs-to-be-Done, etc. — the skill is not the right tool. We picked these because they compose into a working pipeline; replacing one would unravel the others.

2. **It cannot run experiments for you.** Stages 6 and 8 are explicitly outside scope. The skill writes the interview guide; you do the interviews. The skill writes the metrics dashboard; you instrument and ship the product. If you need an automated experimentation platform, look elsewhere.

3. **It assumes a single product per project folder.** A portfolio of 5 products = 5 subfolders. The skill does not coordinate cross-product analysis, shared customer segments across products, or platform-level decisions.

4. **Stage 2 is search-driven, and search has biases.** Web search returns what it returns — successful companies are over-represented, recent companies are over-represented, English-language sources are over-represented. The skill mitigates this by requiring antilogs and by adapting thresholds to market type, but the underlying bias is real.

5. **Sean Ellis is a Western-trained benchmark.** The 40% threshold was empirically derived from a sample of mostly US tech startups. Some cultures systematically give different distributions. The skill notes this but doesn't redefine the threshold.

6. **Deep tech / R&D products don't fit DVF well.** If your product is a quantum computer, a new biotech molecule, or anything where Feasibility is the dominant risk for years, the DVF framework distorts. You probably need Technology Readiness Levels instead, and Stage 4 won't give you what you need.

7. **The skill is in beta.** Edge cases are still being found. The nine stages have been tested end to end on several real products, but every new product exposes new corners. If something breaks for you, please open an issue (see the next section).

---

## How to give feedback

The skill is in beta. It works end to end but has been tested by a small number of people on a small number of products. Outside users are needed to find the rough edges. If you try the skill — even partially, even on a fake practice product, even on a single stage — tell us what happened.

**What is especially useful:**
- Where the skill's suggestions felt wrong or off the mark. Even one example helps.
- Where you got stuck and the skill could not help. Stage, state, what you tried.
- Where the skill produced something useful you did not expect.
- Whether the bilingual setup (EN/RU) worked for your language.
- Anything in the references that was inaccurate, dated, or plain wrong.

**How to share:**
- Open an issue in the [share repo](https://github.com/alenazaharovaux/share).
- Or message the maintainer via any channel you use.

The skill is adjusted based on what outside users find. The first 5–10 outside users are the most valuable feedback it can get.

---

## License

MIT — same as the rest of the share repo. Use it, fork it, change it, share it.

---

# Русская версия

## PMF — движок product-market fit

Скилл для Claude Code, который проводит один продукт через полный цикл product-market fit — от первого наброска гипотезы до метрик после запуска. Десять стадий, три версии нарратива, два языка, один непрерывный цикл.

Цикл занимает месяцы. Скилл возвращается к одним и тем же вопросам в разных формах: сначала как догадки, потом как находки исследования, потом как цитаты пользователей, потом как метрики после запуска. Сделан под такой темп: помнит, где остановились, поднимает разговор между сессиями, не торопит. Неделя на гипотезу, три недели на рыночное исследование, шесть недель на интервью, пауза в два месяца, возврат с метриками — штатная последовательность. При каждом запуске скилл читает папку проекта, определяет стадию и предлагает следующий шаг.

> **🧪 Бета — нужна обратная связь.** Скилл обкатывается на реальных продуктах. Маршрут собран от начала до конца, но каждый продукт свой, и наверняка есть места, где скилл работает хорошо, где работает неуклюже и где просто ошибается. Попробуете — расскажите, что сработало, что сломалось, что показалось странным. Issue в репозитории или сообщение мейнтейнеру. Первые 5–10 внешних пользователей — самое ценное, что сейчас можно получить.

---

## Содержание

- [Что это за скилл](#что-это-за-скилл)
- [Для кого](#для-кого)
- [Что внутри](#что-внутри)
- [Установка](#установка)
- [Первый запуск — настройка](#первый-запуск--настройка)
- [Как работает](#как-работает)
- [Десять стадий подробно](#десять-стадий-подробно)
- [Семь измерений](#семь-измерений)
- [Сквозные правила](#сквозные-правила)
- [Источники методологии](#источники-методологии)
- [Триггер-фразы](#триггер-фразы)
- [Зависимости](#зависимости)
- [FAQ](#faq-русский)
- [Ограничения](#ограничения)
- [Как оставить обратную связь](#как-оставить-обратную-связь)

---

## Что это за скилл

PMF-скилл — это один оркестратор, не набор. Одна точка входа: вы говорите «давай сделаем PMF для моего продукта», и скилл ведёт через весь цикл. Никаких вспомогательных скиллов, которые надо помнить и вызывать вручную. Все десять стадий внутри. Каждая стадия читает артефакты предыдущих и записывает свои.

Папка проекта — это и есть состояние. Скилл проверяет, какие файлы лежат в папке, и по ним определяет стадию. Нет базы данных, нет JSON-файла состояния, нет скрытого учёта. Удалили файл — стадия считается несделанной. Скопировали папку — получили полный слепок проекта. Вся система — «файлы в папке»: удобно смотреть глазами, править руками, передавать коллеге, коммитить в git.

Три принципа задают тон скилла от начала до конца.

**Спокойный тон.** Никаких восклицательных знаков, никакой драматизации. Вы делаете PMF не для того, чтобы вас подбодрили, а для того, чтобы понять, что работает и что нет. Скилл — тихий коллега, не коуч.

**Уверенность можно понижать.** Если новые данные противоречат гипотезе, скилл понижает оценку уверенности и говорит об этом прямо, а не замазывает. V2 нарратива с меньшей уверенностью, чем V1, — признак, что цикл делает свою работу. Весь маршрут построен на идее: «я знаю меньше, чем думал» — это продуктивная находка.

**Скилл не претендует на полевую работу.** Две стадии — шестая (интервью в поле) и восьмая (запуск MVP) — явно вне скилла. Скилл готовит гайд интервью и ждёт. Пишет шаблон панели метрик и ждёт. Никогда не симулирует данные пользователей, не выдумывает цитаты респондентов, не делает вид, что «запускает MVP за вас». Работа в реальном мире остаётся вне скилла.

---

## Для кого

Скилл ведёт один продукт через полный PMF-цикл силами одного ответственного — того, кто сидит в Claude Code и работает с артефактами. Размер компании за этим не стоит. Работает одинаково для:

- соло-фаундера с идеей;
- продакт-менеджера в маленькой команде;
- продакт-менеджера в крупной компании, отвечающего за один продукт или одну продуктовую линию;
- исследователя на дискавери-проекте;
- команды, где один человек ведёт цикл, а остальные читают файлы и обсуждают результаты.

Артефакты живут в папке обычными markdown-файлами. Закоммитили в git — коллеги читают те же версии, что и вы. Совместная работа построена именно так, без встроенных инструментов согласования.

Скилл **не** закрывает:
- Встроенную совместную работу. Никаких согласований, комментариев внутри артефактов, ролей, уведомлений. Если в компании это требуется — берите скилл как инструмент ведущего, а согласование выстраивайте отдельно.
- Портфельный анализ. Пять продуктов — пять отдельных папок без связей между ними. Сводную картину по нескольким продуктам придётся собирать руками.
- Замену существующего корпоративного PMF-процесса. Скилл жёсткий по методологии: Каган, Бланд, Хелмер, Шон Эллис, First Round. Если менять методологию нельзя — скилл будет с ней конфликтовать.
- Запуск MVP и управление задачами. Скилл пишет содержательные артефакты, а не ведёт доску задач в Jira или Linear.
- Презентации для инвесторов. Нарратив внутри — рабочая гипотеза, а не продающий текст для презентации о сборе денег.
- Живые интервью. Их проводите вы. Скилл делает разговор точнее: лучше гайд, лучше синтез.

---

## Что внутри

```
pmf/
├── SKILL.md                                  ← сам скилл (английская точка входа)
├── README.md                                 ← этот файл
├── config.md                                 ← настройки (язык, путь к проектам)
└── references/
    ├── en/                                   ← 23 справочных файла на английском
    └── ru/                                   ← 23 справочных файла на русском
        ├── pipeline-overview.md              ← карта маршрута, переходы между стадиями
        ├── stage-0-setup.md                  ← логика стадии 0
        ├── stage-1-hypothesis.md             ← логика стадии 1
        ├── stage-2-research.md               ← логика стадии 2
        ├── stage-3-synthesis.md              ← логика стадии 3
        ├── stage-4-validate.md               ← логика стадии 4
        ├── stage-5-interview-prep.md         ← логика стадии 5
        ├── stage-7-interview-synthesis.md    ← логика стадии 7
        ├── stage-9-metrics.md                ← логика стадии 9
        ├── 7-dimensions.md                   ← семь измерений PMF целиком
        ├── 7-powers.md                       ← семь сил Хэмилтона Хелмера
        ├── dvf-framework.md                  ← желанность / жизнеспособность / осуществимость (Дэвид Бланд)
        ├── sean-ellis-survey.md              ← порог 40%, правила распределения опросника
        ├── levels-of-pmf.md                  ← лестница First Round из четырёх уровней
        ├── narrative-writing-guide.md        ← как писать центральный нарратив
        ├── template-narrative.md             ← шаблон структурного нарратива
        ├── template-narrative-prose.md       ← шаблон прозаического нарратива
        ├── template-market-research.md       ← шаблон отчёта рыночного исследования
        ├── template-risk-prioritization.md   ← шаблон оценки рисков
        ├── template-interview-guide.md       ← шаблон гайда интервью
        ├── template-interview-note.md        ← шаблон заметки одного интервью
        ├── template-interview-synthesis.md   ← шаблон синтеза интервью
        └── template-metrics-dashboard.md     ← шаблон панели метрик
```

Сам скилл — около 480 строк в `SKILL.md`. Справочные файлы загружаются по требованию, только когда вы дошли до стадии, которой они нужны. Это держит активный контекст маленьким, хотя вся методология — больше 250 тысяч символов.

Справочники делятся на три группы.

**Логика стадий** (9 файлов: обзор маршрута плюс восемь стадий). Это операционные руководства: что читает, что пишет, проверки качества, частые ловушки. Загружаются при входе в соответствующую стадию.

**Методология** (6 файлов: семь измерений, семь сил, DVF, опросник Шона Эллиса, уровни PMF, руководство по нарративу). Справочники по фреймворкам. Загружаются, когда нужны: например, `7-powers.md` читается внутри стадии 1, когда вы доходите до измерения «Конкурентное преимущество».

**Шаблоны** (8 файлов: два шаблона нарратива, рыночное исследование, оценка рисков, гайд интервью, заметка интервью, синтез интервью, панель метрик). Это собственно заполняемые шаблоны, которые скилл копирует в папку вашего проекта. Каждый привязан к своей стадии.

---

## Установка

**macOS / Linux:**
```bash
cp -r pmf ~/.claude/skills/pmf
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse pmf $env:USERPROFILE\.claude\skills\pmf
```

После этого скилл доступен в любой сессии Claude Code. Он глобальный, не привязан к проекту.

---

## Первый запуск — настройка

При первом срабатывании скилл задаёт два вопроса и сохраняет ответы в `~/.claude/skills/pmf/config.md`. Оба можно пропустить — скилл подставит значения по умолчанию.

| Вопрос | Зачем | По умолчанию |
|---|---|---|
| **На каком языке работаем — английском или русском?** | Скилл двуязычный. У каждого языка свой набор справочников в `references/en/` или `references/ru/`. На выбранном языке скилл разговаривает с вами дальше. | `en` (английский) |
| **Где хранить PMF-проекты?** | Каждый продукт становится подпапкой. По умолчанию всё лежит в домашней директории; можно указать любую папку — документы, хранилище Obsidian, внешний диск. | `~/pmf-projects/` |

После обоих ответов скилл записывает настройки и подтверждает. Значение можно поменять в любой момент — отредактируйте `~/.claude/skills/pmf/config.md` руками. Удалили файл — скилл создаст его заново при следующем запуске и спросит снова.

Файл настроек выглядит так:
```
language: ru
projects_path: ~/pmf-projects
```

Всё. Ни переменных окружения, ни JSON, ни установочных скриптов.

---

## Как работает

При срабатывании скилл первым делом читает настройки (или задаёт вопросы, если их нет). Потом смотрит папку проектов и то, что в ней лежит. Три сценария.

1. **Новый продукт.** Скилл создаёт подпапку, запускает стадию 0 (настройку) и проводит через базу: имя, короткое обозначение, тип продукта, контекст организации, предполётный чек команды. 10–20 минут. На выходе — `00_setup.md`.

2. **Продолжение существующего продукта.** Скилл находит подпапку, смотрит на файлы внутри и определяет стадию по тому, что есть. Есть `narrative-v1.md`, но нет `market-research.md` — значит, вы между стадией 1 и стадией 2. Скилл сообщает это и спрашивает, что дальше.

3. **Несколько продуктов в работе.** Скилл перечисляет их с текущей стадией и датой последнего изменения и спрашивает, с которым работаем. Не угадывает.

Дальше скилл предлагает следующий разумный шаг и ждёт подтверждения. Вы всегда можете переопределить: «вернись к стадии 2», «дай переписать нарратив», «пропусти стадию 4 для этого измерения» — скилл переключится. Старые артефакты не удаляются. Переделали стадию 2 — получили `market-research-v2.md`, а не перезапись поверх.

Вся машина работает на факте существования файлов. Нет отдельного состояния, нет кэша в памяти. Каждая сессия — свежее чтение папки. Это звучит медленно, но именно так скилл переживает месяцы между сессиями.

---

## Десять стадий подробно

Маршрут — это один основной путь с явными нелинейными выходами. Что делает каждая стадия.

### Стадия 0 — Настройка

Короткая стадия, чтобы собрать базовый контекст до того, как вы тронете гипотезу. Собираются три вещи: тип продукта (B2C / B2B / маркетплейс / DTC / услуги / внутренний / другое), контекст организации (с нуля / зрелая / расширение) и предполётный чек команды из трёх вопросов: соответствие основателя рынку, пробелы в навыках, баланс убеждённости и гибкости.

Почему именно эти три? Потому что они формируют все следующие стадии. B2B-продукт придётся анализировать дважды — раз для покупателя, раз для пользователя. Продукт «с нуля» не может опереться на существующие каналы. Команда без соответствия основателя рынку нуждается в партнёрах, и это меняет карту рисков. Пропуск стадии 0 «чтобы сэкономить время» обычно стоит часов путаницы в стадии 1.

**На выходе:** `00_setup.md`

### Стадия 1 — Гипотеза

Первая версия центрального нарратива. Скилл проводит через семь измерений PMF, задаёт направляющие вопросы, применяет правила проверки и записывает оценку уверенности по каждому измерению.

Результат — `narrative-v1.md`: структурированный документ с одной секцией на измерение, таблицей уверенности и явной меткой «самое рискованное измерение». Оценки уверенности в V1 обычно 4–6 из 10. Если вы ставите 9–10 в V1 — это тревожный знак переоценки, и скилл его поднимет.

Для B2B и маркетплейсов скилл проходит измерения дважды — по разу на роль. Лица, принимающие решения, и конечные пользователи имеют разные проблемы и разные ценностные предложения. Проблема курицы и яйца у маркетплейсов отдельно отмечается в разделе «Стратегия роста».

Формат вывода — один из двух: структурный (лучше для внутреннего отслеживания) или прозаический (лучше для руководства и инвесторов). V1 обычно бывает только в структурном формате.

**На выходе:** `narrative-v1.md`

### Стадия 2 — Рыночное исследование

Скилл выходит из голов команды и ищет свидетельства в мире. Цель: для каждого из семи измерений найти **аналоги** (компании, успешно прошедшие это измерение в реальных условиях) и **антилоги** (известные провалы, показывающие, что ломается на этом измерении).

Метод — последовательный веб-поиск через Exa (приоритет) или WebSearch (запасной вариант). Всего 14–21 поисковый запрос, 2–3 на измерение. **Делегирование агентам здесь запрещено.** Поиск аналогов — содержательная работа, не техническая выборка, и пользователь должен видеть каждый запрос и каждый результат, чтобы вмешаться. Скилл адаптирует порог «что считать аналогом» к типу рынка: $10 млн и выше для зрелых рынков, $1 млн годового дохода и выше для развивающихся.

Результат пишется в `market-research.md` после каждого измерения, не копится в памяти до конца. Если контекст начинает переполняться, скилл разбивает работу на два захода (измерения 1–4 в одну сессию, 5–7 в другую). Это нормально для цикла в месяцы.

В конце стадии 2 — предварительный срез: какие измерения после исследования выглядят рискованными, и рекомендация для стадии 3.

**На выходе:** `market-research.md`

### Стадия 3 — Синтез

Скилл берёт V1 нарратива и материалы рыночного исследования и производит три вещи: численную оценку риска по каждому измерению, проверку согласованности между измерениями и обновлённый нарратив (V2).

**Оценка риска** использует формулу `Риск = (10 − Оценка свидетельств) × Катастрофичность провала`. Оценка свидетельств — насколько сильно данные поддерживают измерение (1–10). Катастрофичность провала — насколько страшно, если измерение окажется ошибочным (1–4, с разумными значениями по умолчанию: «Проблема» и «Бизнес-модель» = 4, «Аудитория» и «Рост» = 3, «Ценностное предложение» и «Сила» = 2). Значения по умолчанию можно перекалибровать под конкретный продукт.

**Проверка согласованности** — два обязательных теста: «Канал + модель» (работает ли канал роста с бизнес-моделью?) и «Модель + рынок» (работает ли бизнес-модель для аудитории?). Здесь часто прячутся фатальные конфликты, которые оценка риска поодиночке пропускает.

**V2 нарратива** — отдельный файл от V1, с разделом «История версий». Если уверенность по измерению упала — V2 говорит это прямо. Если измерение развернули или обнулили — скилл ставит отметку. Уверенность разрешено понижать.

В конце стадии 3 — дерево решений: высокая общая уверенность плюс одно явно рискованное измерение → стадия 4, валидируем его. Средняя уверенность → стадия 4 обязательна. Низкая → возврат к стадии 1 или стадии 2. Конфликт согласованности → возврат к стадии 1 и пересмотр конфликтующих частей.

**На выходе:** `risk-prioritization.md`, `narrative-v2.md`

### Стадия 4 — Валидация (DVF)

Самое рискованное измерение из стадии 3 разворачивается в 9 проверяемых допущений по DVF — фреймворку Дэвида Бланда: желанность × жизнеспособность × осуществимость. Три допущения на категорию, без исключений. Желанность — **только** про нужды пользователя (не про деньги, не про технику). Жизнеспособность — **только** про деньги. Осуществимость — операционная, техническая, регуляторная.

Скилл строг к терминологии. На стадиях 1–3 используется слово «гипотеза». На стадии 4 — «допущение». Фреймворк Бланда построен на том, что допущения — это конкретные проверяемые утверждения вида «я верю, что...». Смешение терминов вызывает путаницу дальше по циклу.

После того как 9 допущений написаны, скилл размещает их на матрице 2×2 по важности и свидетельствам. Критический квадрант — высокая важность плюс слабые свидетельства — это то, что тестируется первым. Скилл проектирует эксперимент для самого рискованного допущения из этого квадранта, используя один из шести стандартных типов экспериментов: глубинное интервью, дымовой тест, консьерж, опрос, прототип, посадочная страница. **Свои типы экспериментов запрещены** — «мини-пилот» и «дискавери-спринт» размытые, скилл откажется выдумывать новые. Если ни один стандартный тип не подходит — допущение переформулируется.

Бриф эксперимента включает конкретные пороги успеха и провала — не «много регистраций», а «не менее 3% посетителей посадочной страницы регистрируются на пробу», — оценку усилий и отдельную заметку о том, чего эксперимент **не** покажет.

Для продуктов из AI, финтеха и медтеха регуляторные допущения автоматически заменяют одно-два операционных или технических в «Осуществимости».

**На выходе:** `assumptions-map.md`, `experiment-brief.md`

### Стадия 5 — Подготовка интервью

На основе 2–3 самых рискованных измерений из стадии 3 скилл строит гайд интервью с пятью тематическими блоками. В каждом блоке — 5–7 открытых вопросов. Вопросы подчиняются строгим правилам: не наводящие, не про гипотетическое будущее, не про мнение пользователя о том, что он «мог бы» делать — только прошлое поведение, только конкретные ситуации.

Структура гайда: вводный сценарий, отсеивающие вопросы (2–3, поведенческие, не демографические), тематические блоки по рисковым измерениям, закрытие с просьбой о рекомендации. Каждый вопрос привязан к измерению и допущению через матрицу покрытия, так что к концу серии интервью на каждое допущение из критического квадранта стадии 4 приходится хотя бы один вопрос.

Скилл рекомендует минимум 15 интервью, оптимум — 20–30. Дополнительно создаётся `note-template.md` — структурированный формат, который пользователь копирует для каждого интервью в поле.

**На выходе:** `interview-guide.md`, `interviews/note-template.md`, пустая папка `interviews/notes/`

### Стадия 6 — Полевые интервью (вне скилла)

Это **состояние ожидания**. Скилл не проводит интервью. Только готовит гайд и потом обрабатывает заметки. Когда вы возвращаетесь на эту стадию, скилл сообщает, что гайд готов, спрашивает, сколько интервью проведено, и ждёт.

Пользователь делает полевую работу неделями или месяцами. Каждое интервью становится заметкой в `interviews/notes/` в формате из шаблона. С одной заметкой скилл уже даст перейти на стадию 7, но 15 и больше — рекомендованный минимум для осмысленного синтеза.

### Стадия 7 — Синтез интервью

Скилл читает все заметки интервью **по одной**, не пакетом, чтобы не усреднить паттерны, и извлекает находки по каждому измерению. На каждое измерение производит: паттерн (что говорят), количество подтверждений (N из M респондентов), 2–3 ключевые цитаты дословно, изменение уверенности (V2 → V3), тип обновления (подтверждено / уточнение / разворот / сброс).

Отдельно вытаскивает **межизмеренческие находки** — паттерны, которые проходят через несколько измерений, — и **сюрпризы**: то, что противоречит гипотезе. Сюрпризы часто самое ценное во всём цикле. Если их нет — скилл помечает возможное подтверждающее искажение и просит перечитать заметки.

Результат — `interview-synthesis.md` и третья версия нарратива, `narrative-v3.md`. V3 переписан на языке пользователей, с прямыми цитатами, более узкими персонами и обновлёнными рисками. Если уверенность по какому-то измерению упала между V2 и V3, скилл помечает это и рекомендует: больше валидации, возврат к рыночному исследованию или разворот.

**На выходе:** `interview-synthesis.md`, `narrative-v3.md`

### Стадия 8 — Запуск MVP (вне скилла)

Ещё одно состояние ожидания. Нарратив валидирован настолько, насколько это позволяют слова. Дальше нужно что-то построить и поставить перед реальными пользователями. При возврате на эту стадию скилл подтверждает, что нарратив готов, и напоминает прийти на стадию 9, когда наберётся около 40 активных пользователей.

На этой стадии скилл можно использовать как собеседника: обсудить объём работ, фичи MVP, целевую аудиторию запуска. Но запускать продукт за вас он не будет.

### Стадия 9 — Метрики

Измерение после запуска через три инструмента, используемых вместе.

**Опросник Шона Эллиса, порог 40%.** Один вопрос — *«Как бы вы себя чувствовали, если бы больше не могли пользоваться [продуктом]?»* — с четырьмя вариантами ответа. Порог: не менее 40% «Очень разочарован» (исключая «не пользуюсь») = PMF. Минимум 40 ответов, рассылать только активным пользователям — не по общей рассылке, не по вручную отобранным топ-клиентам. Скилл генерирует текст вопроса и инструкции по рассылке, но данные не собирает.

**Когорты удержания.** Таблица когорт: неделя регистрации × процент пользователей, вернувшихся в неделю 1, 2, 3, 4, 8, 12. Определение «активный» калибруется под тип продукта. Сигнал PMF: кривая выравнивается на здоровом уровне, а не падает в ноль. Порог сильного PMF: больше 40% для потребительского, больше 60% для B2B, больше 25% для высокочастотного использования. Скилл создаёт шаблон таблицы и инструкции по сбору данных.

**Уровни PMF от First Round.** Лестница из четырёх уровней — зарождающийся / развивающийся / сильный / экстремальный — оценивается по трём измерениям: удовлетворённость, спрос, эффективность. Общий уровень равен **минимуму** из трёх, а не среднему. Команда не может быть «сильной» по удовлетворённости и «зарождающейся» по эффективности одновременно — это рассогласование и есть узкое место.

Стадия 9 разворачивается в три фазы: фаза настройки (создаётся шаблон панели метрик), фаза сбора длиной 4–12 недель (пользователь собирает данные сам), фаза интерпретации (пользователь возвращается с заполненной панелью, скилл рекомендует, что делать в стадии 10).

**На выходе:** `metrics-dashboard.md`

### Стадия 10 — Итерация

По метрикам принимается решение, что дальше.

- **Шон Эллис не меньше 40% + удержание выравнивается + уровень 3 или выше** → PMF достигнут. Скилл выходит — масштабирование вне его области.
- **Шон Эллис 25–40% + частичное выравнивание удержания + уровень 2** → итерация. Возврат к стадии 4 (валидировать следующее рискованное допущение) или к стадии 7 (новый раунд интервью, сфокусированный на сегменте «немного разочарован»).
- **Шон Эллис меньше 25% + падающее удержание + уровень 1** → разворот. Возврат к стадии 1 с явным обоснованием, какое измерение провалилось.

На выходе — `iteration-changelog.md`. После его записи автозапуск скилла снова читает папку и предлагает следующую стадию исходя из нового состояния. Цикл продолжается.

**На выходе:** `iteration-changelog.md`

---

## Семь измерений

Каждая стадия цикла возвращается к этим семи измерениям. Они не независимы — сильные гипотезы показывают, как измерения усиливают друг друга. Полное описание скилл загружает из `references/<язык>/7-dimensions.md` при входе в стадию 1. Короткая версия ниже.

| # | Измерение | Вопрос | Чего опасаться |
|---|---|---|---|
| 1 | **Проблема** | Какого результата пытаются добиться пользователи и что им мешает? | Проблемы в терминах решения («у них нет нашего инструмента»). Абстрактные проблемы («хотят эффективности»). |
| 2 | **Аудитория** | Кто конкретно и почему именно они сейчас (а не те, кто потом)? | Только демографические персоны. «Все малые бизнесы». Текущий сегмент = будущий сегмент. |
| 3 | **Ценностное предложение** | Какая одна выгода на их языке бьёт сильнее всего? | Функции вместо выгод. Общие заявления. Несколько конкурирующих слоганов. |
| 4 | **Конкурентное преимущество** | Какая из семи сил Хелмера — ваш долгосрочный защитный ров? | «Лучшая команда», «первые на рынке», «уникальная технология» — ни одно не сила. |
| 5 | **Стратегия роста** | Как получаете первую тысячу пользователей и как доходите до ста тысяч? | Один и тот же канал для обоих горизонтов. «Станем вирусными» без механизма. |
| 6 | **Бизнес-модель** | Какое у вас уравнение и согласовано ли оно с аудиторией и каналом? | «Будет реклама / фримиум / премиум» без чисел. Цены, скопированные у конкурента. |
| 7 | **Время / почему сейчас** | Какой конкретный сдвиг сделал это возможным или нужным за последние 1–3 года? | «Нам кажется, время пришло». «Хайп вокруг AI». Размытое «рынок созрел». |

Восьмое половинное измерение — «защищённость» — часть конкурентного преимущества. Проверяется отдельно на стадии 1 и снова на стадии 9, когда есть метрики.

---

## Сквозные правила

Через весь цикл проходит несколько скучных, но несущих правил.

**Версионирование нарратива.** V1, V2 и V3 — **отдельные файлы**, никогда не перезапись. В каждой новой версии есть раздел «История версий», объясняющий, что изменилось и почему. Смысл — сделать эволюцию понимания видимой. Разница между V1 и V3 часто самый полезный артефакт всего цикла.

**Уверенность можно понижать.** Если данные противоречат гипотезе, скилл снижает оценку уверенности и говорит это прямо. V3 с меньшей уверенностью, чем V2, — признак, что цикл работает. Накручивание чисел ради приятного ощущения — самый частый тип провала в самостоятельной PMF-работе, и скилл построен так, чтобы этому сопротивляться.

**Обнаружение циклов.** Если уверенность по одному и тому же измерению падает версия за версией, скилл помечает возможный цикл и рекомендует одно из трёх: больше валидации, возврат к исследованию, разворот. Не даст бесконечно крутить «интервью → небольшая правка → ещё интервью» без явного поднятия паттерна.

**Возврат назад — полноценная операция.** Пользователь в любой момент может сказать «вернись к стадии 2» — скилл переключится. Старые артефакты не удаляются. Переделали стадию 2 — появится `market-research-v2.md` рядом с оригиналом. Папка растёт со временем.

**Между сессиями скилл всё перечитывает.** Памяти о том, «что мы делали в прошлый раз», он не доверяет. На каждом возобновлении автозапуск заново сканирует папку и определяет состояние. Это позволяет циклу длиной в месяцы пережить много коротких сессий.

**Никакого делегирования агентам для содержательной работы.** Стадия 2 (рыночное исследование) и стадия 7 (синтез интервью) делаются в основной сессии, не через агентов. Исследование — содержательная работа: пользователь должен видеть каждый поисковый запрос и каждую цитату, чтобы вмешаться. Синтез требует чтения заметок по одной в изоляции, а агент усреднит паттерны. Это жёсткое правило.

**Скилл никогда не выдумывает данные.** Не симулирует цитаты интервью, не генерирует фальшивые метрики, не допускает «а давайте представим, что Шон Эллис равен 47%». Где данных нет, скилл говорит «данных ещё нет» и просит собрать.

---

## Источники методологии

Скилл построен на нескольких устоявшихся фреймворках. Если есть время прочитать по одной вещи у каждого — вот с чего начать.

- **Марти Каган — «Empowered» и «Inspired».** Разбиение на семь измерений (с временем как седьмым) опирается на работу Кагана по продуктовому дискавери. Его настойчивое требование формулировать проблему независимо от решения лежит в основе правил проверки в стадии 1.

- **Дэвид Бланд и Алекс Остервальдер — «Testing Business Ideas» (2019, Strategyzer).** Фреймворк DVF, 9 допущений, матрица 2×2 «важность × свидетельства» и шесть стандартных типов экспериментов в стадии 4 — всё из этой книги. Строгое разделение «допущение» и «гипотеза» у Бланда сохранено.

- **Хэмилтон Хелмер — «7 Powers: The Foundations of Business Strategy».** Измерение конкурентного преимущества использует семь сил Хелмера (эффект масштаба, сетевые эффекты, контр-позиционирование, издержки переключения, бренд, уникальный ресурс, операционная сила) как единственно приемлемые ответы. «У нас отличная команда» в списке нет, и скилл это скажет.

- **Шон Эллис — опросник 40%.** Опубликован в 2009 как ответ на вопрос «как понять, что у нас есть PMF?». Порог 40% эмпирический, не теоретический. Эллис собрал данные примерно со 100 стартапов, которые консультировал, и увидел, что у тех, где не меньше 40% «очень разочарованы», платный маркетинг работает с положительной экономикой.

- **First Round Capital — «The Levels of Product/Market Fit (& What to Focus on at Each)».** Тодд Джексон, Брайан Ротенберг, Кэролайн Стайн. Лестница из четырёх уровней — зарождающийся / развивающийся / сильный / экстремальный — и сетка оценки по трём измерениям (удовлетворённость × спрос × эффективность) взяты из этой статьи в First Round Review.

- **Билл Гросс — TED-доклад про главный фактор успеха стартапов.** После анализа более 200 компаний Гросс нашёл, что время — самый сильный предиктор успеха: важнее команды, идеи, бизнес-модели и финансирования. Поэтому «время / почему сейчас» включено в семёрку наравне с «проблемой» и «аудиторией».

- **Рахул Вора — «How Superhuman Built an Engine to Find Product/Market Fit».** Опубликовано в First Round Review. Расширяет подход Эллиса в полноценный процесс: выделить сегмент «очень разочарованных», понять, что они ценят, перестроить продукт вокруг них, повторить. Эта петля и реализована в стадиях 9 ↔ 10.

- **gnurio/pmf-plugin.** Идея разбиения цикла на примерно десять последовательных стадий с автоопределением состояния из папки заимствована у этого плагина. Измерения, методологии и проверки качества внутри другие, но сама форма оркестрации — его заслуга.

---

## Триггер-фразы

Скилл срабатывает на естественный язык, на русском или английском. Что-то в этой грубой форме сработает.

**Русский:**
- «сделай PMF для [продукта]»
- «нужен product market fit для X»
- «PMF [имя]»
- «запусти PMF-цикл»
- «хочу пройти PMF»
- «помоги валидировать [идею]»
- «продолжаем PMF»
- «продолжай PMF [имя]»
- «проверь PMF»
- «на какой стадии у меня PMF»
- «покажи мои PMF-проекты»
- «готов ли мой продукт к запуску»

**Английский:**
- «do PMF for [product name]»
- «I need product market fit for X»
- «PMF [name]»
- «start a PMF cycle»
- «continue PMF»
- «what stage is my PMF at»

Скилл также старается поймать любое сообщение, где вы упомянули продукт и хотите его систематически валидировать, даже если слова «PMF» там нет.

---

## Зависимости

**Обязательно:**
- Claude Code (это скилл под Claude Code)
- WebSearch (встроен в Claude Code)

**Необязательно, но рекомендуется:**
- **Exa MCP** для рыночного исследования в стадии 2. Скилл предпочитает `mcp__exa__web_search_exa`, потому что смысловой поиск Exa заметно лучше находит аналоги и антилоги по описанию проблемы, а не только по ключевым словам. Если Exa не установлен, скилл автоматически переходит на WebSearch. Стадия 2 продолжит работать, просто поиск станет более буквальным.

Установка Exa MCP — см. [документацию Exa MCP](https://github.com/exa-labs/exa-mcp-server). Не хотите настраивать — пропустите, скилл обойдётся WebSearch.

**Не нужно:**
- Никаких библиотек Python
- Никаких внешних API, кроме поисковых выше
- Никакой базы данных
- Никаких учётных записей или ключей

---

## FAQ (русский)

**В: Сколько занимает PMF-цикл с этим скиллом?**

Полный цикл (стадии 0–10) — месяцы, не дни. Реалистичные оценки: стадия 0 — 10–20 минут; стадия 1 — 1–3 сессии по часу; стадия 2 — 1–2 дня сосредоточенной работы; стадия 3 — полдня; стадия 4 — полдня на допущения плюс время на сам эксперимент; стадия 5 — полдня; стадия 6 (полевые интервью) — **недели**, 15–25 интервью, которые пользователь планирует и проводит сам; стадия 7 — полдня-день; стадия 8 (запуск MVP) — **недели или месяцы**; стадия 9 требует минимум 4 недели сбора данных; стадия 10 — одна сессия. Скилл работает под такой темп и возобновляется между сессиями.

**В: Можно ли пропустить стадию?**

Можно, но скилл предупредит. Некоторые пропуски разумны — например, пропустить стадию 4, если уверенность в стадии 3 высокая и самое рискованное измерение лучше валидируется через интервью напрямую. Другие пропуски — тревожный знак. Желание прыгнуть сразу на стадию 9 обычно значит: вы надеетесь, что метрики скажут то, чего не сказала гипотеза. Шон Эллис на случайной аудитории даст случайный результат. Ранние стадии существуют, чтобы метрика стала осмысленной.

**В: Что если продукт многосторонний (маркетплейс) или с несколькими персонами (B2B)?**

Скилл обрабатывает это в стадии 1 через прохождение ролей по очереди. Для B2B вы проходите семь измерений дважды — по разу для лиц, принимающих решения (кто платит), и конечных пользователей (кто пользуется). Для маркетплейсов — дважды, по разу на каждую сторону, с явной пометкой проблемы курицы и яйца в «Стратегии роста». Обе роли лежат в одном `narrative-v1.md` отдельными секциями.

**В: Мой продукт уже запущен. Можно начать с середины?**

Да. Создаёте папку проекта, кладёте существующие данные в соответствующие файлы артефактов (например, готовую презентацию для инвесторов → `narrative-v1.md`), и скилл определит стадию и предложит, куда дальше. В начале со стадии 0 нет ничего магического. Автозапуск принимает за текущее состояние те артефакты, которые лежат в папке.

**В: Моя команда использует другую терминологию — можно переименовать?**

Скилл жёсток к нескольким терминам, у которых есть методологический вес: «допущение» и «гипотеза» в стадии 4 (разделение Бланда важно) и четыре варианта ответа Шона Эллиса, которые должны быть в оригинальной формулировке. Всё остальное можно переименовать в своём нарративе как угодно — шаблоны просто предлагают удобную отправную точку.

**В: Это замена разговорам с пользователями?**

Нет. Стадия 6 явно не может быть сделана скиллом. Весь цикл построен на том, что вы разговариваете с реальными людьми. Задача скилла — сделать разговоры полезнее (лучший гайд, лучший синтез) и окружающую структуру честнее (гипотеза, исследование, оценка рисков, метрики).

**В: Что если я не знаю, мой продукт B2C или B2B?**

В стадии 0 есть разрешающий вопрос: кто реально платит — конечный пользователь или его компания? Это и есть тип. Если ни одно не очевидно, продукт, скорее всего, ещё не готов к PMF-анализу: сначала выберите целевой рынок.

**В: Скилл коммитит файлы проекта в git?**

Нет. Скилл создаёт файлы в вашей папке проектов, и всё. Коммитить, шарить, делать резервные копии — ваш выбор. Кто-то держит PMF-проекты в хранилище Obsidian со своей синхронизацией, кто-то в приватном git-репозитории, кто-то локально.

---

## Ограничения

Честный список от команды, которая это построила.

1. **Скилл с мнением.** Он требует конкретные фреймворки: семь измерений Кагана, DVF Бланда, семь сил Хелмера, порог 40% Шона Эллиса, уровни First Round. Если вам ближе другая методология — канвас Lean Startup, Jobs-to-be-Done и так далее — это не тот инструмент. Мы выбрали эти фреймворки, потому что они собираются в работающий цикл; замена одного развалит остальные.

2. **Не умеет проводить эксперименты за вас.** Стадии 6 и 8 явно вне области. Скилл пишет гайд — интервью проводите вы. Скилл пишет панель метрик — ставите её и выкатываете продукт вы. Если нужна автоматизированная платформа для экспериментов — ищите в другом месте.

3. **Один продукт на папку.** Портфель из пяти продуктов — это пять подпапок. Скилл не координирует межпродуктовый анализ, общие сегменты клиентов между продуктами или решения на уровне платформы.

4. **Стадия 2 работает на поиске, а у поиска есть искажения.** Веб-поиск возвращает то, что возвращает: успешные компании представлены чаще, свежие чаще, англоязычные источники чаще. Скилл смягчает это требованием искать антилоги и адаптацией порогов под тип рынка, но базовое искажение реально.

5. **Шон Эллис — западный эталон.** Порог 40% эмпирически выведен из выборки в основном американских технологических стартапов. Некоторые культуры системно дают другие распределения. Скилл это отмечает, но порог не переопределяет.

6. **Глубокотехнические и R&D-продукты плохо вписываются в DVF.** Если ваш продукт — квантовый компьютер, новая биотехнологическая молекула или что-то ещё, где осуществимость остаётся доминирующим риском годами, фреймворк DVF искажает картину. Вам скорее нужны уровни готовности технологии, и стадия 4 не даст того, что нужно.

7. **Скилл в бете.** Крайние случаи ещё находятся. Девять стадий протестированы от начала до конца на нескольких реальных продуктах, но каждый новый продукт вскрывает новые углы. Если что-то сломалось — откройте issue (см. следующий раздел).

---

## Как оставить обратную связь

Скилл в бете. Он работает от начала до конца, но его пробовало немного людей на небольшом числе продуктов. Нужны внешние пользователи, чтобы найти острые углы. Попробовали скилл — даже частично, даже на выдуманном тренировочном продукте, даже на одной стадии — расскажите, что получилось.

**Что особенно полезно:**
- Где предложения скилла показались неправильными или мимо. Даже один пример помогает.
- Где вы застряли и скилл не помог. Стадия, состояние, что пробовали.
- Где скилл выдал что-то полезное, чего вы не ждали.
- Сработала ли двуязычная пара EN/RU для вашего языка.
- Что в справочниках было неточным, устаревшим или просто ошибочным.

**Как поделиться:**
- Открыть issue в [репозитории share](https://github.com/alenazaharovaux/share).
- Написать мейнтейнеру любым удобным каналом.

Скилл правится по тому, что находят внешние пользователи. Первые 5–10 из них — самая ценная обратная связь, которую он может получить.

---

## Лицензия

MIT — как и весь репозиторий share. Используйте, форкайте, меняйте, делитесь.
