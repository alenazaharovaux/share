---
name: tool-scout
description: >
  Search for tools (services, MCP servers, AI models, no-code platforms, libraries, APIs, GitHub repos,
  awesome-lists) to solve project tasks. Searches 5 sources: web, GitHub, MCP catalogs,
  awesome-lists, package registries. Freshness is critical — finds current tools.
  Triggers: "find tools for...", "what tools can solve...", "tool scout",
  "best way to do...", "search for services...", "how to build...",
  "is there a skill for...", "is there an MCP server for...", "find a library for...".
---

# Tool Scout — find the right tools for your tasks

This skill helps discover tools for project tasks. Not everything needs to be built from scratch —
a service, MCP server, AI model, library, or no-code platform might already solve your problem.

Searches 5 sources: web search, GitHub, MCP server catalogs, awesome-lists,
and package registries. Sources are selected adaptively based on the task type.

## Step 0. Configuration (First Run)

Read the config file at `~/.claude/skills/tool-scout/config.md`.

If the config file does not exist, run the setup:

**Question 1 — Search engine:**

Ask the user: "Which web search tool do you have available in Claude Code?"

Options:
- **Exa MCP** (recommended) — best results, supports both web search and code context search
- **WebSearch** — built-in Claude Code web search (no setup needed, but less precise)
- **Other MCP search** — if you have a different search MCP server, specify its tool name

**Question 2 — GitHub CLI:**

Check automatically: `gh --version`
- If available → `github_cli: true`
- If not → `github_cli: false` (GitHub search falls back to web queries with `site:github.com`)

**Question 3 — Language:**

Ask the user: "What language should I use for results and communication?"
Default: English.

Write answers to `~/.claude/skills/tool-scout/config.md`:

```
search_engine: exa | websearch | other
search_tool_name: mcp__exa__web_search_exa
code_search_tool_name: mcp__exa__get_code_context_exa
github_cli: true | false
language: english
```

## Input

A task or list of subtasks from the user's prompt:
- Free text: "need to build a UI for a dashboard"
- Plan reference: "find tools for tasks 3-5 from the plan"
- Specific subtask: "best way to generate PDF reports"

If a plan file is referenced — read it and extract tasks.

## Process

### Step 1. Parse input

Identify specific tasks/subtasks from the prompt. If input is a plan file, read it.
Formulate each task as a short search phrase.

### Step 2. Classify by domain

Group tasks by domain:
- UI/design
- Backend/API
- Data/analytics
- Automation/integration
- Content/text
- Infrastructure/deployment
- Other

### Step 3. Search (adaptive source selection)

Determine task type and select sources:

| Task type | Web | GitHub | MCP catalogs | Awesome |
|---|---|---|---|---|
| SaaS/service | + | | | |
| Library/package | + | + | | + |
| MCP server | + | + | + | |
| AI tool | + | + | | + |
| Skill/plugin | + | + | | + |
| Unclear | + | + | + | + |

Rule: **web + GitHub = always. MCP catalogs and awesome = when relevant. If unsure — include all.**

#### Source 1: Web search (always)

Established tools query:
`"best tools for [task] [current year]"`

New tools query:
`"new AI tool [task] launch [current and previous year]"`

Library query (when task needs code):
`"best [language] library for [task] [current year]"`

This is more effective than `site:npmjs.com` — comparison articles provide more context than registry pages.

Always use the current year. Never hardcode a specific year.

#### Source 2: GitHub (always)

**If `github_cli: true`:**
- `gh search repos "[task]" --sort=stars --limit=5`
- `gh search repos "[task] tool" --sort=stars --limit=5`

**If `github_cli: false` (fallback):**
- Web search `site:github.com [task] tool`

#### Source 3: MCP catalogs (when task involves integration, automation, Claude Code)

**If `github_cli: true`:**
- `gh search repos "mcp server [task]" --sort=stars`
- `gh search code "[task]" --repo=modelcontextprotocol/servers --filename=README.md`

**If `github_cli: false`:**
- Web search `"mcp server [task]" site:github.com`

Additionally (always):
- Web search `site:smithery.ai [task]`

#### Source 4: Awesome-lists (when looking for curated tool lists)

**If `github_cli: true`:**
- `gh search repos "awesome-[topic]" --sort=stars --limit=3`

**If `github_cli: false`:**
- Web search `awesome [topic] github`

If a relevant awesome-list is found — **read the README** (first 200 lines) and extract relevant tools.

#### Parallelism

If there are multiple tasks or domains — run queries across different sources in parallel.

### Step 4. Deduplication and table

Compile a single table from results across all sources.

**Deduplication:** if a tool is found in multiple sources — one row, signals aggregated. Found in multiple places = higher confidence (mention in "Why it fits").

| Task | Tool | Type | Maturity | Signals | Why it fits | Link |
|------|------|------|----------|---------|-------------|------|

**Tool types:**
- MCP server — can be connected to Claude Code
- SaaS/service — external web service
- AI model — specialized neural network
- Library — npm/pip package
- API — external API for integration
- No-code — visual builder

**Maturity:**
- Established — 1+ year, has community
- New — recently launched, promising
- Archived — repo archived, no longer maintained (red flag)

**Signals column:**
- ★ GitHub stars (visible in `gh search` results, no extra API calls)
- 🔴 Archived — if repo is archived

Last commit date is NOT a signal of abandonment — small tools and skills are often stable and don't need updates.

npm/PyPI download counts — only in Deep Dive (requires extra API calls).

### Step 5. Output and offer deep dive

Display the table in chat. After the table, ask:

> Want to dig deeper? Say "dig into [name]".
> Or ask about a specific source: "any MCP servers for this?", "what about skills?", "any awesome-lists?"

## Deep Dive (Level 2)

If the user asks to dig deeper into a specific tool, domain, or source:

1. Launch an Agent tool (subagent) with a detailed prompt:
   - Make 5-8 search queries about the tool
   - Find: detailed description, usage examples, pricing, limitations, alternatives
   - If request targets a specific source ("any skills?") — targeted search via GitHub + awesome
   - Get npm/PyPI download counts (if applicable)
   - Return a structured report

2. Show result in chat:

### [Tool name]

**What it is:** brief description
**Price:** free / freemium / paid (how much)
**Maturity:** when launched, how many users
**Signals:** ★ stars, downloads, found in [sources]
**Pros:** list
**Cons/limitations:** list
**Alternatives:** list
**How to integrate:** MCP / API / web interface
**Link:** URL

## Important

- Communicate in the language specified in config (default: English)
- Freshness is critical — always search for tools from the current and previous year
- Do not recommend dead or abandoned tools (archived, no activity for years)
- If a tool is an MCP server, say so explicitly (can be connected to Claude Code)
- If the task is trivial and better solved with code — say so directly
- Search engine and GitHub CLI are abstracted — check config.md
