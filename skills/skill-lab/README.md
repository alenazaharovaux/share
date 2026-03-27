# skill-lab

A full-cycle skill creation environment: draft a skill, run test cases with subagents, review outputs in a browser-based viewer, iterate based on feedback, benchmark with variance analysis, and optimize the description for reliable triggering.

**by [Anthropic](https://anthropic.com)** · [claude-plugins-official](https://github.com/anthropics/claude-code-plugins) · Apache 2.0

> **How is this different from `skill-creator`?**
> `skill-creator` (Jesse Vincent / superpowers) teaches the **philosophy** of writing skills — TDD discipline, pressure scenarios, rationalization tables. It answers: *"How should I think about skill quality?"*
>
> `skill-lab` (Anthropic) is the **tooling** — eval runner, grader agents, benchmark aggregation, HTML review viewer, description optimizer. It answers: *"How do I build, test, measure, and ship a skill?"*
>
> They complement each other: use `skill-creator` for the design principles, `skill-lab` for the execution pipeline.

---

## What it does

`skill-lab` guides you through the iterative cycle of skill development:

```
1. Capture intent     → interview: what should the skill do?
2. Draft SKILL.md     → write the skill based on the interview
3. Run test cases     → spawn subagents with and without the skill
4. Review outputs     → browser-based viewer with side-by-side comparison
5. Grade & benchmark  → automated assertion checking, pass rates, timing stats
6. Iterate            → improve the skill based on feedback, re-run, repeat
7. Optimize trigger   → tune the description for accurate activation
8. Package            → create a .skill file for distribution
```

Each step has dedicated tooling — Python scripts, agent instructions, HTML viewers — that automates the tedious parts so you can focus on skill quality.

### Key features

- **Parallel test execution** — runs skill-enabled and baseline subagents simultaneously for every test case
- **HTML review viewer** — interactive browser UI to browse outputs, leave feedback per test case, compare with previous iterations
- **Quantitative benchmarking** — pass rates, execution time, token usage with mean/stddev/delta
- **Blind comparison** — A/B testing where a separate agent judges outputs without knowing which skill produced them
- **Description optimization** — automated loop that tunes the skill description against trigger/no-trigger eval queries using Claude's extended thinking
- **Packaging** — creates distributable `.skill` files (ZIP format)

---

## Contents

```
skill-lab/
├── SKILL.md                     # Main skill reference (480 lines)
├── LICENSE                      # Apache 2.0
├── agents/
│   ├── grader.md                # How to grade assertions against outputs
│   ├── comparator.md            # Blind A/B comparison between two outputs
│   └── analyzer.md              # Post-hoc analysis + benchmark pattern detection
├── references/
│   └── schemas.md               # JSON schemas for all data files
├── scripts/
│   ├── utils.py                 # Parse SKILL.md frontmatter
│   ├── quick_validate.py        # Validate SKILL.md structure (name, desc, YAML)
│   ├── run_eval.py              # Run trigger evaluation for a description
│   ├── run_loop.py              # Full optimization loop: eval → improve → repeat
│   ├── improve_description.py   # Claude + extended thinking to improve descriptions
│   ├── aggregate_benchmark.py   # Aggregate run results into summary statistics
│   ├── generate_report.py       # HTML report for optimization loop results
│   └── package_skill.py         # Package skill folder into .skill (ZIP) file
├── eval-viewer/
│   ├── generate_review.py       # Generate + serve the interactive review page
│   └── viewer.html              # Frontend for reviewing outputs and leaving feedback
└── assets/
    └── eval_review.html         # Editable interface for managing trigger eval sets
```

---

## Installation

### Option 1: Official Plugin (Claude Code) — recommended

`skill-lab` is the `skill-creator` plugin in the Claude Code plugin marketplace, published by Anthropic.

**How to install:**
1. Open Claude Code in your terminal
2. Type `/plugins` and press Enter
3. Search for **skill-creator**
4. Click **Install**

The skill becomes available as `skill-creator:skill-creator` immediately. No manual file management needed.

### Option 2: Copy the skill folder manually

**macOS / Linux:**
```bash
git clone https://github.com/alenazaharovaux/share.git /tmp/share
cp -r /tmp/share/skills/skill-lab ~/.claude/skills/skill-lab
rm -rf /tmp/share
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/alenazaharovaux/share.git $env:TEMP\share
Copy-Item -Recurse "$env:TEMP\share\skills\skill-lab" "$env:USERPROFILE\.claude\skills\skill-lab"
Remove-Item -Recurse -Force "$env:TEMP\share"
```

### Requirements

- Python 3.8+ (for scripts)
- `claude` CLI (for description optimization — uses `claude -p`)
- A browser (for the eval viewer; or use `--static` for headless environments)

---

## Usage

### Creating a new skill

Tell Claude what you want to build:

- *"I want to create a skill for writing database migrations"*
- *"Turn this workflow we just did into a reusable skill"*
- *"Let's build a skill that generates API documentation from code"*
- *"/skill-creator"*

Claude will interview you (intent, triggers, output format, test cases), write a draft SKILL.md, then enter the test-review-iterate loop.

### Improving an existing skill

- *"This skill isn't triggering when it should — can we optimize the description?"*
- *"The PDF skill produces bad tables — let's improve it"*
- *"Run benchmarks on my-skill to see how it compares to baseline"*

### The core loop

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Draft skill  ──►  Run test cases  ──►  Review     │
│       ▲                                    │        │
│       │                                    ▼        │
│       └──────────  Improve skill  ◄── Feedback      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

1. **Test cases run in parallel** — for each test prompt, two subagents are spawned: one with the skill, one without (baseline). Both run simultaneously.
2. **While tests run**, Claude drafts quantitative assertions (e.g., "output is a valid PDF", "contains all input fields").
3. **Results open in the browser** — the viewer shows outputs, previous iteration for comparison, and assertion grades. You leave feedback per test case.
4. **Claude reads your feedback**, improves the skill, and re-runs. Repeat until satisfied.

### Description optimization

After the skill works well, optimize the description for reliable triggering:

1. Claude generates 20 eval queries (10 should-trigger, 10 should-not-trigger)
2. You review and edit them in a browser-based HTML interface
3. An automated loop tests the description, uses extended thinking to improve it, and repeats (train/test split to prevent overfitting)
4. Best description is applied to SKILL.md

### Environment support

| Environment | Test runs | Browser viewer | Description optimization |
|-------------|-----------|---------------|-------------------------|
| **Claude Code** | Parallel subagents | Full support | Full support |
| **Cowork** | Parallel subagents | `--static` mode (HTML file) | Full support |
| **Claude.ai** | Sequential (no subagents) | Skip (inline review) | Skip (needs CLI) |

---

## Scripts reference

| Script | Command | What it does |
|--------|---------|-------------|
| `quick_validate.py` | `python -m scripts.quick_validate <skill-path>` | Validates SKILL.md frontmatter: kebab-case name, description length, YAML structure |
| `run_eval.py` | `python -m scripts.run_eval <args>` | Tests whether Claude triggers a skill for a set of eval queries |
| `run_loop.py` | `python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <id> --max-iterations 5` | Full optimization loop with train/test split |
| `aggregate_benchmark.py` | `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>` | Aggregates grading results into benchmark.json + benchmark.md |
| `generate_report.py` | `python -m scripts.generate_report <args>` | HTML report showing optimization iterations |
| `improve_description.py` | `python -m scripts.improve_description <args>` | Uses Claude with extended thinking to propose better descriptions |
| `package_skill.py` | `python -m scripts.package_skill <skill-folder>` | Creates a distributable .skill file (ZIP) |

Run all scripts from the skill-lab directory (they use relative imports via `scripts/` package).

---

## Agent instructions

The `agents/` directory contains prompts for specialized subagents:

| Agent | File | Role |
|-------|------|------|
| **Grader** | `agents/grader.md` | Evaluates assertions against execution transcript and outputs. Also critiques the evals themselves — flags trivially-satisfied assertions and missing coverage |
| **Blind Comparator** | `agents/comparator.md` | Compares two outputs (A vs B) without knowing which skill produced which. Generates rubric, scores, and declares a winner |
| **Post-hoc Analyzer** | `agents/analyzer.md` | After comparison, "unblinds" and analyzes WHY the winner won. Reads both skills and transcripts, generates actionable improvement suggestions |

---

## Data schemas

All JSON schemas are documented in `references/schemas.md`:

- `evals.json` — test case definitions with prompts and expectations
- `grading.json` — assertion pass/fail results with evidence
- `benchmark.json` — aggregate statistics with mean/stddev/delta
- `comparison.json` — blind A/B comparison results with rubric scores
- `analysis.json` — post-hoc analysis with improvement suggestions
- `timing.json` — execution timing and token usage
- `metrics.json` — tool call counts and output sizes
- `history.json` — version progression tracking

---

## Credits

**Author:** [Anthropic](https://anthropic.com) (support@anthropic.com)
**License:** Apache 2.0 — see [LICENSE](LICENSE)
**Source:** [claude-plugins-official / skill-creator](https://github.com/anthropics/claude-code-plugins)

Published here for reference. Primary installation: `skill-creator` plugin via Claude Code.

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

---

# skill-lab (RU)

Полный цикл создания скиллов: черновик, тестовые прогоны с субагентами, ревью в браузерном вьюере, итерация по фидбеку, бенчмарк с анализом разброса, оптимизация description для надёжного триггеринга.

**автор: [Anthropic](https://anthropic.com)** · [claude-plugins-official](https://github.com/anthropics/claude-code-plugins) · Apache 2.0

> **Чем отличается от `skill-creator`?**
> `skill-creator` (Jesse Vincent / superpowers) учит **философии** создания скиллов — TDD-дисциплина, сценарии давления, таблицы рационализаций. Отвечает на вопрос: *«Как правильно думать о качестве скиллов?»*
>
> `skill-lab` (Anthropic) — это **инструментарий**: раннер для тестов, агенты-грейдеры, агрегация бенчмарков, HTML-вьюер для ревью, оптимизатор описаний. Отвечает на вопрос: *«Как создать, протестировать, измерить и выпустить скилл?»*
>
> Они дополняют друг друга: `skill-creator` — принципы проектирования, `skill-lab` — конвейер исполнения.

---

## Что делает

`skill-lab` ведёт через итеративный цикл разработки скиллов:

```
1. Сбор требований     → интервью: что должен делать скилл?
2. Черновик SKILL.md   → пишет скилл по результатам интервью
3. Тестовые прогоны    → запуск субагентов с и без скилла
4. Ревью результатов   → вьюер в браузере с попарным сравнением
5. Оценка и бенчмарк   → автоматическая проверка утверждений, pass rate, тайминги
6. Итерация            → улучшение скилла по фидбеку, повторный прогон
7. Оптимизация триггера → тюнинг description для точного срабатывания
8. Упаковка            → создание .skill-файла для распространения
```

На каждом шаге есть свой инструмент — Python-скрипты, инструкции для агентов, HTML-вьюеры — которые автоматизируют рутину, чтобы вы фокусировались на качестве скилла.

### Ключевые возможности

- **Параллельные тесты** — для каждого кейса одновременно запускаются субагент со скиллом и без (baseline)
- **HTML-вьюер для ревью** — интерактивный интерфейс в браузере: просмотр результатов, фидбек по каждому тесту, сравнение с прошлыми итерациями
- **Количественный бенчмаркинг** — pass rate, время выполнения, токены с mean/stddev/delta
- **Слепое сравнение** — A/B-тест, в котором отдельный агент оценивает результаты, не зная, какой скилл их создал
- **Оптимизация description** — автоматический цикл, который тюнит описание скилла по trigger/no-trigger запросам с помощью extended thinking Клода
- **Упаковка** — создаёт `.skill`-файлы (формат ZIP) для распространения

---

## Содержимое

```
skill-lab/
├── SKILL.md                     # Основной файл скилла (480 строк)
├── LICENSE                      # Apache 2.0
├── agents/
│   ├── grader.md                # Как оценивать утверждения по результатам
│   ├── comparator.md            # Слепое A/B-сравнение двух выходов
│   └── analyzer.md              # Пост-анализ + обнаружение паттернов в бенчмарках
├── references/
│   └── schemas.md               # JSON-схемы всех файлов данных
├── scripts/
│   ├── utils.py                 # Парсинг frontmatter из SKILL.md
│   ├── quick_validate.py        # Валидация структуры SKILL.md (имя, описание, YAML)
│   ├── run_eval.py              # Запуск триггер-теста для описания
│   ├── run_loop.py              # Полный цикл оптимизации: eval → улучшение → повтор
│   ├── improve_description.py   # Claude + extended thinking для улучшения описаний
│   ├── aggregate_benchmark.py   # Агрегация результатов в сводную статистику
│   ├── generate_report.py       # HTML-отчёт по итерациям оптимизации
│   └── package_skill.py         # Упаковка в .skill-файл (ZIP)
├── eval-viewer/
│   ├── generate_review.py       # Генерация + сервер интерактивной страницы ревью
│   └── viewer.html              # Фронтенд для просмотра результатов и фидбека
└── assets/
    └── eval_review.html         # Редактируемый интерфейс для управления trigger-тестами
```

---

## Установка

### Вариант 1: Официальный плагин (Claude Code) — рекомендуется

`skill-lab` — это плагин `skill-creator` в магазине плагинов Claude Code, опубликованный Anthropic.

**Как установить:**
1. Открой Claude Code в терминале
2. Введи `/plugins` и нажми Enter
3. Найди **skill-creator**
4. Нажми **Установить**

Скилл доступен сразу как `skill-creator:skill-creator`. Без ручного управления файлами.

### Вариант 2: Скопировать папку скилла вручную

**macOS / Linux:**
```bash
git clone https://github.com/alenazaharovaux/share.git /tmp/share
cp -r /tmp/share/skills/skill-lab ~/.claude/skills/skill-lab
rm -rf /tmp/share
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/alenazaharovaux/share.git $env:TEMP\share
Copy-Item -Recurse "$env:TEMP\share\skills\skill-lab" "$env:USERPROFILE\.claude\skills\skill-lab"
Remove-Item -Recurse -Force "$env:TEMP\share"
```

### Требования

- Python 3.8+ (для скриптов)
- CLI `claude` (для оптимизации описаний — использует `claude -p`)
- Браузер (для вьюера результатов; или `--static` для headless-сред)

---

## Использование

### Создание нового скилла

Расскажи Клоду, что хочешь построить:

- *«Хочу создать скилл для написания миграций базы данных»*
- *«Преврати этот воркфлоу, который мы только что прошли, в скилл»*
- *«Давай сделаем скилл, который генерирует документацию API из кода»*
- *«/skill-creator»*

Клод проведёт интервью (цель, триггеры, формат выхода, тест-кейсы), напишет черновик SKILL.md и перейдёт в цикл тест-ревью-итерация.

### Улучшение существующего скилла

- *«Этот скилл не срабатывает когда нужно — давай оптимизируем описание»*
- *«Скилл для PDF делает плохие таблицы — давай улучшим»*
- *«Запусти бенчмарки для my-skill, сравни с baseline»*

### Основной цикл

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Черновик скилла  ──►  Тестовые прогоны  ──►  Ревью│
│       ▲                                       │     │
│       │                                       ▼     │
│       └───────────  Улучшение скилла  ◄── Фидбек    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

1. **Тест-кейсы запускаются параллельно** — для каждого промпта спавнятся два субагента: со скиллом и без (baseline). Оба работают одновременно.
2. **Пока тесты идут**, Клод пишет количественные утверждения (например, «выход — валидный PDF», «содержит все поля из входа»).
3. **Результаты открываются в браузере** — вьюер показывает выходы, предыдущую итерацию для сравнения и оценки утверждений. Вы оставляете фидбек по каждому кейсу.
4. **Клод читает фидбек**, улучшает скилл и перезапускает тесты. Повтор до удовлетворения.

### Оптимизация description

После того как скилл работает хорошо, оптимизируй описание для надёжного триггеринга:

1. Клод генерирует 20 eval-запросов (10 should-trigger, 10 should-not-trigger)
2. Вы ревьюите и правите их в браузерном HTML-интерфейсе
3. Автоматический цикл тестирует описание, использует extended thinking для улучшения, повторяет (с разделением на train/test против переобучения)
4. Лучшее описание применяется к SKILL.md

### Поддержка сред

| Среда | Тестовые прогоны | Вьюер в браузере | Оптимизация description |
|-------|-----------------|-----------------|------------------------|
| **Claude Code** | Параллельные субагенты | Полная поддержка | Полная поддержка |
| **Cowork** | Параллельные субагенты | `--static` режим (HTML-файл) | Полная поддержка |
| **Claude.ai** | Последовательно (без субагентов) | Пропустить (ревью в чате) | Пропустить (нужен CLI) |

---

## Справочник скриптов

| Скрипт | Команда | Что делает |
|--------|---------|-----------|
| `quick_validate.py` | `python -m scripts.quick_validate <путь-к-скиллу>` | Валидация frontmatter: kebab-case имя, длина описания, структура YAML |
| `run_eval.py` | `python -m scripts.run_eval <args>` | Проверяет, триггерит ли Клод скилл для набора eval-запросов |
| `run_loop.py` | `python -m scripts.run_loop --eval-set <путь> --skill-path <путь> --model <id> --max-iterations 5` | Полный цикл оптимизации с train/test-разделением |
| `aggregate_benchmark.py` | `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>` | Агрегация результатов в benchmark.json + benchmark.md |
| `generate_report.py` | `python -m scripts.generate_report <args>` | HTML-отчёт по итерациям оптимизации |
| `improve_description.py` | `python -m scripts.improve_description <args>` | Claude + extended thinking для генерации улучшенных описаний |
| `package_skill.py` | `python -m scripts.package_skill <папка-скилла>` | Создаёт .skill-файл (ZIP) для распространения |

Запускай все скрипты из директории skill-lab (используют относительные импорты через пакет `scripts/`).

---

## Инструкции для агентов

Директория `agents/` содержит промпты для специализированных субагентов:

| Агент | Файл | Роль |
|-------|------|------|
| **Грейдер** | `agents/grader.md` | Оценивает утверждения по транскрипту и выходным файлам. Также критикует сами тесты — отмечает тривиально проходящие утверждения и пробелы в покрытии |
| **Слепой компаратор** | `agents/comparator.md` | Сравнивает два выхода (A vs B), не зная, какой скилл их произвёл. Генерирует рубрику, баллы и объявляет победителя |
| **Пост-анализатор** | `agents/analyzer.md` | После сравнения «рассекречивает» и анализирует, ПОЧЕМУ победитель победил. Читает оба скилла и транскрипта, генерирует конкретные предложения по улучшению |

---

## Схемы данных

Все JSON-схемы документированы в `references/schemas.md`:

- `evals.json` — определения тест-кейсов с промптами и ожиданиями
- `grading.json` — результаты pass/fail утверждений с доказательствами
- `benchmark.json` — агрегированная статистика с mean/stddev/delta
- `comparison.json` — результаты слепого A/B-сравнения с баллами рубрики
- `analysis.json` — пост-анализ с предложениями по улучшению
- `timing.json` — тайминги выполнения и потребление токенов
- `metrics.json` — счётчики вызовов инструментов и размеры выходов
- `history.json` — отслеживание прогресса версий

---

## Авторство

**Автор:** [Anthropic](https://anthropic.com) (support@anthropic.com)
**Лицензия:** Apache 2.0 — см. [LICENSE](LICENSE)
**Источник:** [claude-plugins-official / skill-creator](https://github.com/anthropics/claude-code-plugins)

[Алена Захарова](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

Опубликовано здесь для справки. Основной способ установки: плагин `skill-creator` через Claude Code.

---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
