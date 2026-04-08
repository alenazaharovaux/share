# Stage 5 — Interview Prep

**Goal:** prepare the guide for in-depth interviews on the 2-3 riskiest dimensions from risk-prioritization. This is **preparation**, not running them — the field (Stage 6) is the user's own work.

**Reads:** `narrative-v2.md`, `risk-prioritization.md`, `assumptions-map.md`
**Writes:** `interview-guide.md`, `interviews/note-template.md`

---

## Step 5.1 — Pick the target dimensions

From `risk-prioritization.md` take the top 2-3 risk-dimensions. If one was already validated in Stage 4 — pick from the remaining.

If only one dimension is left — add a cross-dimensional block (general questions about behavior, alternatives, willingness to pay).

---

## Step 5.2 — Guide structure

### Introduction script

Template (adapt to the product):

```
Hi, [name]. Thank you for finding the time.

I'm [name], I'm working on [product/idea]. Right now I'm in the research phase
— understanding what people like you do in [context] and how. This is not a
product pitch, I'm not going to sell you anything — I want to hear your
experience as it really is.

The conversation will take about 30-45 minutes. If you don't mind, I'd like
to record it so I don't miss the details. The recording is just for my
analysis, no one else will see it. We can stop at any time or skip any
question.

Sound good? Let's start.
```

### Screening questions (2-3)

Goal: make sure the respondent matches the target audience.

**Rules:**
- Ask at the very beginning
- Not leading: not "you do use X every day, right?"
- Concrete behavior: "tell me how often you've done Y in the last 2 weeks"
- If no fit → politely end the interview

**Examples for e-commerce sellers:**
1. "Tell me about your business — what you sell, on which platforms, roughly how many orders per month?"
2. "How often do you personally handle orders — every day, several times a week?"
3. "When was the last time you manually moved orders between systems? Tell me about that."

### Thematic blocks

**For each risk-dimension** — a separate block of 5-7 open questions.

**Question rules:**
- ⛔ **No leading questions.** Not "do you agree that X is hard?" → "How do you do X today?"
- ⛔ **No hypotheticals.** Not "if there were a tool Y, would you use it?" → "Tell me about the last time you tried to solve this"
- ⛔ **No opinions about the future.** Not "what do you think about the future of this market?" → "What has changed in your work over the last year?"
- ✅ **Past behavior over future intent.** Past behavior predicts the future. Hypothetical answers do not.
- ✅ **Specific situations.** "Tell me about the last time...", "When did you last..."
- ✅ **Open questions** (not yes/no). Start with "how", "what", "tell me", "describe", "why"
- ✅ **Five Whys** (depth). If the respondent says "this is annoying" → "why exactly?" → "what would be different if..." → ...

**Example questions for the Problem to Solve dimension:**
1. "Walk me through how you handle orders today — step by step, the way you did it yesterday/today"
2. "What part of this process takes the most time?"
3. "What was the most annoying episode in the last month?"
4. "What have you tried to improve it? Did it work?"
5. "If you could change one thing in the process today — what would it be?"
6. "Roughly how many hours a week does this take?"

**Example questions for the Value Proposition dimension:**
1. "Which tools for X have you tried? What about them grabbed you?"
2. "In [a specific competitor tool] what do you use the most?"
3. "If [the specific tool] disappeared tomorrow — what would change in your work?"
4. "What keeps you on [the current solution]?"
5. "Which tool would you recommend to a colleague in a similar spot? Why that one?"

**Example questions for the Business Model dimension (willingness to pay):**
1. "How much do you spend now on tools for [task]?"
2. "Tell me how you picked [the current tool] — what was the key factor?"
3. "What needs to be in a new tool for you to decide to try it?"
4. "How much time/money does it have to save to be worth [a concrete price point]?"
5. "Tell me about the last time you bought a paid subscription to a tool — how did you decide?"

### Closing

```
Thank you so much! That was really useful.

One last question: do you know anyone else who is similar to you on
[attribute] and might be interesting to talk to? I'm looking for more
people for the research.

[If there's an incentive:] As a thank-you for your time — a small gift,
[concretely what].

Thanks! If you remember anything else — write to [contact]. Good luck
with [the business]!
```

---

## Step 5.3 — Coverage matrix

Table: question → dimension → assumption from assumptions-map.md.

Goal: make sure all risk-dimensions are covered, and that most of the Critical quadrant assumptions get at least 1 question.

