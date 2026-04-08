# PMF — Product-Market Fit Engine

A Claude Code skill that walks one product through a full product-market fit cycle, from a first sketch of the hypothesis all the way to post-launch metrics. Ten stages, three artifact versions, two languages, one continuous loop.

A PMF cycle takes months. It comes back to the same questions in different forms — first as guesswork, then as research findings, then as user quotes, then as launch metrics. This skill is designed for that pace. It remembers where you left off, picks up the conversation between sessions, and refuses to rush. You can spend a week on the hypothesis, three weeks on market research, six weeks running interviews, and then come back two months later with metrics. The skill will know what state your project is in by reading the folder, and will tell you the next reasonable step.

> **🧪 Beta — feedback wanted.** This skill is still being shaken down on real products. The pipeline holds together end to end, but every product is its own beast and there are bound to be places where the skill works well, places where it's awkward, and places where it's just wrong. If you try it, please tell us what worked, what broke, and what felt off — open an issue or drop a note in the share repo. We will adjust the skill based on what you find. The first 5–10 outside users are probably the most valuable thing we can get right now.

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

The PMF skill is **one orchestrator, not a bundle**. There is one entry point — you say something like "let's do PMF for my new product" — and the skill takes you through the whole cycle without you having to remember which sub-skill to call next. All ten stages live inside it. Each stage reads the artifacts of the previous stages and writes its own.

The project folder is the state machine. The skill checks which files exist in the folder and figures out which stage you are on. There is no separate database, no JSON state file, no hidden bookkeeping. If you delete a file, the skill thinks the corresponding stage is undone. If you copy a folder, you have a full snapshot of the project. The whole system is "files in a folder", which makes it easy to inspect, edit by hand, share with a teammate, or commit to git.

Three principles shape the skill from end to end:

**Calm tone.** No exclamation marks, no dramatization. You are not doing PMF to get cheered on — you are doing it to find out what actually works and what does not. The skill is supposed to be a quiet collaborator, not a coach.

**Confidence is allowed to drop.** This is the part most teams get wrong. If new data contradicts the hypothesis, the skill will drop the confidence score and say so explicitly instead of papering over it. A V2 narrative with lower confidence than V1 means the cycle is doing its job. The whole pipeline is built around the idea that "I know less than I thought" is a productive finding.

**The skill does not pretend to do field work.** Two stages — Stage 6 (Field Interviews) and Stage 8 (MVP Launch) — are explicitly **outside** the skill. The skill prepares the interview guide and waits. It writes the metrics dashboard template and waits. It never simulates user data, never invents respondent quotes, never pretends to "run the MVP for you." The work that happens in the real world stays in the real world.

---

## Who it's for

This skill exists for the person who is sitting on a product idea, or is a few months into building something, and is suddenly asking "do I actually have product-market fit, or am I just busy?" It is for solo founders, product managers, indie hackers, researchers running a discovery project, and small teams who want a structured second opinion without paying $50K for a consultant.

It is **not** for:
- Pure pitch decks (this is a discovery tool, not a fundraising deck builder)
- Marketing copy (the narratives produced here are honest hypotheses, not landing-page copy)
- Auto-launching MVPs (the skill stops at the door of the real world — it does not deploy code, run ads, or message your users)
- Replacing user research (you still have to talk to humans; the skill makes the talking more useful)

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

The skill itself is ~480 lines in `SKILL.md`. The references are loaded on demand — only when you actually reach the stage that needs them. This keeps the active context small even though the full methodology is over 250K characters of text.

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

When you trigger the skill, the very first thing it does is read your config (or ask the setup questions if there is no config yet). Then it lists the projects folder and looks at what's there. Three things can happen:

1. **You're starting a brand-new product.** The skill creates a new subfolder, runs Stage 0 (Setup), and walks you through the basics: name, slug, product type, organizational context, team pre-flight check. About 10–20 minutes. The output is `00_setup.md`.

2. **You're continuing an existing product.** The skill finds your subfolder, looks at the files inside it, and figures out which stage you're on by file presence. If `narrative-v1.md` exists but no `market-research.md`, you're between Stage 1 and Stage 2. The skill tells you exactly that and asks what to do next.

3. **You have several products in flight.** The skill lists them with their current stage and last-updated date, and asks which one you want to work on. It does not assume.

After that the skill proposes the next reasonable step and waits for your confirmation. You can always override — say "go back to Stage 2", "let me redo the narrative", "skip Stage 4 for this dimension" — and the skill will switch. Old artifacts are never deleted. If you redo Stage 2 you get `market-research-v2.md`, not an overwrite.

The whole machine runs on file presence — no separate state, no in-memory cache. Every session is a fresh read of the folder. This sounds slow, but it is what makes the skill survive months between sessions.

---

## The 10 stages in depth

The pipeline is one happy path with explicit non-linear escapes. Here is what each stage actually does.

### Stage 0 — Setup

A short stage to gather basic context before you touch the hypothesis. Three things are collected: product type (B2C / B2B / Marketplace / DTC / Services / Internal / Other), organizational context (Zero-to-one / Established / Extension), and a team Pre-Flight Check (3 questions: founder-market fit, skill gaps, conviction-flexibility).

Why these three? Because they shape every later stage. A B2B product needs to be analyzed twice — once for the buyer, once for the user. A zero-to-one product cannot lean on existing channels. A team with no founder-market fit needs partners, and that affects the risk map. Skipping Stage 0 to "save time" usually costs hours of confusion in Stage 1.

**Output:** `00_setup.md`

### Stage 1 — Hypothesis

The first version of the central narrative. The skill walks you through 7 PMF dimensions, asking guided questions, applying validation rules, and recording confidence scores for each.

The output is `narrative-v1.md` — a structured document with one section per dimension, a confidence table, and an explicit "riskiest dimension" mark. Confidence scores in V1 are usually 4–6 out of 10 for most dimensions; if you find yourself writing 9–10 in V1, that's a red flag for overconfidence and the skill will flag it.

For B2B and Marketplace products, the skill goes through the dimensions twice — once per role. Decision Makers and End Users have different problems and different value props. The chicken-and-egg side of marketplaces is called out explicitly in Growth Strategy.

You can pick between two output formats — structured (better for internal tracking) or prose (better for stakeholders). V1 is usually structured only.

**Output:** `narrative-v1.md`

### Stage 2 — Market Research

Now the skill leaves the team's heads and goes looking for evidence in the world. The goal: for each of the 7 dimensions, find **analogs** (companies that successfully validated this dimension under real conditions) and **antilogs** (known failures that show what breaks on this dimension).

The method is sequential web search via Exa (preferred) or WebSearch (fallback). 14–21 searches total — 2–3 per dimension. **Subagents are explicitly forbidden** here. Researching analogs is content work, not file lookup, and the user has to see every search and every result so they can intervene. The skill also adapts the "what counts as an analog" threshold to the market type: $10M+ for mature markets, $1M+ ARR for emerging ones.

