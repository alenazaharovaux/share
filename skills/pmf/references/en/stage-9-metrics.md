# Stage 9 — Metrics

**Goal:** set up post-launch PMF measurement through 3 instruments: Sean Ellis 40% survey, retention cohorts, First Round Levels of PMF.

**Reads:** `narrative-v3.md`
**Writes:** `metrics-dashboard.md`

---

## ⛔ Critical rules for Stage 9

1. **The skill does NOT collect data.** It creates a template + collection instructions. The user collects (a minimum of 40 Sean Ellis responses takes weeks).

2. **Distribute Sean Ellis only to active users**, not the newsletter list. Active = actually used the product ≥ 1 time in the last 2 weeks.

3. **Minimum 40 responses for Sean Ellis.** Less than that — statistically meaningless.

4. **Analyze retention by cohorts**, not by overall average. The overall average hides retention falling over time.

5. **Use the 3 instruments together**, not just one. Sean Ellis + retention + Levels — each lights up a different facet.

---

## Step 9.1 — Read narrative V3

From narrative-v3.md extract:
- Final hypothesis (V3) — what we will measure
- Target audience definition — who Sean Ellis is sent to
- Value proposition — to interpret Sean Ellis answers
- Needed to make sure the metrics measure what we are validating

---

## Step 9.2 — Sean Ellis Survey setup

**Full instructions:** `references/<lang>/sean-ellis-survey.md`.

**Quick reference:**

**The question (exact wording):**
> "How would you feel if you could no longer use [product]?"

**Answer options:**
1. Very disappointed
2. Somewhat disappointed
3. Not disappointed — it's not very useful
4. I no longer use [product] (N/A)

**Threshold:** ≥ 40% picking "Very disappointed" (excluding N/A) = PMF.

**Distribution:**
- Active users only
- In the context of usage (in-product modal, email after a key action)
- Not a massive reminder blast

**Extra questions (optional but recommended):**
- "Who would benefit most from this product?" (helps sharpen the target)
- "What is the main benefit you get?" (helps sharpen the value prop)
- "What needs to be improved?" (helps prioritize the roadmap)

**Minimum:** 40 responses. Better 100+.

---

## Step 9.3 — Retention Cohorts setup

**Quick reference:**

**What to collect:**
- For every user — date of first action + date of every following session (or key action)
- Cohort = users who signed up in the same week
- Track what % of the cohort came back in week 2, 3, 4, 5, 8, 12

**Cohort table format:**

| Cohort | Week 1 | Week 2 | Week 3 | Week 4 | Week 8 | Week 12 |
|--------|--------|--------|--------|--------|--------|---------|
| Jan W1 | 100% | 60% | 50% | 45% | 42% | 40% |
| Jan W2 | 100% | 65% | 55% | 50% | 47% | 45% |
| ... | | | | | | |

**PMF signal:**
- **Healthy retention:** the curve flattens at some %, does not fall to zero
- **Unhealthy retention:** the curve drops monotonically, does not stabilize
- **Strong PMF:** flatten at > 40% for consumer / > 60% for B2B / > 25% for high-frequency

**What defines "active":**
- B2B SaaS: ≥ 1 key action per week
- Consumer: ≥ 1 session per week or ≥ 3 per month
- High-frequency (social, chat): ≥ 1 per day or ≥ 3 per week
- Depends on the expected usage frequency

---

## Step 9.4 — First Round Levels of PMF

**Full instructions:** `references/<lang>/levels-of-pmf.md`.

**Quick reference (4 levels):**

| Level | Name | Signals |
|-------|------|---------|
| 1 | **Nascent** | A few early adopters, manual everything, no clear retention signal yet |
| 2 | **Developing** | Some signals (Sean Ellis 25-40%, retention partly flatten, 1-2 word-of-mouth referrals/week), but not stable |
| 3 | **Strong** | Sean Ellis ≥ 40%, retention flattens at a healthy level, organic WOM growth, customers cannot live without |
| 4 | **Extreme** | Non-linear growth, hype, customers evangelize without prompting, supply cannot keep up with demand |

**Each level is determined by 3 signals:**
- **Satisfaction** — Sean Ellis %, NPS, retention rate
- **Demand** — growth rate (organic), waitlist if any, conversion rate
- **Efficiency** — CAC payback, LTV/CAC ratio, support load

**Write into metrics-dashboard.md:** which level we are at now, what is needed for the next, evidence for each signal.

---

## Step 9.5 — Create metrics-dashboard.md

From the template `references/<lang>/template-metrics-dashboard.md`.

Structure:
1. Metadata (date, narrative version V3+)
2. **Sean Ellis Survey:**
   - Question text (ready to copy into a form)
   - Distribution instructions
   - Results table (filled by the user)
   - Calculation of % Very disappointed
   - Interpretation
3. **Retention Cohorts:**
   - Definition of "active" for this product
   - Cohort table template (5-10 rows)
   - What to fill (where the data comes from)
   - Interpretation guide (flatten / fall)
4. **Levels of PMF Assessment:**
   - 4 rows (one per level) with criteria + checkbox + evidence
   - Final assigned level
5. **Recommended next** (decision tree from stage-10):
   - PMF achieved → scale
   - Promising signals → iterate (Stage 4 or Stage 7)
   - Weak signals → rethink (Stage 1)

---

## Step 9.6 — Flow

**Not a one-shot.** Stage 9 unfolds over time:

1. **Setup phase** (1 session with the skill): create the metrics-dashboard.md template + instructions
2. **Collection phase** (4-12 weeks, no skill): the user collects the data on their own
3. **Interpretation phase** (1 session with the skill): the user comes back with a filled metrics-dashboard, the skill interprets and recommends Stage 10

When resuming Stage 9: check whether metrics-dashboard.md is filled (has numbers, not placeholders). If not — keep waiting. If yes — move to interpretation.

---

## Quality gates for Stage 9

- [ ] Sean Ellis question in the Sean Ellis wording (not rewritten)
- [ ] Distribution explicitly limited to active users
- [ ] Minimum 40 responses noted as a requirement
- [ ] Cohort table structure correct (cohort × weeks)
- [ ] "Active" definition fits the product type
- [ ] Levels of PMF — 4 rows with concrete signals
- [ ] Decision tree links the results to Stage 10
- [ ] The skill does NOT simulate or invent data itself

---

## Common pitfalls in Stage 9

| Mistake | Symptom | Fix |
|--------|---------|------|
| Sean Ellis on the newsletter list | 5% Very disappointed | Distribution only to active users |
| < 40 responses | "We have 12 responses, fine" | Wait. < 40 = noise |
| Rewriting the Sean Ellis question | "How likely are you to recommend..." | That is NPS, not Sean Ellis. Use the original wording |
| Overall retention rate | "We have 50% retention" | By cohort. 50% — over a month or all time? |
| Only Sean Ellis, no retention | 45% Very disappointed = "we have PMF" | Sean Ellis is fooled by selection bias. Retention cohort is mandatory |
| "We are at Level 3" with no evidence | Wishful thinking | Each level needs evidence on 3 signals |
| Ranking users by revenue for Sean Ellis | "We asked the top 10%" | Distribution is a random sample of active users, not cherry-picked |
| Retention 7 days vs 30 days confusion | "Retention 80%" (per day) | State the window: D1, D7, D30, W4, M3 |
| The skill generates fake data | "Let's say Sean Ellis is 47%" | The skill creates a template, not data. Data is from the user |
