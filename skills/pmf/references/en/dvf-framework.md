# DVF Framework — Desirability × Viability × Feasibility

**Source:** David Bland & Alex Osterwalder, *Testing Business Ideas* (2019). Strategyzer.

**Why:** decompose the risk-dimension into concrete testable assumptions across three axes, so you know **what exactly to validate** and in **which order**.

**When applied:** Stage 4 (Validate). Once on the riskiest dimension from risk-prioritization. May be repeated for the second and third riskiest dimensions if the Stage 4 experiment is successful.

---

## Three categories

### Desirability — "Do they want it?"

Assumptions **only about user needs, behavior, motivation**. Nothing about money, nothing about technology.

What goes here:
- Real user behavior (how often, in what context, through what workarounds)
- Severity of the problem (does it block or just annoy)
- Frequency (once a day, once a month, once a year)
- Trigger (what kicks the need off)
- Desired outcome (what they want, not what we offer)
- Willingness to switch from the current solution

What does NOT go here:
- "They will buy it for $29" → Viability
- "They love a beautiful UI" → Desirability only if the beauty gives them benefit; otherwise it is Feasibility (we can make it pretty)
- "They will want a Slack integration" → Desirability only if the integration solves work; otherwise it is a feature wishlist

**Desirability test:** remove the product from the wording. Does the problem remain? If not — it is not Desirability, it is a feature request.

### Viability — "Will it bring money?"

Assumptions **only about economics, finance, monetization**.

What goes here:
- Pricing model (subscription, one-time, freemium, usage-based)
- Willingness to pay at a concrete price point
- Conversion rates (visitor → trial → paid)
- CAC (customer acquisition cost) per channel
- LTV (lifetime value) and its drivers
- Unit economics (gross margin, payback period)
- Market size (TAM/SAM/SOM) if pre-launch
- Pricing power (can you raise the price)

**Viability test:** remove the product from the wording and replace it with "the solution to this problem." Does the financial statement still hold? If yes — it is Viability.

### Feasibility — "Can we build and support it?"

Assumptions about **operational + technical + regulatory** capability.

Three sub-categories:

**Operational** — about the team and processes:
- Are there enough people on the team
- Can we support N customers with the current headcount
- Are the right skills inside the team
- Can we build the supply chain / distribution
- Can we meet the SLA

**Technical** — about code and infrastructure:
- Do the APIs/tools we need exist
- Are they stable enough for production
- Can we hit the needed latency / throughput / accuracy
- Are ML models of the needed quality available (for AI products)
- Can we migrate existing users

**Regulatory** — about laws and compliance:
- Is a license needed (fintech, healthtech, education)
- Do we comply with GDPR / CCPA / HIPAA / AI Act
- Are there intellectual property risks (patents, trademarks)
- Can we operate in the needed territories

---

## Regulatory sub-check

For three product types, regulatory becomes a **first-class** Feasibility, not a footnote:

| Product type | Minimum regulatory assumptions |
|--------------|-------------------------------|
| **AI / ML** | Data privacy for training data, AI Act if EU, copyright for outputs, model bias for regulated decisions (hiring, credit, healthcare) |
| **Fintech** | Licensing (BaaS provider or your own), KYC/AML, PCI DSS if cards, local financial regulators |
| **Healthtech** | HIPAA if US, GDPR-medical if EU, FDA classification if a medical device, telemedicine licensing per state/country |

If the product falls into a category — the regulatory assumptions **replace** part of the operational/technical inside the three Feasibility ones, they are not added on top.

---

## 9 assumptions: 3+3+3

DVF unfolds the risk-dimension into **strictly 9 assumptions, 3 per category**.

Why exactly 3:
- 1-2 — too few, do not cover all aspects of the dimension
- 4-5 — too many, duplicates and distractions appear
- 3 — forces you to prioritize the most important in each category

Why balanced (3+3+3) and not 5D + 2V + 2F:
- Imbalance masks missed risks
- If there really are no Viability questions — you are overestimating monetization confidence
- If Feasibility is "all easy" — you have not thought about regulatory or scaling

Each assumption starts with "I believe" — this turns an opinion into a testable statement.

---

## DVF Tension Check

After generating the 9 assumptions, look for the **biggest conflicts between categories**. Tensions = places where validating one category kills another.

Typical tensions:

| Tension | Example |
|---------|--------|
| **Desirability vs Viability** | "Users want it free" vs "We need a subscription for unit economics" |
| **Desirability vs Feasibility** | "They want real-time" vs "Technically only batch is possible" |
| **Viability vs Feasibility** | "$29/mo for the plan" vs "Cost to serve = $35/mo" |
| **Regulatory vs Desirability** | "They want anonymity" vs "KYC requires documents" |