The output is written into `market-research.md` after each dimension, not held in memory until the end. If the context starts overflowing, the skill splits the work into two passes (dimensions 1–4 in one session, 5–7 in the next). This is normal for a months-long cycle.

The end of Stage 2 includes a "preview" of which dimensions look risky after the research, and a recommendation for Stage 3.

**Output:** `market-research.md`

### Stage 3 — Synthesis

The skill takes the V1 narrative and the market research and produces three things: a numerical risk score per dimension, a cross-fit analysis, and an updated narrative (V2).

**Risk scoring** uses the formula `Risk Score = (10 - Evidence Score) × Failure Impact`. Evidence Score is how strongly the data supports the dimension (1–10). Failure Impact is how catastrophic it would be if this dimension turned out to be wrong (1–4, with sensible defaults — Problem and Business Model are 4, Audience and Growth are 3, Value Prop and Power are 2). The default impacts can be recalibrated for the specific product.

**Cross-fit analysis** is two mandatory consistency checks: Channel-Model Fit (does the growth channel work with the business model?) and Model-Market Fit (does the business model work for the audience?). These often hide fatal conflicts that scoring alone misses.

**V2 narrative** is a separate file from V1, with a Version History changelog. If a dimension's confidence dropped, V2 says so explicitly. If a dimension was pivoted or reset, the skill marks it. Confidence is allowed to go down — that is the whole point.

The end of Stage 3 includes a decision tree: high overall confidence + a clear riskiest dimension → go to Stage 4 to validate it. Mid confidence → Stage 4 is mandatory. Low confidence → return to Stage 1 or Stage 2. Cross-fit conflicts → return to Stage 1 to rethink the conflicting pieces.

**Outputs:** `risk-prioritization.md`, `narrative-v2.md`

### Stage 4 — Validate (DVF)

The riskiest dimension from Stage 3 gets unfolded into 9 testable assumptions across DVF — David Bland's Desirability × Viability × Feasibility framework. Three assumptions per category, no exceptions. Desirability is *only* about user needs (no money, no tech). Viability is *only* about money. Feasibility is operational + technical + regulatory.

The skill is strict about terminology here. In stages 1–3 it uses "hypothesis." In Stage 4 it switches to "assumption." Bland's framework is built around assumptions being concrete, testable "I believe..." statements, and mixing the two terms causes real confusion.

After the 9 assumptions are written, the skill places them on a 2×2 of importance × evidence. The Critical quadrant — high importance, weak evidence — is what gets tested first. The skill then designs an experiment for the riskiest assumption from this quadrant, using one of 6 standard experiment types: Customer Interview, Smoke Test, Concierge, Survey, Prototype, Landing Page. **Custom experiment types are forbidden** — "mini-pilot" and "discovery sprint" are vague and the skill will refuse to invent new ones. If nothing fits, the assumption gets reframed.

The experiment brief includes concrete success and failure thresholds (not "lots of sign-ups" but "≥3% landing → trial sign-up"), estimated effort, and a note on what the experiment will *not* show.

For AI / fintech / healthtech products, regulatory assumptions automatically replace one or two operational/technical ones in Feasibility.

**Outputs:** `assumptions-map.md`, `experiment-brief.md`

### Stage 5 — Interview Prep

Now the skill prepares the field. Based on the 2–3 riskiest dimensions from Stage 3, it builds an interview guide with five thematic blocks. Each block has 5–7 open questions. The questions follow strict rules: no leading, no hypothetical futures, no opinions about what people might do — only past behavior, only concrete situations.

The guide is structured: introduction script, screening questions (2–3, behavioral not demographic), thematic blocks per risk-dimension, closing with a referral request. Every question is mapped to a dimension and an assumption in a coverage matrix, so by the end of the interview cycle every Critical-quadrant assumption from Stage 4 has at least one question pointed at it.

The skill recommends 15+ interviews as a minimum, with 20–30 as the sweet spot. It also creates a `note-template.md` — the structured format the user will copy for each interview during the field.

**Outputs:** `interview-guide.md`, `interviews/note-template.md`, empty `interviews/notes/` folder

### Stage 6 — Field Interviews (outside the skill)

This is a **waiting state**. The skill cannot conduct interviews. It can only prepare the guide and then process the notes. When you resume the skill on this stage, it tells you the guide is ready, asks how many interviews you've done, and waits.

The user does the field work over weeks or months. Each interview becomes a note in `interviews/notes/`, written in the structured format from the template. With at least one note in the folder the skill will let you move to Stage 7, but 15+ is the recommended minimum for meaningful synthesis.

### Stage 7 — Interview Synthesis

The skill reads all the interview notes — **one at a time**, not batched, to avoid averaging out the patterns — and extracts findings per dimension. For each dimension it produces: pattern (what they say), supporting evidence count (N out of M respondents), 2–3 verbatim key quotes, confidence change (V2 → V3), and an update type (Validated / Refinement / Pivot / Reset).

It also pulls out **cross-dimensional insights** (patterns that span multiple dimensions) and **surprises** (findings that contradict the hypothesis). Surprises are often the most valuable thing in the whole pipeline — if you find none, the skill flags possible confirmation bias and asks you to re-read the notes.

The result is `interview-synthesis.md` and a third version of the narrative — `narrative-v3.md`. V3 is rewritten in user language, with real quotes, narrower personas, and updated risks. If confidence dropped on any dimension between V2 and V3, the skill flags it and recommends what to do next: more validation, return to research, or a pivot.

**Outputs:** `interview-synthesis.md`, `narrative-v3.md`

### Stage 8 — MVP Launch (outside the skill)

Another waiting state. The narrative is validated as far as words can take you. Now you have to build something and put it in front of real users. The skill stops at the door. When you resume it on this stage, it confirms the narrative is ready and reminds you to come back for Stage 9 once you have ~40 active users.

You can use the skill as a sounding board during this stage — discussing scope, MVP features, target audience for the launch — but it will not "launch the MVP for you."

### Stage 9 — Metrics

Post-launch measurement, set up through three instruments used together:

**Sean Ellis 40% Survey.** One question — *"How would you feel if you could no longer use [product]?"* — with four answer options. The threshold is ≥40% "Very disappointed" (excluding N/A) = PMF. Minimum 40 responses, distributed only to active users (not the newsletter list, not cherry-picked top customers). The skill generates the question text and the distribution instructions but does NOT collect data itself.

**Retention Cohorts.** A cohort table (signup week × percent of users returning in week 1, 2, 3, 4, 8, 12), with the definition of "active" calibrated to the product type. PMF signal: the curve flattens at a healthy level, instead of falling to zero. Strong PMF threshold is >40% for consumer, >60% for B2B, >25% for high-frequency. The skill creates the table template and the data-collection instructions.

**First Round Levels of PMF.** A 4-level ladder — Nascent / Developing / Strong / Extreme — assessed across three dimensions (Satisfaction, Demand, Efficiency). The overall level is the *minimum* of the three, not the average. A team cannot be Strong on Satisfaction and Nascent on Efficiency at the same time — that mismatch is the bottleneck.

