# Triage Finding — Claude Code Skill

A skill for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that helps you quickly assess links, posts, articles, and videos you find — and decide what to do with them.

## What it does

You share a link, post, or screenshot. The skill:

1. **Reads and understands** the content (articles, GitHub repos, YouTube videos with transcript extraction)
2. **Explains** what it is in plain language
3. **Maps** the finding to your current projects
4. **Recommends** an action: apply now, save for later, or skip

It also has an **Ideas Review** mode — scans your saved ideas folder and tells you what became relevant.

## Installation

Copy the `triage-finding` folder to your Claude Code skills directory:

```bash
# macOS/Linux
cp -r triage-finding ~/.claude/skills/triage-finding

# Windows
xcopy triage-finding %USERPROFILE%\.claude\skills\triage-finding /E /I
```

### Optional: Install skill-creator

If you also install the `skill-creator` skill (included in this repo), triage-finding can suggest creating new skills when a finding inspires one.

```bash
cp -r skill-creator ~/.claude/skills/skill-creator
```

## First run

On first use, the skill asks 4 setup questions. You can skip any of them:

| Question | What it's for | Example |
|----------|--------------|---------|
| Language | What language to communicate in | English, Russian, Serbian |
| Projects folder | To match findings to your work | `~/Projects/` |
| Ideas folder | Where to save "for later" notes | `~/Projects/Ideas/` |
| Memory file | Your priorities/context file | `~/.claude/memory/MEMORY.md` |

Settings are saved in `~/.claude/skills/triage-finding/config.md` — edit anytime.

## Usage examples

Just share something with Claude Code:

- `"Look what I found: https://github.com/some/cool-tool"`
- `"Triage this: [paste post text]"`
- `"Check this out: https://youtube.com/watch?v=..."`
- Share a screenshot
- `"Review my ideas"` — scans your ideas folder

## YouTube support

The skill extracts full transcripts from YouTube videos using the `youtube-transcript-api` Python library. If the library isn't installed, the skill will install it automatically. Large transcripts are processed by a background agent to keep the main conversation clean.

## Credits

This skill uses `skill-creator` from the [superpowers](https://github.com/anthropics/claude-code-plugins) plugin by Jesse Vincent (MIT License).

---

# Triage Finding — Скилл для Claude Code

Скилл для [Claude Code](https://docs.anthropic.com/en/docs/claude-code), который помогает быстро оценить найденные ссылки, посты, статьи и видео — и решить, что с ними делать.

## Что делает

Ты скидываешь ссылку, пост или скриншот. Скилл:

1. **Читает и понимает** содержание (статьи, GitHub-репозитории, YouTube-видео с извлечением транскрипта)
2. **Объясняет** простым языком, что это
3. **Сопоставляет** находку с твоими текущими проектами
4. **Рекомендует** действие: применить сейчас, сохранить на будущее или пропустить

Есть режим **Ревизия идей** — просматривает папку сохранённых идей и говорит, что стало актуальным.

## Установка

Скопируй папку `triage-finding` в директорию скиллов Claude Code:

```bash
# macOS/Linux
cp -r triage-finding ~/.claude/skills/triage-finding

# Windows
xcopy triage-finding %USERPROFILE%\.claude\skills\triage-finding /E /I
```

### Опционально: установи skill-creator

Если также установить скилл `skill-creator` (есть в этом репозитории), triage-finding сможет предлагать создание новых скиллов, когда находка вдохновляет на это.

```bash
cp -r skill-creator ~/.claude/skills/skill-creator
```

## Первый запуск

При первом использовании скилл задаст 4 вопроса. Любой можно пропустить:

| Вопрос | Для чего | Пример |
|--------|---------|--------|
| Язык | На каком языке общаться | Русский, English, Srpski |
| Папка проектов | Чтобы сопоставлять находки с работой | `~/Projects/` |
| Папка идей | Куда складывать заметки «на будущее» | `~/Projects/Ideas/` |
| Файл памяти | Файл с приоритетами и контекстом | `~/.claude/memory/MEMORY.md` |

Настройки сохраняются в `~/.claude/skills/triage-finding/config.md` — можно отредактировать в любой момент.

## Примеры использования

Просто поделись чем-то с Claude Code:

- `"Смотри, что я нашла: https://github.com/some/cool-tool"`
- `"Разбери находку: [текст поста]"`
- `"Что с этим делать: https://youtube.com/watch?v=..."`
- Скинь скриншот
- `"Посмотри в идеях"` — ревизия папки идей

## Поддержка YouTube

Скилл извлекает полные транскрипты из YouTube-видео с помощью Python-библиотеки `youtube-transcript-api`. Если библиотека не установлена, скилл установит её автоматически. Большие транскрипты обрабатываются фоновым агентом, чтобы не забивать основной контекст.

## Благодарности

Скилл использует `skill-creator` из плагина [superpowers](https://github.com/anthropics/claude-code-plugins) от Jesse Vincent (лицензия MIT).
