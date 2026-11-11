---
name: clear-text
description: >
  Check and fix any text written for people so a first-time reader understands it: articles,
  reports, interview findings and synthesis, websites, emails, posts, skill files and instructions.
  A text is done when no sentence and no paragraph leaves the reader asking "what is this about,
  who is this, why, what does this word mean, how do we know". Also has a "comments" mode: a
  comment layer is added on top of a well-designed HTML page, the user types or dictates comments
  in the browser, and the skill works through them and adds new rules to itself. Triggers:
  "clear text", "check this text", "make this clearer", "proofread for clarity", "this is hard
  to read", "I want to comment on this text", "comment page", "go through my comments",
  "I've commented", "make an HTML page", "make it HTML". Build every HTML page for the user as a
  page with a comment layer.
---

# Clear text

The skill makes a text clear to someone who reads it for the first time and was not part of our conversation. The rules come from the skill author's comments on real texts (Alena Zakharova, originally in Russian). Every rule in `references/questions.md` comes from a specific comment, quoted there.

## Skill files

- `references/questions.md` — the reader's questions. Every sentence and paragraph is checked against them. This is the main file of the skill.
- `references/examples.md` — before → after pairs from real texts.
- `references/review-*.md` — reviews of the user's comments. They appear as you use the comments mode.
- `scripts/check_text.py` — mechanical search for suspicious spots.
- `scripts/add_comments_to_html.py` — adds a comment layer to a finished HTML page and keeps its design. The main way to get a comment page.
- `scripts/make_comment_page.py` — a plain comment page from a .md file, without design. Only for long .md documents, when the user asks for it.
- `scripts/read_comments.py` — turns a saved comments file into a readable list.

## Mode "check a text"

### Step 1. The task of the text and the reader

Before editing, write down three things for yourself:
1. The task of the text in one phrase. For example: "Walk through the interview-analysis skill step by step and explain why each step works the way it does".
2. The reader: who they are and what they already know. For example: "a course participant, a researcher, sees the skill for the first time, did not see our conversation".
3. Decisions made in the conversation that the text must reflect. For example: "we are adding a review page to the skill".

Check every section of the text against the task. Rewrite or remove a section that does not serve the task.

### Step 2. Show the structure first

If the text describes a system, a process, a document or a skill, show its structure at the start: what parts it has, what it reads, where it writes the result. Use a table, a file tree or a diagram. Explain every term the reader sees for the first time when it first appears.

### Step 3. Sentence by sentence

Read each sentence on its own, as if the neighbouring ones were not there, and ask the questions from `references/questions.md`. If a question comes up, rewrite the sentence so the answer is inside it. The main questions:
- Who or what is this about? Replace every "this, that, such, the other, the second, it, its" with the thing it points to.
- What does this word mean? After a long gap, name your own term in full. Name a part of a document exactly as the document names it.
- How do we know? A reference to a line or a source comes with the quote. A claim about a system comes only after checking the system's files.
- Where is it and where does it go? Verbs like "writes, saves, marks, puts" always come with a place.
- Why? A rule or a ban comes with its reason, shown through what happens to the result without it.

If two sentences depend on each other and the first makes no sense without the second, merge them with a colon or a subordinate clause. Delete announcing phrases like "for a simple reason", "here is an example", "this step is needed because" and write the thought itself.

### Step 4. Paragraph by paragraph

Three checks for each paragraph:
1. Could you make a slide from it? If a paragraph lists more than three rules in a row, turn it into a list or a table with an example for each item.
2. Is there an example? Every rule, type or category gets an example from one running case that goes through the whole text. If there is no such case, pick one and keep it to the end.
3. Is it clear why the paragraph is here? Remove a paragraph that does not serve the task of the text.

### Step 5. Facts

Check every number, quote, name and every claim like "the skill does X" against a file or a source in this session. A quote goes with the line of the source. If the text refers to lines of a document the reader cannot open, attach the document.

### Step 6. The script

```
python -I scripts/check_text.py <file.md> [<report.md>]
```

The script finds suspicious spots: "not X but Y" contrasts, filler phrases, sentences that start with a pointing word, short sentences that may not make sense on their own, long sentences, line numbers without a quote, abbreviations without an explanation. Check every finding by eye: the script looks for signs, you make the decision. The report goes to a file; the console shows only the number of findings.

### Step 7. Hand-off

Read the whole text one last time as the reader from step 1. Check it against the task and the decisions from the conversation. In your report to the user, list what you changed and why, and offer a comment page if the text is long.

## Mode "comments"

Use it when the user wants to type or dictate remarks on a text.

The mode also turns on when the user asks for HTML: "make an HTML page", "make it HTML", "put it in HTML". Build every page they ask for as a page with a comment layer.

A page for the user always has a proper design: cards, columns, labels, lists, spacing. The skill author called bare numbered paragraphs one after another "a wall of text" and "absolutely unreadable". The comment layer goes on top of the design and changes nothing in it.

1. First build a normal designed HTML page: a self-contained file, `meta charset`, system fonts, phone width without horizontal scrolling. Put it in the user's Downloads folder: `~/Downloads/<name>.html`.
2. Add the comment layer:
   ```
   python -I scripts/add_comments_to_html.py <page.html>
   ```
   The result goes to `~/Downloads/comments-<name>-<date-time>.html`. Every heading, paragraph and list item inside `<main>` can be commented: select a phrase, or hover and press "+ comment". A block with a comment gets an outline and a counter. The "Comments: N" and "Save comments" buttons sit at the bottom right. Comments are kept in the browser; "Save comments" downloads a `.json` file with the same name.
3. Check the page in a browser yourself before showing it. Take a screenshot and look at the design: is the page readable, do the buttons cover any text. Then check a comment: selection, saving, reload. If you drive Chrome through an extension that cannot open `file://`, start a temporary local server on a copy of the page in your session's working folder, and stop it by its process ID afterwards. If you have no browser tool, skip this step and say so.
4. Open the page for the user, give them the path and wait for "done".
5. Find the comments file yourself: `comments-<name>-<date-time>.json`, the name matches the page. The browser saves it where all downloads go. Look in this order: Downloads (`~/Downloads`), Desktop (`~/Desktop`), Documents (`~/Documents`), OneDrive folders in the home folder, then the whole home folder. If there are several files, take the newest. Ask the user for the path only if the file is nowhere to be found. Read the comments:
   ```
   python -I scripts/read_comments.py <file.json> <list.md>
   ```
   Open `<list.md>` with your file-reading tool: the Windows console can garble non-Latin text.
6. Go through every comment: the fragment, what the user said, what question the reader had, how to fix it. Group them by the kinds of questions in `references/questions.md`. Write the review to `references/review-<YYYY-MM>-<topic>.md`.
7. Fix the original designed page according to all comments.
8. Add a new kind of question that is not yet in `questions.md`, with the user's quote. Add a good before → after pair to `examples.md`.
9. Add the comment layer to the fixed page for the next round and offer it to the user.

## Do not

- Chop a connected thought into short sentences that make no sense without their neighbours.
- Refer to things the reader has not seen: "the second question", "this log", "our handbook" without an explanation.
- Refer to a line or a source without a quote.
- Write anything about a system that you have not checked against its files.
- Call the check step "rewrite it clearly": the step is called "clarity check".