Stage 9 unfolds across two real sessions: a setup phase where the dashboard template is created, then a collection phase of 4–12 weeks where the user gathers the data on their own, then an interpretation phase where the user comes back with the filled dashboard and the skill recommends what to do in Stage 10.

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

A few rules cut across the whole pipeline. They are the boring but load-bearing parts.

**Narrative versioning.** V1, V2, and V3 are **separate files**, never overwrites. Each new version has a Version History section explaining what changed and why. The point is to make the evolution of understanding visible — looking at the diff between V1 and V3 is often the most useful artifact of the whole cycle.

**Confidence can decrease.** If the data contradicts the hypothesis, the skill will lower the confidence score and say so. A V3 with lower confidence than V2 is a sign the cycle is working. Inflating numbers to feel better is the most common failure mode of self-driven PMF work, and the skill is designed to push back against it.

**Loop detection.** If the same dimension's confidence keeps dropping across versions, the skill flags a possible loop and recommends one of three actions: more validation, return to research, or a pivot. It will not let you run an infinite cycle of "interviews → small refinement → more interviews" without surfacing the pattern.

**Going back is a first-class operation.** The user can say "go back to Stage 2" at any time and the skill switches. Old artifacts are not deleted. If you redo Stage 2 you get `market-research-v2.md` next to the original. The folder grows over time and that is the point.

**Between sessions, the skill re-reads everything.** It does not trust memory of "what we did last time." On every resume, auto-start scans the folder fresh and figures out the state. This is what makes a months-long cycle survive across many short sessions.

**No subagents for content work.** Stage 2 (research) and Stage 7 (synthesis) are done in the main session, not delegated. Research is content work — the user has to see every search and every quote so they can intervene. Synthesis requires reading interview notes one at a time in isolation, and a subagent would average the patterns. This is enforced as a hard rule.

**The skill never invents data.** It will not simulate interview quotes, will not generate fake metrics, will not assume "let's say Sean Ellis is 47%." Where data is missing, the skill says "no data yet" and asks the user to collect it.

---

## Methodology sources

This skill stands on the shoulders of better thinkers. If you only have time to read one thing from each, here's where to start.

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

The skill is designed to fire on natural language in either English or Russian. Anything in this rough shape will work:

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

A full cycle (Stage 0 through Stage 10) is months, not days. Realistic ranges: Stage 0 is 10–20 minutes. Stage 1 is 1–3 sessions of an hour each. Stage 2 (research) is 1–2 days of focused work. Stage 3 (synthesis) is half a day. Stage 4 (DVF) is half a day for the assumptions + however long the experiment takes. Stage 5 (interview prep) is half a day. Stage 6 (field interviews) is **weeks** — 15–25 interviews, scheduled and conducted by the user. Stage 7 (synthesis) is half a day to a day. Stage 8 (MVP launch) is **weeks to months**. Stage 9 (metrics) needs at least 4 weeks of data collection. Stage 10 is one session. The skill is designed for that pace and resumes between sessions.

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

7. **The skill is in beta.** Edge cases are still being found. The 9 stages have been tested end-to-end on multiple real products, but every product is its own beast. If something breaks for you, please open an issue (see the next section).

---

## How to give feedback

This is the most important section in the README, and it's at the bottom because we want the rest to give you context first.

**The skill is in beta.** It works end-to-end, but it has been tested by a small number of people on a small number of products. We need outside users to find the rough edges. If you try the skill — even partially, even on a fake practice product, even for one stage — please tell us what happened.

**What's especially useful:**
- **Where the skill's suggestions felt wrong or off-the-mark** — even one example is gold
- **Where you got stuck and the skill couldn't help** — what stage, what state, what you tried
- **Where the skill produced something useful you didn't expect** — these tell us what to lean into
- **Whether the bilingual setup (EN/RU) actually worked for your language**
- **Anything in the references that was inaccurate, dated, or just wrong**

