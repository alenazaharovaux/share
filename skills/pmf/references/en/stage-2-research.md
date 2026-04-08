# Stage 2 — Market Research

**Goal:** find analogs (successful companies that validate one or another dimension of your hypothesis) and antilogs (known failures due to problems with that dimension) for each of the 7 dimensions.

**Reads:** `narrative-v1.md`
**Writes:** `market-research.md`

---

## ⛔ Critical rules for Stage 2

1. **No subagents.** Search is done by direct calls to `mcp__exa__web_search_exa` (preferred) or `WebSearch` (fallback). In the main session. Hard rule: agents are banned for content tasks.

2. **The user sees every search.** Do not hide the process. The user can step in with a clarification, and that is useful.

3. **It is OK to split into 2 passes.** If the context overflows or the user is tired — note where you stopped and continue in the next session. That is normal for a months-long cycle.

4. **Key rule:** an analog = a company that **successfully validated this dimension under real conditions**. Not "also works in this niche" — but "proved that **this dimension specifically** works."

---

## Step 2.1 — Read narrative-v1

From narrative-v1 extract:
- Product type (for the adaptive threshold)
- 7 dimensions with their wordings
- Confidence scores (research the risk-dimensions more thoroughly)
- Riskiest dimension (priority)

---

## Step 2.2 — Adaptive threshold

**What counts as an analog** (revenue floor):

| Market type | Threshold |
|-----------|-----------|
| Mature SaaS / e-commerce / marketplace / fintech | $10M+ revenue OR 100K+ paying users |
| Emerging (AI, web3, new categories) | $1M+ ARR OR 10K+ active users |
| Hardware | $5M+ revenue OR 50K+ units sold |

**What counts as an antilog:**
- Raised funding ($500K+) and shut down
- Was known (mentions in TechCrunch, Crunchbase, professional press) and shut down
- A pivot was publicly explained as a failure on this specific dimension
- Acquihire after failure ≠ exit (this is a shutdown)

---

## Step 2.3 — Search strategies for the 7 dimensions

For each dimension — concrete query strategies. Run 2-3 searches per dimension.

### Dimension 1: Problem to Solve

**What we're looking for:**
- Companies that solved **the same class of problem** (not necessarily in the same niche) and succeeded
- Companies that tried to solve this problem and failed

**Search queries (examples):**
- `"[problem class]" startup raised funding acquired`
- `"[problem class]" YC company unicorn`
- `"[problem class]" startup shutdown failed reasons`
- Exa semantic: "companies that solved [vivid problem description]"

**What to record:**
- Analog: company + revenue/users + year founded + what specifically validated this dimension
- Antilog: company + funding raised + reason for failure (documented)

### Dimension 2: Target Audience

**What we're looking for:**
- Companies that successfully built a product for **the same demographic / behavioral group**
- Companies that missed on the audience (broad vs narrow, wrong segment)

**Search queries:**
- `"[audience description]" SaaS market size`
- `"[audience description]" startup CAC payback`
- `"[audience description]" startup pivot wrong target`
- Exa: "companies that successfully serve [specific audience]"

**What to record:**
- Analog: company + audience + retention/CAC if known
- Antilog: company + why they missed the audience

### Dimension 3: Value Proposition

**What we're looking for:**
- Companies with **a similar value-prop structure** (tagline + benefits structure)
- Companies that failed because of a vague value prop or features-focused messaging

**Search queries:**
- `"[main benefit]" SaaS positioning success`
- `"[similar value prop]" startup growth trajectory`
- `startup failure feature creep no clear value prop`

**What to record:**
- Analog: company + tagline + why the value prop works
- Antilog: company + how the value prop was muddled

### Dimension 4: Competitive Advantage

**What we're looking for:**
- Companies that built a moat on **the same one of the 7 Powers**
- Companies that thought they had a Power, but did not

**Search queries:**
- `"[power name]" startup moat success [industry]`
- `"network effects" SaaS company growth`
- `"first mover advantage" startup failed lost market`
- `"counter-positioning" startup incumbent unable to copy`

**What to record:**
- Analog: company + which Power + how the compounding actually works
- Antilog: company + the false Power + what failed to defend it

### Dimension 5: Growth Strategy

**What we're looking for:**
- Companies with a similar growth strategy (short + long term)
- Companies that failed because of **a non-working growth channel**

**Search queries:**
- `"[channel name]" SaaS startup first 1000 users`
- `"product-led growth" startup playbook examples`
- `"paid acquisition" startup CAC too high failed`
- `"viral coefficient" startup growth examples`

