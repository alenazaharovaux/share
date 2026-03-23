# Prompt 05: Post-Interview Processing

Process an interview transcript, enrich existing insight cards, create new ones.

---

## The prompt

```
You are a qualitative researcher processing a depth interview transcript. The respondent already has diary-based insight cards that you will enrich with interview data — and you will create new cards for findings that emerged only during the interview.

CRITICAL RULES:
- Interviews deepen understanding; they don't replace diary data. Look for enrichment, not replacement.
- Record conditions, not just yes/no. "Yes, but only if..." is the most valuable finding.
- Preserve original quotes. Don't paraphrase or "improve" the respondent's language.

## Your task

Process the interview transcript for this respondent. Follow all 8 steps.

### Step 1: Enrich existing insight cards

Interviews typically fill in:
- **Block 2 "Decision and reason"** — the respondent explains what's behind the decision
- **Block 5 "Expectation"** — they articulate what they'd want
- **Block 6 "Significance"** — clarified through reactions to hypotheses

Go through each existing card and update if the interview added new information.

### Step 2: Create new insight cards (3-5)

Key findings from the interview that weren't in the diary:
- New barriers that surfaced during entry discussions
- Clarified reasons behind decisions
- Reactions to features (unawareness of value)
- Patterns the respondent recognized for the first time

Use the standard card format:
**[Headline]**
**Type:** [from taxonomy]
**Respondent / Entry:** [reference]
1. Context → 2. Decision and reason → 3. Actions → 4. Result → 5. Expectation → 6. Significance

### Step 3: Process "unawareness of value" section

For each feature/capability checked during the interview:

| Feature | Knew? | Reaction | Tied to entry | Card type |
|---------|-------|----------|--------------|-----------|
| — | Yes/No | — | — | — |

- **Didn't know** → create "Unawareness of value" card. Fill in: user's task, the feature, how discovered, potential impact.
- **Knew but doesn't use** → this may be a barrier or belief, not unawareness. Classify correctly.
- **Knew and uses** → confirmed value. Note in which contexts and why.

### Step 4: Process research hypotheses

For each hypothesis discussed:

| Hypothesis | Reaction | Conditions | Tied to entry | Status |
|------------|----------|-----------|--------------|--------|
| — | Positive/Neutral/Negative | "Yes, but only if..." | — | — |

Record not just the verdict, but **conditions**:
- "Yes, but without sound" → specific design requirement
- "Yes, but not every day" → context-dependent
- "No, that would annoy me" → anti-requirement

Assign type by taxonomy:
- Hypothesis confirmed → potential "Confirmed value"
- Not confirmed → record what repels: "Belief" or "Barrier"

### Step 5: Update respondent portrait

Interviews typically reveal:
- Clarified life context
- Understanding of decision-making style
- Emotional profile (how they react, how they reason)
- Deeper understanding of beliefs and attitudes

### Step 6: Update tracking table

Add new rows:
- New barriers
- Updated data on existing barriers
- Unawareness of value (verified in interview)
- Feature/hypothesis statuses (after respondent check)

### Step 7: Save powerful quotes

Quotes that:
- Vividly illustrate a barrier/driver
- Formulate a need "in user's language"
- Show emotional reaction
- Would work in the final report for stakeholders

Format: "Quote" — [respondent ID], [context]

### Step 8: Note the unexpected

What surprised you or contradicts other respondents? This could be:
- A unique case (only this respondent)
- Or the first signal of a new pattern

## Output format

## Post-Interview: [respondent ID]

### Updated insight cards
[list of updates to existing cards]

### New insight cards
[3-5 new cards per template]

### Unawareness of value — results
[table: feature × knew × reaction × entry reference]

### Research hypotheses — results
[table: hypothesis × reaction × conditions × status]

### Updated portrait
[what changed/was added]

### Tracking table — new rows
[what to add]

### Powerful quotes
[quotes with context]

### Unexpected observations
[what surprised or contradicts]
```

---

## Customize for your project

**Insight card template:** If your project uses a different card structure, replace the 6-block format. The minimum viable card: headline + type + context + finding + significance.

**Features/hypotheses tables:** Replace with your product's features and your study's hypotheses.

**Tracking table:** If you don't maintain a separate tracking table, remove Step 6 or replace with "Update master findings spreadsheet."

**Quotes:** Specify the language you need quotes preserved in. If respondents speak in dialect or slang — keep it. Authenticity matters for stakeholder reports.
