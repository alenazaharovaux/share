# Triage Finding — Claude Code Skill

A skill for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that helps you quickly assess links, posts, articles, and videos you find — and decide what to do with them.

## What it does

You share a link, post, or screenshot, and the skill reads the content, explains what it is in plain language, maps it to your current projects, and recommends one of three actions: apply now, save for later, or skip. It handles articles, GitHub repos, and YouTube videos (with full transcript extraction and a multi-step fallback chain).

Before recommending anything, the skill fact-checks the finding by following links in the original post and verifying claims against the actual source. Posts often contain inaccuracies — wrong language, misidentified license, outdated numbers — and the skill flags any discrepancies so your decisions are based on verified information.

If the finding describes a tool or skill that you already have installed, the skill detects this by checking your skills index and tells you directly, so you don't waste time on duplicates.

The skill also has an **Ideas Review** mode that scans your saved ideas folder and tells you which ideas became relevant to your current work.

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

On first use, the skill asks 5 setup questions (you can skip any of them):

| Question | What it's for | Example |
|----------|--------------|---------|
| Language | What language to communicate in | English, Russian, Serbian |
| Projects folder | To match findings to your work | `~/Projects/` |
| Ideas folder | Where to save "for later" notes | `~/Projects/Ideas/` |
| Memory file | Your priorities/context file | `~/.claude/memory/MEMORY.md` |
| Skills index | Detects already-installed tools | `~/.claude/skills/skill-index.md` |

Settings are saved in `~/.claude/skills/triage-finding/config.md` and can be edited anytime.

## Usage examples

Just share something with Claude Code:

- `"Look what I found: https://github.com/some/cool-tool"`
- `"Triage this: [paste post text]"`
- `"Check this out: https://youtube.com/watch?v=..."`
- Share a screenshot
- `"Review my ideas"` — scans your ideas folder

## Key features

- **Fact-checking:** The skill follows links from posts and verifies claims against the actual source before making a recommendation, so inaccuracies from the original post do not carry through.
- **Installed skills detection:** If you configure a skills index, the skill checks whether the tool or plugin from a finding is already installed and avoids recommending duplicates.
- **YouTube fallback chain:** YouTube content is extracted through a multi-step process — Exa search for metadata, then `youtube-transcript-api` for the full transcript, then a web search fallback if both are unavailable. Large transcripts are processed by a background agent to keep the main conversation clean.
- **Prioritization:** When you share multiple findings at once, the skill processes project-related items first and provides a summary table for three or more findings.

## Credits

By [Alena Zakharova](https://human2aimain.onrender.com/ru/), [Cloud Research](https://cloud-research.onrender.com/) (MIT).

---

# Triage Finding — Скилл для Claude Code

Скилл для [Claude Code](https://docs.anthropic.com/en/docs/claude-code), который помогает быстро оценить найденные ссылки, посты, статьи и видео — и решить, что с ними делать.

## Что делает

Ты скидываешь ссылку, пост или скриншот, и скилл читает содержание, объясняет простым языком, что это такое, сопоставляет с твоими текущими проектами и рекомендует одно из трёх действий: применить сейчас, сохранить на будущее или пропустить. Скилл работает со статьями, GitHub-репозиториями и YouTube-видео (с извлечением полного транскрипта и многошаговой цепочкой fallback-ов).

Перед тем как давать рекомендацию, скилл проверяет факты из находки — переходит по ссылкам из оригинального поста и сверяет утверждения с реальным источником. В постах часто встречаются неточности: неверный язык программирования, перепутанная лицензия, устаревшие цифры. Скилл отмечает расхождения, чтобы решения принимались на основе проверенной информации.

Если находка описывает инструмент или скилл, который у тебя уже установлен, скилл обнаружит это через проверку индекса скиллов и сообщит напрямую, чтобы не тратить время на дубликаты.

Есть режим **Ревизия идей** — просматривает папку сохранённых идей и говорит, что из сохранённого стало актуальным для текущих проектов.

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

При первом использовании скилл задаст 5 вопросов (любой можно пропустить):

| Вопрос | Для чего | Пример |
|--------|---------|--------|
| Язык | На каком языке общаться | Русский, English, Srpski |
| Папка проектов | Чтобы сопоставлять находки с работой | `~/Projects/` |
| Папка идей | Куда складывать заметки «на будущее» | `~/Projects/Ideas/` |
| Файл памяти | Файл с приоритетами и контекстом | `~/.claude/memory/MEMORY.md` |
| Индекс скиллов | Обнаружение уже установленных инструментов | `~/.claude/skills/skill-index.md` |

Настройки сохраняются в `~/.claude/skills/triage-finding/config.md` и доступны для редактирования в любой момент.

## Примеры использования

Просто поделись чем-то с Claude Code:

- `"Смотри, что я нашла: https://github.com/some/cool-tool"`
- `"Разбери находку: [текст поста]"`
- `"Что с этим делать: https://youtube.com/watch?v=..."`
- Скинь скриншот
- `"Посмотри в идеях"` — ревизия папки идей

## Ключевые возможности

- **Проверка фактов:** скилл переходит по ссылкам из постов и сверяет утверждения с реальным источником, прежде чем давать рекомендацию, чтобы неточности из оригинального поста не влияли на решения.
- **Обнаружение установленных скиллов:** если настроен индекс скиллов, скилл проверяет, не установлен ли уже инструмент или плагин из находки, и не рекомендует дубликаты.
- **Цепочка fallback-ов для YouTube:** содержание YouTube-видео извлекается в несколько шагов — сначала поиск через Exa для метаданных, затем `youtube-transcript-api` для полного транскрипта, а если оба способа недоступны, поиск в вебе. Большие транскрипты обрабатываются фоновым агентом, чтобы не забивать основной контекст.
- **Приоритизация:** когда пользователь скидывает несколько находок одновременно, скилл обрабатывает сначала те, что связаны с активными проектами, и выдаёт сводную таблицу при трёх и более находках.

## Благодарности

[Алена Захарова](https://human2aimain.onrender.com/ru/), [Cloud Research](https://cloud-research.onrender.com/) (MIT).
