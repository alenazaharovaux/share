# Stage 3 — Synthesis

**Goal:** based on market research, do risk scoring, identify the riskiest dimension, run a cross-fit analysis, and update the narrative to V2.

**Reads:** `narrative-v1.md`, `market-research.md`
**Writes:** `risk-prioritization.md`, `narrative-v2.md`

---

## Step 3.1 — Per-dimension analysis

For each dimension, lock in:

1. **V1 hypothesis** — what was written in narrative-v1
2. **Evidence summary** — what the research showed (analogs + antilogs)
3. **Confidence change** — V1 score → V2 score
4. **Update type:**
   - **Validated** — data confirms, wording stays
   - **Refinement** — data sharpens, minor edits
   - **Pivot** — data contradicts, a different wording is needed
   - **Reset** — no data or fully refuted, a new hypothesis is needed
5. **V2 hypothesis** — updated wording (if it changed)

---

## Step 3.2 — Risk scoring

**Formula:**
```
Risk Score = (10 - Evidence Score) × Failure Impact
```

**Evidence Score** — how strongly the data supports the dimension (1-10).

**Failure Impact** — how catastrophic it would be if this dimension turned out to be wrong (1-4).

**Failure Impact defaults:**

| Dimension | Default Impact | Why |
|-----------|---------------|---------|
| Problem to Solve | 4 (Critical) | If there is no problem — there is no product. Cannot recover |
| Business Model | 4 (Critical) | If the economics do not add up — the company dies. Hard to recover |
| Target Audience | 3 (High) | Repositioning is possible, but expensive |
| Growth Strategy | 3 (High) | Channels can be changed, but time is lost |
| Timing / Why Now | 3 (High) | If you are late — you are late. If you are early — you need stamina |
| Value Proposition | 2 (Medium) | Messaging can be rewritten, iteratively |
| Competitive Advantage | 2 (Medium) | A moat is built over years, matters long-term, does not kill at the start |

**Defaults can be recalibrated** for a specific product if there is a reason. For example, in a regulated industry Feasibility is more important than Audience (a regulatory failure = death).

**Risk Score Table:**

| Dimension | Evidence Score (1-10) | Failure Impact (1-4) | Risk Score | Rank |
|-----------|----------------------|----------------------|------------|------|
| Problem to Solve | 7 | 4 | 12 | 3 |
| Target Audience | 4 | 3 | 18 | 1 |
| Value Proposition | 6 | 2 | 8 | 5 |
| Competitive Advantage | 5 | 2 | 10 | 4 |
| Growth Strategy | 5 | 3 | 15 | 2 |
| Business Model | 8 | 4 | 8 | 5 |
| Timing / Why Now | 7 | 3 | 9 | 6 |

(Example, not real numbers)

**Riskiest dimension** = highest risk score. If several are tied — pick the one with the higher failure impact.

---

## Step 3.3 — Cross-fit analysis

Two mandatory consistency checks between dimensions:

### Channel-Model Fit

**Question:** do the growth channels work with the business model?

**Conflict examples:**
- Enterprise sales + freemium pricing → impossible (a sales rep needs a $20K+ deal to justify salary)
- Cold outreach + low-ACV product ($10/mo) → CAC is higher than LTV
- Viral / WOM + high-touch onboarding → the viral channel pulls unqualified leads, overloads onboarding
- SEO + new-category product → no search volume, because the audience does not yet know what to look for
- Paid ads + low gross margin → CAC always overtakes
- Product-led growth + a complex enterprise sales cycle → different worlds

**If a conflict is found:** record it → Stage 4 fix or return to Stage 1

### Model-Market Fit

**Question:** does the business model work for this target audience?

**Conflict examples:**
- Subscription SaaS + small e-commerce sellers (not used to paying for software monthly)
- High pricing + students / early-career professionals
- Marketplace take rate of 15%+ + low-margin commodity goods
- Pay-per-use + an audience that wants a predictable budget
- Annual contract + an audience with 6 months of runway
- Self-serve + an audience without technical expertise (needs sales support)

**If a conflict is found:** same way — record it and decide.

---

## Step 3.4 — Update narrative V1 → V2

Create `narrative-v2.md` from `narrative-v1.md` + the changes:

**Mandatory changes in V2:**
- Date updated
- Version: V2
- In Version History — a section "V2: After Market Research (date)" with a changelog (what exactly changed vs V1)
- Each dimension: updated wording + new confidence score
- If update type = Pivot or Reset — explicitly mark "PIVOTED" / "RESET" next to the dimension
- Validation Status table updated: actual evidence (not empty as in V1)
- Recommended next step: "Stage 4 (Validate) for risk-dimension: [name]" or "Stage 5 (Interviews)" if confidence is already high

**Do NOT overwrite narrative-v1.md.** V2 is a separate file. V1 stays for history and comparison.

---

## Step 3.5 — Create risk-prioritization.md

From the template `references/<lang>/template-risk-prioritization.md`. Must contain:

1. Metadata (date, narrative version)
2. Evidence sources (market research, optional expert notes)
3. Risk Scoring Table (formula + 7 rows)
4. Riskiest Dimension section (name + explanation)
5. Cross-Fit Analysis (Channel-Model, Model-Market)
6. Per-Dimension Analysis (V1 hypothesis → evidence → confidence change → update type → V2 hypothesis)
7. Recommended Next Steps (decision tree below)

---

## Step 3.6 — Decision tree (what to do after Stage 3)

| Condition | Recommended next |
|---------|------------------|
| Overall confidence > 7 + a concrete risk-dimension | Stage 4 (validate riskiest) or jump to Stage 5 (interviews) if confidence in the DVF assumptions is there |
| Overall confidence 5-7 | Stage 4 mandatory |
| Overall confidence < 5 | Return to Stage 1 (rethink) or Stage 2 (more research) |
| Cross-fit conflict found | Return to Stage 1 to rethink the conflicting dimensions |
| Pivot/Reset on one dimension | Local return: rewrite that dimension in V2, then continue |
| Pivot/Reset on 2+ dimensions | Full return to Stage 1 |

Record the recommendation in `risk-prioritization.md` and propose it to the user.

---

## Quality gates for Stage 3

- [ ] All 7 dimensions have an evidence score
- [ ] All 7 dimensions have a failure impact (default or recalibrated with rationale)
- [ ] Risk Score calculated for each
- [ ] Riskiest dimension explicitly identified
- [ ] Update type (Validated/Refinement/Pivot/Reset) noted for each
- [ ] Cross-Fit Analysis: both checks done (Channel-Model + Model-Market)
- [ ] Narrative V2 created as a separate file (not overwriting V1)
- [ ] Version History in V2 contains a changelog
- [ ] Recommended next step matches the decision tree

---

## Common pitfalls in Stage 3

| Mistake | Symptom | Fix |
|--------|---------|------|
| Overwriting V1 | narrative-v1.md gets lost | V2 is a separate file |
| Not letting confidence drop when data contradicts | V2 confidence ≥ V1 for every dimension | If data contradicts — confidence MUST drop |
| Skipping cross-fit analysis | Only risk scoring | Cross-fit is mandatory — fatal conflicts often hide there |
| Default impact without rationale | Just copied | If you recalibrated — explain why |
| Riskiest = first in the list | No calculation | Compute the formula for each, pick the highest |
| Pivoting everything at once | "All dimensions need redoing" | Reset on 2+ dimensions = a signal you need Stage 1, not local edits |
| Ignoring confidence change | V1 → V2 with no explicit deltas | Each dimension must show a confidence delta + reason |
