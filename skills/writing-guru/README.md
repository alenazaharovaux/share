# Writing Guru

Choose a narrative strategy before you write. This skill turns "I need to write an article about X" into a structured narrative map with named strategies, block-by-block structure, and sample leads -- so you start writing with a plan, not a blank page.

Built on the **Periodic Table of Narratives** -- a framework of 25 base narratives, 7 groups, and 204 named compounds (narrative combinations). The skill uses three lenses (goal, speech act, temporality) to systematically narrow down which narratives fit your task, then presents 2-5 strategy options with sample leads and contextual recommendations.

## What makes it different from "just asking Claude to help write"

Without this skill, Claude picks a vague approach based on intuition. With Writing Guru:

| Without skill | With skill |
|--------------|-----------|
| Ad-hoc names: "detective angle", "personal touch" | Taxonomy-based: "Analytical reportage (An + Sv)" with named compounds |
| No structure beyond "intro, body, conclusion" | Block-by-block map: Lead = Testimony, Body = Analytics, Finale = Synthesis |
| One suggestion, take it or leave it | 2-5 options with "when to pick which" comparison |
| No mid-writing support | Phase 2: check tone, get transitions, shift narrative on the fly |

## Installation

**macOS / Linux:**
```bash
cp -r writing-guru ~/.claude/skills/
```

**Windows:**
```powershell
xcopy writing-guru %USERPROFILE%\.claude\skills\writing-guru\ /E /I
```

## How it works

### Phase 1 -- Strategy (before writing)

You describe your task. The skill asks 3-4 questions:

| Question | Why it matters |
|----------|---------------|
| What language are we writing in? | Asked every time -- you might write in English today and Russian tomorrow |
| What is the goal? | Narrows to 1-2 narrative groups (persuade = Strategic, explain = Explanatory) |
| Who is the reader? | Shapes the "why this variant for THIS audience" reasoning |
| What tone? | Formal, conversational, expert -- affects narrative selection |

Then it runs the algorithm: **3 lenses, group filtering, compound lookup, 2-5 strategy variants**.

Each variant includes:
- **Why it fits this audience** -- not just "this works" but "this works because your reader values X"
- **Text map** -- which narrative handles each block (lead, body, finale)
- **Sample lead** -- 2-3 sentences in that narrative voice, on your topic
- **When to pick this one** -- context: publication format, goal, situation

After all variants -- a comparison block: "Variant 1 if publishing in a blog, Variant 2 if pitching to stakeholders..."

### Phase 2 -- Mid-writing support

Come back anytime during writing:

| Trigger | What happens |
|---------|-------------|
| `guru, check this` | Identifies the active narrative in your fragment, flags deviations from the map |
| `guru, what's next` | Suggests transition to the next block, gives a sample bridge sentence |
| `guru, shift tone` | Proposes alternative narrative for the current block |

### What's inside

```
writing-guru/
  SKILL.md                        # Main skill (250 lines)
  references/
    compounds.md                  # 204 named narrative combinations (448 lines)
    group-fallbacks.md            # 28 group-level fallbacks for missing pairs
```

## Usage examples

Works with any text task. Some triggers:

- `"writing guru"` or `"narrative strategy"` -- start Phase 1
- `"How should I write this article about X?"` -- triggers automatically
- `"pick a narrative"` / `"which narrative to choose"` -- Russian triggers too
- `"guru, check this"` / `"guru, what's next"` -- Phase 2

## The 25 narratives at a glance

| # | Symbol | Name | Core idea |
|---|--------|------|-----------|
| 1 | Kr | Critique | Verdict + criteria. Negative assessment with reasoning |
| 2 | Pkh | Praise | Status confirmation. Positive assessment |
| 3 | Rn | Ranking | Hierarchy, comparison by criteria |
| 4 | Ev | Taste ethics | Meta-assessment: which criteria are acceptable |
| 5 | Lb | Lobby | Call to action, mobilization |
| 6 | Pt | Pitch | Value proposition |
| 7 | Fr | Framing | Sets the discussion frame without arguing |
| 8 | As | Agenda-setting | Defines what is worth talking about |
| 9 | An | Analytics | Mechanism breakdown: how and why it works |
| 10 | Md | Method | How-to, instruction, algorithm |
| 11 | Sz | Synthesis | Field overview, type map, summary |
| 12 | Sv | Testimony | "I was there." Minimum interpretation |
| 13 | Dl | Datalog | Event log, observation protocol |
| 14 | Ku | Curation | Selection and organization |
| 15 | Vp | Question | Problematization: posing uncertainty as an act |
| 16 | Gp | Hypothesis | Preliminary explanation with caveats |
| 17 | Me | Thought experiment | Counterfactual: what if the opposite? |
| 18 | Ap | Apophatics | Definition through negation |
| 19 | Pd | Support | Empathy, gratitude, emotional connection |
| 20 | Is | Confession | Self-disclosure as action |
| 21 | My | Belonging | Group markers, we-voice |
| 22 | St | Storytelling | Event through plot |
| 23 | Ir | Irony | Expectation subversion |
| 24 | Rt | Ritual | Cementing value. Pure performative |
| 25 | Mf | Manifesto | Establishing a new coordinate system |

