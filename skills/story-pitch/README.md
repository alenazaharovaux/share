# story-pitch

Good stories die in bad pitches. This Claude Code skill gives you five ready-to-use pitch templates — daily news, feature, investigation, op-ed, and freelance query letter — along with angle development tools and the four-question "so what" test that separates pitchable ideas from vague topics.

No configuration needed.

## Installation

**macOS / Linux:**
```bash
cp -r story-pitch ~/.claude/skills/story-pitch
```

**Windows:**
```powershell
Copy-Item -Recurse story-pitch $env:USERPROFILE\.claude\skills\story-pitch
```

## Usage

Say any of these to Claude Code:

- "help me pitch this story"
- "write a query letter for [publication]"
- "develop an angle for this topic"
- "prepare a pitch for my editor"
- "I need to pitch an investigation"

## What's inside

### Five pitch templates

| Template | When to use |
|----------|-------------|
| **Daily news** | Quick-turn story for an assignment editor, filing same day |
| **Feature** | Longer-form pitch with narrative structure, characters, scenes |
| **Investigation** | Accountability journalism requiring resources, FOIA, legal review |
| **Op-ed** | Opinion piece pitched to an external publication's opinion editor |
| **Freelance query** | Cold pitch to an editor at a publication you don't work for |

### The "so what" test

Before writing a single line of your pitch, answer four questions:

1. **Why this story?** — What is its significance?
2. **Why now?** — What makes it timely?
3. **Why you?** — What access, expertise, or angle do you bring?
4. **Why this outlet?** — Why does their audience need this?

If you cannot answer all four, you are not ready to pitch.

### Angle vs. Topic

| Topic | Angle |
|-------|-------|
| Homelessness | The family on the housing waitlist for 3 years |
| Climate change | The town already moving because of rising seas |
| Healthcare costs | The insulin price that tripled while the patent was extended |

Topic is what you cover. Angle is how you cover it. Every pitch needs both.

### Common pitch mistakes

The skill identifies the four most common failures — information dump, missing news hook, vague access claim, no-stakes pitch — each with a broken and a fixed version.

## Example

A daily news pitch using the built-in template:

```
Slug: Council-Budget-Vote
Pitch: City council votes tonight on controversial police budget increase.
Why now: Final vote after months of debate, protests expected.
Sources: Council president, protest organizers, police union rep.
Timeline: File by 10pm for morning.
Format: 600 words + photos from hearing.
```

## Works well with

- [ai-writing-detox](../ai-writing-detox/) — strips AI-flavored language from the pitch text itself
- [newsroom-style](../newsroom-style/) — applies editorial standards to your copy after the pitch is accepted

## Credits

Based on [story-pitch](https://github.com/jamditis/claude-skills-journalism) by [Joe Amditis](https://github.com/jamditis) — MIT license.

---

# story-pitch (RU)

Хорошие истории гибнут в плохих питчах. Этот скилл для Claude Code даёт пять шаблонов питчей — ежедневные новости, фичер, расследование, колонка и freelance query letter — плюс инструменты для развития угла подачи и тест из четырёх вопросов «ну и что?».

Конфигурация не нужна — работает сразу.

## Установка

```bash
cp -r story-pitch ~/.claude/skills/story-pitch
```

## Использование

- «помоги запитчить историю»
- «напиши query letter для [издания]»
- «развей угол подачи для этой темы»
- «подготовь питч для редактора»

## Что внутри

**5 шаблонов:** ежедневная новость, фичер, расследование, колонка, фриланс-запрос.

**Тест «ну и что?»** — четыре вопроса: почему эта история, почему сейчас, почему вы, почему это издание. Нет ответа хотя бы на один — не готовы питчить.

**Угол vs. тема** — тема (бездомность) vs. угол (семья, которая три года ждёт жильё). Питч нуждается в обоих.

**Типичные ошибки** — четыре провала с плохим и исправленным примером.

## Пример

```
Slug: Council-Budget-Vote
Pitch: Городской совет голосует сегодня за увеличение полицейского бюджета.
Why now: Финальное голосование после месяцев дебатов, ожидаются протесты.
Sources: Председатель совета, организаторы протеста, полицейский профсоюз.
Timeline: Сдать до 22:00 для утреннего выпуска.
Format: 600 слов + фото со слушания.
```

## Хорошо работает вместе с

- [ai-writing-detox](../ai-writing-detox/) — убирает ИИ-маркеры из текста питча
- [newsroom-style](../newsroom-style/) — применяет редакционный стиль к материалу после принятия питча

## Авторство

На основе [story-pitch](https://github.com/jamditis/claude-skills-journalism) от [Joe Amditis](https://github.com/jamditis) — лицензия MIT.
