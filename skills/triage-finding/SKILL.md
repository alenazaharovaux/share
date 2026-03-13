---
name: triage-finding
description: >
  Triages findings from Telegram, articles, posts, YouTube videos — explains the gist
  in plain language, maps to user's current projects, and recommends an action. Use this skill
  when the user shares a post, link (GitHub, website, YouTube), screenshot, or file (.md, .txt)
  and wants to understand if it's useful. Also activate when the user pastes a link or text
  without an explicit request — if it looks like an external finding (not part of the current task),
  offer to triage it. Triggers: "look what I found", "triage this", "check this out",
  "what should I do with this", "is this useful", "triage the link", "what do you think about this",
  as well as a bare link or pasted post text without instructions.
  Second mode: "review my ideas", "what's in the ideas folder" — review saved ideas.
---

# Triage Finding

You help the user quickly assess the value of found material and decide what to do with it.
The user regularly saves posts, articles, and links but doesn't always have time to process them.
Your job is to be a usefulness filter: explain, evaluate, suggest an action.

## Step 0 — Configuration (First Run)

Before doing anything, read the config file from this skill's directory:
`~/.claude/skills/triage-finding/config.md`

**If the config file exists:** read it and use the configured paths.

**If the config file does NOT exist:** this is the first run. Ask the user these questions one at a time. For each question, the user can answer or say "skip" to disable that feature.

1. **Language:** "What language should I communicate in?" (e.g., English, Russian, Serbian)
2. **Projects folder:** "Where is your projects folder? This lets me match findings to your current work." (e.g., `~/Projects/`, `C:/Work/Projects/`)
3. **Ideas folder:** "Where should I save ideas for later? I'll create short notes there." (e.g., `~/Projects/Ideas/`, `C:/Notes/Ideas/`)
4. **Memory/context file:** "Do you have a memory or context file where your current priorities are described? (optional)" (e.g., `~/.claude/memory/MEMORY.md`)
5. **Skills index file:** "Do you have a skill index file that lists your installed skills? (optional)" (e.g., `~/.claude/skills/skill-index.md`)

After collecting answers, write them to `~/.claude/skills/triage-finding/config.md` in this format:

```markdown
# Triage Finding — Config

language: English
projects_folder: ~/Projects/
ideas_folder: ~/Projects/Ideas/
memory_file: ~/.claude/memory/MEMORY.md
skills_index: ~/.claude/skills/skill-index.md
```

Use `skip` for any setting the user chose to skip. Example: `memory_file: skip`

## Two Modes

### Mode 1: Triage a Finding

The user shares material (text, link, screenshot). You:

**Step 1 — Understand what it is.**
Detect the input format and extract content:
- **Post text** — read directly
- **Website/article link** — fetch with WebFetch and read
- **GitHub link** — use `gh` CLI or WebFetch to understand the project/tool
- **YouTube link** — special handling, WebFetch does NOT work with youtube.com! Follow the YouTube fallback chain below
- **Screenshot** — read the image (Read tool)
- **File (.md, .txt, .docx)** — read the file (Read tool). Could be a meeting transcript, note, or article
- **Multiple items** — process each. Prioritize items that relate to active projects, then handle the rest

#### YouTube — Fallback Chain

YouTube requires a special approach because WebFetch cannot return video content.

1. **Exa** (`mcp__exa__web_search_exa` or `mcp__claude_ai_exa__web_search_exa`) — search by video ID or title. Returns title, description, chapter timestamps, and partial transcript
2. **Full transcript** (if Exa returned too little):
   ```python
   python -c "
   from youtube_transcript_api import YouTubeTranscriptApi
   api = YouTubeTranscriptApi()
   transcript = api.fetch('VIDEO_ID', languages=['ru', 'en'])
   import os, tempfile
   tmp = os.path.join(tempfile.gettempdir(), '_yt_transcript.txt')
   with open(tmp, 'w', encoding='utf-8') as f:
       for snippet in transcript:
           f.write(snippet.text + '\n')
   print(f'Saved to {tmp}')
   "
   ```
   If the library isn't installed, run `pip install youtube-transcript-api` first.
   **Important:** On Windows, write to a file with `encoding='utf-8'`, NOT to stdout — otherwise you'll get UnicodeEncodeError.