Tension often **points to the riskiest assumption** — the place where the product can fall apart even if all three categories are individually confirmed.

Recorded in `assumptions-map.md` as one paragraph.

---

## 2×2 Matrix: Importance × Evidence

When the 9 assumptions are ready, place them on a matrix:

```
        High Importance
              |
    [Critical]| [Sweet spot]
   weak       |       strong
  evidence ---+--- evidence
  [Distraction]| [Solid]
              |
        Low Importance
```

**Importance scale:**
- **High** = if the assumption is wrong, the product breaks. Cannot adapt without a major pivot.
- **Low** = if the assumption is wrong, you can adapt. Not fatal.

**Evidence scale:**
- **Strong** = there is data from market research, existing users, analogs with concrete numbers
- **Weak** = only team opinion, indirect evidence or nothing

**4 quadrants:**

| Quadrant | What to do |
|----------|-----------|
| **Critical** (High imp + Weak ev) | Test **first**. The main risk lives here. |
| **Sweet spot** (High imp + Strong ev) | Do not touch, use as the foundation |
| **Solid** (Low imp + Strong ev) | Skip, save resources |
| **Distraction** (Low imp + Weak ev) | Ignore. Common mistake — getting carried away with this quadrant "because it is interesting" |

The point of the quadrant is to **pick 1–3 assumptions from Critical** for the experiment in Step 4.4.

---

## 6 standard experiment types

David Bland catalogued ~44 experiments. The PMF skill uses **6 base ones** that cover 95% of cases at early stages:

| Type | What it does | Cost | Best for |
|------|-----------|-----------|----------|
| **Customer Interview** | In-depth interview (45–60 min) with the target audience | Time, no $ | Desirability, behavior understanding |
| **Survey** | A structured survey at scale | $0–$200 for distribution | Desirability + Viability (willingness to pay) |
| **Smoke Test** | Landing page + ad → measure interest (sign-ups) before the product is built | $200–$1000 on ads | Desirability + Viability (intent) |
| **Landing Page** | A full landing with CTA, price, features | $200–$2000 | Demand validation, price testing |
| **Prototype** | A clickable prototype with no real backend (Figma, Framer) | Time, no $ | UX desirability + technical feasibility check |
| **Concierge** | Do the work by hand for 5–10 customers, simulating the product | Team time, no $ | Full D+V+F at small scale |

**Do not invent new types.** "Mini-pilot", "Discovery sprint", "Soft launch" are not experiments, they are vague terms. If nothing fits — reframe the assumption so a standard type works.

---

## Connection to other frameworks

**Lean Startup (Eric Ries):** DVF makes Build–Measure–Learn concrete. "Build" in Lean is not necessarily code, it is an experiment. DVF tells you **what exactly** to build as the experiment.

**Design Thinking (IDEO):** DVF uses the same "Desirable / Viable / Feasible" triad that IDEO proposed in 2009. Bland added systematic testing (assumptions map + experiment library) on top.

**Jobs-to-be-Done:** JTBD feeds Desirability assumptions — a "job to be done" *is* a need formulation. JTBD does not cover V and F.

**Customer Development (Steve Blank):** Customer Discovery in his model = Stage 4 + Stage 5 + Stage 6 in the PMF skill. DVF is how to structure what to validate in Customer Discovery.

---

## Common mistakes

| Mistake | Why it happens | How to avoid |
|--------|-------------------|--------------|
| All 9 assumptions in Desirability | The team is product-led, only thinks about users | Strict 3+3+3, no exceptions |
| Viability assumptions = "we will be able to monetize" | Too abstract | Concrete price point, concrete channel, concrete CAC |
| Feasibility = "we will build it" | Ignores technical unknowns | Decompose into operational/technical/regulatory |
| The assumption starts with "we need" | "We need a Slack integration" | That is a feature, not an assumption. "I believe users won't adopt without integration" |
| All assumptions in Sweet spot after the map | Wishful thinking | If 9/9 are in Sweet spot — Stage 4 is not needed; revisit importance, this is usually self-deception |
| Skipping 2×2 → straight to experiment | Laziness or rush | The 2×2 protects against testing a non-critical assumption |
| Customer Interview as a Viability test | "Let's ask if they would pay" | Interview does not validate pricing — people lie about it. Use a Smoke Test or Landing Page |

---

## When DVF does not work

DVF assumes you know who the target audience is and what problem you are solving. If neither is known — Stage 4 is premature. Go back to Stage 1 (Hypothesis) and work through the 7 dimensions first.

DVF is also not a fit for **deep tech R&D** where Feasibility is the main risk for years ahead (quantum computers, biotech). There you need a different framework (Technology Readiness Levels).

For everything else in B2B SaaS, consumer apps, marketplaces, AI products — DVF covers it.
