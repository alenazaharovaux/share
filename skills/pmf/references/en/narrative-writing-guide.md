# Narrative Writing Guide — how to formulate the narrative for PMF

**Why:** the narrative is the main artifact of the PMF skill. It is not marketing copy and not a technical document. It is a **testable story** describing the product hypothesis at a concrete level of detail.

The narrative goes through 3 versions over the PMF cycle:
- **V1** (Stage 1, Hypothesis) — initial hypothesis across the 7 dimensions
- **V2** (Stage 3, Synthesis) — rewritten after market research, with updated risks
- **V3** (Stage 7, Interview synthesis) — rewritten after field interviews, with real quotes

V1 → V2 → V3 are **separate files**, not overwrites. Comparing versions shows what changed from one validation to the next.

---

## What a good narrative is

A good narrative answers 3 questions in the first 200 words:
1. **Who** specifically the product is for (not "all busy people")
2. **What pain** it removes (visceral, not abstract)
3. **How** it differs from how they solve it today

If the first 200 words do not answer this — rewrite the narrative.

---

## Visceral problems vs abstract

**Visceral** = a tangible, emotional, concrete pain with time, place, context.

**Abstract** = a categorical statement you cannot argue with.

| Abstract (bad) | Visceral (good) |
|------------------|-------------------|
| "Small businesses find it hard to manage orders" | "Small e-commerce sellers spend 4-6 hours a week manually copying orders from Wildberries into Excel, then into 1C — losing 2-3 orders a month to human error" |
| "Students suffer from procrastination" | "Second-year students put off exam prep until the last 3 days, then don't sleep for 2 nights, get a 3 instead of a 5, and are ashamed to tell their parents" |
| "Teams find it hard to coordinate remotely" | "Remote teams lose 45 minutes a day on async status updates in Slack that nobody reads, and then they still do a synchronous standup" |

**Test:** replace "sellers", "students", "teams" with a specific name. Does it sound like a real person you know? If not — too abstract.

**Source of visceral wording:** Stage 5–7 (interviews). After interviews the narrative is rewritten in their language, not in marketing language.

---

## Benefits vs features

**Feature** = what the product does (sync orders, generate code, analyze data).

**Benefit** = what changes in the user's life because of it (4 hours back per week, no more lost orders, sleeping calmly at night).

In the narrative we write **benefits**, not features. Features are for the product spec, not the narrative.

| Feature (bad) | Benefit (good) |
|-----------------|------------------|
| "Real-time sync with the Wildberries API" | "Orders show up in 1C automatically 10 seconds after they are placed — no more checking and copying by hand" |
| "AI-powered code review" | "A junior developer gets feedback on a pull request in 30 seconds instead of waiting for a senior for hours — unblocked, keeps working" |
| "Multi-language support" | "A team from 5 countries reads one document in their native language, with no need to agree on a 'common English'" |

**Test:** read the wording. Can you see how the user's day changes? If it is only about the product — that is a feature.

---

## Flywheels — how to describe the growth mechanic

A flywheel = a self-reinforcing cycle where each iteration strengthens the next. It is stronger than a funnel because it does not require constant input from the top.

In the narrative describe 1-2 potential flywheels:

**Example flywheel (Notion):**
```
Someone makes a beautiful template
  → Shares it on Twitter / Reddit
    → New users copy the template, sign up
      → Remix it, make their own
        → Share on Twitter / Reddit
          → Loop
```

**Example flywheel (e-commerce sync tool):**
```
The seller saves 4 hours a week
  → Can take more orders
    → Earns more
      → Willing to pay for an upgrade
        → The tool team invests in new marketplaces
          → The seller saves even more
            → Loop
```

**Signs of a weak flywheel:**
- Paid acquisition is needed in every iteration (that is a funnel, not a flywheel)
- Every iteration requires a new decision from the team (no automatism)
- The loop closes in > 12 months (too slow)

The narrative must show **at least one** plausible place for a flywheel. Without a flywheel growth = funnel = endless CAC = bad Viability.

---

## Persona divides — who is NOT your user

The most common mistake of a V1 narrative is saying the product is for "all busy people" / "all small businesses" / "all students."

A good narrative explicitly says **whom we exclude**:

**Example (e-commerce sync tool):**
- ✓ YES: sellers across 1-3 marketplaces, $5K-50K/mo turnover, no in-house accountant
- ✗ NO: enterprise (>$200K/mo turnover, has IT team — they have their own)
- ✗ NO: solo selling on one marketplace (no sync problem)
- ✗ NO: dropshipping (different accounting model)

**Persona divide** is the explicit drawing of borders. Without a divide, you will build a product for everyone and fit no one.

