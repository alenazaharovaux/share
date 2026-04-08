# Stage 7 — Interview Synthesis

**Goal:** read all interview notes, extract patterns per dimension, update confidence scores, evolve the narrative to V3.

**Reads:** `narrative-v2.md`, `interviews/notes/*.md`
**Writes:** `interview-synthesis.md`, `narrative-v3.md`

---

## ⛔ Isolation rule

**Read notes one at a time**, not in batches. Do not mix data between notes. This prevents "averaging" the patterns and keeps the specifics intact.

Technically:
1. Read all the file names in `interviews/notes/` (just the listing)
2. For each note: open → extract patterns → close → move to the next
3. **After** processing all notes — synthesis

This is similar to the rule in single-transcript analyses, but a bit looser (there you cannot look at others at all — here you can after processing one).

---

## Step 7.1 — Read narrative V2 and assumptions-map

Context for the synthesis:
- From `narrative-v2.md` — current hypotheses per dimension + V2 confidence
- From `assumptions-map.md` — which Critical-quadrant assumptions you wanted to validate
- From `interview-guide.md` — coverage matrix (questions → assumptions)

---

## Step 7.2 — Per-interview extraction

For each note in `interviews/notes/`:

1. **Read the whole note** (no skipping)
2. **Extract:**
   - Respondent context (1-2 sentences)
   - Markers of whether the respondent is typical / atypical for the target
   - Quotes verbatim — not paraphrase
   - Observations per dimension (only the relevant dimensions)
   - Surprises (the unexpected)
   - Quantitative signals (numbers: time, money, frequency)
3. **Write into an intermediate table** (in memory or in a draft):

```markdown
| Resp ID | Dim 1 finding | Dim 2 finding | Surprise | Quant |
|---------|--------------|---------------|----------|-------|
| R001 | ... | ... | ... | ... |
```

4. **Close the note**, move on to the next

After all notes — go to synthesis.

---

## Step 7.3 — Pattern extraction per dimension

For each dimension covered by the interviews:

1. **Pattern** — what do they say on average? (1-2 sentences)
2. **Supporting evidence** — N of M respondents confirm (e.g. "12 of 15")
3. **Strength of pattern:**
   - **Strong** — 80%+ of respondents confirm, no significant contradictions
   - **Medium** — 50-80% confirm, with nuances
   - **Weak** — < 50% or strongly split
4. **Key quotes** — 2-3 verbatim quotes of the best ones, with the respondent ID
5. **Confidence change:** V2 score → post-interview score
6. **Update type:** Validated / Refinement / Pivot / Reset

**Rule:** N supporting != true even if 15 of 15. If all 15 are close friends of the founder and not the right audience — that is not a pattern, that is an echo chamber. Account for the quality of the respondents, not just the count.

---

## Step 7.4 — Cross-dimensional insights

Patterns spanning several dimensions. Examples:

- "Respondents who complain the most about the Problem (D1) are the same ones who **already pay** for competitors (Business Model V validated). Those who do not complain — do not pay. This means the **audience = paying customers**, not the general market." (cross: Audience + Problem + Business Model)

- "The higher the confidence in the Value Proposition, the less attention to pricing. Respondents who see the value — ask how to buy, not how much it costs." (cross: Value Prop + Business Model)

- "Timing pattern: 11 of 15 respondents started looking for a solution in the last 6 months — after a concrete event (a new law / a new GPT model / a new platform). This validates Why Now with a concrete date." (cross: Timing + Problem)

Write into a separate `## Cross-Dimensional Insights` section in interview-synthesis.md.

---

## Step 7.5 — Surprises

Findings that **contradict** the hypothesis or open a new angle. This is often the most valuable thing from interviews.

**Types of surprises:**
- **Wrong assumption:** "We thought Y, it turned out X"
- **New segment:** "A new audience emerged that we did not think about"
- **Hidden friction:** "A pain point we did not know about"
- **Workaround:** "They are already solving this in X-way that we were not accounting for"
- **Unexpected use case:** "They want to use this for Z, not for what we were doing"

Write each surprise + which respondent + what it means for the hypothesis.

---

## Step 7.6 — Updated Risk Assessment

