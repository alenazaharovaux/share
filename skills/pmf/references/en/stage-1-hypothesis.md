# Stage 1 — Hypothesis

**Goal:** turn the product idea into a structured hypothesis across 7 PMF dimensions with honest 1-10 confidence scores for each and an explicit identification of the riskiest dimension.

**Reads:** `00_setup.md`
**Writes:** `narrative-v1.md`

---

## Step 1.1 — Read the setup

From `00_setup.md` extract:
- Product name
- Type (B2C SaaS / B2B SaaS / Marketplace / DTC / Services / Internal / Other)
- Organizational context (Zero-to-one / Established / Extension)
- Team Pre-Flight Check results (3 answers + risk flag)

This shapes the rest of Stage 1:
- B2B → multi-role handling (Decision Makers vs End Users)
- Marketplace → multi-role handling (Demand vs Supply)
- Established → reuse of existing channels and audiences
- Zero-to-one → more focus on Timing (Why Now)

**Do NOT re-run the Pre-Flight** — it was collected in Stage 0 (`references/<lang>/stage-0-setup.md`). Here you only read it and account for it. If `00_setup.md` is missing or the Pre-Flight is empty — go back to Stage 0, do not try to invent it.

---

## Step 1.2 — Carry Pre-Flight into the narrative

The Pre-Flight results from `00_setup.md` will be included in `narrative-v1.md` as a separate section (see Step 1.6 — Document Generation, "Team Pre-Flight Check" section). They have to be visible in all later stages, so they do not stay only in the setup file.

**Technically:** when assembling the narrative, copy the Team Pre-Flight Check section from `00_setup.md` into the narrative as is. If the risk flag = High — add an explicit warning block at the top of the narrative: "Team risk: high — keep this in mind when interpreting the dimensions below."

---

## Step 1.3 — Working through the 7 dimensions

Go through them one by one. For each dimension:
1. Show "what good looks like" (examples from `references/<lang>/7-dimensions.md`)
2. Ask the guided questions
3. Apply the validation rules
4. Write into the narrative
5. Confidence 1-10

### 1.3.1 — Problem to Solve

**Outcome-Motivation Gap framework** — 3 questions:
1. **What are users trying to achieve?** (desired outcome — a concrete result, not an abstraction)
2. **Why do they want it?** (motivation — what is behind the wish)
3. **Why can they not do it now?** (gap — what is in the way; this is the problem)

**Validation rules:**
- ⛔ The problem must not mention your product or its features
- ⛔ The problem is not "there is no [our product]"
- ✅ Problem framed as an obstacle, not as an absence
- ✅ Concrete: you can picture one person in the situation

**Good example:** "Small e-commerce sellers spend 4-6 hours a week manually copying orders from 5 different channels into their accounting system, because off-the-shelf integrations only exist for the big players, and they can't code their own."

**Bad example:** "There is no good tool for syncing sales channels."

### 1.3.2 — Target Audience

**Questions:**
1. Defining attributes (2-3): what distinguishes this audience from neighboring ones? Attribute + concrete value.
2. **Now segment:** who is hurting right now, ready to pay, easy to reach?
3. **Future segments:** where will you expand in 1-3 years?
4. Why this audience specifically? How does it resonate with the other dimensions (especially value prop and growth)?

**Validation rules:**
- ⛔ Not "all women 25-45", not "all startups"
- ⛔ A defining attribute is not "age" (that is demographic, not behavior)
- ✅ Attribute = action, situation, or pain point ("sellers across 5+ channels", "researchers running 10+ interviews per month")
- ✅ Now segment explicitly separated from Future

**Good example:**
- Now: sellers with 100-1000 orders/month across 3+ channels at once (Wildberries + Ozon + own site), $5K-50K/mo turnover, no in-house developer
- Future 1: sellers with 10-100 orders/mo (easier, but poorer)
- Future 2: enterprise 1000+ orders/mo (harder, richer, requires 1C integration)

### 1.3.3 — Value Proposition

**Ideal Homepage Approach:**
1. **Tagline** — one sentence, **benefit-focused**, not feature-focused
2. **Sub-benefits** — 3-5 of them, also benefits

