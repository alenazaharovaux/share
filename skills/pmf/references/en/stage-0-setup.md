# Stage 0 — Setup

**Goal:** collect basic product and team context so Stage 1 (Hypothesis) can start with the full map of variables. This is a short stage (10–20 minutes), but without it all the later stages lose their footing.

**Reads:** —
**Writes:** `00_setup.md`

---

## When it runs

Auto-start detects one of:
- The project folder was just created (empty)
- The folder has no artifacts in it
- The user explicitly said "new PMF for X"

If `00_setup.md` already exists in the folder — Stage 0 is skipped, jump straight to Stage 1.

---

## Step 0.1 — Product name and slug

**Ask:**
1. **Full product name** — how you will refer to it in the narrative
2. **Slug** — a short folder name, lowercase, hyphenated (e.g. `cloud-research-ai-pipeline`, `bogdana-easter`, `znalica-paid-tier`). If the user does not propose one — propose a variant from the product name and confirm.

**Create the folder:** `<projects_path>/<slug>/` (where `<projects_path>` comes from `~/.claude/skills/pmf/config.md`, default `~/pmf-projects/`)

If a folder with that slug already exists — ask: "A product `<slug>` already exists. Same one or different? If different — pick another slug."

---

## Step 0.2 — Product type

**Ask, picking one option:**

| Type | Examples |
|-----|---------|
| **B2C SaaS** | app / service for individuals with subscription or paid features |
| **B2B SaaS** | service for companies (sold to managers, used by employees) |
| **Marketplace** | platform connecting two sides (buyer↔seller, client↔provider) |
| **DTC (Direct-to-Consumer)** | physical product sold directly to the user |
| **Services / Consulting** | a service delivered by a person or team (research, design, development) |
| **Internal tool** | a product for internal teams in an org, not for sale |
| **Other** | if none fits — briefly describe what it is |

**Why it matters:** the type drives multi-role handling in Stage 1:
- **B2B SaaS** → Decision Makers (who pays) ≠ End Users (who uses). Separate dimensions per role are needed.
- **Marketplace** → Demand side (buyers) ≠ Supply side (sellers). Separate dimensions + the chicken-and-egg problem must be flagged explicitly.
- **Other types** → one audience, one dimensions table.

---

## Step 0.3 — Organizational context

**Ask, picking one option:**

| Context | Description |
|----------|----------|
| **Zero-to-one** | a brand-new product, no existing customers, no channels, no brand |
| **Established** | inside an already running company, has brand, channels, and customers you can show the product to |
| **Extension** | extending an existing product (new feature, new segment, new market) |

**Why it matters:** the context shifts emphasis in Stages 1-3:
- **Zero-to-one** → more focus on Timing (Why Now) and Founder-Market Fit. No shortcut via existing channels.
- **Established** → reuse of existing channels, audiences, reputation. The main risk is cannibalizing the existing offer.
- **Extension** → cross-fit with the existing product matters more than absolute numbers. Which dimensions are inherited from the parent product, which are new.

---

## Step 0.4 — Team Pre-Flight Check

**Before** working on the product dimensions, you need an honest look at the team. Three short questions:

1. **Founder-Market Fit.** Why is this team specifically the one working on this idea? Do you have an "earned secret" — something you know about this problem/market from personal experience that others do not?

2. **Skill gaps.** Which key competencies are missing on the team right now? (product / engineering / sales / marketing / domain expertise)

3. **Conviction vs flexibility.** How willing are you to radically change the hypothesis if the data shows it is wrong? Scale 1-10. (10 = fully ready to pivot, 1 = too emotionally / financially invested to change)

**Risk flag** — record in `00_setup.md`:

| Level | Condition |
|---------|---------|
| **High risk** | no founder-market fit + 2+ key skill gaps + conviction-flex < 5 |
| **Medium risk** | one of the three conditions above |
| **Low risk** | none of the above |

**This is not a blocker for continuing** — it is context for interpreting the rest of the stages. If the risk is high, the priority in Stages 2-4 is to find partners or advisors who close the gaps.

The pre-flight results will be carried into `narrative-v1.md` in Stage 1 (as a separate section), so they are visible in all later stages.

---

## Step 0.5 — Write `00_setup.md`

File structure:

```markdown
# Setup — <Product name>

**Slug:** <slug>
**Date:** <YYYY-MM-DD>
**Stage:** Stage 0 (Setup) → ready for Stage 1 (Hypothesis)

## Product

**Name:** <full name>
**Type:** <B2C SaaS | B2B SaaS | Marketplace | DTC | Services | Internal | Other>
**Org context:** <Zero-to-one | Established | Extension>

**Short description (1-2 sentences):** <what it is and for whom, in the most general form, no claim to a final wording — that will be sharpened in Stage 1>

## Team Pre-Flight Check

**Founder-Market Fit:**
<answer — what the team knows about this problem/market that others do not>

**Skill gaps:**
- <gap 1>
- <gap 2>
- ...

**Conviction vs flexibility:** <X/10>
<short note>

**Risk flag:** <High | Medium | Low>
<rationale if high or medium>

## Notes

<any extra important context that did not fit above — company state, deadlines, constraints, existing data, relevant personal background>

---

## Next step

Stage 1 — Hypothesis (7 dimensions). Go to `references/<lang>/stage-1-hypothesis.md`.
```

---

## Quality gates

Before moving to Stage 1, verify:

- [ ] Project folder created at the correct path
- [ ] Slug is lowercase, hyphenated, no spaces, ASCII
- [ ] Product type picked from the list (not "not sure")
- [ ] Organizational context picked from the list
- [ ] Team Pre-Flight Check filled — all 3 questions
- [ ] Risk flag explicitly set (High / Medium / Low)
- [ ] `00_setup.md` saved in the project folder

If anything is missing — do not move to Stage 1, go back and fill it. Stage 1 will reference this data, gaps will break the work on dimensions.

---

## Common pitfalls

| Mistake | How to avoid |
|--------|--------------|
| "Not sure if this is B2C or B2B" | Ask: who actually pays — the end user or their company? That is the type. |
| Pre-flight check filled mechanically, without honesty | The skill's tone is calm, non-judgmental. Explain: pre-flight does not block, it only adjusts the priorities in Stages 2-4. The more honest, the more useful. |
| Conviction-flex = 10 for everyone | 10 means "I will fully pivot if the data says so." That is rare in practice. Usually 5-7. A 10 is a flag that the question was not understood. |
| Slug in non-ASCII or with spaces | Slug is a folder name. ASCII, lowercase, hyphens. |
| Skipping Stage 0 because "I already know everything about my product" | Do not skip. 5-10 minutes on 00_setup.md saves hours of mismatch in Stage 1. |
| 00_setup.md written as "an essay about the product" | It is a structured context, not a narrative. The narrative is in Stage 1. Here only the facts needed to unpack the dimensions. |

---

## What NOT to do in Stage 0

- **Do not formulate the hypothesis** — that is Stage 1
- **Do not describe the problem / value prop** — that is Stage 1
- **Do not do market research** — that is Stage 2
- **Do not flatter the team** — pre-flight requires honesty, otherwise it loses meaning
