# Levels of PMF — First Round Capital framework

**Source:** First Round Capital, *The Levels of Product/Market Fit (& What to Focus on at Each)*. Authors — Todd Jackson, Brian Rothenberg, Carolyn Stein. Published in First Round Review.

**Why:** PMF is not a binary "have/have not" state, it is a 4-level ladder. Each level demands different metrics, different priorities, and different kinds of work. Teams often think PMF either exists or does not — and because of that they take wrong actions (scaling prematurely or sitting on an achievable level).

**When applied:** Stage 9 (Metrics) once Sean Ellis and retention cohorts are collected, to determine **where exactly** on the ladder the product is.

---

## 4 levels

### Level 1 — Nascent PMF

**What it means:** there are a few early adopters for whom the product is genuinely useful, but everything is held together by manual work from the founder/team. There is no repeatable acquisition process. Retention signals are too small for statistics.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | < 20% Sean Ellis Very disappointed (or no 40 responses to measure yet) |
| Demand | 1-10 active users, ~0 organic growth, manual acquisition (founder outreach, friends) |
| Efficiency | Manual everything: onboarding, support, billing. Does not scale. |

**What to do at this level:**
- Do NOT scale
- Do NOT raise large rounds
- In-depth interviews with these 1-10 users
- Concierge-level service (answer personally, fix bugs in an hour)
- Goal: understand for **whom** specifically it works and **why**

**Anti-pattern:** launching paid ads at this level. Acquisition without retention = a leaky bucket.

---

### Level 2 — Developing PMF

**What it means:** there are signals of repeatable demand. A few cohorts of retention start to flatten (do not fall to zero). Sean Ellis is between 25-40%. Word of mouth has started but it is weak — 1-2 referrals a week.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis 25-40% Very disappointed at ≥ 40 responses |
| Demand | Retention of the first cohorts partly flattens, 1-2 organic referrals/week, growth unstable |
| Efficiency | Some processes are automated, but customer success is still manual |

**What to do at this level:**
- Deepen the understanding of the "Very disappointed" segment (Superhuman PMF Engine)
- Segment the "Somewhat disappointed" — what blocks them from becoming "Very disappointed"
- Close the top-3 blockers from interviews
- Start experimenting with acquisition channels, **but carefully** — at this level CAC is usually > LTV
- Goal: drive Sean Ellis to 40%+ via product improvements, not via redefining the metric

**Anti-pattern:** running a growing features roadmap. At Level 2 you do not need features, you need fit. Less new, more polishing of what is there.

---

### Level 3 — Strong PMF

**What it means:** Sean Ellis ≥ 40%. Retention flattens at a healthy level (> 40% consumer / > 60% B2B / > 25% high-frequency). Customers say they cannot live without the product. Organic word of mouth becomes a measurable channel. The team feels "pull" — demand outruns capacity.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis ≥ 40%, NPS ≥ 30, customers actively use it > 3 times/week |
| Demand | Retention flattens, organic growth ≥ 20% MoM, there is a waitlist or organic inbound, trial→paid conversion > 25% |
| Efficiency | CAC payback < 12 months, LTV/CAC > 3, support load grows linearly not exponentially |

**What to do at this level:**
- Scaling is OK: paid acquisition with positive economics
- Hire a growth team (not earlier)
- Raise Series A (if not already)
- Standardize processes (onboarding flows, support playbooks)
- Goal: expand acquisition without losing satisfaction. Defend Sean Ellis %, monitor monthly.

**Anti-pattern:** stop listening to users. The transition to Level 3 is the most dangerous moment for arrogance. Keep doing customer interviews monthly.

---

### Level 4 — Extreme PMF

**What it means:** a rare state. Non-linear growth. Customers evangelize without prompting. Supply (capacity, hiring, infrastructure) cannot keep up with demand. The press writes on its own. Competitors copy. Sean Ellis is often > 60%, retention curves are nearly horizontal.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis > 60%, customers literally write unsolicited testimonials, NPS ≥ 50 |
| Demand | Non-linear organic growth, long waitlists, press writes on its own, copies on social |
| Efficiency | LTV/CAC > 5, payback < 6 months, the constraint is supply, not demand |

**What to do at this level:**
- Scale supply: hiring, infrastructure, fundraising (Series B+)
- Defend against copying: 7 Powers (see `references/<lang>/7-powers.md`)
- Prepare for international expansion / adjacent markets
- Goal: do not break culture and quality during the spike

