# Template — Metrics Dashboard

**Used in:** Stage 9 (Metrics)
**Save as:** `metrics-dashboard.md`
**Companion guides:** `references/<lang>/stage-9-metrics.md`, `references/<lang>/sean-ellis-survey.md`, `references/<lang>/levels-of-pmf.md`

**Purpose:** template + instructions for post-launch PMF measurement through 3 instruments: Sean Ellis 40% survey, retention cohorts, First Round Levels of PMF.

**⛔ The skill does NOT collect data.** It creates the template + instructions. The user collects.

---

## Template

```markdown
# Metrics Dashboard — [Product name]

**Date created:** YYYY-MM-DD
**Reads:** `narrative-v3.md`
**Status:** [Setup phase / Collection phase / Interpretation phase]

---

## What we are measuring

**Final hypothesis (V3):**
[Short wording of what we are validating — from narrative-v3]

**Target audience for measurement:**
[Who the active users are — from narrative-v3]

**Value proposition tested:**
[Main value prop wording — for interpreting Sean Ellis answers]

---

## 1. Sean Ellis Survey

**⛔ Do not rewrite the question. Do not change the answer order.**

### Question (ready to copy)

> How would you feel if you could no longer use [product name]?

### Answer options

| # | Option |
|---|----|
| 1 | Very disappointed |
| 2 | Somewhat disappointed |
| 3 | Not disappointed — it isn't really that useful |
| 4 | N/A — I no longer use [product] |

### Distribution rules

- **Active users only** (≥ 1 key action in the last 2 weeks)
- **In-context** — after a key action, not a massive reminder blast
- **Random sample**, not cherry-picked

**Recommended channel:** [in-product modal / email 1-2 hours after key action / other]

### Optional follow-up questions

1. Who would benefit most from this product?
2. What is the main benefit you get?
3. What needs to be improved?

### Results table (filled by the user)

| Date | Total responses | Very disappointed | Somewhat | Not disappointed | N/A | Score (excl N/A) |
|------|----------------|-------------------|----------|------------------|-----|------------------|
| YYYY-MM-DD | | | | | | % |
| YYYY-MM-DD | | | | | | % |

**Minimum 40 responses for a valid score.**

### Calculation

```
PMF score = Very disappointed / (Total - N/A) × 100%
```

### Interpretation

| Score | Status | Action |
|-------|--------|--------|
| < 25% | No PMF | Stage 1 (rethink) |
| 25-40% | Developing | Stage 7 (interview synthesis on "Somewhat disappointed") |
| 40-60% | Strong PMF | Scale via paid acquisition |
| > 60% | Extreme PMF | Defend via 7 Powers, scale supply |

---

## 2. Retention Cohorts

### Definition of "active" for this product

[Fill per product type:]
- B2B SaaS: ≥ 1 key action per week
- Consumer: ≥ 1 session per week or ≥ 3 per month
- High-frequency: ≥ 1 per day or ≥ 3 per week

**Our definition:** [concretely for this product]

### Cohort table (filled by the user)

| Cohort (week of signup) | Week 1 | Week 2 | Week 3 | Week 4 | Week 8 | Week 12 |
|------------------------|--------|--------|--------|--------|--------|---------|
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |

### Where to get the data

- [Tool: Mixpanel, Amplitude, custom DB query, etc.]
- [Concrete SQL/event filter if applicable]

### Interpretation guide

**Healthy retention curve:**
- Drops in the first 1-2 weeks, then **flattens**
- Strong PMF threshold:
  - Consumer: flatten at > 40%
  - B2B: flatten at > 60%
  - High-frequency: flatten at > 25%

**Unhealthy retention curve:**
- Falls monotonically toward 0% — the product does not stick
- "Smiley curve" (recovers after a month) — re-engagement works, but the initial onboarding is weak

---

## 3. Levels of PMF Assessment

| Level | Name | Satisfaction | Demand | Efficiency | Currently? |
|-------|------|--------------|--------|------------|-----------|
| 1 | **Nascent** | < 20% or no data | 1-10 users, manual acq | Manual everything | [ ] |
| 2 | **Developing** | 25-40% Sean Ellis | Partial flatten, 1-2 referrals/wk | Mixed manual/auto | [ ] |
| 3 | **Strong** | ≥ 40% Sean Ellis | Flat retention, ≥ 20% MoM organic | LTV/CAC > 3, payback < 12mo | [ ] |
| 4 | **Extreme** | > 60% Sean Ellis | Non-linear, supply-constrained | LTV/CAC > 5, payback < 6mo | [ ] |

**Rule:** the overall level = the minimum of the three dimensions.

### Evidence per dimension

**Satisfaction:**
- [What is measured: Sean Ellis %, NPS, retention rate]
- [Concrete numbers]

**Demand:**
- [What is measured: growth rate, organic %, conversion rate, waitlist size]
- [Concrete numbers]

**Efficiency:**
- [What is measured: CAC, LTV, payback period, support load]
- [Concrete numbers]

### Currently assigned level

**Level:** [1/2/3/4]
**Bottleneck dimension:** [satisfaction/demand/efficiency]
**Why this level (1-2 phrases):**
[reasoning]

### What is needed to reach the next level

[1-2 concrete steps from the levels-of-pmf.md table]

---

## Decision tree (Stage 10)

```
IF Level = Strong PMF and bottleneck = none:
  → Stage 10 (Iterate). Defend satisfaction, accelerate growth, start building a power.

IF Level = Developing:
  → Stage 7 (Interview synthesis on "Somewhat disappointed"). Close top blockers.

IF Level = Nascent:
  → Stage 4 (Validate). Validate assumptions deeper through interviews + experiments.

IF Level = Extreme:
  → Outside PMF skill scope. Scaling, hiring, expansion.
```

---

## Flow notes

Stage 9 unfolds over time:

1. **Setup phase** (1 session with the skill): this dashboard + instructions are created
2. **Collection phase** (4-12 weeks, no skill): the user collects the data
3. **Interpretation phase** (1 session with the skill): you come back with the filled dashboard, the skill interprets and recommends Stage 10

**Status now:** [Setup / Collection / Interpretation]

**Next checkpoint:** [when you plan to fill the data and come back]
```

---

## ⛔ What NOT to do when using this template

| Don't | Why |
|-------|-----|
| Simulate data | The skill creates a template, not data. Numbers come from the user |
| Sean Ellis on the newsletter list | Selection bias |
| Treat < 40 responses as a valid score | Statistical noise |
| Rewrite the Sean Ellis question | That is no longer Sean Ellis |
| Overall retention rate without cohorts | Hides falling over time |
| "We are at Strong because revenue is growing" | Revenue ≠ fit. You can grow with CAC > LTV |
| Self-assess Level without evidence | Wishful thinking |
