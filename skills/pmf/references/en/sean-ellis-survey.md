# Sean Ellis Survey — the 40% PMF benchmark

**Source:** Sean Ellis, founder of GrowthHackers (the term "growth hacker" is his). He published the method in 2009 in response to the question "how do we know we have PMF?" — before that, PMF was felt out by intuition.

**Why:** a one-question survey that, over 5 years, accumulated data from hundreds of startups and showed a stable threshold: **≥ 40% "very disappointed" = PMF; < 40% = not yet PMF**.

**When applied:** Stage 9 (Metrics) after the product launch, when there are at least 40 active users who used the product ≥ 1 time in the last 2 weeks.

---

## Exact wording

> How would you feel if you could no longer use [product name]?

**4 answer options (in this order):**

| # | Option |
|---|----|
| 1 | Very disappointed |
| 2 | Somewhat disappointed |
| 3 | Not disappointed — it isn't really that useful |
| 4 | N/A — I no longer use [product] |

**⛔ Do not rewrite the question.** Any reframing ("how much do you value", "how likely are you to recommend") turns the survey into a different instrument — NPS, CSAT, satisfaction score. Sean Ellis only works in the original wording because it measures **emotional withdrawal**, not satisfaction.

**⛔ Do not change the order of the answers.** The order from positive to negative in the visual form systematically changes the distribution.

---

## The 40% threshold

**Calculation:**
1. Exclude N/A (option 4) from the denominator — they are not active users
2. Compute the % of "Very disappointed" out of the remaining responses
3. ≥ 40% = PMF signal; 25–40% = developing PMF; < 25% = no PMF yet

**Formula:**
```
PMF score = (Very disappointed responses) / (Total responses - N/A responses) × 100%
```

**Example:**
- 100 responses in total
- 15 N/A (no longer using)
- 38 "Very disappointed"
- PMF score = 38 / (100 - 15) = 38 / 85 = 44.7% → PMF signal

**Where 40% comes from:** Sean Ellis collected data from ~100 startups he consulted to and found that companies at ≥ 40% "Very disappointed" could scale through paid marketing with positive economics. Those at < 40% either hit a plateau after the first wave or could not earn back CAC. 40% is an empirically confirmed threshold, not a theoretical one.

**Known exceptions:** some viral consumer products reached PMF at 30-35% (compensated by organic growth). Some niche B2B products needed > 50% because the target audience is small and random churn is dangerous.

---

## Distribution rules — who and where

**Who to send it to:**
- **Active users only.** Active = actually used the product ≥ 1 time in the last 2 weeks. Not newsletter subscribers, not trial without activation, not registered but never used.
- **Random sample**, not cherry-picked. Not "let's ask the top 10% by revenue" — that gives a fake high score. Not "let's ask people who left positive feedback" — the most common mistake.

**When to send it:**
- **In context, after a key action.** In-product modal after the user completed the task. Email 1-2 hours after a key action.
- **Not a massive reminder blast** after 6 months of silence.

**Channel:**
- In-product modal (best response rate, ~30-50%)
- Email 24 hours after a key action (~10-20%)
- On the login page (~5-10%, biased toward active)

---

## Minimum 40 responses

**Rule:** fewer than 40 responses = statistical noise, do not use for decisions.

**Why:** 40 = the minimum for a reasonable confidence interval on a binary metric (Very disappointed vs the rest). At 40 responses ±15% confidence; at 100 responses ±10%; at 400 responses ±5%.

**If you have 12 responses and 6 "Very disappointed"** — that is **not** "50% PMF." That is "not enough data." Wait.

**If active users < 40 over 2 weeks:**
- Too early for Sean Ellis
- Use only qualitative interviews (Stage 5–7)
- Come back in a month

---

## Extra questions (optional but recommended)

After the main question it is useful to add 3-4 follow-ups:

1. **"Who would benefit most from this product?"**
   Sharpens the target audience through the words of real users. The description is often better than what the team wrote.

2. **"What is the main benefit you get?"**
   Sharpens the value proposition. Users often describe the benefit differently than the team.

3. **"What needs to be improved?"**
   Helps prioritize the roadmap, especially answers from "Somewhat disappointed" — they are potential future "Very disappointed" if the blocker is removed.

4. **"How did you hear about [product]?"** (if not tracked separately)
   Confirms the channels with the best product-market fit.

These 4 questions are not required to compute the PMF score, but they turn the survey from a measurement tool into an insight tool.

---

## Interpretation

| Score | Meaning | Action |
|-------|-----------|----------|
| < 25% | No PMF | Return to Stage 1 — rethink target audience and/or value proposition |
| 25–40% | Developing | Stage 7 (interview synthesis) on the "Somewhat disappointed" — what blocks them from becoming "Very disappointed" |
| 40–60% | Strong PMF | You can scale via paid acquisition. Time to focus on growth, not product |
| > 60% | Extreme PMF | Rare. Likely a niche audience or an unusually strong value prop |

---

## Known limitations

**Selection bias:** the survey only reaches the people who stayed. The stronger the churn, the stronger the positive distortion. Mitigation — measure Sean Ellis together with retention cohorts (Stage 9).

**Cultural variance:** in some cultures direct negatives ("not disappointed, useless") are socially unacceptable. Some samples may systematically give +5-10% to Very disappointed relative to Western benchmarks. Do not redefine the threshold, but keep it in mind.

**Static measurement:** Sean Ellis gives a snapshot at the moment of the survey. It does not show a trend. For a trend you need to repeat it every 1-3 months with the same distribution method.

**Does not work for:**
- B2B enterprise sales (decision makers ≠ users, low N)
- Marketplaces before critical mass on both sides
- Products with very rare usage (once a year, like insurance)

For these cases — qualitative interviews + retention + revenue per user, not Sean Ellis.

---

## Related: Rahul Vohra's "Superhuman PMF Engine"

Rahul Vohra (CEO of Superhuman) extended the Sean Ellis approach into a full process:
1. Run Sean Ellis
2. Segment "Very disappointed" — who are these people (job, behavior, use case)
3. Ask the same group for the main benefit and must-have features
4. Rebuild the product to maximize "Very disappointed" in this segment
5. Repeat the survey

This loop is what Stage 9 ↔ Stage 10 in the PMF skill does via `iteration-changelog.md`.

Original link: First Round Review, *How Superhuman Built an Engine to Find Product/Market Fit* (Rahul Vohra).