**Validation rules:**
- ⛔ Features ("integrations with 5 marketplaces")
- ⛔ Generic ("better, faster, cheaper")
- ✅ Benefits ("you stop losing orders to manual copying")
- ✅ Specific ("4-6 hours a week back in your day")

**Good example:**
- Tagline: "All your orders from all marketplaces in one table — no developer, no manual work."
- Sub-benefits:
  1. No more missed orders from tab-switching
  2. 4-6 hours a week freed up
  3. A ready-made accountant report in one click
  4. Works with Wildberries, Ozon, Y.Market, AliExpress, your own site
  5. No code — set up in 15 minutes

### 1.3.4 — Competitive Advantage

**Long-term moat:** one of the 7 Powers (Helmer). Full description — `references/<lang>/7-powers.md`.

Short list:
1. **Scale Economies** — unit cost falls with growth
2. **Network Economies** — value to a user grows with the number of other users
3. **Counter-Positioning** — a position incumbents cannot copy without harming their own business
4. **Switching Costs** — costly/complex for the user to leave
5. **Branding** — users will pay a premium for the brand
6. **Cornered Resource** — exclusive access to a key resource
7. **Process Power** — operational superiority that is hard to copy

**Questions:**
1. Which of the 7 Powers will be your long-term moat?
2. Why will it work in your context?
3. What do you need to do to build it?

**Plus a short competitive landscape:**
- **Direct competitors:** who does the same thing for the same audience
- **Indirect competitors:** who solves the same problem in a different way
- **Underserved segments:** where competitors do not cover the market enough

**Validation:**
- ⛔ "We have the best team" — not a Power
- ⛔ "We are first" — not a Power (first-mover advantage is rarely sustainable)
- ⛔ "We have unique technology" — not a Power without a patent moat or process advantage
- ✅ A concrete compounding mechanism

### 1.3.5 — Growth Strategy

**Two horizons:**

**Short-term traction** — how to get the first 1K users / 10 customers:
- Which channels work at small volumes? (cold outreach, founder communities, content, partnerships)
- What does **not** work at this scale (paid ads are usually too expensive without an optimized funnel)

**Long-term sustainable** — how to scale to 100K+:
- Which channels can survive the scale? (paid ads with optimized CAC, viral loops, an SEO content engine, a sales team)
- They have to be **different** from the short-term ones (that is normal)

**Validation:**
- ⛔ Short-term = long-term (example mistake: "cold outreach" — does not scale)
- ⛔ "We will go viral" without a concrete mechanism
- ✅ Each channel has a concrete owner / cost model / expected CAC

### 1.3.6 — Business Model

**Business equation** (the formula depends on the product type):

| Type | Formula |
|-----|---------|
| B2B SaaS | LTV > 3× CAC, payback < 12 months |
| Freemium B2C | Free→Paid conversion × ARPU > CAC |
| Marketplace | (Take rate × GMV) > Cost-to-serve both sides |
| DTC | (LTV × Repeat rate) > CAC + COGS + ops |

**What to lock in:**
- **Revenue streams** — where the money comes from
- **Pricing** — model + concrete price point + rationale
- **LTV estimate** — an estimate
- **Cost structure** — fixed vs variable
- **Path to profitability** — how LTV grows faster than CAC over time

**Validation:**
- ⛔ "There will be ads / freemium / premium" without numbers
- ⛔ Pricing copied from a competitor without checking it against your audience
- ✅ Concrete estimates even if rough ("LTV ~$500 based on X")

### 1.3.7 — Timing / Why Now

**Two questions:**
1. **What changed?** — a concrete shift (technology, behavior, regulation, economics)
2. **Why now?** Not a year ago and not in 3 years?
   - What was impossible/unprofitable before?
   - What closes the window of opportunity later?

**Validation:**
- ⛔ "We feel the market is ready" — not timing
- ⛔ "AI hype" — that is noise, not timing
- ✅ A concrete triggering event ("GPT-4 made translation 100× cheaper", "the new labeling law arrived in 2025", "Gen Z hit the labor market in volume")
- ✅ Window optionally explained ("the window closes when incumbents adapt — estimate 2-3 years")

