# Template — Narrative (Prose)

**Used in:** Stage 3 (V2), Stage 7 (V3) — usually not needed for V1
**Save as:** `narrative-v2-prose.md`, `narrative-v3-prose.md`
**Companion guide:** `references/<lang>/narrative-writing-guide.md`

**Purpose:** the prose form of the narrative for stakeholders (investors, partners, new hires, early-access customers). Same information as the structured narrative, but in the form of a connected story.

---

## Principles of the prose form

1. **One document, no tables.** Connected text 800-1500 words.
2. **Opens with the story of a specific user**, not with a category. Visceral problem first.
3. **All 7 dimensions are woven into the text**, but not as section headers — as parts of the story.
4. **Calm, confident tone.** No exclamation marks, no "revolutionary." The reader should feel that you know what you are talking about.
5. **Evidence inline**, not in a footnote. "From 2026-04-05 interviews (15 sellers) — 12 of 15 spend..." in the body.

---

## Template

```markdown
# [Product name] — Narrative

**Version:** V[2/3]
**Date:** YYYY-MM-DD
**For:** [investors / partners / team / early users]

---

## The story

[1-2 paragraphs] [User name or specific segment] [a concrete day, a concrete moment] [a visual scene with a workaround / pain]. [Numbers: time, money, frequency]. [Emotional aspect].

[This is the first paragraph. The reader has to see a person, not a category. Open with a visceral scene.]

---

## Why this matters now

[1-2 paragraphs] [What changed in the world / technology / market in 1-3 years that makes this problem sharp / solvable now]. [Concrete facts — API price changes, a new law, new user behavior].

[This is the second context. The reader has to understand why now is the moment for this product.]

---

## Who we built it for

[2-3 paragraphs] [A concrete segment: where they live, what they do, what context they live in]. [Persona divides — who is NOT our user and why]. [Where the understanding came from — interviews / personal experience / market research].

[The reader should leave with a clear image of one persona, not a broad category.]

---

## What it actually does

[2-3 paragraphs] [Benefits, not features. How the user's day changes]. [Core experience in one sentence: "X does Y in Z, using W"]. [Top 3 benefits with specifics].

[Not a feature list. Not bullet points. A connected story about how the product changes the situation from "The story".]

[Out of scope: 1 paragraph on what we are NOT doing and why — that gives focus.]

---

## How we'll reach them

[1-2 paragraphs] [Concrete acquisition channels]. [Why here specifically — where the target audience lives now, which messages resonate]. [Flywheel — how one successful iteration creates the conditions for the next].

[The reader should understand the GTM strategy, not "marketing through social media".]

---

## How we make money

[1 paragraph] [Pricing model + first hypothesis price point]. [Reasoning behind that number]. [Key unit economics: ARPU, target LTV/CAC, payback period]. [If pre-revenue — which assumptions you are testing].

---

## Why this is defensible

[1-2 paragraphs] [Which of the 7 Powers applies]. [A concrete accumulation mechanism — not "we will have a moat", but "every transaction adds data to a shared dataset that improves recommendation accuracy"]. [When defensibility starts to work — usually after Strong PMF].

---

## What we know and what we don't

[1-2 paragraphs] [What is confirmed by data — interviews, market research, analogs]. [What is still weak evidence — which assumptions are waiting for validation]. [What the biggest risk is and how you plan to test it].

[This is the most important section. The reader should see that you do NOT hide weak spots. That is stronger than "everything is great".]

---

## Where we are now

[1 paragraph] [Current stage — Strong PMF / Developing / Validating through Stage 4]. [What was done up to this point — interviews, MVP, beta]. [What the next milestone is].
```

---

## Size per version

| Version | Words | When |
|--------|------|-------|
| V2 prose | 800-1200 | After market research, for investors / advisors |
| V3 prose | 1000-1500 | After field interviews, with real quotes |

V1 is not done in prose form — structured is enough for V1. V1 is the initial hypothesis, prose without evidence = a pitch without grounding.

---

## Tone examples

**Bad (hype):**
> "We are building a revolutionary AI tool that will completely change the world of e-commerce! Our unique technology will give sellers unprecedented freedom!"

**Good (calm):**
> "Small e-commerce sellers spend 4-6 hours a week on manually moving orders between marketplaces and 1C. We talked to 15 of them — 12 described the same problem in almost the same words. Existing tools (Linnworks, Veeqo) target enterprise. We are building a minimal version for the self-employed."

**Bad (vague):**
> "Our product helps teams be more productive."

**Good (concrete):**
> "Remote teams lose 45 minutes a day on async status updates in Slack — we measured this in 8 interviews. We replace those 45 minutes with one 5-minute dashboard that pulls updates automatically from commit messages, calendar events and the task tracker."

---

## Common mistakes

| Mistake | Symptom | Fix |
|--------|---------|------|
| Pitch deck instead of narrative | Bullet points, icons in headers, exclamations | This is not a deck. This is a story. Connected text. |
| All features, no benefits | "Real-time sync, AI-powered, multi-platform" | Flip: "What changes in the user's day?" |
| Hype instead of evidence | "It will revolutionize the market" | Numbers, quotes, concrete sources |
| Hiding weak evidence | The whole story sounds confident | Openly admit what is Weak — that is stronger |
| Too much feature exploration | 3000+ words | Compress. Details go to the product spec |
| Opens with the company, not the user | "We are a team of 5 people..." | Open with a specific user at a specific moment |
| Generic persona | "Young busy professionals" | Name, place, day, problem |