**How to share:**
- Open an issue on the [share repo](https://github.com/alenazaharovaux/share)
- Or drop a note via any channel you use to reach the maintainer

We will adjust the skill based on what you find. The first 5–10 outside users are probably the most valuable source of feedback we will ever get on this.

---

## License

MIT — same as the rest of the share repo. Use it, fork it, change it, share it.

---

# Русская версия

## PMF — Engine для product-market fit

Скилл для Claude Code, который проводит один продукт через полный цикл product-market fit — от первого наброска гипотезы до пост-launch метрик. Десять стадий, три версии нарратива, два языка, один непрерывный цикл.

PMF-цикл занимает месяцы. Он возвращается к одним и тем же вопросам в разных формах — сначала как догадки, потом как находки рисёрча, потом как цитаты пользователей, потом как метрики после запуска. Скилл сделан под этот темп. Он помнит где вы остановились, поднимает разговор между сессиями и не торопит. Можно неделю писать гипотезу, три недели делать market research, шесть недель проводить интервью — а потом вернуться через два месяца с метриками. Скилл прочитает папку проекта, поймёт на какой вы стадии и предложит следующий разумный шаг.

> **🧪 Бета — нужен фидбек.** Скилл ещё обкатывается на реальных продуктах. Pipeline собран от начала до конца, но каждый продукт — свой зверь, и наверняка есть места где скилл работает хорошо, места где работает неуклюже, и места где просто ошибается. Если вы попробуете — пожалуйста, расскажите что сработало, что сломалось и что показалось странным. Откройте issue или напишите в share-репо. Мы будем править скилл по вашим находкам. Первые 5–10 внешних пользователей — самое ценное что мы можем сейчас получить.

---

## Содержание

- [Что это за скилл](#что-это-за-скилл)
- [Для кого](#для-кого)
- [Что внутри](#что-внутри)
- [Установка](#установка)
- [Первый запуск — настройка](#первый-запуск--настройка)
- [Как работает](#как-работает)
- [10 стадий подробно](#10-стадий-подробно)
- [7 dimensions](#7-dimensions)
- [Cross-stage правила](#cross-stage-правила)
- [Источники методологии](#источники-методологии)
- [Триггер-фразы](#триггер-фразы)
- [Зависимости](#зависимости)
- [FAQ](#faq-русский)
- [Ограничения](#ограничения)
- [Как оставить фидбек](#как-оставить-фидбек)

---

## Что это за скилл

PMF skill — это **один оркестратор, не пакет**. Один вход — вы говорите что-то вроде «давай сделаем PMF для моего продукта» — и скилл ведёт вас через весь цикл, не заставляя вспоминать какой sub-skill вызвать следующим. Все десять стадий внутри. Каждая стадия читает артефакты предыдущих и пишет свои.

Папка проекта — это и есть state machine. Скилл проверяет какие файлы есть в папке и определяет на какой вы стадии. Нет отдельной базы данных, нет JSON state-файла, нет скрытой бухгалтерии. Удалили файл — скилл считает что соответствующая стадия не сделана. Скопировали папку — у вас полный snapshot проекта. Вся система — это «файлы в папке», что делает её удобной для инспекции, ручной правки, передачи коллеге или коммита в git.

Три принципа задают тон скилла от начала до конца:

**Спокойный тон.** Никаких восклицательных знаков, никакой драматизации. Вы делаете PMF не для того чтобы вас подбодрили — а чтобы понять что реально работает а что нет. Скилл должен быть тихим коллегой, не коучем.

**Confidence можно понижать.** Это та часть, которую большинство команд делают неправильно. Если новые данные противоречат гипотезе, скилл понизит confidence-скор и явно об этом скажет вместо того чтобы замаскировать. V2 narrative с меньшим confidence чем V1 значит что цикл делает свою работу. Весь pipeline построен вокруг идеи что «я знаю меньше чем думал» — это полезная находка.

**Скилл не претендует делать полевую работу.** Две стадии — Stage 6 (Field Interviews) и Stage 8 (MVP Launch) — явно **вне** скилла. Скилл готовит гайд интервью и ждёт. Создаёт template метрик-дашборда и ждёт. Никогда не симулирует данные пользователей, не выдумывает цитаты респондентов, не делает вид что «запускает MVP за вас». Работа в реальном мире остаётся в реальном мире.

---

## Для кого

Этот скилл существует для человека, который сидит над идеей продукта или несколько месяцев что-то строит и вдруг спрашивает себя: «а у меня вообще есть product-market fit, или я просто занят?». Это для соло-фаундеров, продактов, indie hackers, исследователей в discovery-проекте, и небольших команд которые хотят структурированное второе мнение без оплаты $50K консультанту.

Это **не для:**
- Чистых pitch-deck'ов (это discovery-инструмент, не построитель fundraising-deck)
- Маркетинговых текстов (нарративы здесь — честные гипотезы, не landing-page копи)
- Авто-запуска MVP (скилл останавливается у двери реального мира — не деплоит код, не запускает рекламу, не пишет вашим пользователям)
- Замены user research (с людьми всё равно надо разговаривать; скилл делает разговоры полезнее)

---

## Что внутри

```
pmf/
├── SKILL.md                                  ← сам скилл (английская точка входа)
├── README.md                                 ← этот файл
├── config.md                                 ← пользовательская конфигурация (язык, путь к проектам)
└── references/
    ├── en/                                   ← 23 английских reference-файла
    │   └── ... (см. английскую секцию выше)
    └── ru/                                   ← 23 русских reference-файла
        ├── pipeline-overview.md              ← state machine, переходы между стадиями
        ├── stage-0-setup.md                  ← детальная логика Stage 0
        ├── stage-1-hypothesis.md             ← детальная логика Stage 1
        ├── stage-2-research.md               ← детальная логика Stage 2
        ├── stage-3-synthesis.md              ← детальная логика Stage 3
        ├── stage-4-validate.md               ← детальная логика Stage 4
        ├── stage-5-interview-prep.md         ← детальная логика Stage 5
        ├── stage-7-interview-synthesis.md    ← детальная логика Stage 7
        ├── stage-9-metrics.md                ← детальная логика Stage 9
        ├── 7-dimensions.md                   ← 7 PMF измерений целиком
        ├── 7-powers.md                       ← 7 Powers Хэмильтона Хелмера
        ├── dvf-framework.md                  ← Desirability/Viability/Feasibility (David Bland)
        ├── sean-ellis-survey.md              ← 40% бенчмарк, правила дистрибуции
        ├── levels-of-pmf.md                  ← First Round 4-уровневая лестница
        ├── narrative-writing-guide.md        ← как писать центральный narrative
        ├── template-narrative.md             ← структурный шаблон narrative
        ├── template-narrative-prose.md       ← прозаический шаблон (для стейкхолдеров)
        ├── template-market-research.md       ← шаблон market research
        ├── template-risk-prioritization.md   ← шаблон risk scoring
        ├── template-interview-guide.md       ← шаблон гайда интервью
        ├── template-interview-note.md        ← шаблон заметки одного интервью
        ├── template-interview-synthesis.md   ← шаблон синтеза интервью
        └── template-metrics-dashboard.md     ← шаблон метрик-дашборда
```

Сам скилл — около 480 строк в `SKILL.md`. References грузятся on demand — только когда вы реально дошли до стадии которой они нужны. Это держит активный контекст маленьким даже при том что полная методология — больше 250K символов текста.

References делятся на три группы:

**Stage logic** (9 файлов: pipeline-overview + 8 стадий). Это операционные мануалы для каждой стадии — что читает что, что пишет что, quality gates, common pitfalls. Грузятся когда вы входите в соответствующую стадию.

**Methodology** (6 файлов: 7-dimensions, 7-powers, dvf-framework, sean-ellis-survey, levels-of-pmf, narrative-writing-guide). Это справочники по фреймворкам которые лежат в основе. Грузятся когда нужны — например, `7-powers.md` читается внутри Stage 1 когда вы доходите до dimension Competitive Advantage.

**Templates** (8 файлов: narrative × 2, market research, risk prioritization, interview guide, interview note, interview synthesis, metrics dashboard). Это собственно fill-in-the-blanks шаблоны которые скилл копирует в папку вашего проекта. Каждый сцеплен со своей стадией.

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

После этого скилл доступен из любой Claude Code сессии — он глобальный, не per-project.

---

## Первый запуск — настройка

При первом триггере скилл задаёт два вопроса и сохраняет ответы в `~/.claude/skills/pmf/config.md`. Оба вопроса можно пропустить — скилл использует дефолты.

| Вопрос | Зачем спрашивается | Дефолт |
|---|---|---|
| **На каком языке работаем — английский или русский?** | Скилл полностью двуязычный. У каждого языка свой набор references в `references/en/` или `references/ru/`. Скилл общается с вами на выбранном языке весь цикл. | `en` (English) |
| **Где хранить PMF-проекты?** | Каждый продукт становится подпапкой. Дефолт держит всё в домашней директории; можете указать любую папку — Documents, Obsidian vault, внешний диск, что угодно. | `~/pmf-projects/` |

После обоих ответов скилл записывает config и подтверждает. Любое значение можно поменять в любой момент — просто отредактируйте `~/.claude/skills/pmf/config.md`. Если удалить файл, скилл создаст его заново при следующем запуске, спросив снова.

Файл config выглядит так:
```
language: ru
projects_path: ~/pmf-projects
```

Всё. Никаких environment variables, никакого JSON, никаких install-скриптов.

---

## Как работает

При триггере скилл первым делом читает config (или задаёт вопросы setup'а если конфига нет). Потом листит папку проектов и смотрит что там. Возможны три сценария:

1. **Вы начинаете новый продукт.** Скилл создаёт новую подпапку, запускает Stage 0 (Setup) и проводит вас через базу: имя, slug, тип продукта, контекст организации, team pre-flight check. 10–20 минут. Результат — `00_setup.md`.

2. **Вы продолжаете существующий продукт.** Скилл находит вашу подпапку, смотрит на файлы внутри и определяет на какой вы стадии — по присутствию файлов. Если есть `narrative-v1.md` но нет `market-research.md` — вы между Stage 1 и Stage 2. Скилл говорит вам именно это и спрашивает что делать дальше.

3. **У вас несколько продуктов в работе.** Скилл показывает их с текущей стадией и last-updated датой и спрашивает с каким работаем. Не предполагает.

После этого скилл предлагает следующий разумный шаг и ждёт подтверждения. Вы всегда можете переопределить — сказать «вернись к Stage 2», «дай мне переписать narrative», «пропусти Stage 4 для этой dimension» — и скилл переключится. Старые артефакты никогда не удаляются. Если переделываете Stage 2 — получаете `market-research-v2.md`, не перезапись.

Вся машина работает на присутствии файлов — нет отдельного state, нет in-memory кэша. Каждая сессия — свежее чтение папки. Это звучит медленно, но именно так скилл переживает месяцы между сессиями.

---

## 10 стадий подробно

Pipeline — это один happy path с явными нелинейными выходами. Что делает каждая стадия в реальности:

### Stage 0 — Setup

Короткая стадия чтобы собрать базовый контекст до того как вы тронете гипотезу. Собираются три вещи: тип продукта (B2C / B2B / Marketplace / DTC / Services / Internal / Other), контекст организации (Zero-to-one / Established / Extension), и team Pre-Flight Check (3 вопроса: founder-market fit, skill gaps, conviction-flexibility).

Почему именно эти три? Потому что они формируют все следующие стадии. B2B продукт надо анализировать дважды — раз для покупателя, раз для пользователя. Zero-to-one продукт не может опереться на существующие каналы. Команда без founder-market fit нуждается в партнёрах, и это влияет на риск-карту. Пропуск Stage 0 «чтобы сэкономить время» обычно стоит часов путаницы в Stage 1.

**Output:** `00_setup.md`

### Stage 1 — Hypothesis

Первая версия центрального narrative. Скилл проводит вас через 7 PMF dimensions, задавая guided questions, применяя validation rules и записывая confidence-скоры на каждую.

Результат — `narrative-v1.md`, структурированный документ с одной секцией на dimension, таблицей confidence и явной пометкой «riskiest dimension». Confidence-скоры в V1 обычно 4–6 из 10 для большинства dimensions; если вы пишете 9–10 в V1 — это красный флаг overconfidence, и скилл его поднимет.

Для B2B и Marketplace продуктов скилл проходит dimensions дважды — раз на роль. Decision Makers и End Users имеют разные проблемы и разные value props. Chicken-and-egg сторона маркетплейсов явно отмечается в Growth Strategy.

Можно выбрать один из двух форматов вывода — структурный (лучше для внутреннего трекинга) или прозаический (лучше для стейкхолдеров). V1 обычно делается только в структурном.

**Output:** `narrative-v1.md`

### Stage 2 — Market Research

Теперь скилл выходит из голов команды и идёт искать evidence в мире. Цель: для каждой из 7 dimensions найти **аналоги** (компании которые успешно валидировали эту dimension в реальных условиях) и **антилоги** (известные провалы которые показывают что ломается на этой dimension).

Метод — последовательный веб-поиск через Exa (приоритет) или WebSearch (fallback). Всего 14–21 поиск — 2–3 на dimension. **Subagents здесь явно запрещены.** Исследование аналогов — это содержательная работа, не file lookup, и пользователь должен видеть каждый поиск и каждый результат чтобы вмешаться. Скилл также адаптирует threshold «что считать аналогом» под тип рынка: $10M+ для зрелых рынков, $1M+ ARR для emerging.

Результат пишется в `market-research.md` после каждой dimension, не накапливается в памяти до конца. Если контекст начинает переполняться, скилл разбивает работу на 2 захода (dimensions 1–4 в одну сессию, 5–7 в следующую). Это нормально для месячного цикла.

В конце Stage 2 — preview каких dimensions выглядят рискованными после рисёрча и рекомендация для Stage 3.

**Output:** `market-research.md`

### Stage 3 — Synthesis

Скилл берёт V1 narrative и market research и производит три вещи: numerical risk score per dimension, cross-fit analysis, и обновлённый narrative (V2).

**Risk scoring** использует формулу `Risk Score = (10 - Evidence Score) × Failure Impact`. Evidence Score — насколько сильно данные поддерживают dimension (1–10). Failure Impact — насколько катастрофично если эта dimension окажется неверной (1–4, с разумными дефолтами — Problem и Business Model = 4, Audience и Growth = 3, Value Prop и Power = 2). Дефолтный impact можно перекалибровать под конкретный продукт.

**Cross-fit analysis** — две обязательные проверки согласованности: Channel-Model Fit (работает ли growth channel с business model?) и Model-Market Fit (работает ли business model для аудитории?). Здесь часто прячутся фатальные конфликты которые scoring в одиночку пропускает.

**V2 narrative** — отдельный файл от V1, с Version History changelog. Если confidence dimension'а упал — V2 говорит это явно. Если dimension был pivoted или reset — скилл отмечает. Confidence можно понижать — в этом весь смысл.

В конце Stage 3 — decision tree: высокий overall confidence + явный riskiest → Stage 4 валидировать его. Средний confidence → Stage 4 обязателен. Низкий confidence → возврат к Stage 1 или Stage 2. Cross-fit конфликты → возврат к Stage 1 для пересмотра конфликтующих частей.

**Outputs:** `risk-prioritization.md`, `narrative-v2.md`

### Stage 4 — Validate (DVF)

Самая рискованная dimension из Stage 3 разворачивается в 9 проверяемых assumptions по DVF — фреймворку David Bland: Desirability × Viability × Feasibility. Три assumption на категорию, без исключений. Desirability — *только* про user needs (никаких денег, никакой техники). Viability — *только* про деньги. Feasibility — operational + technical + regulatory.

Скилл строг к терминологии здесь. В стадиях 1–3 используется «hypothesis». В Stage 4 переключается на «assumption». Фреймворк Bland'а построен на том что assumptions — конкретные проверяемые «I believe...» утверждения, и смешение терминов вызывает реальную путаницу.

После того как 9 assumptions написаны, скилл размещает их на 2×2 importance × evidence. Critical quadrant — high importance + weak evidence — это что тестируется первым. Скилл проектирует эксперимент для самой рискованной assumption из этого квадранта, используя один из 6 стандартных типов экспериментов: Customer Interview, Smoke Test, Concierge, Survey, Prototype, Landing Page. **Кастомные типы запрещены** — «mini-pilot» и «discovery sprint» размытые, и скилл откажется выдумывать новые. Если ничего не подходит — assumption переформулируется.

Experiment brief включает конкретные success/failure thresholds (не «много sign-ups», а «≥3% landing → trial sign-up»), estimated effort, и заметку о том что эксперимент *не* покажет.

Для AI / fintech / healthtech продуктов regulatory assumptions автоматически заменяют одну-две operational/technical в Feasibility.

**Outputs:** `assumptions-map.md`, `experiment-brief.md`

### Stage 5 — Interview Prep

Теперь скилл готовит поле. На основе 2–3 рискованных dimensions из Stage 3 строится гайд интервью с пятью тематическими блоками. Каждый блок — 5–7 открытых вопросов. Вопросы следуют строгим правилам: не leading, не hypothetical futures, не мнения о том что люди *могли бы* делать — только past behavior, только конкретные ситуации.

Гайд структурирован: introduction script, screening questions (2–3, поведенческие не demographic), thematic blocks per risk-dimension, closing с просьбой о референсе. Каждый вопрос мапится на dimension и assumption в coverage matrix, так что к концу серии интервью каждая Critical-quadrant assumption из Stage 4 имеет хотя бы один вопрос направленный на неё.

Скилл рекомендует минимум 15 интервью, sweet spot — 20–30. Также создаётся `note-template.md` — структурированный формат который пользователь будет копировать для каждого интервью в поле.

**Outputs:** `interview-guide.md`, `interviews/note-template.md`, пустая папка `interviews/notes/`

### Stage 6 — Field Interviews (вне скилла)

Это **состояние ожидания**. Скилл не может проводить интервью. Может только подготовить гайд и потом обработать заметки. Когда вы возобновляете скилл на этой стадии, он говорит что гайд готов, спрашивает сколько интервью провели, и ждёт.

Пользователь делает полевую работу неделями или месяцами. Каждое интервью становится заметкой в `interviews/notes/`, написанной в структурированном формате из шаблона. С хотя бы одной заметкой в папке скилл позволит перейти к Stage 7, но 15+ — рекомендованный минимум для осмысленного синтеза.

### Stage 7 — Interview Synthesis

Скилл читает все заметки интервью — **по одной**, не пакетно, чтобы не усреднять паттерны — и извлекает findings per dimension. На каждую dimension производит: pattern (что говорят), supporting evidence count (N из M респондентов), 2–3 verbatim key quotes, confidence change (V2 → V3), и update type (Validated / Refinement / Pivot / Reset).

Также вытаскивает **cross-dimensional insights** (паттерны спанящие несколько dimensions) и **surprises** (находки противоречащие гипотезе). Surprises часто — самое ценное во всём pipeline. Если их нет — скилл флагает возможный confirmation bias и просит перечитать заметки.

Результат — `interview-synthesis.md` и третья версия narrative — `narrative-v3.md`. V3 переписан на языке пользователей, с реальными цитатами, более узкими персонами и обновлёнными рисками. Если confidence упал на какой-то dimension между V2 и V3 — скилл флагает и рекомендует следующий шаг: больше валидации, возврат к рисёрчу, или pivot.

**Outputs:** `interview-synthesis.md`, `narrative-v3.md`

### Stage 8 — MVP Launch (вне скилла)

Ещё одно состояние ожидания. Narrative валидирован настолько насколько слова это позволяют. Теперь надо что-то построить и поставить перед реальными пользователями. Скилл останавливается у двери. Когда вы возобновляете на этой стадии — скилл подтверждает что narrative готов и напоминает прийти на Stage 9 когда соберётся ~40 active users.

Можно использовать скилл как собеседника на этой стадии — обсуждать scope, MVP-фичи, target audience для запуска — но он не «запустит MVP за вас».

### Stage 9 — Metrics

Пост-launch измерение через три инструмента используемых вместе:

**Sean Ellis 40% Survey.** Один вопрос — *«Как бы вы себя чувствовали, если бы больше не могли использовать [продукт]?»* — с четырьмя вариантами ответа. Threshold: ≥40% «Очень разочарован» (исключая N/A) = PMF. Минимум 40 ответов, дистрибутировать только active users (не newsletter list, не cherry-picked top customers). Скилл генерирует текст вопроса и инструкции по дистрибуции, но НЕ собирает данные сам.

**Retention Cohorts.** Когортная таблица (неделя регистрации × процент возвратившихся в неделю 1, 2, 3, 4, 8, 12) с definition «active» откалиброванным под тип продукта. PMF signal: кривая выравнивается на здоровом уровне, а не падает к нулю. Strong PMF threshold — >40% для consumer, >60% для B2B, >25% для high-frequency. Скилл создаёт template таблицы и инструкции по сбору данных.

**First Round Levels of PMF.** 4-уровневая лестница — Nascent / Developing / Strong / Extreme — оцениваемая по трём dimensions (Satisfaction, Demand, Efficiency). Общий уровень = *минимум* из трёх, не среднее. Команда не может быть Strong по Satisfaction и Nascent по Efficiency одновременно — этот mismatch и есть bottleneck.

Stage 9 разворачивается через две реальные сессии: setup phase где создаётся dashboard template, потом collection phase 4–12 недель где пользователь собирает данные сам, потом interpretation phase где пользователь возвращается с заполненным dashboard и скилл рекомендует что делать в Stage 10.

**Output:** `metrics-dashboard.md`

### Stage 10 — Iterate

На основе метрик — решение что дальше:

- **Sean Ellis ≥40% + retention flatten + Level 3+** → PMF достигнут. Скилл выходит — scaling вне его scope.
- **Sean Ellis 25–40% + частичный retention flatten + Level 2** → Iterate. Возврат к Stage 4 (валидировать следующую риск-assumption) или Stage 7 (новый раунд интервью на сегмент «Несколько разочарован»).
- **Sean Ellis <25% + падающий retention + Level 1** → Pivot. Возврат к Stage 1 с явным reasoning о том какая dimension провалилась.

Output — `iteration-changelog.md`. После того как он написан, auto-start скилла снова прочитает папку и предложит следующую стадию на основе нового состояния. Цикл продолжается.

**Output:** `iteration-changelog.md`

---

## 7 dimensions

Каждая стадия pipeline возвращается к этим 7 dimensions. Они не независимы — сильные гипотезы показывают как они усиливают друг друга. Скилл загружает полное описание из `references/<lang>/7-dimensions.md` когда вы доходите до Stage 1, но вот короткая версия:

| # | Dimension | Вопрос | На что смотреть |
|---|---|---|---|
| 1 | **Problem to Solve** | Какого результата пытаются достичь пользователи и что мешает? | Solution-framed проблемы («у них нет нашего инструмента»). Абстрактные проблемы («хотят эффективности»). |
| 2 | **Target Audience** | Кто конкретно, и почему именно они сейчас (vs кто потом)? | Demographic-only персоны. «Все малые бизнесы». Now segment = future segment. |
| 3 | **Value Proposition** | Какой один benefit, на их языке, бьёт сильнее всего? | Features вместо benefits. Generic claims. Несколько конкурирующих taglines. |
| 4 | **Competitive Advantage** | Какая из 7 Powers Хелмера — ваш long-term moat? | «Лучшая команда», «первые на рынке», «уникальная технология» — ни одно не Power. |
| 5 | **Growth Strategy** | Как получаете первых 1K, и как доходите до 100K? | Один и тот же канал на оба горизонта. «Будем вирусными» без механизма. |
| 6 | **Business Model** | Какая equation, и согласована ли она с аудиторией и каналом? | «Будет реклама / freemium / премиум» без чисел. Pricing скопирован у конкурента. |
| 7 | **Timing / Why Now** | Какой конкретный shift сделал это возможным/нужным в последние 1–3 года? | «Нам кажется что время пришло». «AI hype». Размытое «рынок созрел». |

Восьмая половинка-dimension, Defensibility / Power, рассматривается как часть Competitive Advantage, но проверяется отдельно во время Stage 1 и снова в Stage 9 когда есть метрики.

---

## Cross-stage правила

Через весь pipeline проходит несколько правил — скучных, но несущих.

**Versioning narrative.** V1, V2 и V3 — **отдельные файлы**, никогда не перезаписи. Каждая новая версия имеет секцию Version History объясняющую что изменилось и почему. Цель — сделать эволюцию понимания видимой. Diff между V1 и V3 часто — самый полезный артефакт всего цикла.

**Confidence можно понижать.** Если данные противоречат гипотезе, скилл понизит confidence-скор и скажет это. V3 с меньшим confidence чем V2 — знак что цикл работает. Накручивать числа чтобы было приятно — самый частый failure mode self-driven PMF работы, и скилл сделан чтобы этому сопротивляться.

**Loop detection.** Если confidence одной и той же dimension продолжает падать через версии, скилл флагает возможный loop и рекомендует одно из трёх действий: больше валидации, возврат к research, или pivot. Не даст вам бесконечно крутить «interviews → small refinement → more interviews» не подняв паттерн.

**Возврат назад — first-class операция.** Пользователь может в любой момент сказать «вернись к Stage 2» — скилл переключится. Старые артефакты не удаляются. Если переделать Stage 2 — получите `market-research-v2.md` рядом с оригиналом. Папка растёт со временем — это и есть смысл.

**Между сессиями скилл всё перечитывает.** Не доверяет «памяти» о том что мы делали в прошлый раз. На каждом возобновлении auto-start свежо сканирует папку и определяет состояние. Это то что позволяет месячному циклу пережить много коротких сессий.

**Никаких subagents для контентной работы.** Stage 2 (research) и Stage 7 (synthesis) делаются в основной сессии, не делегируются. Research — содержательная работа, пользователь должен видеть каждый поиск и каждую цитату чтобы вмешаться. Synthesis требует чтения заметок интервью по одной в изоляции, и subagent усреднит паттерны. Это enforced как жёсткое правило.

**Скилл никогда не выдумывает данные.** Не симулирует цитаты интервью, не генерирует фейковые метрики, не предполагает «допустим Sean Ellis 47%». Где данных нет, скилл говорит «no data yet» и просит пользователя собрать.

---

## Источники методологии

Этот скилл стоит на плечах людей которые думали лучше нас. Если есть время прочитать одну вещь от каждого — вот с чего начать.

- **Marty Cagan — *Empowered* и *Inspired*.** Декомпозиция на 7 dimensions (с Timing как 7-й) опирается на product discovery работу Cagan'а. Его настойчивость что problem должна быть formulated независимо от solution отражена в validation rules Stage 1.

- **David Bland & Alex Osterwalder — *Testing Business Ideas* (2019, Strategyzer).** DVF фреймворк, 9 assumptions, 2×2 importance × evidence, и 6 стандартных типов экспериментов в Stage 4 — всё из этой книги. Bland'овская строгость к «assumption» vs «hypothesis» сохранена.

- **Hamilton Helmer — *7 Powers: The Foundations of Business Strategy*.** Competitive advantage dimension использует семь powers Helmer'а (Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power) как единственно приемлемые ответы. «У нас отличная команда» нет в списке, и скилл это скажет.

- **Sean Ellis — 40% survey.** Опубликовано в 2009 как ответ на «как мы поймём что у нас PMF?». Threshold 40% эмпирический, не теоретический — Ellis собрал данные от ~100 стартапов которые консультировал и обнаружил что те у кого ≥40% «Очень разочарован» могли scale через paid marketing с положительной экономикой.

- **First Round Capital — *The Levels of Product/Market Fit (& What to Focus on at Each)*.** Todd Jackson, Brian Rothenberg, Carolyn Stein. 4-уровневая лестница — Nascent / Developing / Strong / Extreme — и 3-dimensional grid оценки (Satisfaction × Demand × Efficiency) — из этой статьи в First Round Review.

- **Bill Gross — TED talk про #1 фактор успеха стартапов.** После анализа 200+ компаний Gross нашёл что timing — самый сильный предиктор успеха стартапа, важнее команды, идеи, бизнес-модели или финансирования. Поэтому Timing / Why Now входит в семёрку на тех же правах что Problem и Audience.

- **Rahul Vohra — *How Superhuman Built an Engine to Find Product/Market Fit*.** Опубликовано в First Round Review. Расширяет подход Sean Ellis в полноценный процесс — сегментировать «Очень разочарован» группу, выявить что они ценят, перестроить вокруг них, повторить. Эта loop-форма — то что Stage 9 ↔ Stage 10 реализует.

- **gnurio/pmf-plugin.** Структурный паттерн разбиения цикла на ~10 последовательных стадий с auto-detection из folder state заимствован у этого плагина. Dimensions, методологии и quality gates внутри другие, но форма оркестрации — должное этому плагину.

---

## Триггер-фразы

Скилл задизайнен срабатывать на естественный язык на английском или русском. Что-то в этой грубой форме сработает:

**Русский:**
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

**English:**
- «do PMF for [product name]»
- «I need product market fit for X»
- «PMF [name]»
- «start a PMF cycle»
- «continue PMF»
- «what stage is my PMF at»

Скилл также пытается поймать любое сообщение где вы упомянули продукт и хотите его систематически валидировать — даже если не сказали «PMF» по имени.

---

## Зависимости

**Обязательно:**
- Claude Code (это Claude Code скилл)
- WebSearch (встроен в Claude Code)

**Опционально но рекомендовано:**
- **Exa MCP** для Stage 2 market research. Скилл предпочитает `mcp__exa__web_search_exa` потому что Exa семантический поиск значительно лучше для нахождения аналогов и антилогов по описанию проблемы, не только по ключевым словам. Если Exa не установлен — скилл автоматически fallback на WebSearch. Stage 2 всё равно работает, поиски просто более keyword-driven.

Установка Exa MCP — см. [документацию Exa MCP](https://github.com/exa-labs/exa-mcp-server). Если не хотите настраивать — игнорируйте, скилл просто использует WebSearch.

**Не нужно:**
- Никаких Python-библиотек
- Никаких внешних API кроме поисковых выше
- Никакой базы данных
- Никаких login или API-ключей куда-либо

---

## FAQ (русский)

**В: Сколько занимает PMF цикл с этим скиллом?**

Полный цикл (Stage 0 — Stage 10) — месяцы, не дни. Реалистичные диапазоны: Stage 0 — 10–20 минут. Stage 1 — 1–3 сессии по часу. Stage 2 (research) — 1–2 дня сосредоточенной работы. Stage 3 (synthesis) — полдня. Stage 4 (DVF) — полдня на assumptions + сколько займёт эксперимент. Stage 5 (interview prep) — полдня. Stage 6 (field interviews) — **недели**: 15–25 интервью, спланированных и проведённых пользователем. Stage 7 (synthesis) — полдня-день. Stage 8 (MVP launch) — **недели или месяцы**. Stage 9 (metrics) нужно минимум 4 недели сбора данных. Stage 10 — одна сессия. Скилл задизайнен под этот темп и возобновляется между сессиями.

**В: Можно ли пропустить стадию?**

Можно, но скилл предупредит. Некоторые пропуски разумны — например, пропустить Stage 4 если confidence в Stage 3 высокий и риск-dimension лучше валидируется через интервью напрямую. Другие пропуски — warning sign. Желание прыгнуть сразу к Stage 9 (метрики) обычно значит что вы надеетесь что числа скажут вам то что гипотеза не говорит. Sean Ellis на случайной аудитории даёт случайный результат; ранние стадии существуют чтобы сделать метрику осмысленной.

**В: Что если мой продукт многосторонний (marketplace) или имеет несколько персон (B2B)?**

Скилл это handle'ит в Stage 1 через multi-role processing. Для B2B вы проходите 7 dimensions дважды — раз для Decision Makers (кто платит), раз для End Users (кто пользуется). Для marketplaces — дважды, по одному разу на каждую сторону, с chicken-and-egg проблемой явно отмеченной в Growth Strategy. Обе роли оказываются в одном `narrative-v1.md` отдельными секциями.

**В: У меня уже есть продукт в продакшене. Можно начать с середины?**

Да. Можно создать папку проекта, бросить существующие данные в соответствующие artifact-файлы (например, существующий pitch deck → `narrative-v1.md`), и скилл определит стадию и предложит куда дальше. Нет ничего магического в начале с Stage 0; auto-start считает текущим состоянием то какие артефакты существуют.

**В: Моя команда использует другую терминологию — можно переименовать?**

Скилл opinionated к нескольким терминам потому что у них методологический вес: «assumption» vs «hypothesis» в Stage 4 (Bland'овское разделение важно), и 4 варианта ответа Sean Ellis должны быть в оригинальной формулировке. Кроме этого, можно переименовывать что угодно в своём narrative — шаблоны просто предложение.

**В: Это замена разговорам с пользователями?**

Нет. Stage 6 явно не может быть сделан скиллом. Весь pipeline построен на предположении что вы говорите с реальными людьми, и работа скилла — сделать разговоры полезнее (лучший гайд, лучший синтез) и окружающую структуру (гипотеза, рисёрч, риск scoring, метрики) честнее.

**В: Что если я не знаю B2C мой продукт или B2B?**

Stage 0 имеет tiebreaker вопрос: кто реально платит — конечный пользователь или его компания? Это и есть тип. Если ни одно не очевидно — продукт скорее всего ещё не готов к PMF анализу, надо сначала выбрать target.

**В: Скилл коммитит файлы проекта в git?**

Нет. Скилл создаёт файлы в вашей папке проектов и всё. Коммитить, шарить, бэкапить — ваш выбор. Многие пользователи держат PMF проекты в Obsidian vault который sync'ается отдельно, другие — в приватном git репо, третьи — локально.

---

## Ограничения

Честный список от команды которая это построила:

1. **Скилл opinionated.** Он enforce'ит конкретные фреймворки (7 dimensions Cagan'а, DVF Bland'а, 7 Powers Helmer'а, Sean Ellis 40%, First Round Levels). Если вы предпочитаете другую методологию — Lean Startup canvas, Jobs-to-be-Done, и т.д. — скилл не тот инструмент. Мы выбрали эти потому что они композитятся в работающий pipeline; замена одного развалит остальные.

2. **Не может проводить эксперименты за вас.** Stages 6 и 8 явно вне scope. Скилл пишет гайд интервью; вы проводите интервью. Скилл пишет dashboard метрик; вы инструментируете и shipping продукт. Если нужна автоматизированная experimentation платформа — смотрите в другом месте.

3. **Предполагает один продукт на папку.** Портфолио из 5 продуктов = 5 подпапок. Скилл не координирует cross-product анализ, общие сегменты клиентов между продуктами, или платформенные решения.

4. **Stage 2 search-driven, и search имеет смещения.** Веб-поиск возвращает то что возвращает — успешные компании over-represented, недавние компании over-represented, английские источники over-represented. Скилл это смягчает требованием антилогов и адаптацией thresholds под тип рынка, но базовое смещение реально.

5. **Sean Ellis — Western-trained бенчмарк.** Threshold 40% эмпирически выведен из выборки в основном US tech стартапов. Некоторые культуры систематически дают другие распределения. Скилл это отмечает но не переопределяет threshold.

6. **Deep tech / R&D продукты плохо вписываются в DVF.** Если ваш продукт — квантовый компьютер, новая biotech-молекула, или что-то где Feasibility — доминирующий риск на годы — DVF фреймворк искажает. Вам скорее нужны Technology Readiness Levels, и Stage 4 не даст что нужно.

7. **Скилл в бете.** Edge cases ещё находятся. 9 стадий тестировались end-to-end на нескольких реальных продуктах, но каждый продукт — свой зверь. Если что-то ломается — пожалуйста откройте issue (см. следующую секцию).

---

## Как оставить фидбек

Это самая важная секция в README, и она внизу потому что мы хотим чтобы остальное дало вам контекст сначала.

**Скилл в бете.** Он работает end-to-end, но был протестирован небольшим числом людей на небольшом числе продуктов. Нам нужны внешние пользователи чтобы найти острые края. Если попробуете скилл — даже частично, даже на фейковом тренировочном продукте, даже на одной стадии — пожалуйста расскажите что произошло.

**Что особенно полезно:**
- **Где предложения скилла показались неправильными или мимо** — даже один пример золото
- **Где вы застряли и скилл не помог** — какая стадия, какое состояние, что пробовали
- **Где скилл произвёл что-то полезное чего вы не ожидали** — это говорит нам куда давить
- **Сработала ли двуязычная (EN/RU) настройка для вашего языка**
- **Что в references было неточным, устаревшим или просто неправильным**

**Как поделиться:**
- Откройте issue в [share репо](https://github.com/alenazaharovaux/share)
- Или напишите через любой канал которым вы достигаете maintainer'а

Мы будем править скилл по тому что вы найдёте. Первые 5–10 внешних пользователей — самый ценный фидбек который мы когда-либо получим.

---

## Лицензия

MIT — как и остальной share-репо. Используйте, форкайте, меняйте, шарьте.