**Bill Gross research:** timing is the #1 factor in startup success (more important than team, idea, business model and funding). Do not skip this dimension.

---

## Step 1.4 — Multi-role handling

If the setup says the product is **B2B** or **Marketplace** — go through the dimensions a second time for the second role:

**B2B SaaS:**
- Decision Makers (who pays) ≠ End Users (who uses)
- Their Problem, Value Prop and Audience may be different
- Pricing works on DM, retention works on EU

**Marketplace:**
- Demand side (buyers) ≠ Supply side (sellers)
- Each side = a separate audience with separate dimensions
- Chicken-and-egg problem must be flagged explicitly in Growth Strategy

**The same `narrative-v1.md`** holds both roles — as separate sections.

---

## Step 1.5 — Confidence Assessment

After working through all 7 (or 14 for multi-role) dimensions — score confidence 1-10 for each:

| Score | Meaning |
|-------|-----------|
| 9-10 | Backed by strong data or personal experience, unlikely to be wrong |
| 7-8 | Has grounds, but needs validation |
| 5-6 | Logical, but no data. A hypothesis. |
| 3-4 | Weak hypothesis, many unknowns |
| 1-2 | Guessing |

**In V1, confidence is usually 4-6 for most dimensions.** 9-10 in V1 is a red flag (overconfidence).

**Identifying the riskiest:**
- The lowest confidence
- If several are tied — the one with the higher Failure Impact (see defaults in `references/<lang>/stage-3-synthesis.md`)

Record: **"Riskiest dimension: [name] (confidence: X/10, impact: Y)"**

---

## Step 1.6 — Document Generation

**Ask the user:**
- Structured or prose format?
  - Structured (`template-narrative.md`) — for your own work and the team, easier to update
  - Prose (`template-narrative-prose.md`) — for stakeholders and investors

Load the template, fill it, save as `narrative-v1.md` in the project folder.

Mandatory sections:
1. Metadata (product, type, context, date, version V1)
2. Version History (for V1: "Initial hypothesis")
3. Team Pre-Flight Check (with risk flag)
4. 1-7 dimensions
5. Validation Status table (7 rows, for V1 confidence + "riskiest" mark, evidence empty)
6. Recommended next step: "Stage 2 (Market Research) for the risk-dimension first"

---

## Quality gates for Stage 1

Before closing Stage 1:

- [ ] All 7 dimensions worked through (no "we forgot Timing")
- [ ] Problem does not mention the product
- [ ] Audience has 2-3 defining attributes (not demographics)
- [ ] Value prop = benefits, not features
- [ ] Competitive Advantage = one of the 7 Powers with rationale
- [ ] Growth: short-term ≠ long-term, both concrete
- [ ] Business model has at least rough number estimates
- [ ] Timing — a concrete triggering event
- [ ] Confidence recorded for every dimension
- [ ] Riskiest explicitly identified
- [ ] Multi-role handled (if B2B or Marketplace)
- [ ] Team pre-flight check done

---

## Common pitfalls in Stage 1

| Mistake | Symptom | Fix |
|--------|---------|------|
| Solution-framed problem | "Our product does not exist" | Frame what is in the user's way independently of your product |
| Audience = demographic | "Women 25-45" | Find a **behavioral** attribute |
| Features in value prop | "Integration with 5 marketplaces" | Reframe as a benefit: "No tab-switching needed" |
| Generic competitive advantage | "Best team" | One of the 7 Powers with a concrete mechanism |
| Same channel short+long | "SEO" in both horizons | Split: what works at 100 users vs 100K |
| Pricing without rationale | "$29/mo — standard" | Where does $29 come from? What confirms the audience will pay? |
| Timing = "AI everywhere" | Generic hype | A concrete triggering event |
| Confidence 9-10 in V1 | "We are sure" | Lower it. V1 is a hypothesis, not a fact |
| Ignoring multi-role in B2B | One set of dimensions | Decision Makers ≠ End Users — two sets |
| Skipping team pre-flight | "We are fine" | Ask the 3 questions anyway — it is context |
