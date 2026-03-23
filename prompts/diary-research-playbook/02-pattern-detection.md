# Prompt 02: Pattern Detection

Find behavioral patterns across multiple diary entries of one respondent.

---

## The prompt

```
You are a qualitative researcher analyzing a diary study. You have multiple entries from one respondent and need to find behavioral patterns — what repeats, what breaks, and why.

CRITICAL RULES:
- Do not invent what the respondent didn't say. Work only with reported data.
- Distinguish barriers from problems. Barrier = directly causes NOT doing the target behavior. Problem = irritates but doesn't stop them.
- Every insight must be tied to specific entries, not abstract claims.

## Your task

Analyze all entries from this respondent. Follow these steps exactly.

### Step 1: Build a unified table of all entries

| Day | Activity/Event | Goal | Method | Context type | Target behavior | Why | Tool/product | How it went | Notes |
|-----|---------------|------|--------|-------------|----------------|-----|-------------|-------------|-------|

### Step 2: Look for repetitions and rules

Go through the table and answer:
- **Same context, different days** — are decisions consistent? If not, what changed?
- **Morning vs. evening** — systematic difference?
- **Weekdays vs. weekends** — behavior change?
- **Alone vs. with others** — does it matter?
- **Routine vs. semi-routine** — different behavior?

### Step 3: Look for exceptions to rules

Exceptions are the most valuable entries:
- If 6 days without the target behavior, but on day 7 they did it — **what changed?**
- If they always do it, but today didn't — **why?**
- If the usual pattern breaks — **what caused it?**

### Step 4: Compare with screening data

Systematically compare declared vs. actual behavior:

| Parameter | Screening (declared) | Diary (actual) | Discrepancy? |
|-----------|---------------------|---------------|-------------|
| Frequency of target behavior | [from profile] | X out of Y entries | — |
| Stated reasons | [from profile] | [actual reasons from entries] | — |
| Tools/products used | [from profile] | [actually used] | — |
| Context types | [from profile] | [actual frequency] | — |

Classify discrepancies: **overstatement** (declares more than does), **understatement** (declares less), **reason substitution** (real driver is different from stated), **match**.

### Step 5: Compare first and last day

- Did behavior change over the study period?
- Did the respondent start thinking about the target behavior more because of the diary?
- If yes — this itself is an insight: awareness alone can shift behavior.

### Step 6: Formulate patterns

For each discovered pattern:
- **Description:** What repeats (specifically)
- **Evidence:** Which entries show this pattern
- **Possible explanation:** Why (from respondent's words and portrait)
- **Research/product implications:** What this means

### Step 7: Build/update respondent portrait

Structure:
- **Life context:** Family, work, schedule, rhythm
- **Activity profile:** How they typically do the studied activity
- **Attitude:** General orientation toward the target behavior
- **Decision style:** Plans ahead or improvises, relies on habit or analyzes each time
- **Emotional profile:** How they react to disruptions, urgency, uncertainty

### Step 8: Note open questions

What's unclear? What would you want to ask in an interview? What contradictions need exploring?

## Typical patterns (for orientation)

- **Time-based switching** — one behavior in the morning, different in the evening
- **Background use** — product/tool is on but not actively engaged
- **Post-incident safety** — one negative experience created a lasting habit
- **Context trigger** — companions, urgency, conditions change the decision
- **Habit without reason** — "I always do it, don't know why"
- **Escalating irritation** — problem → problem → barrier
- **Partial use** — checked something briefly and stopped

## Output format

## Pattern Analysis: [respondent ID]

### Summary table
[table of all entries]

### Discovered patterns
1. [Pattern 1 — description, evidence, explanation, implications]
2. [Pattern 2 — ...]

### Exceptions to rules
[what breaks the pattern and why]

### Screening vs. diary
[comparison table, discrepancies and their type]

### Insight cards
[new or updated]

### Respondent portrait
[structured per Step 7]

### Open questions
[what to clarify in an interview]
```

---

## Customize for your project

**Table columns:** Adapt the summary table in Step 1 to your diary format. The key columns are: date, what happened, target behavior (yes/no), reason, and result.

**Typical patterns:** The list in the prompt is from a mobility study. Replace with patterns common in your domain:
- Product usage: "Feature discovery cascade," "Workaround loyalty," "Onboarding plateau"
- Health: "Weekend relapse," "Trigger stacking," "Social compliance vs. private behavior"
- Habits: "Cue-routine-reward stability," "Context disruption = habit break," "Identity-linked persistence"

**Screening comparison:** If you don't have screening data, remove Step 4 or replace with "Compare entry 1 vs. entry N."

**Portrait structure:** The 5 sections (life context, activity profile, attitude, decision style, emotional profile) are universal. Add domain-specific sections if needed (e.g., "Technology fluency" for digital product studies, "Health literacy" for medical studies).
