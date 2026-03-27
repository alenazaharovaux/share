# skill-stress-test

Verify skill quality through TDD discipline: write pressure scenarios (tests), watch agents fail without the skill (RED), write the skill (GREEN), close loopholes (REFACTOR).

**by [Jesse Vincent](https://github.com/jessevondoom)** · [superpowers plugin](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

> **How is this different from `skill-lab`?**
> `skill-lab` (Anthropic) is the **tooling** for creating skills — eval runner, benchmark scripts, browser-based review viewer, description optimizer. It answers: *"How do I build, test, measure, and ship a skill?"*
>
> `skill-stress-test` (Jesse Vincent / superpowers) is the **philosophy** — TDD discipline, pressure scenarios, rationalization tables, bulletproofing. It answers: *"How do I make sure my skill actually works under real-world pressure?"*
>
> Use them together: create a skill with `skill-lab`, then stress-test it with `skill-stress-test`.

---

## What it does

`skill-stress-test` applies Test-Driven Development to process documentation. The core insight: if you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

The cycle:

```
1. RED     → Write pressure scenarios, run them WITHOUT the skill
           → Document exactly how the agent fails (verbatim rationalizations)
2. GREEN   → Write the skill addressing those specific failures
           → Run the same scenarios WITH the skill — agent should now comply
3. REFACTOR → Agent found new loopholes? Add explicit counters
           → Build rationalization table, create red flags list
           → Re-test until bulletproof
```

### Key concepts

- **Pressure scenarios** — test cases that combine multiple pressures (time urgency + sunk cost + authority) to force the agent into rationalization mode
- **Rationalization tables** — catalog of every excuse agents make to skip the rule, with explicit counters
- **Red flags lists** — self-check triggers for agents to recognize when they're about to violate a rule
- **CSO (Claude Search Optimization)** — making sure future Claude instances can find and correctly trigger your skill
- **The Iron Law** — no skill without a failing test first. Same as TDD for code.

---

## Installation

### Option 1: Official Plugin (Claude Code) — recommended

This skill is the `writing-skills` part of the **superpowers** plugin.

1. Open Claude Code in your terminal
2. Type `/plugins` and press Enter
3. Search for **superpowers**
4. Click **Install**

### Option 2: Copy the skill folder manually

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/skill-stress-test
git clone --depth 1 https://github.com/alenazaharovaux/share.git /tmp/share
cp -r /tmp/share/skills/skill-stress-test/* ~/.claude/skills/skill-stress-test/
rm -rf /tmp/share
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\skill-stress-test"
git clone --depth 1 https://github.com/alenazaharovaux/share.git $env:TEMP\share
Copy-Item -Recurse "$env:TEMP\share\skills\skill-stress-test\*" "$env:USERPROFILE\.claude\skills\skill-stress-test\"
Remove-Item -Recurse -Force "$env:TEMP\share"
```

---

## Contents

```
skill-stress-test/
├── SKILL.md                           # Main reference: TDD cycle, CSO, rationalization defense, checklist
├── LICENSE                            # MIT
├── persuasion-principles.md           # Research-backed persuasion techniques (Cialdini, Meincke)
├── testing-skills-with-subagents.md   # Pressure scenario methodology
├── graphviz-conventions.dot           # Flowchart style guide for skills
├── render-graphs.js                   # Render dot diagrams from SKILL.md to SVG
└── examples/
    └── CLAUDE_MD_TESTING.md           # Worked example: testing CLAUDE.md variants
```

---

## Usage

Use after creating a skill (with `skill-lab` or manually) to verify it holds up under pressure:

- *"Stress-test this skill with pressure scenarios"*
- *"Run TDD for this skill — I want to see how agents rationalize without it"*
- *"Does this skill actually prevent the bad behavior, or can agents talk their way around it?"*

### Testing different skill types

| Skill type | Test approach | Success criteria |
|-----------|--------------|-----------------|
| **Discipline** (TDD, verification) | Pressure scenarios: time + sunk cost + exhaustion | Agent follows rule under maximum pressure |
| **Technique** (how-to guides) | Application + variation + missing info | Agent applies technique to new scenarios |
| **Pattern** (mental models) | Recognition + counter-examples | Agent knows when to apply and when NOT to |
| **Reference** (API docs) | Retrieval + application + gap testing | Agent finds and uses info correctly |

---

## Credits

Skill by **Jesse Vincent** · [superpowers plugin](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

Published here with attribution. Primary installation: superpowers plugin via Claude Code.

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

---

# skill-stress-test (RU)

Проверка качества скиллов через TDD-дисциплину: пишешь сценарии давления (тесты), смотришь как агент проваливается без скилла (RED), пишешь скилл (GREEN), закрываешь лазейки (REFACTOR).

**автор: [Jesse Vincent](https://github.com/jessevondoom)** · [плагин superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

> **Чем отличается от `skill-lab`?**
> `skill-lab` (Anthropic) — это **инструментарий** для создания скиллов: раннер тестов, бенчмарк-скрипты, вьюер для ревью в браузере, оптимизатор описаний. Отвечает: *«Как создать, протестировать, измерить и выпустить скилл?»*
>
> `skill-stress-test` (Jesse Vincent / superpowers) — это **философия**: TDD-дисциплина, сценарии давления, таблицы рационализаций, закалка. Отвечает: *«Как убедиться, что скилл реально работает под давлением?»*
>
> Используй вместе: создай скилл через `skill-lab`, затем проверь через `skill-stress-test`.

---

## Что делает

`skill-stress-test` применяет Test-Driven Development к процессной документации. Ключевая идея: если ты не видела, как агент проваливается без скилла, ты не знаешь, учит ли скилл правильным вещам.

Цикл:

```
1. RED     → Пиши сценарии давления, запускай их БЕЗ скилла
           → Документируй как именно агент проваливается (рационализации дословно)
2. GREEN   → Пиши скилл, адресуя конкретные провалы
           → Запускай те же сценарии СО скиллом — агент должен следовать правилам
3. REFACTOR → Агент нашёл новые лазейки? Добавь явные контрмеры
           → Собери таблицу рационализаций, создай список красных флагов
           → Тестируй повторно до пуленепробиваемости
```

### Ключевые концепции

- **Сценарии давления** — тест-кейсы, комбинирующие несколько давлений (срочность + невозвратные затраты + авторитет), чтобы заставить агента рационализировать
- **Таблицы рационализаций** — каталог всех отговорок агентов с явными контрмерами
- **Списки красных флагов** — триггеры для самопроверки, чтобы агент распознал, когда он собирается нарушить правило
- **CSO (Claude Search Optimization)** — как обеспечить, чтобы будущие Клоды нашли и правильно триггернули скилл
- **Железный закон** — ни одного скилла без провального теста. Тот же принцип, что TDD для кода.

---

## Установка

### Вариант 1: Официальный плагин (Claude Code) — рекомендуется

Этот скилл — часть `writing-skills` в плагине **superpowers**.

1. Открой Claude Code в терминале
2. Введи `/plugins` и нажми Enter
3. Найди **superpowers**
4. Нажми **Установить**

### Вариант 2: Скопировать папку скилла вручную

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/skill-stress-test
git clone --depth 1 https://github.com/alenazaharovaux/share.git /tmp/share
cp -r /tmp/share/skills/skill-stress-test/* ~/.claude/skills/skill-stress-test/
rm -rf /tmp/share
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\skill-stress-test"
git clone --depth 1 https://github.com/alenazaharovaux/share.git $env:TEMP\share
Copy-Item -Recurse "$env:TEMP\share\skills\skill-stress-test\*" "$env:USERPROFILE\.claude\skills\skill-stress-test\"
Remove-Item -Recurse -Force "$env:TEMP\share"
```

---

## Содержимое

```
skill-stress-test/
├── SKILL.md                           # Основной файл: цикл TDD, CSO, защита от рационализаций, чеклист
├── LICENSE                            # MIT
├── persuasion-principles.md           # Техники убеждения (Cialdini, Meincke)
├── testing-skills-with-subagents.md   # Методология сценариев давления
├── graphviz-conventions.dot           # Стайлгайд для блок-схем в скиллах
├── render-graphs.js                   # Рендеринг dot-диаграмм из SKILL.md в SVG
└── examples/
    └── CLAUDE_MD_TESTING.md           # Практический пример: тестирование вариантов CLAUDE.md
```

---

## Использование

Используй после создания скилла (через `skill-lab` или вручную) для проверки на прочность:

- *«Стресс-тест этого скилла со сценариями давления»*
- *«Запусти TDD для этого скилла — хочу увидеть, как агенты рационализируют без него»*
- *«Этот скилл реально предотвращает плохое поведение, или агенты могут его обойти?»*

### Тестирование разных типов скиллов

| Тип скилла | Подход к тестам | Критерий успеха |
|-----------|----------------|-----------------|
| **Дисциплина** (TDD, верификация) | Сценарии давления: срочность + затраты + усталость | Агент следует правилу под максимальным давлением |
| **Техника** (how-to гайды) | Применение + вариации + нехватка информации | Агент применяет технику к новым сценариям |
| **Паттерн** (ментальные модели) | Распознавание + контрпримеры | Агент знает, когда применять, а когда НЕТ |
| **Справочник** (API-доки) | Поиск + применение + поиск пробелов | Агент находит и правильно использует информацию |

---

## Авторство

Скилл создан **Jesse Vincent** · [плагин superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License
[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

Опубликовано здесь с атрибуцией. Основной способ установки: плагин superpowers через Claude Code.

---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