Compare confidence before and after the interviews:

```markdown
| Dimension | Pre-Interview | Post-Interview | Change | Status |
|-----------|---------------|----------------|--------|--------|
| Problem to Solve | 6 | 8 | +2 | Validated |
| Target Audience | 5 | 4 | -1 | Refined (segment narrowed) |
| Value Proposition | 5 | 7 | +2 | Validated |
| Competitive Advantage | 5 | 5 | 0 | Unchanged |
| Growth Strategy | 4 | 3 | -1 | At risk |
| Business Model | 6 | 8 | +2 | Validated |
| Timing / Why Now | 7 | 9 | +2 | Validated |
```

**Loop detection:** if confidence dropped for some dimension in V3 vs V2 → flag + recommendation:
- Drop on a risk-dimension you were validating → return to Stage 4 (new assumptions) or Stage 1 (rethink)
- Drop on a non-critical dimension → maybe you can continue with a lower score
- Drop on several dimensions → return to Stage 1, check the hypothesis as a whole

---

## Step 7.7 — Update narrative V2 → V3

Create `narrative-v3.md`:
- Date updated, version V3
- Version History: "V3: After Field Interviews (date)" with a changelog
- Each dimension: new wording (if changed) + post-interview confidence
- If there is a **new segment** or a **wrong assumption** — mark it explicitly
- Validation Status table updated with evidence-data from interviews
- Recommended next step (decision tree below)

**Do NOT overwrite V2.** V3 is a separate file.

---

## Step 7.8 — Decision tree after Stage 7

| Condition | Recommended next |
|---------|------------------|
| All key assumptions validated, confidence high (avg > 7) | Stage 8 (MVP launch) |
| Confidence rose, but the risk-dimension is still weak | Stage 4 for another risk-dimension or more interviews with a different segment |
| Confidence dropped on some dimension | Stage 4 (new assumptions) or Stage 1 (rethink that dimension) |
| A new risk-dimension surfaced that you did not validate | Stage 4 for it |
| Wrong assumption on a critical dimension | Stage 1 (pivot that dimension) |
| Wrong assumption on 2+ critical dimensions | Stage 1 (full rethink, possibly reset) |

Write into `interview-synthesis.md` and into narrative-v3.md.

---

## Step 7.9 — Create interview-synthesis.md

From the template `references/<lang>/template-interview-synthesis.md`. Must contain:

1. Metadata (date, interview count, narrative version V2 → V3)
2. Summary (one-sentence key finding + overall confidence change)
3. Per-Dimension Patterns (1-7 sections, each with pattern + evidence + quotes + confidence change)
4. Cross-Dimensional Insights
5. Surprises
6. Updated Risk Assessment table
7. Loop detection notes
8. Recommended next steps

---

## Quality gates for Stage 7

- [ ] All notes read (isolation: one at a time)
- [ ] Per-dimension patterns with supporting evidence count
- [ ] Strength of pattern (strong/medium/weak) for each
- [ ] Key quotes verbatim, with respondent ID
- [ ] Cross-dimensional insights in a separate section
- [ ] Surprises explicitly listed
- [ ] Updated Risk Assessment table filled
- [ ] Confidence delta for each dimension calculated
- [ ] Loop detection: if there are drops — flag
- [ ] narrative-v3.md created as a separate file
- [ ] Recommended next step matches the decision tree

---

## Common pitfalls in Stage 7

| Mistake | Symptom | Fix |
|--------|---------|------|
| Reading notes in a batch | All 15 in one context | One at a time — isolation |
| Averaging patterns | "On average they say..." | Concrete numbers: N of M, key quotes |
| Ignoring surprises | Only what fits | Surprises = the most valuable, separate section |
| Echo chamber pattern | 15 of 15 = strong, but all are friends | Account for respondent quality |
| No confidence drops | All confidence only goes up | If data contradicts — a drop is mandatory |
| Quotes rewritten | "Respondents broadly said that..." | Verbatim in quotes |
| Pivoting everything | Reset on 2+ dimensions in a row | Return fully to Stage 1, not local edits |
| narrative V3 = narrative V2 | Confidence updated, wording not | If a pattern is strong → the wording should update (refinement) |
