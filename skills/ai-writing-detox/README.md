# ai-writing-detox

A Claude Code skill that catches the patterns readers associate with AI-generated text — and kills them before publication. Banned words, hollow phrases, corporate jargon, fake enthusiasm, and the choppy dramatic fragments that are the single biggest tell of machine writing. If your readers think "AI wrote this," you have already lost their trust.

No configuration needed — works out of the box.

## Installation

**macOS / Linux:**
```bash
cp -r ai-writing-detox ~/.claude/skills/ai-writing-detox
```

**Windows:**
```powershell
Copy-Item -Recurse ai-writing-detox $env:USERPROFILE\.claude\skills\ai-writing-detox
```

## Usage

Say any of these to Claude Code:

- "write an article about..."
- "edit this text to sound human"
- "check this draft for AI patterns"
- "clean up this copy before publishing"
- "review this press release for AI tells"

## What's inside

### Banned words
A table of 16 words that scream "AI wrote this" — each with an explanation and a plain alternative:

| Word | Why it's bad | Use instead |
|------|-------------|-------------|
| delve | AI signature word | explore, examine, look at |
| leverage | Jargon | use |
| robust | Meaningless filler | strong, reliable |
| seamless | Almost always false | smooth, easy |
| comprehensive | Rarely necessary | full, complete |

Full list inside the skill — 16 words total.

### Banned phrases
Four categories: throat-clearing openers ("It's important to note that..."), empty hedges ("At the end of the day..."), AI enthusiasm ("This is a game-changer!"), and corporate buzzwords ("Moving forward..."). The skill deletes them entirely.

### Banned rhythm patterns — the #1 AI tell
Choppy dramatic fragments are the most recognizable machine-writing pattern. Readers spot it instantly, even if they cannot name it:

**AI staccato:**
> Police estimated fifty victims. The court proved two. Not a series.

**Human writing:**
> Police estimated fifty victims, but the court proved only two.

The skill catches three variants: contrast fragments, punch-line fragments, and staccato lists.

### Substitution table
14 quick swaps: "utilize" → "use", "in order to" → "to", "due to the fact that" → "because", "has the ability to" → "can", and more.

### Self-check before publishing
Seven-point scan: search your text for delve, landscape, crucial, robust, leverage, comprehensive, and opening "So,". Found any? Your writing needs another pass.

## Before and after

**AI slop:**
> The city council meeting was a comprehensive and transformative discussion that fundamentally addressed key issues affecting residents in a meaningful way.

**Human writing:**
> The city council voted 5-2 Tuesday to raise property taxes by 3 percent.

---

**AI slop:**
> In the rich tapestry of American journalism, few stories are as compelling as the one about to unfold. This isn't just a profile — it's a journey into the heart of what makes local news truly matter.

**Human writing:**
> Maria Rodriguez has published a newspaper for 47 years. She has never missed an issue.

## Works well with

- [newsroom-style](../newsroom-style/) — after stripping AI patterns, apply AP Style and editorial conventions to make the text publication-ready

## Credits

Based on [ai-writing-detox](https://github.com/jamditis/claude-skills-journalism) by [Joe Amditis](https://github.com/jamditis) — MIT license.

---

# ai-writing-detox (RU)

Скилл для Claude Code, который ловит паттерны, по которым читатели опознают ИИ-текст, — и убивает их до публикации. Запрещённые слова, пустые фразы, корпоративный жаргон, фальшивый энтузиазм и рубленые драматические фрагменты, которые являются главным маркером машинного текста. Если читатель подумал «это написал ИИ» — доверие уже потеряно.

Конфигурация не нужна — работает сразу.

## Установка

```bash
cp -r ai-writing-detox ~/.claude/skills/ai-writing-detox
```

## Использование

- «напиши статью про...»
- «проверь текст на следы ИИ»
- «почисти черновик перед публикацией»
- «убери ИИ-паттерны из этого текста»
- «отредактируй пресс-релиз — убери машинные обороты»

## Что внутри

**Запрещённые слова** — 16 слов-маркеров (delve, leverage, robust, seamless...) с альтернативами.

**Запрещённые фразы** — четыре категории: вводные-пустышки, пустые хеджи, ИИ-восторг, корпоративные штампы.

**Запрещённые ритмические паттерны** — главный маркер ИИ: рубленые драматические фрагменты. «Полиция насчитала пятьдесят жертв. Суд доказал два.» → «Полиция оценивала жертв в пятьдесят, но доказать удалось лишь два случая.»

**Таблица замен** — 14 быстрых подстановок: utilize → use, in order to → to, due to the fact that → because.

**Чеклист перед публикацией** — 7 точек проверки.

## До и после

**ИИ-слоп:**
> The city council meeting was a comprehensive and transformative discussion that fundamentally addressed key issues affecting residents in a meaningful way.

**Человеческий текст:**
> The city council voted 5-2 Tuesday to raise property taxes by 3 percent.

## Хорошо работает вместе с

- [newsroom-style](../newsroom-style/) — после очистки от ИИ-паттернов применяет AP Style и редакционные стандарты

## Авторство

На основе [ai-writing-detox](https://github.com/jamditis/claude-skills-journalism) от [Joe Amditis](https://github.com/jamditis) — лицензия MIT.
