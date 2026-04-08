# Stage 4 — Validate / DVF

**Goal:** take the riskiest dimension from risk-prioritization, decompose it into 9 assumptions across DVF (Desirability × Viability × Feasibility), prioritize via a 2×2 (importance × evidence), and design an experiment for the riskiest assumption.

**Reads:** `narrative-v2.md`, `risk-prioritization.md`
**Writes:** `assumptions-map.md`, `experiment-brief.md`

**Methodology:** David Bland, *Testing Business Ideas*. Full DVF description — `references/<lang>/dvf-framework.md`.

---

## ⛔ Terminology

In Stage 4 we use **"assumption"**, not "hypothesis."

**Why:** methodologically in the DVF framework, an assumption is a concrete testable statement "I believe X." A hypothesis is a larger construct (the whole dimension is a hypothesis). Stage 4 unfolds the hypothesis into 9 assumptions for a specific dimension.

Do not mix them. In the narrative — hypothesis. In assumptions-map — assumption.

---

## ⛔ Tone

Calm, coaching. No exclamation marks. No dramatization. Do not ask clarifying questions before generating — generate the first draft right away, then refine.

---

## Step 4.1 — Read the risk-dimension

From `risk-prioritization.md` extract:
- The name of the riskiest dimension
- The V2 wording of this dimension from narrative-v2
- Risk score + reasoning
- What data already exists (from market research)

---

## Step 4.2 — Extract: 9 assumptions

Decompose the risk-dimension into 9 assumptions, 3 per DVF category.

### Desirability assumptions (3)

**What they are:** assumptions about user needs ONLY. Nothing about money, nothing about whether it can be built.

**Format:** "I believe that [users / segment] [action / attitude / behavior]"

**Examples:**
- "I believe that small e-commerce sellers spend 4-6 hours a week manually copying orders"
- "I believe these sellers are willing to try a new tool if it saves at least 2 hours a week"
- "I believe these sellers prefer a table-style interface over a CRM-style one"

### Viability assumptions (3)

**What they are:** assumptions about money ONLY. Pricing, willingness to pay, unit economics, LTV, CAC, costs.

**Format:** "I believe that [financial statement]"

**Examples:**
- "I believe these sellers are willing to pay $29/mo for this tool"
- "I believe CAC via cold outreach will be $150 with LTV of $500"
- "I believe 30% of trial users will convert to paid in the first 14 days"

### Feasibility assumptions (3)

**What they are:** assumptions about operational + technical + regulatory.

**Format:** "I believe that we can [build / launch / comply]"

**Examples:**
- **Operational:** "I believe we can support 100 customers with a team of 2"
- **Technical:** "I believe the marketplace APIs are stable enough for real-time sync"
- **Regulatory:** "I believe storing sales data does not require a special license"

### Regulatory sub-check

If the product type from setup = AI / fintech / healthtech → automatically add at least 1-2 regulatory assumptions to Feasibility:

- AI: data privacy, model compliance, AI Act if EU
- Fintech: licensing, KYC/AML, payment processing
- Healthtech: HIPAA / GDPR-medical, FDA if US, ML medical device classification

These are **not extra** assumptions — they live **inside** the 3 Feasibility ones, replacing operational/technical when regulatory matters more.

### DVF Tension Check

After generating 9 assumptions — look at the **biggest conflicts between categories**:

- Desirability says "they want X" + Viability says "but they do not pay for X"
- Desirability says "they love simplicity" + Feasibility says "but simplicity requires backend complexity"
- Viability says "$29/mo works" + Desirability says "they are used to free tools"

Write 1-2 sentences about the biggest DVF tension in `assumptions-map.md`. This is often = the riskiest assumption.

---

## Step 4.3 — Map: 2×2 importance × evidence

Place the 9 assumptions on a matrix:

```
        High Importance
              |
    [Critical]| [Sweet spot]
   weak       |       strong
  evidence ---+--- evidence
  [Distraction]| [Solid]
              |
        Low Importance
```

**Quadrants:**

| Quadrant | Meaning | Action |
|----------|------------|----------|
| **Critical** (high importance + weak evidence) | Riskiest. Without validation the product dies. | Test these first |
| **Sweet spot** (high importance + strong evidence) | Confirmed. | Do not touch, use as the foundation |
| **Solid** (low importance + strong evidence) | Confirmed but not critical. | Do not spend time |
| **Distraction** (low importance + weak evidence) | Not critical and no data. | Ignore for now |

**Importance scale:**
- **High:** if the assumption is wrong → the product does not work / economics do not add up / cannot be built
- **Low:** if the assumption is wrong → can be adapted without catastrophe

**Evidence scale:**
- **Strong:** there is data from market research, existing users, analogs
- **Weak:** no data, only a guess

**Write into assumptions-map.md** — a 9-row table with columns:
- Assumption text (verbatim)
- Category (D/V/F)
- Importance (high/low)
- Evidence (strong/weak)
- Quadrant
- Notes

**After placing them** — pick out **1-3 assumptions from the Critical quadrant** as candidates for an experiment.

---

## Step 4.4 — Test: experiment brief

For the **riskiest assumption** from the Critical quadrant — design an experiment.

**Experiment types** (standard, use only these names):

