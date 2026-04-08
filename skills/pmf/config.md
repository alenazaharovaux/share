# PMF Skill — Configuration

This file is read by the PMF skill on every run. The first time you trigger the skill, it asks you a few questions and writes your answers here. You can edit this file by hand at any time.

Format: `key: value`. Keep one key per line. Lines starting with `#` are comments and ignored by the skill.

---

## Settings

```
language: en
projects_path: ~/pmf-projects
```

---

## Available values

**`language`** — what language the skill communicates in and which references it loads.

| Value | Effect |
|---|---|
| `en` | English. References loaded from `references/en/`. Skill talks to you in English. |
| `ru` | Russian. References loaded from `references/ru/`. Skill talks to you in Russian. |

**`projects_path`** — where the skill stores PMF projects. Each product gets its own subfolder named by slug.

Examples:
- `~/pmf-projects` (default — home folder)
- `~/Documents/PMF`
- `D:/Work/PMF` (Windows)
- `/Users/me/Projects/PMF` (macOS)

The folder is created automatically if it does not exist.

---

## Notes

- This file is **not** committed to your repo. It is a local config, lives next to the skill, and is read on every trigger.
- If the file is missing or a key is absent, the skill asks you about it on the next run and writes the answer here.
- To reset the config, delete this file. The skill will recreate it on the next run.