## Works well with

- [ai-writing-detox](../ai-writing-detox/) -- run after writing to kill AI patterns (recommended by the skill automatically)
- [newsroom-style](../newsroom-style/) -- AP Style enforcement for publications
- [story-pitch](../story-pitch/) -- Writing Guru can precede story-pitch for angle selection

These are recommendations, not dependencies. Writing Guru works standalone.

## Credits

- **Skill:** [Alena Zakharova](https://github.com/alenazaharovaux)
- **Periodic Table of Narratives:** [Arseniy Popov](https://t.me/votposmotrim), channel "dolphin befriends cuckoo" -- texts on how technology changes perception, aesthetics, and ways of thinking. The 25 narratives, 7 groups, and 204 compounds are based on his framework.

---

# Writing Guru (RU)

Подбирает нарративную стратегию текста до начала написания. Превращает "мне нужна статья про X" в структурированную нарративную карту с именованными стратегиями, поблочной структурой и семплами лидов.

Построен на **Периодической таблице нарративов** -- фреймворке из 25 базовых нарративов, 7 групп и 204 именованных соединений. Скилл использует три линзы (цель, речевой акт, темпоральность), чтобы систематически отфильтровать подходящие нарративы, и предлагает 2-5 вариантов стратегий с семплами лидов и контекстными рекомендациями.

## Чем отличается от "просто попросить Claude помочь написать"

| Без скилла | Со скиллом |
|------------|-----------|
| Ad-hoc названия: "детектив", "личный подход" | Из таксономии: "Аналитический репортаж (Ан + Св)" с именованными соединениями |
| Структура "введение, основная часть, заключение" | Поблочная карта: Лид = Свидетельство, Тело = Аналитика, Финал = Синтез |
| Один вариант, бери или уходи | 2-5 вариантов с блоком "когда какой выбрать" |
| Никакой поддержки во время написания | Фаза 2: проверить тональность, получить переход, сменить нарратив на ходу |

## Установка

**macOS / Linux:**
```bash
cp -r writing-guru ~/.claude/skills/
```

**Windows:**
```powershell
xcopy writing-guru %USERPROFILE%\.claude\skills\writing-guru\ /E /I
```

## Как работает

### Фаза 1 -- Стратегия (до написания)

Описываете задачу. Скилл задает 3-4 вопроса:

| Вопрос | Зачем |
|--------|-------|
| На каком языке пишем? | Спрашивается каждый раз -- сегодня русский, завтра английский |
| Какая цель? | Сужает до 1-2 групп нарративов |
| Кто читатель? | Формирует аргументацию "почему этот вариант для ЭТОЙ аудитории" |
| Какая тональность? | Формальная, разговорная, экспертная -- влияет на отбор |

Затем алгоритм: **3 линзы, фильтрация по группам, поиск соединений, 2-5 вариантов стратегий**.

Каждый вариант содержит:
- **Почему подходит для этой аудитории** -- конкретная привязка к читателю
- **Карта текста** -- какой нарратив за какой блок отвечает (лид, тело, финал)
- **Семпл лида** -- 2-3 предложения в голосе этого нарратива
- **Когда выбрать** -- контекст: формат, цель, ситуация

### Фаза 2 -- Сопровождение (во время написания)

| Триггер | Что происходит |
|---------|---------------|
| `guru, проверь фрагмент` | Определяет активный нарратив, отмечает отклонения от карты |
| `guru, что дальше` | Предлагает переход к следующему блоку, дает семпл |
| `guru, хочу сменить тональность` | Предлагает альтернативный нарратив |

## Примеры использования

- "writing guru" или "нарративная стратегия" -- запуск Фазы 1
- "Как лучше написать статью про X?" -- сработает автоматически
- "narrative strategy" / "which narrative for this text" -- английские триггеры
- "guru, проверь фрагмент" / "guru, check this" -- Фаза 2
- "guru, что дальше" / "guru, what's next" -- Фаза 2

## Работает в связке с

- [ai-writing-detox](../ai-writing-detox/) -- прогнать после написания, убрать AI-паттерны
- [newsroom-style](../newsroom-style/) -- стандарты AP Style для публикаций
- [story-pitch](../story-pitch/) -- Writing Guru может предшествовать story-pitch

Это рекомендации, не зависимости. Writing Guru работает автономно.

## Авторство

- **Скилл:** [Алена Захарова](https://github.com/alenazaharovaux)
- **Периодическая таблица нарративов:** [Арсений Попов](https://t.me/votposmotrim), канал "дельфин дружит с кукушкой" -- тексты о том, как технологии меняют восприятие, эстетику и способы думать. 25 нарративов, 7 групп и 204 соединения основаны на его фреймворке.