**What to record:**
- Analog: company + concrete channel + numbers (CAC, viral coefficient, conversion)
- Antilog: company + the channel that did not work + why

### Dimension 6: Business Model

**What we're looking for:**
- Companies with a similar monetization model in the same category
- Companies that failed on business model (mismatch of pricing/audience/cost)

**Search queries:**
- `"[pricing model]" SaaS company unit economics`
- `"freemium" startup conversion rate examples`
- `"marketplace take rate" successful examples`
- `startup failed unit economics LTV CAC`

**What to record:**
- Analog: company + concrete numbers (LTV, CAC, payback, gross margin)
- Antilog: company + why the numbers did not add up

### Dimension 7: Timing / Why Now

**What we're looking for:**
- Companies that landed in the window of a technology/behavior/regulation shift
- Companies that arrived too late or too early

**Search queries:**
- `"[triggering event]" startup founded year`
- `"first to market" startup failed too early`
- `"perfect timing" startup case study`
- `Bill Gross "single biggest reason" timing`
- Exa: "companies that succeeded because of timing [shift description]"

**What to record:**
- Analog: company + which shift + why right then (and not earlier)
- Antilog: company + why it was late or early

---

## Step 2.4 — Write into market-research.md

After each dimension write straight into `market-research.md` (create it at the start of Stage 2 from the template `references/<lang>/template-market-research.md`). Do not accumulate in memory.

Per-dimension structure in market-research.md:

```markdown
### Dimension N: [Name]

**Analogs:**
1. **[Company]** — [revenue/users] — founded [year]
   - **What it validates:** [concrete aspect of this dimension]
   - **Evidence:** [what we know — link / quote]
   - **Relevance:** [how applicable to our context, 1-5]

2. ...

**Antilogs:**
1. **[Company]** — raised [amount] — closed [year]
   - **Failure mode:** [how exactly they failed on this dimension]
   - **Evidence:** [source / quote]
   - **Lesson:** [what we can use from this]

**Patterns observed:** [what repeats across analogs]
**Counter-patterns:** [what repeats across antilogs]

**Confidence change:** [V1 score] → [updated score]
**Status:** Validated / Needs more research / At risk
```

---

## Step 2.5 — Cross-dimension themes

After all 7 dimensions — pull out patterns that **span several dimensions**:

- Analogs that validate 3+ dimensions at once (these are "similar deals" — the most valuable references)
- Antilogs where a failure on one dimension dragged down others (this shows risk sequencing)
- Incompatibility between dimensions in competitors (hints at a competitive gap for us)

Write into the `## Cross-Dimension Themes` section in market-research.md.

---

## Step 2.6 — Risk prioritization (preview)

Do not do a full risk scoring (that is Stage 3) — but at the end of market-research.md give a preview:

```markdown
## Preview: dimensions at risk after research

| Dimension | V1 Confidence | Post-research Confidence | Status |
|-----------|---------------|--------------------------|--------|
| ...       | ...           | ...                      | ...    |

**Riskiest after research:** [name]
**Recommended next:** Stage 3 (Synthesis) for full risk scoring
```

---

## Quality gates for Stage 2

- [ ] All 7 dimensions researched
- [ ] At least 3 analogs and 2 antilogs per dimension (or explicitly noted that none exist)
- [ ] Analogs meet the threshold (not "a startup with 10 users")
- [ ] Antilogs are documented (not rumors)
- [ ] Confidence updated for each dimension
- [ ] Cross-dimension themes pulled out
- [ ] Sources cited (no claims without backing)
- [ ] Context-aware: 2010 analog ≠ 2026 market — flagged where relevant

---

## Common pitfalls in Stage 2

| Mistake | Symptom | Fix |
|--------|---------|------|
| The analog does not validate this specific dimension | "It is a similar product" | State concretely: which dimension this company proves |
| The antilog is rumor | "I heard they shut down" | Find confirmation (article, Crunchbase, announcement) |
| Ignoring antilogs | Only success stories | Antilogs are more valuable: they show the rakes |
| Context not accounted for | "Facebook did this in 2007" | Note: what was true in 2007 ≠ now |
| Cherry-picking | Only what confirms the hypothesis | Look for antilogs with the same energy as analogs |
| Searching one source | Only Crunchbase | Diversify: TechCrunch, ProductHunt, IndieHackers, Twitter, Reddit |
| Spinning up an agent "do the research for me" | The agent writes the substance | Search in the main session. Every query — the user sees it |
| Not writing immediately | Hold everything in memory, write later | Write after each dimension. Otherwise it gets lost |
