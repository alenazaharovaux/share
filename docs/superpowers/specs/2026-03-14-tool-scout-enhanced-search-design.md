# Tool Scout — Enhanced Search Sources

**Date:** 2026-03-14
**Status:** Approved
**Scope:** Upgrade tool-scout skill with GitHub CLI, MCP catalogs, awesome-lists search

## Problem

Tool-scout currently searches only via web search (Exa/WebSearch). This misses:
- GitHub repositories (libraries, tools, MCP servers)
- Curated awesome-lists
- MCP server catalogs (smithery.ai, glama.ai)
- Package registries (npm, PyPI) — indirectly

Users don't know WHERE a tool might live. The skill should cover all sources automatically.

## Design

### Configuration (Step 0 — extended)

Add to existing config check:
- Run `gh --version` to detect GitHub CLI availability
- Store `github_cli: true | false` in config.md
- If `gh` unavailable — all GitHub queries fall back to web search with `site:github.com`

### Process (5 steps)

**Step 1 — Parse input** (unchanged)

**Step 2 — Classify by domain** (unchanged)

**Step 3 — Search** (single adaptive step)

Core queries (always run):
- Web: `"best tools for [task] [year]"`, `"new AI tool [task] launch [year]"`
- GitHub: `gh search repos "[task]" --sort=stars --limit=5`
  - Fallback (no gh): web search `site:github.com [task] tool`

Conditional queries (when relevant):
- **MCP** (when task involves integrations, automation, Claude Code):
  - `gh search repos "mcp server [task]" --sort=stars`
  - `gh search code "[task]" --repo=modelcontextprotocol/servers --filename=README.md`
  - Web: `site:smithery.ai [task]`
- **Awesome-lists** (when looking for curated tool lists):
  - `gh search repos "awesome-[topic]" --sort=stars --limit=3`
  - **Read the README** of top result (first 200 lines) → extract relevant tools
- **Libraries/packages** (when task needs a code dependency):
  - Web: `"best [language] library for [task] [year]"` (NOT `site:npmjs.com` — comparison articles are more informative than registry pages)

Source selection rule: **web + GitHub = always. MCP catalogs and awesome = when relevant. If unclear — include all.**

Multiple domains → run queries in parallel.

### Step 4 — Deduplication and table

Table structure:

| Task | Tool | Type | Maturity | Signals | Why it fits | Link |
|------|------|------|----------|---------|-------------|------|

**Signals column:**
- ★ GitHub stars (visible in `gh search` results, no extra API call)
- 🔴 Archived — red flag if repo is archived
- npm/PyPI download counts — only in Deep Dive (requires extra API calls)

**Deduplication:** if a tool is found in multiple sources — one row, signals aggregated. Multiple sources = higher confidence signal (mention in "Why it fits").

**Maturity:**
- Established — 1+ year, has community
- New — recently launched, promising
- Archived — repo archived, no longer maintained (red flag)

Do NOT use "last commit date" as a freshness signal — small tools and skills are often done and stable, infrequent commits don't indicate abandonment.

### Step 5 — Output and Deep Dive

Display table. After table, ask:
> "Want to dig deeper? Say 'dig into [name]' or ask about a specific source ('any MCP servers for this?', 'what about skills?')"

**Deep Dive (Level 2)** — enhanced:
- Can now target specific sources: "any skills for this?" → GitHub + awesome search
- npm/PyPI download counts retrieved here (not in Level 1)
- Agent subagent makes 5-8 targeted queries
- Returns structured report (unchanged format)

### What does NOT change

- Overall Level 1 → Level 2 structure
- Deep Dive report format
- Search engine configuration (Exa / WebSearch / other)
- "If task is trivial — say so directly" principle
- Language configuration

## Affected files

- `~/.claude/skills/tool-scout/SKILL.md` — local skill (Russian)
- `_repos/share/skills/tool-scout/SKILL.md` — shared skill (English)
- `~/.claude/skills/tool-scout/config.md` — add `github_cli` field

## Risks

- `gh search` has rate limits (30 requests/minute for authenticated users) — unlikely to hit with 2-5 queries per run
- Awesome-list READMEs can be very long — read with line limits
- `gh search code` in `modelcontextprotocol/servers` may return noisy results — limit to README.md files
