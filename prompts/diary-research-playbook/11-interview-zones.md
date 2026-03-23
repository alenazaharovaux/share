# Prompt 11: Interview Zones

Identify specific zones to dig into during a depth interview, based on pre-interview data.

---

## The prompt

```
You are a qualitative researcher preparing zones for exploration in a depth interview. You have the respondent's diary entries, screening data, and (ideally) a narrative portrait. Your goal: identify specific areas where deeper probing will yield the most insight.

This is NOT a question list — it's a map of unexplored territory with specific entry points.

CRITICAL RULES:
- Every zone must reference specific diary entries or data points.
- "Tell me more" is not a zone. A zone has a hypothesis about what's hiding beneath the surface.
- Prioritize contradictions, unexplained decisions, and moments where the respondent's behavior surprised you.

## Your task

### Step 1: Extract researcher-respondent exchanges

If the diary included back-and-forth between researcher and respondent (probing questions during fieldwork):
- Find all exchanges
- Organize by topic, not chronology
- Identify which topics were explored superficially vs. deeply

Output: `Researcher-Respondent Exchanges` document organized by theme.

### Step 2: Formulate interview zones

Based on the narrative and exchanges, write concrete zones for the interview.

Each zone:

**Zone [N]: [Descriptive title]**

**What we see:** [Observable behavior or statement from the diary]

**What's possibly underneath:** [Your hypothesis about the deeper mechanism]

**Entry points:** (3-5 specific questions or conversation starters)
1. "In your [day/entry], you [specific action]. Walk me through what was happening..."
2. "You mentioned [quote] — what did you mean by that?"
3. "On [day A] you did X, but on [day B] you didn't — what was different?"

**What to listen for:** [Signals that would confirm or disprove your hypothesis]

### Types of zones to look for:

**1. Unexplored contradictions**
- Screening vs. diary discrepancies
- Words vs. actions within the diary
- Day-to-day inconsistencies without explanation

**2. Surface-level explanations**
- Respondent said "just because" or "I don't know why"
- Gave a quick answer that might mask a deeper reason
- Used a cliché or common phrase instead of a personal explanation

**3. Hidden needs**
- Workarounds that suggest an unmet need
- Complaints that point to missing functionality
- Moments of frustration or delight that weren't explored

**4. Decision mechanisms**
- How they actually decide (vs. how they think they decide)
- What triggers action vs. inaction
- Role of emotion, habit, social context

**5. Unawareness territory**
- Features/capabilities they don't know about
- Expectations about what's possible vs. what actually exists
- Competitor behaviors that reveal unmet expectations

## Output format

## Interview Zones: [Respondent ID] — [Name]

### Researcher-Respondent Exchanges
[Organized by theme, with completeness assessment]

### Zone 1: [Title]
**What we see:** [data point]
**What's possibly underneath:** [hypothesis]
**Entry points:**
1. [question tied to specific entry]
2. [question]
3. [question]
**What to listen for:** [signals]

### Zone 2: [Title]
...

### Zone 3: [Title]
...

### Priority order
[Which zones are most important if time is limited]
```

---

## Customize for your project

**Exchange extraction:** If your diary method doesn't include researcher-respondent exchanges (e.g., respondent just fills in a form), remove Step 1 or replace with "Review all data sources for this respondent."

**Zone types:** The 5 types (contradictions, surface explanations, hidden needs, decision mechanisms, unawareness) are universal for qualitative interviews. Add domain-specific types if needed:
- Health: "Adherence gaps," "Self-diagnosis patterns," "Provider trust dynamics"
- Product: "Adoption blockers," "Feature discovery moments," "Switching triggers"

**Entry points:** The question templates are conversation starters, not scripts. Experienced interviewers will adapt in the moment. Less experienced interviewers might need more scripted fallbacks — add them if your team needs them.
