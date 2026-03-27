# newsroom-style

Enforce AP Style and newsroom conventions so your journalism clears editorial standards the first time. Works on raw notes, rough drafts, or finished copy — attribution, numbers, dates, ledes, and headlines all follow the Associated Press Stylebook.

Professional standards build reader trust. AP Style is the industry baseline for credible journalism worldwide.

## Installation

**macOS / Linux:**
```bash
cp -r newsroom-style ~/.claude/skills/newsroom-style
```

**Windows:**
```powershell
Copy-Item -Recurse newsroom-style $env:USERPROFILE\.claude\skills\newsroom-style
```

No configuration needed — works out of the box.

## Usage

Say any of these to Claude Code:

- "write a news article about..."
- "edit this draft in AP Style"
- "convert these notes into publishable copy"
- "check this article for style errors"
- "format this for publication"
- "write a headline for this story"

## What's inside

**Numbers** — Spell out one through nine, numerals for 10 and above. Always numerals for ages, percentages, addresses, and money. Never start a sentence with a numeral.

**Titles and names** — Capitalize formal titles before names ("Mayor Jane Smith said"), lowercase after ("Jane Smith, the mayor, said"). No courtesy titles on second reference — just the last name.

**Attribution** — "said," placed after the quote at the first natural pause. Not "stated," "remarked," or "noted." The skill enforces this consistently.

**Dates and times** — Abbreviate months when paired with a date (Sept. 15), spell out when standing alone (September 2025). Use "9 a.m." not "9:00 a.m." Use "noon" and "midnight," not "12 p.m."

**Common word choices** — "more than" instead of "over" for quantities, "fewer" instead of "less" for countable items, "because" instead of "due to the fact that."

**Ledes (inverted pyramid)** — Most important information first, 35 words or fewer. The skill flags ledes that bury the news or run long.

**Headlines** — Sentence case, no period, present tense for past events ("Council approves budget"), infinitive for future ("Mayor to announce plan").

**Pre-publish checklist** — Nine-point verification before you send: names, titles, numbers, attribution, dates, paragraph length, lede word count, no editorializing, named sources.

## Example transformations

**Attribution and numbers:**

Before:
> Yesterday the Mayor said that he was "very excited" about the new $5,000,000 project that will create over 100 jobs.

After:
> Mayor John Smith said Tuesday he was "very excited" about the $5 million project, which will create more than 100 jobs.

---

**Date and time formatting:**

Before:
> The meeting started at 9:00 AM on Monday, October 14th, 2024.

After:
> The meeting began at 9 a.m. Monday, Oct. 14, 2024.

---

**Lede — cut the throat-clearing (57 words → 18):**

Before:
> The city council, which has been debating the issue for several months and heard from dozens of residents at multiple public meetings, voted Tuesday night to approve a controversial new zoning ordinance that would allow high-rise buildings in the downtown area.

After:
> The city council approved a zoning ordinance Tuesday that allows high-rise buildings downtown, ending months of debate.

## Works well with

- [ai-writing-detox](../ai-writing-detox/) — strips AI staccato rhythm, dramatic fragments, and tabloid patterns before you apply AP Style. Run it first.

## Credits

Based on [newsroom-style](https://github.com/jamditis/claude-skills-journalism) by [Joe Amditis](https://github.com/jamditis) — MIT license.

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

# newsroom-style (RU)

Приводит тексты к стандартам AP Style и редакционным нормам, чтобы материал проходил редактора с первого раза. Работает с сырыми заметками, черновиками и готовыми текстами — атрибуция, числа, даты, лиды и заголовки по Associated Press Stylebook.

Конфигурация не нужна — работает сразу.

## Установка

```bash
cp -r newsroom-style ~/.claude/skills/newsroom-style
```

## Использование

- «напиши новостную статью о...»
- «отредактируй по AP Style»
- «переведи заметки в публикуемый текст»
- «проверь стиль статьи»
- «напиши заголовок к этому материалу»

## Что внутри

**Числа** — от одного до девяти словами, от 10 и выше цифрами. Всегда цифры для возраста, процентов, адресов и денег.

**Атрибуция** — только "said", после цитаты. Не "stated," "remarked," "noted."

**Лиды** — главное вперёд, не более 35 слов. Скилл помечает лиды, которые прячут новость.

**Чеклист** — 9 пунктов проверки перед публикацией.

## Примеры трансформации

До:
> Yesterday the Mayor said that he was "very excited" about the new $5,000,000 project that will create over 100 jobs.

После:
> Mayor John Smith said Tuesday he was "very excited" about the $5 million project, which will create more than 100 jobs.

## Хорошо работает вместе с

- [ai-writing-detox](../ai-writing-detox/) — убирает ИИ-паттерны до применения AP Style. Запускайте первым.

## Авторство

На основе [newsroom-style](https://github.com/jamditis/claude-skills-journalism) от [Joe Amditis](https://github.com/jamditis) — лицензия MIT.

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
