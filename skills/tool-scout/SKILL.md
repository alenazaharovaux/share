---
name: tool-scout
description: >
  Search for tools (services, MCP servers, Claude Code skills and plugins, AI models, no-code platforms,
  libraries, APIs, GitHub repos, awesome-lists) to solve project tasks. First checks what is already
  installed, then searches 5 sources: web, GitHub, MCP catalogs, awesome-lists, skill and plugin catalogs.
  Freshness is critical — finds current tools.
  Triggers: "find tools for...", "what tools can solve...", "tool scout",
  "best way to do...", "search for services...", "how to build...",
  "is there a skill for...", "find a skill for...", "is there a plugin for...",
  "is there an MCP server for...", "find a library for...".
---

# Tool Scout — find the right tools for your tasks

This skill helps discover tools for project tasks. Not everything needs to be built from scratch —
a service, MCP server, skill, plugin, AI model, library, or no-code platform might already solve your problem.

It first checks what you already have installed. Then it searches 5 sources: web search, GitHub,
MCP server catalogs, awesome-lists, and skill and plugin catalogs. Sources are selected adaptively based on the task type.

## Step 0. Configuration (First Run)

Read the config file at `~/.claude/skills/tool-scout/config.md`.

If the config file does not exist, run the setup:

**Question 1 — Search engine:**

Ask the user: "Which web search tool do you have available in Claude Code?"

Options:
- **Exa MCP** (recommended) — best results; `agent_run` works well for deep dives
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
research_tool_name: mcp__exa__agent_run
github_cli: true | false
language: english
```

If a tool from the config is missing in the current session — fall back to built-in WebSearch and mention it in the output.

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

### Step 2. Check what is already installed

Before searching outside, check whether the user already has a solution:

- Skills: `~/.claude/skills/skill-index.md` (if it exists), otherwise the folder list in `~/.claude/skills/`. Match task keywords against names and descriptions.
- Plugins: `claude plugin list`.
- MCP servers: `claude mcp list`.

Show any match as the first line of the output: "You already have X — it does Y". Still run the external search: something noticeably better may exist.

### Step 3. Classify by domain

Group tasks by domain:
- UI/design
- Backend/API
- Data/analytics
- Automation/integration
- Content/text
- Infrastructure/deployment
- Other

### Step 4. Search (adaptive source selection)

Determine task type and select sources:

| Task type | Web | GitHub | MCP catalogs | Awesome | Skills & plugins |
|---|---|---|---|---|---|
| SaaS/service | + | | | | |
| Library/package | + | + | | + | |
| MCP server | + | + | + | | + |
| AI tool | + | + | | + | |
| Skill/plugin | + | + | | + | + |
| Task inside Claude Code (writing, analysis, file work) | + | + | + | | + |
| Unclear | + | + | + | + | + |

Rule: **web + GitHub = always. Other sources = when relevant. If unsure — include all.**

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

#### Source 5: Claude Code skills and plugins

A skill is a folder with a `SKILL.md` file. A plugin is a package of skills, commands, hooks, and MCP servers installed from a marketplace.

**Official marketplace (local, offline):**
- If `~/.claude/plugins/marketplaces/claude-plugins-official/.claude-plugin/marketplace.json` exists — search its plugins by task keywords (`name`, `description` fields).

**If `github_cli: true`:**
- `gh search code "[task]" --filename=SKILL.md --limit=10` — finds skills by content. Use 2–3 English words ("pdf redact"). Long phrases return nothing; if empty, shorten and retry.
- `gh search repos "claude skill [task]" --sort=stars --limit=5`

**If `github_cli: false`:**
- Web search `"SKILL.md" [task] site:github.com`

**Catalogs (web search or fetch):**
- `anthropics/skills` — official Anthropic skills.
- `ComposioHQ/awesome-claude-skills`, `travisvn/awesome-claude-skills`, `hesreallyhim/awesome-claude-code` — curated lists.
- skillsmp.com — search across skills from public GitHub repos.
- claudemarketplaces.com — directory of plugins, skills, and MCP servers ranked by installs.
- aitmpl.com — Claude Code templates: agents, commands, skills, hooks.
- smithery.ai/skills — skills in the Smithery catalog.

Catalogs verified on 2026-10-20. If a catalog does not open — skip it and mention that in the output.

#### Parallelism

If there are multiple tasks or domains — run queries across different sources in parallel.

### Step 5. Deduplication and table

Compile a single table from results across all sources.

**Deduplication:** if a tool is found in multiple sources — one row, signals aggregated. Found in multiple places = higher confidence (mention in "Why it fits").

| Task | Tool | Type | Maturity | Signals | Why it fits | Link |
|------|------|------|----------|---------|-------------|------|

**Tool types:**
- Already installed — found in step 2
- Skill — folder with `SKILL.md`, copied into `~/.claude/skills/`
- Plugin — installed with `claude plugin install`
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
- ⚠ Code — the skill or MCP server ships scripts that will run on the user's machine

Last commit date is NOT a signal of abandonment — small tools and skills are often stable and don't need updates.

npm/PyPI download counts — only in Deep Dive (requires extra API calls).

### Step 6. Output and offer deep dive

Display the table in chat.

After the table — a 2–3 sentence verdict: what to take, why this one, first action.
Example: "Take X: it already does Y and was updated this month. First step — read its SKILL.md and copy it into `~/.claude/skills/`."

Then ask:

> Want to dig deeper? Say "dig into [name]".
> Or ask about a specific source: "any MCP servers for this?", "what about skills?", "any awesome-lists?"

## Deep Dive (Level 2)

If the user asks to dig deeper into a specific tool, domain, or source:

1. If `research_tool_name` from the config (Exa `agent_run`) is available in the session — run it. Otherwise launch an Agent tool (subagent). Prompt:
   - Make 5-8 search queries about the tool
   - Find: detailed description, usage examples, pricing, limitations, alternatives
   - If request targets a specific source ("any skills?") — targeted search via Source 5
   - Get npm/PyPI download counts (if applicable)
   - For a skill, plugin, or MCP server — read `SKILL.md` / README and list scripts, network calls, and required keys
   - Return a structured report with a source link for every fact

2. Show result in chat:

### [Tool name]

**What it is:** brief description
**Price:** free / freemium / paid (how much)
**Maturity:** when launched, how many users
**Signals:** ★ stars, downloads, found in [sources]
**Pros:** list
**Cons/limitations:** list
**Security:** what runs locally, what access it needs (for skills, plugins, MCP)
**Alternatives:** list
**How to integrate:** skill / plugin / MCP / API / web interface
**Link:** URL

## Important

- Communicate in the language specified in config (default: English)
- Freshness is critical — always search for tools from the current and previous year
- Every link and every number (stars, prices) must come from search results in this session. Never write links from memory.
- Do not recommend dead or abandoned tools (archived, no activity for years)
- If a tool is an MCP server, skill, or plugin, say so explicitly (can be connected to Claude Code)
- Read a third-party skill, plugin, or MCP server in full before installing. Tell the user what code they are about to run.
- If the task is trivial and better solved with code — say so directly
- Search engine and GitHub CLI are abstracted — check config.md
