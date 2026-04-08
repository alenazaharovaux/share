# Template — Interview Synthesis

**Used in:** Stage 7 (Interview Synthesis)
**Save as:** `interview-synthesis.md` + `narrative-v3.md` (updated narrative)
**Companion guide:** `references/<lang>/stage-7-interview-synthesis.md`

**Purpose:** condense findings from 15+ interviews into patterns, surprises, an updated narrative wording and an updated risk map.

---

## ⛔ Synthesis rules

1. **Read in isolation, one note at a time.** Do not load all interviews at once — patterns get distorted. Read one by one, write down citations + observations, then merge.
2. **At least 15 interviews.** Less = individual opinions, not patterns.
3. **A pattern = ≥ 3 respondents said something similar.** Less — that is an outlier, mark as a surprise.
4. **Surprises are mandatory.** If the synthesis found nothing unexpected, you heard what you wanted to hear. Re-read.
5. **Loop detection:** if patterns fully match the V2 narrative — interviews gave nothing, check for leading questions.

---

## Template

```markdown
# Interview Synthesis — [Product name]

**Date:** YYYY-MM-DD
**Reads:** all interviews from `interviews/notes/*.md`
**Writes:** this file + `narrative-v3.md`
**Number of interviews:** [N]
**Date range:** [first] – [last]

---

## Coverage

| Segment | Planned | Actual | Notes |
|---------|---------|--------|-------|
| Primary segment | 12-15 | [N] | |
| Adjacent segment 1 | 3-5 | [N] | |
| Adjacent segment 2 | 3-5 | [N] | |
| Non-target (control) | 2-3 | [N] | |
| **TOTAL** | 20-28 | [N] | |

**Minimum met?** [yes/no — if total < 15, the synthesis is weak]

---

## Patterns

Each pattern must:
- Show up in ≥ 3 respondents
- Have concrete quotes (not paraphrase)
- Be tied to dimension(s)

### Pattern 1: [short name]

**Dimension(s):** [Customer / Problem / Solution / Distribution / Business model]

**Description:**
[1-2 paragraphs: what specifically was common]

**Quotes (at least 3):**
- "[verbatim quote]" — [respondent ID, segment]
- "[verbatim quote]" — [respondent ID, segment]
- "[verbatim quote]" — [respondent ID, segment]

**Frequency:** [how many respondents out of N]

**Strength:** [Strong / Moderate / Weak]
- Strong: 7+ of 15 articulated this clearly
- Moderate: 4-6 articulated it
- Weak: 3 articulated + a few more indirectly

**Implication for narrative:**
[How this pattern changes narrative-v2 → v3]

---

### Pattern 2: [...]

[Same structure]

---

### Pattern 3-N: [...]

[Minimum 3 patterns, usually 5-8]

---

## Surprises

Surprises are unexpected findings that were not in narrative-v2.

### Surprise 1: [short name]

**What was unexpected:**
[What you did not expect]

**Where it appeared:**
- "[quote]" — [respondent ID]
- "[quote]" — [respondent ID]

**Why it matters:**
[Implication for the narrative or for the risk map]

**Confidence:**
[Strong / Moderate / Weak — how many respondents support this surprise]

---

### Surprise 2-N: [...]

**Minimum 2 surprises.** If less — leading questions and/or confirmation bias. Re-read the notes.

---

## Anti-patterns / disconfirmed assumptions

Things we assumed in narrative-v2, but the interviews did NOT confirm:

| Assumption (V2) | What interviews showed | Action |
|-----------------|----------------------|--------|
| [e.g.: "target users spend 4-6 hours"] | "Actually 1-2 hours" | Revisit problem severity |
| | | |

---

## Persona refinement

After 15+ interviews, the persona should become more concrete.

**V2 persona:** [as it was]
**V3 persona:** [as it became after the interviews]

**New persona divides:**
- ✗ [a new exclusion category, surfaced in interviews]

**Different sub-segments inside the primary segment:**
[If the interviews showed there are 2-3 different groups inside the segment with different needs — describe them]

---

## Updated risk map

| Dimension | V2 risk score | V3 risk score | Why changed |
|-----------|---------------|---------------|-------------|
| 1. Customer | [X] | [Y] | [interviews confirmed / refuted / sharpened] |
| 2. Problem | | | |
| 3. Why now | | | |
| 4. Why us | | | |
| 5. Solution | | | |
| 6. Distribution | | | |
| 7. Business model | | | |
| 8. Power | | | |

**New riskiest dimension (for the next cycle):** [name]

---

## Recommendations for narrative-v3

**What to rewrite:**
- Customer section: [concretely what to change]
- Problem section: [...]
- Solution section: [...]

**New visceral quotes to include:**
- "[quote]" — for Problem section
- "[quote]" — for Solution section

**What to remove:**
- [feature/claim/assumption that interviews did not support]

---

## Decision tree (what to do next)

```
IF patterns mostly confirm V2 narrative AND ≥ 3 surprises found:
  → Strong validation. Write narrative-v3 with refinements. Move to Stage 8 (MVP).

IF patterns mostly confirm BUT 0-1 surprises:
  → Suspect confirmation bias. Re-read interviews with fresh eyes OR run 5 more with a different recruiter.

IF patterns disconfirm V2 in 2-3 dimensions:
  → Significant pivot needed. Rewrite narrative-v3 with major changes. Return to Stage 3 (synthesis) with a new risk map.

IF patterns disconfirm V2 in 4+ dimensions:
  → Hypothesis broken. Return to Stage 1 (Hypothesis) with learnings.
```
```

---

## Common mistakes

| Mistake | Symptom | Fix |
|--------|---------|------|
| Loading all interviews at once | Patterns seem obvious right away | Isolation: one note → write down → next |
| Pattern from 1-2 respondents | "We already have 5 patterns after 5 interviews" | ≥ 3 respondents per pattern, at least 15 interviews |
| 0 surprises | Wishful thinking | Re-read with focus on "what does not fit" |
| Pattern = team paraphrase | "We knew they would say this" | Use verbatim quotes, not paraphrase |
| Ignoring adjacent segments | Only primary | Adjacent gives persona divides |
| Skipping risk map update | Old risk map after new data | Mandatory: update the scores |
