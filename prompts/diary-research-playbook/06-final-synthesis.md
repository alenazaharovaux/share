# Prompt 06: Final Synthesis

Build the final analysis: influence map, prioritized findings, answers to research questions.

---

## The prompt

```
You are a qualitative researcher producing the final synthesis of a diary study. You have insight cards, respondent portraits, tracking tables, hypothesis results, and entry summaries from all respondents. Your goal: transform individual findings into a structured, prioritized, actionable deliverable.

CRITICAL RULES:
- Not bare lists, but linked bundles. Every factor includes context, coverage, and evidence.
- Concrete quotes. Every claim is backed by the respondent's voice.
- Distinguish confirmation from discovery. If something was already known, mark it as "confirmed" — but with new context/nuance.
- Think about action. Every finding should lead to a concrete recommendation: what to build, what to fix, what to leave alone.

## Your task

Produce a complete synthesis. Follow all 8 steps.

### Step 1: Group insights by type

Collect all insight cards and sort by the 8 taxonomy types:
- How many barriers? Problems? Drivers? Unawareness of value? etc.
- Within each type — group by content (same barrier from different respondents = one group)

### Step 2: Count frequencies

For each insight group:
- How many respondents show it
- In which segments
- Strength of influence (absolute / conditional / weak)

Format:
[Insight/factor] — [N of M respondents] — segments: [X, Y] — strength: [strong/medium/weak]

### Step 3: Build the influence map

The influence map is the central artifact. For each factor:

[Factor] → [Type: barrier/driver/...]
  Contexts: [where it manifests — activities, times, conditions]
  Strength: [strong / medium / weak]
  Coverage: [N of M, in segments X, Y]
  Product/solution status: [feature exists / no feature / feature exists but unknown]
  Examples: [specific entries and quotes]

Rank factors within each type by: coverage × strength.

### Step 4: Sort into functionality groups

Based on the influence map + hypothesis results:

**Group 1: No value**
Functionality that doesn't solve the user's problem in the studied context.
- Which features? Why not valued? By which segments?

**Group 2: Value exists, but implementation blocks it**
Feature is useful, but UX ruins the experience.
- Which features? What specifically blocks? How could it be fixed?

**Group 3: Can do without**
Doesn't harm, but doesn't motivate the target behavior.
- Which features? Why not motivating?

**Group 4: Missing features**
User situations without solutions.
- Which situations? For which segments? What could help?

**Group 5: Lost trust**
Rejected because of past failures, even if improved since.
- Which features? What experience caused the loss? Recoverable?

### Step 5: Formulate development directions

Prioritized directions based on analysis:

| Direction | Solution type | Character | Coverage | Strength | Priority |
|-----------|-------------|-----------|----------|----------|----------|
| — | Feature / Interface / Notifications / Communication | New / Improvement / Amplification | N of M | — | — |

**Solution types:**
- Feature — new capability or improvement of existing
- Interface — UX improvements
- Notifications — push, contextual hints
- Communication — onboarding, education, marketing

**Change character:**
- New — what's needed doesn't exist
- Improvement — feature exists but implementation blocks it
- Amplification — feature exists and works but users don't know about it

### Step 6: Assess hypothesis statuses

| Hypothesis | Status | Segments | Conditions | Key quotes |
|------------|--------|----------|-----------|------------|
| [H1] | Confirmed / Partial / Rejected | — | — | — |
| [H2] | — | — | — | — |

### Step 7: Group respondents by behavioral types

Based on portraits and patterns:
- What groups emerged?
- How do they differ?
- How does this affect strategy?

### Step 8: Answer the research questions

For each research question from the study design:
- What did we find?
- With what confidence?
- What's the evidence base?
- What remains unanswered?

## Output format

## Final Synthesis

### 1. Influence map
[factors with full context × factor × frequency bundles]

### 2. Functionality groups
[5 groups with content]

### 3. Prioritized directions
[table of directions]

### 4. Hypothesis statuses
[table of statuses]

### 5. Behavioral types
[grouping with descriptions]

### 6. Answers to research questions
[structured answers]

### 7. Top findings (top 10)
[most important insights with quotes]

### 8. Recommendations
[what to do first, second, what not to touch]

## Synthesis principles

- **Linked bundles, not lists.** Every factor has context, coverage, evidence.
- **Concrete quotes.** Every claim backed by a user's voice.
- **Confirm vs. discover.** Mark what was already known vs. what's new.
- **Don't devalue the obvious.** "Obvious" findings backed by field data are valuable when quantified.
- **Action-oriented.** Every finding leads to: what to build, fix, launch, or leave alone.
```

---

## Customize for your project

**Functionality groups:** The 5 groups (no value / value blocked by implementation / can do without / missing features / lost trust) are from a product study. Adapt to your domain:
- Service design: "Works well / Friction point / Missing step / Broken handoff / Abandoned channel"
- Health research: "Effective behavior / Knows but doesn't do / Doesn't know it helps / Tried and failed / Believes it doesn't work"

**Research questions:** Replace Step 8 with your actual research questions from the study design. This is the most important customization — the synthesis exists to answer these questions.

**Hypothesis list:** Replace with your project's hypotheses in Step 6.

**Prioritization:** The coverage × strength formula is simple and effective. If your organization uses a specific prioritization framework (RICE, ICE, MoSCoW), map the output to that framework.
