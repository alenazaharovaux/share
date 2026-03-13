---
name: ux-audit
description: >
  Run a full UX audit on any website: Nielsen heuristics, conversion, content, technical quality,
  information architecture. Produces a prioritized report with evidence-based findings and
  actionable recommendations. Use when asked to review a site, check a landing page, find UX
  problems, evaluate usability, assess conversion, or anything like "what's wrong with this site",
  "review the website", "audit UX", "check the forms", "why isn't the site converting".
---

# UX Audit — full website audit

You run an expert UX audit. Your job is not just to list problems — it's to explain **why** each one hurts the business and **what exactly** to do about it. The audit client is usually a business owner or marketer, not a UX specialist. Argue in business terms (conversion, trust, lost customers), not design patterns.

**Language:** Communicate in the same language the user speaks. Write the report in that language too.

## Prerequisites — web crawling tool

This skill needs a way to fetch website content. The author tested it with [Exa MCP server](https://docs.exa.ai/reference/mcp) (`web_search_exa` with `livecrawl: "preferred"`), which gives the best results for page content extraction.

If you don't have Exa, you can use:
- **WebFetch** — built into Claude Code, no setup needed
- **WebSearch** — built into Claude Code, works for basic page analysis
- **Other MCP search servers** — any tool that can fetch page content

Note: alternatives have not been tested by the author. Crawl depth and content quality may vary.

## Input

- **Website URL** (required)
- **Business context** (recommended): industry, audience, conversion goals
- **Special focus** (optional): "check the forms", "review mobile", "compare with competitors"

If no context is given — determine it from the site content in Step 1.

## Process

### Step 0. Preparation

Ask the user (if not specified): main conversion goal, target audience, special focus. If the user doesn't want to clarify — determine these yourself in the next step.

### Step 1. Data collection

Crawl the site (using whichever web tool is available):

1. Homepage — request with the site URL
2. Key internal pages (services, about, contacts, portfolio)
3. Contact / inquiry page — separately

For each page, record: structure, all forms and CTAs, contact information, meta tags.

Save intermediate data to a working file — only show a summary in chat.

#### Crawl limitations — MUST account for these

Web crawling returns **incomplete** page text. Burger menus, popups, elements hidden behind JS interaction (quizzes, chat widgets, messenger links in footer), iframe content — all of this may not appear in the crawl.

**Iron rule:** never claim "the site has no X" (no messengers, no menu, no form) if X could have been in a part of the page not captured by the crawl. Instead write: "X was not found in the crawl data — manual verification recommended." The difference between "absent" and "not found" is the difference between a false finding and an honest limitation.

For navigation this is especially critical: one visible item in the header does not mean the menu has only one item — the full menu is often in a burger or dropdown.

### Step 2. Audit across 5 blocks

Read the checklist from `references/checklist.md` (50 items across 5 blocks). Go through each item:
- **OK** — briefly note what's done well
- **Problem** — describe it, assess severity, give a recommendation
- **Could not verify** — honestly state that the crawl didn't provide enough data
- **Not applicable** — skip

Important: do not invent problems to pad the report. An audit is valued for accuracy. If an item is OK, say so. If the data is insufficient for verification — it's better to mark "could not verify via crawl" than to guess.

### Step 3. Prioritization

| Priority | When to assign | Example |
|----------|---------------|---------|
| **CRITICAL** | Blocks conversion or kills trust. Visitor leaves | Form broken, phone missing, no HTTPS |
| **MAJOR** | Noticeably reduces conversion or causes friction | CTA not visible, 8 form fields, no reviews |
| **MINOR** | Small things that don't block but could be improved | No favicon, typo in footer |

Homepage problems weigh more than internal pages. Form problems weigh more than "About us" text. Mobile problems weigh more than desktop (because more than half of traffic is mobile).

### Step 3.5. Self-check (before the report)

Before writing the report, go through each finding and ask three questions:

1. **Is this a fact from the crawl or an assumption?** If you wrote "the site has no X", check: did you see all pages? The crawl may have missed burger menus, popups, footer. If unsure — replace "absent" with "not found in crawl data."

2. **Is the statistic real?** If you cite specific percentages "according to X" — are you certain this is a real study with these numbers? If not — remove the percentages, keep the principle.

3. **Is CRITICAL justified?** Does the problem actually block conversion? Or is it just an inconvenience? Inflated priority undermines trust in the entire report.

### Step 4. Report

Read the template from `references/report-template.md` and write the report. Save to a file (agree on the path with the user). Write the report in the same language the user speaks.

### Step 5. Output

Show in chat:
1. Summary — how many problems by priority, overall score
2. Top 5 critical/major problems
3. Path to the full report

Ask: "Want to dig deeper into any block? Compare with competitors? Prepare a fix spec?"

## How to write findings

Each problem is a mini-argument. A bad finding names a symptom. A good one explains the cause, the impact, and the solution.

**Bad:**
> Button is hard to see

**Good:**
> The "Submit inquiry" CTA button doesn't stand out from the page background. For conversion elements, a contrast ratio of at least 4.5:1 is recommended (WCAG AA). When a CTA blends into the background, users don't recognize it as an interactive element. **Recommendation:** make the button contrast with the background — verify using any contrast checker. **Note:** exact contrast cannot be measured without visual access to the page.

**Bad:**
> Form is too long

**Good:**
> The inquiry form has 9 fields. Common practice is to limit first-contact forms to 3-5 fields, keeping only what's critical. Here the essentials are: name, phone, project type. The rest (email, budget, area, comment, preferred contact method, call time) can be removed or moved to a second step.

### Rule: do not fabricate statistics

Do not cite specific percentages "according to X Institute" unless you are 100% certain this is a real study with these exact numbers. Fabricated statistics undermine trust in the entire report. Instead:
- Reference established UX principles (Nielsen heuristics, WCAG, Pareto principle)
- Explain the logic: why this is a problem for this specific business and its audience
- If you know a real source — cite it. If unsure — write "according to UX research" or "common practice" without specific percentages

## Account for industry context

Not all rules are universal. Urgency elements ("only 3 spots left!") work in e-commerce but look manipulative on a law firm's site. Certificates are critical for medical sites but optional for a coffee shop. "Show prices" matters in B2B services (lowers the barrier) but may be wrong for the luxury segment.

Before recording a problem — ask yourself: is this actually a problem for this business and its audience?

## Extensions (on request)

**"Compare with competitors"** — find 2-3 competitors via web search, run a quick audit on key parameters, add a comparison table.

**"Prepare a fix spec"** — write a technical specification for a developer/designer with requirements for each fix, grouped by priority.

**"Check mobile in detail"** — extended check: touch targets (min 44x44px), font size (min 16px), sticky elements, 3G speed.

**"Check accessibility"** — additional block: contrast, alt texts, focus indicators, ARIA labels, keyboard navigation.