| Type | What it does | When to use |
|------|-----------|-----------------|
| **Customer Interview** | In-depth interview with the target audience | Desirability assumptions, behavior understanding |
| **Smoke Test** | Landing page + ad → measure interest (sign-ups) before the product is built | Desirability + Viability (intent to pay) |
| **Concierge** | Do the work by hand for 5-10 customers, simulating the product | Feasibility + Desirability together |
| **Survey** | A structured survey at scale | Desirability + Viability (willingness to pay) |
| **Prototype** | A clickable prototype with no real backend | Desirability (UX) + Feasibility (do we need a backend?) |
| **Landing Page** | A full landing page with a CTA | Demand validation, price testing |

**Do not invent new types.** The standard set covers 95% of cases.

### Experiment brief structure

```markdown
## Experiment Brief

**Assumption:** [verbatim from assumptions-map.md]

**What we'll learn:** [what exactly will be confirmed or refuted]

**Experiment type:** [one of the 6 standards]

**How to run:**
1. [step 1]
2. [step 2]
3. [step 3]

**How to measure:**
- **Success signal:** [concrete threshold] — if this result, the assumption is confirmed
- **Failure signal:** [concrete threshold] — if this result, the assumption is refuted
- **Inconclusive:** [in between] — if this result, the experiment needs to be repeated or redesigned

**Estimated effort:** [hours / days]

**Remaining uncertainty:** [what the experiment will NOT show — needs other methods]
```

**Example:**

```markdown
**Assumption:** "Small e-commerce sellers are willing to pay $29/mo for an order-sync tool"

**What we'll learn:** Confirm willingness to pay at a concrete price point. Not user interest (that is desirability), but readiness to open the wallet.

**Experiment type:** Smoke Test

**How to run:**
1. Build a landing page describing the product (3-5 benefits, screenshot mockup, social proof placeholder)
2. On the page — a Pricing block with one $29/mo plan. The "Start free trial" button leads to a form (email + Stripe Checkout with no charge — pre-authorize only)
3. Run $200 of cold ads on FB / IG targeted at e-commerce sellers in RU/UA/CIS

**How to measure:**
- **Success:** ≥3% landing → trial sign-up + ≥30% trial → entered card details. If 100 visitors give 3 sign-ups and 1 entered card details — pass
- **Failure:** <1% landing → trial OR <10% trial → entered card details
- **Inconclusive:** anything in between → redesign landing copy and repeat

**Estimated effort:** 8-12 hours to build the landing + 1 week of data collection

**Remaining uncertainty:** The experiment shows intent, but not retention. Retention needs a Concierge experiment with at least 5-10 users.
```

---

## Step 4.5 — Cross-loop

If the experiment requires **more data** before launching (for example, you need to know specific competitor pricing) — recommend a local return to Stage 2 (research) for one data point. Do not return entirely, only on one question.

If the experiment is **successful** → move to Stage 5 (Interview Prep) for the other risk-dimensions, or jump to Stage 8 (if everything is validated).

If the experiment **fails** → return to Stage 1 to rethink this dimension (Pivot or Reset).

---

## Quality gates for Stage 4

- [ ] Terminology held: "assumption" everywhere, not "hypothesis"
- [ ] 9 assumptions = exactly 3 per category (Desirability, Viability, Feasibility)
- [ ] Every assumption starts with "I believe..."
- [ ] Desirability assumptions are ONLY about user needs (no money or backend)
- [ ] Viability assumptions are ONLY about money
- [ ] Feasibility assumptions are about operational/technical/regulatory
- [ ] Regulatory sub-check done for AI/fintech/healthtech products
- [ ] DVF tension recorded (1-2 sentences)
- [ ] 2×2 map built, all 9 placed in quadrants
- [ ] Critical quadrant marked (1-3 candidate assumptions)
- [ ] Experiment brief done for the 1 riskiest
- [ ] Experiment type — one of the 6 standards, not invented
- [ ] Success/failure signals have concrete thresholds (not "many sign-ups")
- [ ] Estimated effort noted

---

## Common pitfalls in Stage 4

| Mistake | Symptom | Fix |
|--------|---------|------|
| "Hypothesis" terminology in Stage 4 | Mixed with the narrative | Only "assumption" |
| Desirability contains pricing | "They want this for $29/mo" | That is Viability. Desirability is only "want/do not want" |
| Viability contains UX | "They will buy if the design is pretty" | That is Desirability |
| 9 assumptions not balanced | 5 D + 2 V + 2 F | Must be strictly 3+3+3 |
| All assumptions in Sweet spot | "Everything is confirmed" | If everything is confirmed — Stage 4 is not needed. Most likely you underestimated importance |
| Distractions get researched | Time spent on low importance + weak evidence | Skip. Only Critical matters |
| Experiment without a quantitative threshold | "Lots of interest" | Concrete numbers: ≥3%, ≥10 sign-ups, etc. |
| Custom experiment type | "Mini-pilot", "Discovery sprint" | Only the 6 standards. If none fits — reframe |
| Skipping Map → straight to Test | No 2×2 | The Map is needed to pick the RIGHT assumption to test, otherwise the test is on a non-critical one |
| Ignoring regulatory for AI | Skip Feasibility regulatory | For AI it is mandatory: data privacy, AI Act, copyright |
