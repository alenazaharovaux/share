# Claude Doctor

> 📦 **This is a documentation snapshot.** The actual plugin lives at **[github.com/alenazaharovaux/claude-doctor](https://github.com/alenazaharovaux/claude-doctor)** — install it from there with `/plugin install claude-doctor`. This README is mirrored here so you can read what the plugin does without leaving the share repo.

> Structural guardrails for Claude Code. Hook-based in-moment reminders for production actions, architectural questions, and completion claims without evidence.

[🇷🇺 Читать на русском](README.ru.md)

**Why this exists:** Rules in CLAUDE.md / AGENTS.md are post-hoc appeals — Claude reads them at session start, then drifts away from them mid-session. This plugin injects reminders at the exact event where the pattern would repeat (`UserPromptSubmit` / `Stop`), not as text that needs to be re-read. See [references/philosophy.md](https://github.com/alenazaharovaux/claude-doctor/blob/main/references/philosophy.md) for the full rationale with external citations.

**Status:** v0.2.1. Log-only detection by default; selective blocking available for phrases you add to `claim_phrases_blocking` via `/claude-doctor:triage`. Cross-platform (Linux / macOS / Windows with Git Bash).

---

## What it does

**Production-keyword detector** (UserPromptSubmit). Triggers when the user's message contains production-operation language — defaults are bilingual (`deploy`, `migrate`, `publish to`, `push to production`, plus Russian equivalents `деплой`, `миграци`, `опублик`). On match, injects a five-point self-check block the assistant must fill with concrete tool output before acting. Extend the default list via `prod_keywords_add` in your project config.

**Architectural-question detector** (UserPromptSubmit). Triggers on advisory phrasings (`how should I...`, `what's the best approach`, `which pattern`, `посоветуй`, `как лучше`). On match, requires at least one tool call on real files (Read / Bash / Grep / Glob) before the assistant generates any recommendation. Addresses Pattern B from the philosophy doc — advisory questions tend to be answered from auto-loaded context rather than from fresh file reads.

**Fabrication detector** (Stop). Scans the assistant's last response when it tries to stop. Two sub-checks: (1) attribution fabrication — assistant claims the user has «code words» that the user never actually used in declarative form; (2) completion claims without evidence — assistant says «done», «deployed», «works» in a response that made no evidence-producing tool call (Read, Bash, Grep, Glob, WebFetch, MCP reads). Log-only in v0.1; flagged patterns are written to `$CLAUDE_PLUGIN_DATA/audit.log` (or `~/.claude/plugin-data/claude-doctor/audit.log` as fallback).

**Session-start analyzer** (SessionStart). Once per session, reads the last seven days of audit log, produces a concise summary, writes a human-readable monitoring file, and injects a one-line status into the session's initial context. Makes accumulated audit visible without requiring manual file inspection.

---

## Installation

These three commands are slash commands you type **inside Claude Code** (in the prompt, the same place you type your messages to Claude). They are not shell commands — don't paste them into your terminal.

Step 1 — register the marketplace:

```
/plugin marketplace add alenazaharovaux/claude-doctor
```

Expected response from Claude Code: a confirmation that the marketplace was added, listing one available plugin (`claude-doctor`).

Step 2 — install the plugin:

```
/plugin install claude-doctor@claude-doctor
```

Expected response: the plugin appears in the «Installed» tab of `/plugin`.

Step 3 — create your project config:

```
/claude-doctor:setup
```

This creates the file `.claude/claude-doctor.local.md` inside your current project directory (the folder Claude Code was opened in). The file contains all available settings with their default values — open it in any text editor to customize.

Hooks work even without the config file (they use built-in defaults), but the file is needed if you want to add project-specific keywords, change the language, or disable individual detectors.

### Prerequisites

**Python 3.** Open your terminal and run:

```bash
python3 --version
# or, if that says "command not found":
python --version
```

If you see something like `Python 3.10.0` or higher — you're good. If both commands say «command not found», install Python from [python.org/downloads](https://www.python.org/downloads/) (any 3.x version works, no extra packages needed).

**On Windows — Git for Windows.** The plugin uses a small shell script (`hooks/run.sh`) to detect which Python command to call. On Windows this script needs `sh` to run, which comes from Git Bash. Download and install Git for Windows here: [git-scm.com/download/win](https://git-scm.com/download/win). Default install options are fine — Git Bash is added automatically.

To check it's installed, open any terminal (PowerShell or cmd) and run `sh --version`. If you see a Bash version, you're set.

---

## First test after install

To confirm the plugin works, send these three messages to Claude one at a time (as separate prompts) and look for the responses below.

**Test 1 — production-keyword detector.** Type:

> let's deploy this to production

Expected: before Claude responds with anything else, you'll see a block starting with `🔍 CLAUDE DOCTOR — production keyword detected` followed by a five-point self-check checklist. If you see this, the `prod-keyword-detector` hook is firing.

By default the detector catches both English and Russian production verbs (`deploy`, `migrate`, `публикуй`, `деплой`, etc.), so the same test works in either language.

**Test 2 — architectural-question detector.** Start a fresh prompt and type:

> how should i structure this project?

Expected: a block starting with `🔍 CLAUDE DOCTOR — architectural/advisory question detected`, followed by instructions requiring Claude to read real files before answering. If you see this, the `architectural-question-detector` hook is firing.

**Test 3 — session-start summary.** Exit Claude Code completely (close the terminal or run `/quit`), then start a new session in any project. In the first system messages of the new session, look for a line like:

```
📊 Claude Doctor: 0 flags in last 7 days. Good or hooks disabled.  (details: ...path...)
```

If you see this, the `SessionStart` hook is firing. The path in parentheses points to the monitoring file written each session.

**The fabrication detector is harder to test directly** — it's the `Stop` hook, runs when Claude finishes a turn, and writes to a log in the background. To verify it ran at least once, check the heartbeat file in your terminal:

```bash
cat ~/.claude/plugin-data/claude-doctor/heartbeat.log
```

Each line is one `Stop` event with a timestamp and session ID. If the file exists and has lines, the hook is running.

If any test fails — see [Troubleshooting](#troubleshooting) below.

---

## Triaging flags interactively

The interactive flow uses `AskUserQuestion` — a built-in Claude Code tool that renders clickable buttons directly in the chat. No extra install, no extra dependency: if you're running Claude Code, you already have it. Official reference for the slash-command model and tools: [code.claude.com/docs/en/slash-commands](https://code.claude.com/docs/en/slash-commands).

After a few days of use, the audit log accumulates flags. Some correspond to real fabrication moments where Claude claimed completion without verifying anything. Others are noise — a phrase that legitimately shows up in the way you write, with no intent to mislead. The log on its own does not distinguish between them; you do, through `/claude-doctor:triage`.

The command reads the log, filters out flags that were already triaged in an earlier run, and walks you through the remainder one phrase at a time. For the most frequent phrases it starts with a bulk prompt — `AskUserQuestion` buttons let you resolve every occurrence of a phrase in a single click:

- **Block all** — adds the phrase to `claim_phrases_blocking`. The next time Claude writes this phrase without calling an evidence tool (`Read`, `Bash`, `WebFetch`, and so on), the `Stop` hook blocks the turn with exit code 2 and asks Claude to either verify the claim or retract it.
- **Ignore all** — adds the phrase to `claim_phrases_ignore`. Future occurrences are dropped before they reach the log. Pick this for phrases that are part of your normal vocabulary.
- **Review individually** — expands into a per-flag loop with the full context of each occurrence, so you can decide case by case.
- **Skip** — leaves the flag for a later run.

**When to pick «Review individually».** The bulk view shows three sample contexts per phrase — usually enough to recognise the pattern and choose block or ignore. If those three samples point in opposite directions (one looks like honest reporting after a tool call, another looks like an unverified claim), that is the signal to switch to review. The per-flag loop walks you through occurrences one at a time until you see enough to decide. The final decision is still per-phrase: as soon as you pick **Block this phrase** or **Ignore this phrase** on any single flag, that choice applies to all remaining occurrences of the same phrase, and the review ends. You don't process every flag individually — you read until you understand, then act once.

After the top phrases are handled in bulk, anything left is shown one flag at a time with the same three decisions minus the «all» qualifier. Phrases you've already blocked or ignored are filtered out automatically on every run, so the next `/triage` does not re-ask about resolved cases. Phrases you skipped come back on the next run — skip is «decide later», not «never show again».

The point of this flow is gradual training. You start with every phrase treated equally; over a few sessions the blocking list collects the small number of patterns that actually predict trouble for your work, and the ignore list absorbs whatever happens to overlap with normal writing. Once both lists stabilise, the detector runs on the residual — which is where real signal tends to be.

If you prefer to work by hand, open `.claude/claude-doctor.local.md` and edit `claim_phrases_blocking` or `claim_phrases_ignore` directly. `/triage` is a convenience, not a requirement.

---

## Configuration

Edit `.claude/claude-doctor.local.md` in your project:

| Field | Type | Default | Meaning |
|---|---|---|---|
| `enabled` | bool | `true` | Master switch. When `false`, all Claude Doctor hooks skip. |
| `language` | string | `"en"` | Injected-message language: `"en"`, `"ru"`, or `"both"` |
| `prod_keywords_add` | list[str] | `[]` | Words added to the default prod-keyword list |
| `prod_keywords_replace` | list[str] | `[]` | If non-empty, fully replaces defaults |
| `architectural_enabled` | bool | `true` | Enable architectural-question detector |
| `fabrication_enabled` | bool | `true` | Enable Stop-hook fabrication detector |
| `claim_phrases_add` | list[str] | `[]` | Extra completion-claim phrases |
| `claim_phrases_replace` | list[str] | `[]` | If non-empty, fully replaces defaults |
| `claim_phrases_blocking` | list[str] | `[]` | v0.2+: phrases that trigger Stop-hook `exit 2` when detected without an evidence tool. Normally populated through `/claude-doctor:triage`. |
| `claim_phrases_ignore` | list[str] | `[]` | v0.2+: phrases excluded from flagging entirely. Populated through `/claude-doctor:triage` (Ignore / Ignore all). |
| `last_triage_timestamp` | string | `""` | Legacy field from v0.2.0. Kept in the schema for backward compatibility but no longer used since v0.2.1. Skipped phrases now come back on every run until blocked or ignored. |
| `scan_history` | bool | `true` | Let fabrication-detector read `~/.claude/history.jsonl` |
| `monitoring_path` | string | `""` | Override SessionStart summary file location |

Example:

```yaml
---
enabled: true
language: "both"
prod_keywords_add: ["kubectl apply", "terraform apply", "helm upgrade"]
architectural_enabled: true
fabrication_enabled: true
scan_history: false
monitoring_path: "~/notes/claude-audit.md"
---

# Notes (free-form, ignored by plugin)
Configured for infra project — added K8s/TF/Helm verbs to prod triggers.
Turned off history scan for privacy.
```

Changes take effect on the **next** hook invocation. No Claude Code restart required — the config file is read per event.

---

## Philosophy

Why does this need to be a hook instead of just another rule in CLAUDE.md? Short answer: rules in CLAUDE.md activate post-hoc, hooks activate in-moment. Long answer, with external citations (four GitHub issues on anthropics/claude-code, Andrej Karpathy's public comments, Huang et al. 2023 on LLM self-correction, Anthropic alignment-faking research), in [references/philosophy.md](https://github.com/alenazaharovaux/claude-doctor/blob/main/references/philosophy.md).

---

## Troubleshooting

**Hooks silent — nothing happens on trigger words.** Run `claude --debug` and watch the output for hook registration messages. If hooks aren't registered, check that the plugin is enabled via `/plugin` menu. If hooks are registered but not firing, check that `python3` or `python` is in your `PATH`.

**Windows: `sh: command not found`.** The plugin's launcher (`hooks/run.sh`) needs `sh` available. On Windows this comes from Git Bash. Install [Git for Windows](https://git-scm.com/download/win) — Git Bash is bundled and adds `sh` to your PATH automatically.

**Configuration changes don't take effect.** Config is re-read per hook invocation, but you need to trigger a hook event to see the new behavior. Send a new user message with a trigger word. If still no effect, check that you saved the file and that YAML frontmatter is syntactically valid (starts and ends with `---` on their own lines).

**`/plugin update` says «already at latest version» but I see a new release on GitHub.** Known Claude Code bug — see [anthropics/claude-code issue #25244](https://github.com/anthropics/claude-code/issues/25244). The plugin manager doesn't `git pull` the marketplace clone before checking versions. Workaround:

```bash
cd ~/.claude/plugins/marketplaces/claude-doctor && git pull
# then back in Claude Code:
/plugin update claude-doctor@claude-doctor
```

**Where are the logs?** Audit log: `$CLAUDE_PLUGIN_DATA/audit.log` if that env var is set by Claude Code, otherwise `~/.claude/plugin-data/claude-doctor/audit.log`. Heartbeat log (proves hook ran even without flags): same directory, `heartbeat.log`. Monitoring summary: same directory, `monitoring.md`, unless you override `monitoring_path`.

**How do I turn it off without uninstalling?** Two options. (1) `/plugin disable claude-doctor@claude-doctor` — disables until you re-enable. (2) In `.claude/claude-doctor.local.md`, set `enabled: false` — disables per-project. Per-project setting is preferred when you want the plugin on globally but off in a specific repo.

**False positives on fabrication-detector.** By default the Stop hook is log-only, so false positives never block your work — they just accumulate in the audit log. Process them through `/claude-doctor:triage`: phrases you mark **Ignore all** stop being flagged entirely; only phrases you explicitly choose to **Block all** will start enforcing with `exit 2`. Report patterns of systematic false positives as an issue so the shipped default phrase list can improve.

---

## Contributing

Issues and PRs welcome at [github.com/alenazaharovaux/claude-doctor](https://github.com/alenazaharovaux/claude-doctor). The most useful contributions for v0.2:

- Keyword list suggestions for additional languages
- False-positive reports from fabrication-detector with examples from your transcripts
- New detectors for patterns not yet covered (proposals via issue first)
- Test cases — `tests/test_completion_claims.py` currently covers 13 cases; more are welcome

---

## License

MIT — see [LICENSE](LICENSE).

---

## Credits

Author: Alena Zakharova ([github.com/alenazaharovaux](https://github.com/alenazaharovaux)).

Origin: project «Анализ Клода — апрель», April 2026 — a collection of concrete incidents where rule-following broke down mid-session, which led to the observation that CLAUDE.md rules activate post-hoc while hooks can activate in-moment.

Implementation co-authored by Claude Opus 4.6 with empirical verification at each step (see commit history).
