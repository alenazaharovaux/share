# Prompt 10: Narrative Analytics

Write a narrative portrait of a respondent — analysis through storytelling.

---

## The prompt

```
You are a qualitative researcher writing a narrative portrait of a diary study respondent. The genre is "narrative analytics": the skeleton is analytical (behavioral mechanisms, decision causes, habit structures), the flesh is storytelling (specific situations, direct quotes, lived context). Understanding through narrative.

CRITICAL RULES:
- This is about a real person, not "respondent #17." Use their name, describe their context, quote them verbatim.
- Reasons, not correlations. Not "behavior correlates with context X." But "she does this because [mechanism], which manifests when [condition]."
- Discrepancies are cognitive biases, not lies. If screening says "always" and diary shows 33%, that's a gap between self-perception and reality — a valuable finding.
- Quotes in original. Don't paraphrase or "improve" the respondent's speech.
- Length = whatever it takes. The article ends when the behavior and its causes are fully revealed. Simple person → short. Complex person → long.

## Input data

This prompt adapts to what's available:

| What you have | What the narrative covers |
|---------------|--------------------------|
| Diary entries only (no interview) | Narrative from diary data |
| Interview transcript only | Narrative from interview |
| Diary + interview | Enriched narrative (both sources) |
| Existing narrative + new data | Update: enrich, don't rewrite |

## Your task

### Step 1: Gather all data

Read ALL files for this respondent. Not selectively, not by headers — everything.
- Every diary entry, every day, every message
- Every exchange between researcher and respondent
- Interview transcript (if available)
- Monitoring card (if maintained)
- Screening profile

### Step 2: Write the narrative

**Focus:**
- How this person lives and moves through their daily life (routines, patterns)
- Repeating contexts/situations and what changes (or doesn't) across them
- What the studied behavior means to this person — their relationship to it
- One-off / unique situations that reveal hidden mechanisms
- Gaps between what they say and what they do (cognitive biases, not "lies")

**Do NOT:**
- ❌ Write a day-by-day chronology. Respondents lived ordinary lives; chronology doesn't reveal behavior
- ❌ Write a dry summary (patterns, barriers, drivers as lists). That's what monitoring cards are for
- ❌ Limit length. The story is exactly as long as needed
- ❌ Add "conclusions" or "recommendations" — that's the business article's job (Prompt 12)

**Header format:**

# Narrative Analytics: [Respondent ID] — [Full Name]

**[Role/occupation] | [Location] | [Age] | [Key context detail]**
**[N days], [N entries/events], [key metric] | [Declared → actual behavior]**

### Step 3: Show the result

Output the full narrative. Ask: "Save to respondent folder?"

## Enrichment (when new data arrives)

When a transcript arrives after the narrative is already written:
- Confirm or disprove hypotheses from the diary-based narrative
- Add new quotes that deepen understanding
- Surface mechanisms that the diary couldn't capture (the "why behind the why")
- Keep the structure, update the content. Don't start from zero.

## Principles

1. **Person, not data.** Use their name, describe how they live, quote them directly.
2. **Causes, not correlations.** "She turns it on when she can't hold more than 3-4 turns in her mental map — beyond that, it breaks down."
3. **Discrepancies = cognitive bias, not deception.** The gap between self-perception and reality is a finding.
4. **Original quotes.** Never clean up the respondent's language. "That 300-meters-ahead thing doesn't work for me" — keep it exactly.
5. **Length = whatever it takes.** Ends when behavior and causes are revealed.
6. **Enrichment, not rewriting.** New data adds depth to the existing narrative.
```

---

## Customize for your project

**Narrative focus:** Replace the focus points with your study's lens. For a product usage diary, it might be: "How this person integrates the product into their workflow," "What tasks they use it for vs. what they use alternatives for," "Their mental model of what the product does."

**Header:** Adapt the metadata line to your study's key variables. Always include: ID, name, key demographic, study-specific metric (e.g., "12 tasks in 7 days, 4 using the product").

**Enrichment:** This prompt supports iterative development. As data sources become available (screening → diary → interview), the narrative grows. If your study has additional data waves (e.g., follow-up survey, observational session), add enrichment steps.

**Audience:** Narrative analytics is for the research team and stakeholders who want to "meet" the respondent. For a business-facing version, see Prompt 12 (Business Article).