**Examples:** ChatGPT in its first 2 months, Slack 2014, Zoom March 2020, Notion 2019, Linear 2021. These are rare cases, not the norm.

**Anti-pattern:** hire too fast, lose product quality, lose culture. Most companies that hit Extreme PMF and failed — failed here, not at Level 1-3.

---

## 3 dimensions × 4 levels = an assessment matrix

Each level is evaluated on 3 dimensions: **Satisfaction, Demand, Efficiency**. A team cannot be at one level on one dimension and at another on another — that is most likely self-deception.

| Level | Satisfaction | Demand | Efficiency |
|-------|--------------|--------|------------|
| Nascent | < 20% or no data | 1-10 users, manual acq | Manual everything |
| Developing | 25-40% Sean Ellis | Partial retention flatten, 1-2 referrals/wk | Mixed manual/auto |
| Strong | ≥ 40% Sean Ellis | Flat retention curve, organic growth ≥ 20% MoM | LTV/CAC > 3, payback < 12mo |
| Extreme | > 60% Sean Ellis | Non-linear growth, supply-constrained | LTV/CAC > 5, payback < 6mo |

**Assessment rule:** the level is determined by the **minimum** dimension. If Satisfaction = Strong but Demand = Developing, the overall level = Developing. The weakest link defines the real position.

---

## How to assess level

**Step 1.** Collect data on the 3 dimensions:
- Satisfaction: Sean Ellis (Stage 9, primary), NPS if available
- Demand: retention cohorts, growth rate (MoM), conversion rate, organic %
- Efficiency: CAC, LTV, payback period, support load

**Step 2.** For each dimension, determine the level from the table above.

**Step 3.** The overall level = the minimum of the three.

**Step 4.** Write into `metrics-dashboard.md`:
- Current level
- Which dimension is the bottleneck
- What is needed to move to the next level (one or two concrete steps)

---

## What is needed to move up a level

| Current → Next | Main change |
|---------------------|-------------------|
| Nascent → Developing | Segment the first users, find a repeating pattern. Usually 5-10 interviews in Stage 7 + an iteration in Stage 4 |
| Developing → Strong | Close the top-3 blockers from the "Somewhat disappointed" segment. Move Sean Ellis from ~30% to ≥ 40% via product improvements |
| Strong → Extreme | Strengthen a power (see 7 Powers), often = network effects or counter-positioning. Cannot be forced — the product either has potential for Extreme or it does not |

**Important:** Strong PMF is **enough** for a profitable business. Not every product can be Extreme. It does not have to be. Strong PMF = most successful SaaS, marketplaces, B2B tools.

Extreme PMF is a venture-scale outcome, and it is rare. ~5% of products that reached Strong ever reach Extreme.

---

## Common mis-assessments

| Mistake | What it looks like | How to avoid |
|--------|--------------|--------------|
| "We are at Strong because 200 paying" | Volume ≠ fit. 200 paying with 10% retention = Nascent | Look at the retention curve, not the absolute numbers |
| "We are at Strong because Sean Ellis 45%" | Only satisfaction measured | All 3 dimensions are mandatory |
| "We are at Extreme because press writes about us" | Hype ≠ retention | Press without retention = vanity. What is in the retention cohorts? |
| "We are at Developing because revenue is growing" | Growth ≠ fit. You can grow with CAC > LTV | Look at unit economics |
| "We have been at Nascent for a year" | Maybe Developing signs are hidden inside a segment | Segment the users — maybe one segment is already Strong, others Nascent |
| "We are at Strong but Sean Ellis is 25%" | Self-deception by redefining | Do not redefine the threshold. 40% is not for decoration |

---

## Connection to Stage 10 (Iterate)

The level decides the **next action**:

- **Nascent → Stage 4** (Validate): validate assumptions deeper through interviews, do not launch new features
- **Developing → Stage 7** (Interview synthesis): deepen understanding of the "Very disappointed" segment and the blockers of "Somewhat disappointed"
- **Strong → Stage 10** (Iterate): defend satisfaction, strengthen growth channels, start building a power
- **Extreme → outside the scope of the PMF skill**: scaling, hiring, expansion — no longer a PMF task

This decision tree is generated automatically in `metrics-dashboard.md` (see `references/<lang>/template-metrics-dashboard.md`).
