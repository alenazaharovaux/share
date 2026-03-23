# Diary Research Playbook

A set of 13 universal prompts for analyzing qualitative diary studies with any LLM (ChatGPT, Claude, Gemini, Cursor, etc.).

## What this is

Diary studies generate massive amounts of qualitative data: daily entries, photos, voice messages, screening data, interviews. This playbook gives you structured prompts to process each stage — from the first entry to the final synthesis report.

Each prompt is **self-contained** — paste it into any LLM, add your data, and get a structured result. No special tools, plugins, or frameworks required.

## Who this is for

- UX researchers running diary studies (product usage, mobility, habits)
- Qualitative researchers working with longitudinal self-reported data
- Research managers who need consistent analytical output across a team
- Anyone processing diary/journal data and wanting structured analysis

## The 13 prompts

### Daily analysis (during fieldwork)

| # | Prompt | What it does |
|---|--------|-------------|
| 01 | [Entry Analysis](01-entry-analysis.md) | Structure a single diary entry into a table row, extract insight candidates, classify by taxonomy |
| 02 | [Pattern Detection](02-pattern-detection.md) | Find behavioral patterns across multiple entries of one respondent |
| 07 | [Launch Brief](07-launch-brief.md) | Prepare analytical focus before a new respondent starts their diary |
| 08 | [Monitoring Card](08-monitoring-card.md) | Maintain a compact daily-updated card per respondent |
| 09 | [Daily Summary](09-daily-summary.md) | Write a daily analytical summary across all respondents |

### Interview stage

| # | Prompt | What it does |
|---|--------|-------------|
| 04 | [Interview Prep](04-interview-prep.md) | Prepare materials for a depth interview based on diary data |
| 05 | [Post-Interview](05-post-interview.md) | Process interview transcript, enrich existing insight cards |
| 11 | [Interview Zones](11-interview-zones.md) | Identify specific zones to dig into during the interview |

### Synthesis and reporting

| # | Prompt | What it does |
|---|--------|-------------|
| 03 | [Cross-Respondent](03-cross-respondent.md) | Compare multiple respondents, find inter-respondent patterns |
| 06 | [Final Synthesis](06-final-synthesis.md) | Build influence map, prioritize findings, answer research questions |
| 10 | [Narrative Analytics](10-narrative-analytics.md) | Write a narrative portrait of a respondent (analysis + storytelling) |
| 12 | [Business Article](12-business-article.md) | Map one respondent's behavior to business goals |
| 13 | [Review Interview Guide](13-review-interview-guide.md) | Evaluate the quality of an interview guide (8 assessment blocks) |

### Recommended workflow

```
Study launch:
  07 (Launch Brief) → per respondent, before fieldwork starts

During fieldwork (daily):
  01 (Entry Analysis) → per entry
  08 (Monitoring Card) → per respondent, daily update
  09 (Daily Summary) → across all respondents

Before interviews:
  02 (Pattern Detection) → per respondent
  04 (Interview Prep) → per respondent
  11 (Interview Zones) → per respondent

After interviews:
  05 (Post-Interview) → per respondent

Synthesis:
  10 (Narrative Analytics) → per respondent
  03 (Cross-Respondent) → groups or all
  06 (Final Synthesis) → final deliverable
  12 (Business Article) → per respondent, for stakeholders
```

## How to use

1. **Pick the prompt** that matches your current stage
2. **Open the prompt file** and read the "Customize for your project" section at the bottom
3. **Replace the placeholders** with your project's specifics (research questions, taxonomy, data format)
4. **Paste the prompt** into your LLM of choice
5. **Add your data** (diary entry, transcript, respondent profile, etc.)
6. **Review and iterate** — the prompt gives you structure, your expertise gives it meaning

### Tips

- Start with prompts 01 and 08 — they cover 80% of daily fieldwork
- The taxonomy (8 insight types) is a starting point — adapt it to your domain
- Each prompt includes a "Principles" section — read it once, internalize, skip later
- Prompts build on each other: Entry Analysis feeds Pattern Detection feeds Interview Prep

## Credits

By [Alena Zakharova](https://github.com/alenazaharovaux) ([Cloud Research](https://cloud-research.onrender.com)). Extracted and universalized from production Claude Code skills used in real diary studies.

## License

MIT — use freely, adapt, share.
