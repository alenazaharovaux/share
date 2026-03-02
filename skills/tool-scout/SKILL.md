---
name: tool-scout
description: >
  Search for tools (services, MCP servers, AI models, no-code platforms, libraries, APIs) to solve project tasks.
  Finds both established and new tools — freshness is critical.
  Triggers: "find tools for...", "what tools can solve...", "tool scout",
  "best way to do...", "search for services...", "how to build...".
---

# Tool Scout — find the right tools for your tasks

This skill helps you discover tools for project tasks. Not everything needs to be built from scratch —
a service, MCP server, AI model, or no-code platform might already solve your problem.

## Step 0. Configuration (First Run)

Read the config file at `~/.claude/skills/tool-scout/config.md`.

If the config file does not exist, run the setup:

**Question 1 — Search engine:**

Ask the user: "Which web search tool do you have available in Claude Code?"

Options:
- **Exa MCP** (recommended) — best results, supports both web search and code context search. Setup: https://docs.exa.ai/reference/mcp
- **WebSearch** — built-in Claude Code web search (no setup needed, but less precise)
- **Other MCP search** — if you have a different search MCP server, specify its tool name

**Question 2 — Language:**

Ask the user: "What language should I use for results and communication?"

Default: English.

Write answers to `~/.claude/skills/tool-scout/config.md` in this format:

```
search_engine: exa | websearch | other
search_tool_name: mcp__exa__web_search_exa
code_search_tool_name: mcp__exa__get_code_context_exa
language: english
```

If search_engine is "websearch", use the built-in WebSearch tool.
If search_engine is "other", use the tool name specified by the user.

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

### Step 3. Quick scan (Level 1)

For each domain, make 2-3 search queries using the configured search engine:

**Established tools query:**
`"best tools for [task] [current year]"`

**New tools query:**
`"new AI tool [task] launch [current and previous year]"`

**Technical integration query (if applicable):**
`"[task] MCP server"` or `"[task] library [language]"`

Always use the current year in queries. Never hardcode a specific year.

If multiple domains — run queries in parallel.

### Step 4. Build the table

From search results, compile a table:

| Task | Tool | Type | Maturity | Why it fits | Link |
|------|------|------|----------|-------------|------|

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

### Step 5. Output and offer deep dive

Display the table in chat. After the table, ask:

> Want to dig deeper into any of these? Say "dig into [name]".

## Deep Dive (Level 2)

If the user asks to dig deeper into a specific tool or domain:

1. Launch an Agent tool (subagent) with a detailed prompt:
   - Make 5-8 search queries about the tool
   - Find: detailed description, usage examples, pricing, limitations, alternatives
   - Return a structured report

2. Show result in chat:

### [Tool name]

**What it is:** brief description
**Price:** free / freemium / paid (how much)
**Maturity:** when launched, how many users
**Pros:** list
**Cons/limitations:** list
**Alternatives:** list
**How to integrate:** MCP / API / web interface
**Link:** URL

## Important

- Communicate in the language specified in config (default: English)
- Freshness is critical — always search for tools from the current and previous year
- Do not recommend dead or abandoned tools
- If a tool is an MCP server, say so explicitly (can be connected to Claude Code)
- If the task is trivial and better solved with code — say so directly
- Search engine is configurable — check config.md for which tool to use
