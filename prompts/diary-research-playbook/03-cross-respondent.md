# Prompt 03: Cross-Respondent Analysis

Compare multiple respondents, find inter-respondent patterns and behavioral groups.

---

## The prompt

```
You are a qualitative researcher synthesizing data across multiple respondents in a diary study. Your goal: find what's shared, what's different, and why — to move from individual stories to project-level insights.

CRITICAL RULES:
- Every claim must be tied to specific respondents and entries.
- Frequency matters: "3 out of 10 in segment X" is an insight. "Some respondents" is not.
- Same behavior in different people can mean different things. Check portraits before grouping.

## Your task

Compare the respondents listed below. Follow these steps exactly.

### Step 1: Build a comparison table

| Parameter | Respondent A | Respondent B | Respondent C |
|-----------|-------------|-------------|-------------|
| Segment | — | — | — |
| Location | — | — | — |
| Quota / recruitment group | — | — | — |
| Primary context | — | — | — |
| Total entries | — | — | — |
| Target behavior: declared → actual | — | — | — |
| Main barrier | — | — | — |
| Main driver | — | — | — |
| Key pattern | — | — | — |
| Unawareness of value | — | — | — |
| Decision-making style | — | — | — |
| Screening ↔ diary discrepancy | — | — | — |

### Step 2: Find commonalities

- Same barriers across different people → confirmation of scale
- Same drivers → confirmation of value
- Same patterns → structural regularity
- Same unawareness of features → systemic communication failure

### Step 3: Find differences

- One person does X in situation Y, another doesn't → what differs? (portrait, belief, experience)
- Different segments, different behavior → does segmentation hold?
- Different locations → does geography matter?
- Different activity types → different barriers/drivers?

### Step 4: Group by behavioral types

As you analyze, groups emerge. Typical axes:

**By target behavior:**
- "Always does it" — ritual/habit/safety net
- "Situational" — triggered by context
- "Principled non-doer" — barrier or belief

**By key driver:**
- Control/planning — wants predictability
- Safety/insurance — "just in case"
- Passive/background — calmer with it on

**By key barrier:**
- "Don't need it" — attitude/belief
- "It annoys me" — problem escalated to barrier
- "Too much effort" — high activation threshold

**By life context:**
- Predictable rhythm — same routine daily
- Chaotic rhythm — different every day
- Coordination-heavy — managing multiple people/schedules

### Step 5: Quota/segment analysis

Use your recruitment structure for systematic comparison:

**Within quota groups:**
- All "frequent" respondents — actually frequent? Or does each have their own trigger?
- All "always" — really always? Or some overstate?

**Between quotas:**
- How does "always" actually differ from "sometimes"? Quantitatively and qualitatively.
- Any respondents whose quota is inaccurate? (screening says "always," diary says "half")

**By segments:**
- Which barriers/drivers are segment-specific?
- Which are universal across segments?

### Step 6: Count frequencies

For each identified barrier/driver/pattern:
- How many respondents show it
- In which segments
- With what strength of influence

### Step 7: Formulate project-level insights

These are insights about the *study*, not individuals:
- "Barrier X appears in 7 of 10 [segment A] respondents, but only 1 of 6 in [segment B]"
- "Unawareness of feature Y is systemic: 80% of respondents don't know about it"
- "Pattern Z correlates with [life context] in 60% of cases"

## Output format

## Cross-Respondent Analysis: [respondent list]

### Comparison table
[table]

### Shared patterns
[what unites them]

### Key differences
[what distinguishes and why]

### Behavioral types
[grouping with descriptions]

### Quota/segment analysis
[within and between groups]

### Frequencies
[barriers × coverage × segments]

### Project-level insights
[study-level findings]

### Product/research implications
[what this means collectively]
```

---

## Customize for your project

**Comparison table:** Adapt parameters to your study. The essential ones: segment, target behavior (declared vs. actual), main barrier, main driver. Add domain-specific rows.

**Behavioral types:** The grouping axes are illustrative. Your data will produce different groups. The prompt encourages emergent grouping (from data) rather than pre-defined segments.

**Quota structure:** If your study uses quotas (e.g., frequency of behavior, demographics, usage tier), replace the quota analysis section with your structure. If no quotas — remove Step 5 or replace with demographic cross-cuts.

**Frequency counting:** For small samples (< 15), report exact counts ("4 of 12"). For larger samples, percentages are acceptable but always show the denominator.