```markdown
| # | Question | Dimension | Assumption tested |
|---|----------|-----------|---------------------|
| 1 | Walk me through how you handle orders... | Problem | D1: "sellers spend 4-6 hours/week" |
| 2 | What part takes the most time? | Problem | D1 (drilldown) |
| 3 | How much do you spend on tools for X? | Business Model | V1: "willing to pay $29/mo" |
| ... | | | |
```

Every assumption from the Critical quadrant of assumptions-map.md should have at least one question. If any assumption is not covered — add a question or explicitly mark "out of scope this round."

---

## Step 5.4 — Quantity recommendation

**Minimum: 15 interviews.**
**Sweet spot: 20-30.**

**Why 15+:**
- Saturation (new patterns stop appearing) usually hits around 12-20 interviews with one target audience
- Fewer than 12 — high risk that the sample is unrepresentative
- 15 is the conventional minimum for a qualitative PMF study
- 30+ is overkill for one risk-dimension, better to do fewer but deeper

**If you have several target segments** — 15 each, not in total.

Write into the guide explicitly:

```markdown
## Quantity

- Minimum: 15 interviews with [primary target segment]
- [If there is a Future segment] +5 interviews with [secondary target segment] for contrast
- Saturation: expected at 12-20 interviews
- If patterns repeat after 15 → you can stop
- If patterns are not yet there at 20 → the guide may need rework
```

---

## Step 5.5 — Note template for the user

Create `interviews/note-template.md` (a short single-note template) — the user will copy it for each interview.

Structure:

```markdown
# Interview: [respondent ID or alias]

**Date:** [YYYY-MM-DD]
**Duration:** [minutes]
**Format:** [in-person / video / phone]
**Recording:** [yes / no]
**Screening:** [passed / failed + key attributes]

## Respondent context
[2-3 sentences about who this is: business, experience, situation]

## Key Quotes
[Verbatim quotes — not paraphrase, but the respondent's words in quotes]
- "..."
- "..."

## Observations per Dimension

### Problem to Solve
- What they say about the problem:
- Concrete examples from experience:
- Emotional tone (annoyance / calm / hopelessness / ...):

### Target Audience (fit)
- Confirms screening attributes:
- What makes them a typical/atypical example:

### [Other risk-dimensions from the coverage matrix]
- ...

## Surprises
[The unexpected — things contradicting the hypothesis or opening a new angle]

## Quantitative signals
[If they mentioned numbers: time, money, frequency]
- ...

## Follow-up needed
[What is still unclear — add to the guide for the next interviews]
```

---

## Step 5.6 — Saving

- `interview-guide.md` in the project folder root
- `interviews/` subfolder with `note-template.md` inside
- Also create an empty `interviews/notes/` subfolder (where the user will drop notes during Stage 6)

---

## Quality gates for Stage 5

- [ ] Identified 2-3 risk-dimensions from risk-prioritization
- [ ] Introduction script adapted to the product (not generic)
- [ ] 2-3 screening questions cover target audience attributes
- [ ] For each risk-dimension — 5-7 open questions (not leading, not hypothetical)
- [ ] Closing asks for a referral
- [ ] Coverage matrix covers all assumptions from the Critical quadrant
- [ ] Quantity recommendation: 15+ minimum
- [ ] note-template.md created in `interviews/`
- [ ] `interviews/notes/` folder created empty

---

## Common pitfalls in Stage 5

| Mistake | Symptom | Fix |
|--------|---------|------|
| Leading questions | "You agree X is hard, right?" | "How do you do X today?" |
| Hypothetical questions | "If there were a tool Y, would you..." | "Tell me about the last time you tried..." |
| Yes/no questions | "Do you use Excel?" | "Which tools do you use for X? Describe" |
| Future intent | "What are your plans for next year?" | "What has changed in the last year?" |
| Demographic screening | "How old are you?" | Behavior screening: "How often do you do Y?" |
| Generic introduction | "Hi, we are building a product" | Personal, concrete, emphasizing "not selling" |
| All questions about the product | "What do you think about features X, Y, Z?" | Most questions — about their life, their process, their pain |
| 30+ questions | A 2-hour guide | 5-7 per block × 2-3 blocks = 10-21 questions. Plenty |
| No coverage matrix | Not clear what is being validated | Every question → dimension → assumption |
| Closing on "thanks!" | No referral | In closing — always "do you know anyone else who..." |