In the narrative call out at least **2-3 groups you exclude** and why (one phrase).

---

## Narrative structure across the 7 dimensions

The 7 dimensions from `references/<lang>/7-dimensions.md`:
1. Customer
2. Problem
3. Why now (timing)
4. Why us (founder-market fit / unique insight)
5. Solution shape
6. Distribution / Channel
7. Business model (Monetization)

Plus an 8th ("+1"): Defensibility / Power.

In the narrative each dimension = its own section (1-2 paragraphs). Do not merge them.

**Anti-pattern:** "narrative = marketing copy about the product." Marketing is about features/benefits. The narrative is about the hypothesis.

**Size:** V1 narrative ~600-1000 words. V2 ~800-1200 (more evidence). V3 ~1000-1500 (more real quotes).

---

## Evidence per dimension

Each dimension in V2 and V3 narrative must have **evidence** or explicitly mark its absence:

| Level | Example |
|---------|--------|
| **Strong evidence** | "From 2026-04-05 interviews (15 sellers) — 12 of 15 spend 3-6 hours a week on manual sync" |
| **Indirect evidence** | "An analog in the US (Linnworks) showed ARPU of $89/mo on 8K customers — for our market adjusted to $30-40" |
| **Weak / no evidence** | "The team assumes this problem exists for these sellers, but it has not been validated" |

The point of the narrative is not to hide weak spots, but to **show where the weakest evidence is**, so you know where to validate next. A narrative with 100% strong evidence on every dimension = wishful thinking.

---

## Versioning

| Version | When | What changes |
|--------|-------|--------------|
| **V1** | Stage 1, after the first hypothesis brainstorm | Initial wording across the 7 dimensions, little evidence, lots of assumptions |
| **V2** | Stage 3, after market research + risk synthesis | Dimensions with weak evidence corrected, analogs/antilogs added, 1-3 main risks called out |
| **V3** | Stage 7, after field interviews | Rewritten in user language, quotes added, persona divides corrected, risks updated |

Each version = a separate file in the project folder: `narrative-v1.md`, `narrative-v2.md`, `narrative-v3.md`. Do not overwrite.

**Why keep old versions:** they show the evolution of understanding. Often V3 differs from V1 so much that without a comparison you cannot see what you learned. That is a valuable artifact in its own right.

---

## Structured vs prose

The PMF skill uses **2 forms of narrative** for each version:

1. **Structured** (`template-narrative.md`) — a 7-dimensions table with fields, evidence, validation status. For internal team tracking.

2. **Prose** (`template-narrative-prose.md`) — a flowing story for stakeholders (investors, partners, new hires). Same information, but in story form.

V1 is usually only created in the structured form. V2 and V3 — in both.

---

## Common mistakes

| Mistake | Symptom | Fix |
|--------|---------|------|
| Narrative = marketing | Hype, exclamation marks, "revolutionary" | This is a hypothesis. Calm tone, evidence, weakness explicit |
| "For all busy people" | Persona too broad | Persona divide: explicitly call out who is excluded |
| All features, no benefits | Product spec description | Flip: what changes in the user's day |
| Abstract problems | "Hard to manage time" | Visceral: time, place, concrete numbers, real workarounds |
| No flywheel | Only funnel-based growth | Find 1 potential flywheel, describe it explicitly |
| One narrative.md file, overwritten | No evolution history | V1, V2, V3 — separate files |
| Evidence missing or fake | "Everyone wants this" | State the source or explicitly "no evidence yet" |
| 100% Strong evidence on all dimensions | Wishful thinking | If everything is confirmed — validation is not needed, the skill is useless |
| Narrative > 2000 words | Too detailed for V1/V2 | Compress to the core hypothesis. Details go into research/interview docs |

---

## Quality gate checklist (for all three versions)

- [ ] Customer dimension: segment name + persona divides
- [ ] Problem dimension: visceral wording with time/numbers/workarounds
- [ ] Why now: what changed in the world/technology/market in the last 1-3 years
- [ ] Why us: which unique insight the team has (not "we like this area")
- [ ] Solution: benefits, not features
- [ ] Distribution: 1-2 concrete channels with a hypothesis about why they will work
- [ ] Business model: pricing model + first hypothesis price point
- [ ] +1 (Power): which of the 7 powers applies long term
- [ ] Flywheel: 1+ closed loop described
- [ ] Evidence: each dimension has an evidence level (strong/indirect/weak)
- [ ] Persona divides: 2-3 groups explicitly excluded
- [ ] Tone: calm, no exclamations, no "revolutionary/unique/disruptive"
