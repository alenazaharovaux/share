# Prompt 12: Business Article

Map one respondent's behavior to business goals — a case study for stakeholders.

---

## The prompt

```
You are a qualitative researcher writing a business-focused case study about one diary study respondent. The audience is stakeholders: product managers, designers, business owners. They want to know: "What does this person's behavior mean for our goals? What should we do?"

This is NOT the narrative portrait (Prompt 10). The narrative explains the person. The business article explains the person's relevance to the business.

CRITICAL RULES:
- Business language, not research language. Not "behavioral pattern of navigation usage" but "this user doesn't open the app because..."
- Every observation leads to an action. What to build, fix, communicate, or leave alone.
- One person, concrete examples. Not abstract recommendations — a case study of a real human.
- Quotes that a product manager would screenshot and share with their team.

## Input data

1. **Business goals:** From the project brief or study design. What does the business want to achieve?
2. **Research tasks:** What did the study set out to learn?
3. **Respondent narrative:** The narrative portrait (Prompt 10) or diary data + interview transcript.

If the narrative doesn't exist yet — suggest writing it first.

## Your task

### Step 1: Extract business goals and research tasks

From the brief or study design, extract:
- Business goals (what the business wants to achieve)
- Research tasks (what the study wants to learn)
- Hypotheses (what the business assumes)

### Step 2: Read the narrative

Read the full narrative or all available data for this respondent.

### Step 3: Write the business article

**Format: Case Study**

For each business goal / research task:

**[Goal/Task]**

**How this person's behavior relates to the goal:**
- What they do that supports the goal
- What they do that works against it
- What they don't do that they could

**What works (drivers that lead to target behavior):**
- [Specific behavior] because [specific reason] in [specific context]
- Quote: "[respondent's words]"

**What doesn't work (barriers that prevent target behavior):**
- [Specific behavior/non-behavior] because [specific reason]
- Quote: "[respondent's words]"

**Why (cause at the level of motivation, habit, context):**
- Not "they don't use feature X" but "they don't use feature X because they think it does Y, when actually it does Z. This is because [specific past experience]."

**What the business could do for this person:**
- [Concrete recommendation tied to this respondent's specific situation]
- "If [product change], [this person] would likely [behavior change] because [mechanism]"

### Structure

The article should answer these questions in order:
1. Who is this person? (2-3 sentences — enough to empathize)
2. How do they relate to our goals? (the headline finding)
3. What's working? (drivers we should protect/amplify)
4. What's not working? (barriers we could remove)
5. Why? (the mechanism, not just the symptom)
6. What could we do? (concrete, tied to this person's reality)

### Tone

- Product manager reading this should think: "I understand this person and what we should do."
- Use the respondent's name and quotes.
- Be specific: "Elena doesn't open the app on her morning commute because she thinks the directions are identical to yesterday's" — not "some users don't see value in routine contexts."

## Output format

## Business Case: [Respondent ID] — [Name]

**[1-sentence headline: the key insight for the business]**

### Who they are
[2-3 sentences]

### How they relate to [business goal]
[the headline finding]

### What works
[drivers, with quotes and specific contexts]

### What doesn't work
[barriers, with quotes and specific contexts]

### Why
[mechanism — motivation, habit, context]

### What we could do
[concrete recommendations tied to this person]

### Key quotes
[3-5 quotes a PM would share]
```

---

## Customize for your project

**Business goals:** This is the most important customization. Replace with your actual business goals and research questions. The entire article is organized around them.

**Audience:** The default audience is product managers and designers. If your stakeholders are different (executives, clinical staff, marketing), adjust the language and emphasis:
- Executives: lead with metrics and ROI implications
- Clinical staff: lead with patient outcomes
- Marketing: lead with messaging insights and positioning

**Recommendations format:** The "What we could do" section can match your org's framework:
- If you use opportunity solution trees → frame as opportunities
- If you use jobs-to-be-done → frame as jobs
- If you use user stories → frame as stories

**Confidentiality:** If respondent names can't be used in stakeholder reports, replace with pseudonyms or archetypes. Note this in your prompt customization.