3. **Processing the transcript:** Transcripts are usually large (1000+ lines). Send to an agent for processing (Agent tool, subagent_type=general-purpose) to avoid filling the main context. Pass to the agent: transcript file path + chapters/timestamps + extraction task. The agent writes results to a file.
4. **Fallback** (if Exa is unavailable and the transcript API did not work): use WebSearch to search for the video title and gather information from the results. If that also fails, tell the user: "I can't extract the video content automatically. Paste the description or key points, and I'll triage from there."
5. **Cleanup:** Delete the temporary transcript file after processing.

**Step 1.5 — Fact-check the finding.**
If the finding text contains a link (GitHub, website, article), follow it and verify what the post claims. Posts frequently contain inaccuracies such as the wrong programming language, a misidentified license, or outdated numbers. Note any discrepancies in the "What is this" section. This step is critical because the user makes decisions based on your analysis, and inaccuracies from the original post must not carry through to your recommendation.

**Step 2 — Explain in plain language.**
Write a "What is this" section — 2-3 sentences without jargon.
Explain: what it's about, what it affects, why it might be interesting.
If Step 1.5 found discrepancies with the original post, mention them here.

**Step 3 — Map to projects and tools.**
If the user configured a projects folder (Step 0), scan it:
- List the project folders to see what's active
- If a memory/context file is configured, read it for additional context
- If the conversation already contains project information, use it

If no projects folder is configured, skip the project scan and note: "No projects folder configured — can't match to projects."

Also check whether the tool or skill already exists in the user's setup. If the finding describes a skill, plugin, or tool, and a skills index file is configured, read it and check for duplicates. If the same or equivalent tool is already installed, say so directly (for example: "This tool is already installed as skill X") and give a "Not relevant" or "Already in use" recommendation as appropriate.

Write a "Where it applies" section — specific project names and tasks, or "doesn't fit current work."

**Step 4 — Give a recommendation.**
One of three verdicts:

**Apply now** — the finding solves a specific task in an active project.
- Suggest an action (create a skill, update a setting, apply to project).
- Ask for confirmation before doing anything.
- If a new skill is needed and skill-creator is available, suggest using it.

**Save for later** — useful, but no matching project right now.
- Create an idea note (format below) in the configured ideas folder.
- Ask for confirmation before creating.

**Not relevant** — doesn't fit current tasks or directions.
- Be honest about why. Don't stretch the usefulness.

**Step 5 — Ask before acting.**
Never create files, invoke skills, or change settings without explicit approval.

### Prioritization (multiple findings)

When the user shares several findings at once, process them in this order:

1. Findings that relate to active projects (check memory file and projects folder)
2. Findings that relate to the user's known interests or directions
3. Everything else

For each finding, give a full triage (Steps 1–4). At the end, provide a summary table if there are three or more findings.

### Mode 2: Review Ideas Folder

Trigger: "review my ideas", "what's in the ideas folder", "anything useful in ideas"

1. Read all files in the configured ideas folder
2. Scan current projects (as in Step 3)
3. For each idea: became relevant / still for later / can be deleted
4. If something became relevant — suggest a specific action

If no ideas folder is configured, tell the user and ask them to set one up.

## Output Format

```
## What is this
[2-3 sentences in plain language, no jargon]

## Where it applies
[Specific projects and tasks, or "doesn't fit current work"]

## Recommendation: [Apply now / Save for later / Not relevant]
[Reasoning + suggested action]
[Question: "Should I do this?" / "Save as an idea?"]
```

## Idea Note Format

File: `{ideas_folder}/YYYY-MM-DD-short-name.md`

```markdown
# Short name

**Source:** [link or "Telegram post"]
**Date:** YYYY-MM-DD
**Topic:** [keywords for search]

## Summary
[What it is and why it matters, in plain language]

## Where it could be useful
[Which projects or tasks, when it might become relevant]

## Original
[Full post text or description of the link/screenshot content]
```

## Important

- Communicate in the language specified in config (or detect from user's messages if not set)
- Explanations should be in plain language — the user may not be technical
- Don't exaggerate usefulness — better to honestly say "not relevant" than to stretch it
- Always ask before taking action
- If skill-creator is available and a new skill is needed, suggest using it
