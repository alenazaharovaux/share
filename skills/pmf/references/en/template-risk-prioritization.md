# Template — Risk Prioritization

**Used in:** Stage 3 (Synthesis)
**Save as:** `risk-prioritization.md`
**Companion guide:** `references/<lang>/stage-3-synthesis.md`

**Purpose:** turn findings from market research into a numerical risk score per dimension and identify the **riskiest dimension** for Stage 4 (Validate).

---

## Template

```markdown
# Risk Prioritization — [Product name]

**Date:** YYYY-MM-DD
**Reads:** `narrative-v1.md`, `market-research.md`
**Writes:** this file + `narrative-v2.md` (updated)

---

## Risk scoring formula

**Risk score = Failure impact × Uncertainty**

- **Failure impact (1–5):** if this dimension turns out to be wrong, how catastrophic the consequences are
  - 5 = product is dead, cannot adapt
  - 4 = a major pivot is needed
  - 3 = significant rework
  - 2 = adaptation within the current course
  - 1 = cosmetic

- **Uncertainty (1–5):** how much we do NOT know the right answer
  - 5 = team opinion only, zero data
  - 4 = indirect evidence from analogs
  - 3 = one data point or social proof
  - 2 = multiple confirmations from different sources
  - 1 = strong evidence from interviews / measured data

**Risk score range:** 1 (min) to 25 (max).

---

## Failure impact defaults (if not sure)

| Dimension | Default impact | Reasoning |
|-----------|---------------|-----------|
| 1. Customer | 5 | Wrong audience = everything else is meaningless |
| 2. Problem | 5 | No problem = no product |
| 3. Why now | 3 | Wrong timing — you can wait or accelerate |
| 4. Why us | 3 | Capability can be hired / acquired |
| 5. Solution | 4 | Solution shape can be iterated, but expensively |
| 6. Distribution | 4 | Without a channel there is no growth |
| 7. Business model | 4 | Pricing iterates, but the base model is hard |
| 8. Power | 2 | Long-term, not fatal in the first 1-2 years |

---

## Risk table

| # | Dimension | V1 formulation (short) | Failure impact (1-5) | Uncertainty (1-5) | Risk score | Top reason for uncertainty |
|---|-----------|--------------------------|---------------------|-------------------|------------|---------------------------|
| 1 | Customer | [one phrase] | | | | [why uncertainty is high] |
| 2 | Problem | | | | | |
| 3 | Why now | | | | | |
| 4 | Why us | | | | | |
| 5 | Solution | | | | | |
| 6 | Distribution | | | | | |
| 7 | Business model | | | | | |
| 8 | Power | | | | | |

**Sort by Risk score descending.** The riskiest is on top.

---

## Cross-fit checks

After scoring, check the intersections of dimensions — sometimes individual dimensions look safe, but their combination does not.

### Channel × Business Model fit

**Question:** does cost-per-acquisition in the chosen channel match the target unit economics?

| Channel | Typical CAC range | Compatible with pricing $X? |
|---------|-------------------|--------------------------|
| Cold outreach | $20-200 | [yes/no] |
| Paid search | $50-300 | |
| Content marketing | $10-100 (long-term) | |
| Partnerships | $0-50 | |

If channel CAC > LTV margin → cross-fit risk is high, add +1 to the Distribution Risk score.

### Solution × Customer fit

**Question:** does the solution shape match the real customer behavior?

- If customer = enterprise but solution = self-serve sign-up → mismatch
- If customer = consumer but solution = manual onboarding → mismatch
- If customer = mobile-first but solution = desktop-only → mismatch

If a mismatch is found → +1 to the Solution Risk score.

### Why now × Distribution fit

**Question:** do the channels we picked work in the current market cycle?

- If Why now = "AI became accessible" but Distribution = "cold email" → the channel does not use the timing
- If Why now = "a new law mandates X" but Distribution = "content marketing" → the channel is too slow for the urgency

---

## Riskiest dimension

**Selected for Stage 4:** [dimension name]

**Risk score:** [number]

**Why this is the riskiest:**
[2-3 phrases about what is unknown and why the impact is high]

**What Stage 4 will validate:**
[Which main question Stage 4 will resolve]

---

## Updates to the narrative

**Dimensions to revise in narrative-v2:**

| Dimension | What changes |
|-----------|--------------|
| [Dim 1] | [how to reformulate after research] |
| [Dim 2] | |

**Persona divides to add:**
- [new exclusions seen in the research]

**New evidence sections:**
- [which dimensions got Strong evidence]

---

## Decision tree (what to do next)

```
IF top 1 risk score ≥ 16:
  → Critical risk. Stage 4 (Validate) is mandatory before any further investment.

IF top 1 risk score 10-15:
  → Significant risk. Stage 4 recommended, but you can start Stage 5 (Interview Prep) in parallel.

IF top 1 risk score 6-9:
  → Manageable risk. You can go straight to Stage 5 (Interview Prep), skipping Stage 4.

IF top 1 risk score ≤ 5:
  → Low risk overall. Suspect overconfidence. Re-check uncertainty scores.
```
```

---

## Common mistakes

| Mistake | Symptom | Fix |
|--------|---------|------|
| All scores = 3 | "Average everywhere" | 1-5 — force yourself to differentiate |
| Failure impact = 1 for all | We think everything can be adapted | 5 of 8 dimensions have default ≥ 3 — that is not random |
| Uncertainty = 1 for favorite dimensions | Wishful thinking | If the evidence is not from interviews/measurement, do not put 1 |
| Skip cross-fit | Pairs of dimensions not checked | Cross-fit is mandatory — that is where hidden risks often live |
| Outsource the Stage 4 vs 5 decision | "I don't know, validate or interview?" | Use the decision tree |
