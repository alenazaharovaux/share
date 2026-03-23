# Prompt 07: Launch Brief

Prepare the analytical focus for a new respondent before they start their diary.

---

## The prompt

```
You are a qualitative researcher launching a new respondent's diary. You have their screening/recruitment data and (optionally) data from respondents already in the field. Your goal: prepare a focused analytical brief so you know exactly what to watch for when entries start coming in.

## Your task

Create a launch brief for this respondent. Follow all 6 steps.

### Step 1: Respondent card

From screening data, build a brief portrait in 5-7 lines:
- **Who:** age, location, profession, work format
- **Activity profile:** how they typically do the studied behavior, frequency, regular contexts
- **Target behavior:** declared frequency, stated reasons, tools/products used
- **Study role:** which quota/segment, why they're in the sample

### Step 2: Define analytical focus

Based on the profile, formulate 3-5 key questions for this respondent.

Think about what their screening data makes you curious about:
- Is their declared behavior likely to match reality?
- What might explain their behavior that screening can't capture?
- What unique contexts does this person bring to the study?
- What would be surprising to learn from their diary?

### Step 3: Formulate hypotheses for testing

Based on screening answers, 2-3 hypotheses that the diary can confirm or disprove:

Format:
Hypothesis: [statement]
Basis: [what in screening data suggests this]
How to check in diary: [what to look for in entries]

Example:
"Respondent declares 'always' but is in the 'sometimes' quota — likely has contexts where they don't do it but don't count those. Look for: entries where they skip the behavior and how they frame it."

### Step 4: Define what to track

Specific signals to watch for when analyzing entries:

- **Red flags:** what would indicate a screening-diary discrepancy
- **Interesting situations:** what kinds of entries will be most valuable
- **Features/capabilities to check:** what this person probably doesn't know about (based on profile)

### Step 5: Sample context

- Which quota cell is this respondent in
- How many respondents are already in this cell
- How this respondent complements or duplicates existing ones
- What the sample needs from this respondent (unique context, location, profile)

### Step 6: Preliminary interview questions

Even before the diary starts, draft 2-3 questions for the eventual depth interview — based on screening data alone:
- Internal contradictions in screening answers
- Unusual combinations
- Location/context-specific questions

## Output format

## Launch Brief: [respondent ID] — [Name]

### Respondent card
[brief portrait from screening]

### Analytical focus (3-5 questions)
1. [question] — [why it matters]
2. ...

### Hypotheses for testing
1. [hypothesis] — [basis] — [how to check]
2. ...

### What to track in diary
- Red flags: [list]
- Interesting situations: [list]
- Features for awareness check: [list]

### Sample context
[cell, neighbors, uniqueness]

### Preliminary interview questions
1. [question] — [why]
2. ...
```

---

## Customize for your project

**Respondent card:** Adapt the 4 bullet points to your study's key variables. What information from screening is most relevant for interpreting diary data?

**Analytical focus questions:** These depend entirely on your research questions. The prompt asks the LLM to generate them, but you can add project-specific prompts:
- "For this study, always ask: does their [variable] match what we'd predict from their [demographic]?"
- "We're particularly interested in [context] — watch for entries in this context."

**Sample context:** If your study uses quotas, keep Step 5. If not, replace with "What makes this respondent unique in the sample" or remove.

**Features to check:** Replace with features/capabilities from the product or service you're studying. These will become interview questions later (see Prompt 04).
