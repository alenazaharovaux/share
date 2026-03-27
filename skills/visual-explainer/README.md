# visual-explainer

Turn complex data, systems, and workflows into beautiful self-contained HTML pages — instead of ASCII art and terminal tables nobody wants to read.

**Adapted from [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT)** · Extended for journalism and research by [Alena Zakharova](https://github.com/alenazaharovaux) · MIT License

---

## What it does

`visual-explainer` generates single-file HTML pages with real typography, interactive Mermaid diagrams, styled data tables, timelines, dashboards, and investigation maps. Every page opens automatically in your browser. No ASCII art, ever.

Before/after:
- ❌ Asking Claude for an architecture diagram → wall of `┌─┐│└─┘` box-drawing characters
- ✅ Same request → a styled HTML page with an interactive zoomable diagram, opens in browser

Built-in diagram types: architecture overviews, flowcharts, sequence diagrams, ER schemas, timelines, dashboards, source networks, investigation maps, editorial workflows, story structures, data tables.

Aesthetic modes: editorial broadsheet, monochrome terminal, blueprint/technical, neon dashboard, paper and ink, newsroom board (cork/pushpin), investigation wall, magazine feature, and more.

---

## Installation

**macOS / Linux:**
```bash
git clone https://github.com/alenazaharovaux/share.git /tmp/alenazaharovaux-share
cp -r /tmp/alenazaharovaux-share/skills/visual-explainer ~/.claude/skills/
rm -rf /tmp/alenazaharovaux-share
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/alenazaharovaux/share.git "$env:TEMP\alenazaharovaux-share"
Copy-Item -Recurse "$env:TEMP\alenazaharovaux-share\skills\visual-explainer" "$env:USERPROFILE\.claude\skills\"
Remove-Item -Recurse "$env:TEMP\alenazaharovaux-share"
```

> **Note:** This skill includes template files and reference docs in subdirectories. Clone the full directory — a single SKILL.md won't work on its own.

---

## First run setup

On first use, the skill will ask two questions:

| Question | Why | Default |
|----------|-----|---------|
| Output directory | Where to save generated HTML files | `~/.agent/diagrams` |
| Language | What language to communicate in | Your language |

Both questions can be skipped — defaults will be used. Settings are saved to `config.md` in the skill directory.

---

## Usage

- *"Draw an architecture diagram of our authentication flow"*
- *"Create a comparison table of these 5 research methods"*
- *"Make a timeline of this investigation"*
- *"Visualize the editorial workflow from pitch to publication"*
- *"Map the relationships between these sources"*
- *"Build a dashboard showing these project metrics"*

The skill also activates **proactively**: if you ask Claude to display a table with 4+ rows or 3+ columns, it will automatically render it as a styled HTML page instead of terminal ASCII.

---

## How to use in the HTML page workflow

`visual-explainer` is the **second step** — it generates the HTML structure after brainstorming defines what to build:

```
1. brainstorming   → figure out structure, content, and goals
2. visual-explainer → generate the HTML page with data and diagrams
3. frontend-design  → elevate the visual quality and aesthetics
4.                 → "create the page"
```

**Why this order?**

Each skill handles a different layer:
- `brainstorming` extracts the *real* requirements through dialogue — what the page is for, who reads it, what data matters
- `visual-explainer` knows how to *organize and structure information visually* — which diagram type fits, how to build hierarchy, how to render tables and charts
- `frontend-design` knows how to make it *beautiful* — distinctive typography, depth, motion, an aesthetic point-of-view

Loading all three before saying "create the page" gives Claude a complete set of instructions. The result looks intentionally designed, not assembled from defaults.

**What happens without this workflow:**
Ask Claude to "build a project page" without these skills → you get a generic card grid with Inter font and blue primary color. With all three skills loaded → Claude commits to an aesthetic direction, chooses distinctive typography, structures the content properly, and the result feels custom-made for your project.

---

## visual-explainer vs frontend-slides

| | visual-explainer | frontend-slides |
|---|---|---|
| Format | Single scrollable page | Slide deck (one screen = one slide) |
| Navigation | Sticky nav, scrolling sections | Keyboard / swipe / scroll-snap |
| Best for | Project pages, dashboards, reports, client deliverables | Talks, pitches, client presentations |
| Diagram support | Full (Mermaid, Chart.js, tables) | Limited (focus on content per slide) |

Both output a single `.html` file. Choose based on whether you want to *share a page* (visual-explainer) or *present slides* (frontend-slides).

---

## What's included

```
visual-explainer/
├── SKILL.md                        # Main skill instructions
├── config.md                       # Your settings (created on first run)
├── templates/
│   ├── architecture.html           # Text-heavy architecture / editorial layout
│   ├── mermaid-flowchart.html      # Flowcharts, sequences, diagrams
│   └── data-table.html             # Data tables, audits, comparisons
└── references/
    ├── css-patterns.md             # CSS layout patterns and overflow protection
    ├── responsive-nav.md           # Multi-section sticky navigation
    └── libraries.md                # Mermaid theming, Chart.js, anime.js, fonts
```

---

## Credits

Original skill by **nicobailon** · [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) · MIT License

Extended with journalism, newsroom, and academic design sensibilities by **Alena Zakharova** ([alenazaharovaux](https://github.com/alenazaharovaux))

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

---

# visual-explainer (RU)

Превращает сложные данные, системы и процессы в красивые самодостаточные HTML-страницы — вместо ASCII-арта и терминальных таблиц, которые никто не хочет читать.

**Адаптировано из [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT)** · Расширено для журналистики и исследований: [Alena Zakharova](https://github.com/alenazaharovaux) · MIT License

---

## Что делает

`visual-explainer` генерирует однофайловые HTML-страницы с настоящей типографикой, интерактивными Mermaid-диаграммами, стилизованными таблицами, таймлайнами, дашбордами и картами расследований. Каждая страница автоматически открывается в браузере. Никакого ASCII-арта — никогда.

До/после:
- ❌ Просишь Клода нарисовать архитектурную схему → стена из `┌─┐│└─┘` псевдографики
- ✅ Тот же запрос → стилизованная HTML-страница с интерактивной масштабируемой диаграммой, открывается в браузере

Встроенные типы диаграмм: обзоры архитектур, блок-схемы, схемы последовательностей, ER-схемы, таймлайны, дашборды, сети источников, карты расследований, редакционные процессы, структуры историй, таблицы данных.

Эстетические режимы: редакционная широкополосная газета, монохромный терминал, технический чертёж, неоновый дашборд, бумага и чернила, доска новостной редакции (пробковая/пины), стена расследования, страница журнала и другие.

---

## Установка

**macOS / Linux:**
```bash
git clone https://github.com/alenazaharovaux/share.git /tmp/alenazaharovaux-share
cp -r /tmp/alenazaharovaux-share/skills/visual-explainer ~/.claude/skills/
rm -rf /tmp/alenazaharovaux-share
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/alenazaharovaux/share.git "$env:TEMP\alenazaharovaux-share"
Copy-Item -Recurse "$env:TEMP\alenazaharovaux-share\skills\visual-explainer" "$env:USERPROFILE\.claude\skills\"
Remove-Item -Recurse "$env:TEMP\alenazaharovaux-share"
```

> **Важно:** Скилл включает файлы шаблонов и справочные документы в подпапках. Клонируй всю директорию — одного файла SKILL.md будет недостаточно.

---

## Настройка при первом запуске

При первом использовании скилл задаст два вопроса:

| Вопрос | Зачем | Значение по умолчанию |
|--------|-------|----------------------|
| Папка для вывода | Куда сохранять HTML-файлы | `~/.agent/diagrams` |
| Язык | На каком языке общаться | Твой язык |

Оба вопроса можно пропустить — будут использованы значения по умолчанию. Настройки сохраняются в `config.md` в директории скилла.

---

## Использование

- *«Нарисуй архитектурную схему нашего процесса аутентификации»*
- *«Создай таблицу сравнения этих 5 методов исследования»*
- *«Сделай таймлайн этого расследования»*
- *«Визуализируй редакционный процесс от питча до публикации»*
- *«Покажи связи между этими источниками»*
- *«Построй дашборд с метриками проекта»*

Скилл также активируется **проактивно**: если ты просишь Клода показать таблицу с 4+ строками или 3+ столбцами, он автоматически отрендерит её как стилизованную HTML-страницу вместо терминальной псевдографики.

---

## Как использовать в связке для создания HTML-страниц

`visual-explainer` — это **второй шаг**: он генерирует HTML-структуру после того, как brainstorming определил, что строить:

```
1. brainstorming   → структура, содержание, цели
2. visual-explainer → HTML-страница с данными и схемами
3. frontend-design  → уровень визуального дизайна
4.                 → «создай страницу»
```

**Почему такой порядок?**

Каждый скилл отвечает за свой слой:
- `brainstorming` извлекает *реальные* требования через диалог — для чего страница, кто её читает, какие данные важны
- `visual-explainer` знает, как *организовать и структурировать информацию визуально* — какой тип диаграммы подходит, как выстроить иерархию, как отрендерить таблицы и графики
- `frontend-design` знает, как сделать это *красивым* — самобытная типографика, глубина, движение, эстетическая позиция

Загрузка всех трёх перед командой «создай страницу» даёт Клоду полный набор инструкций. Результат выглядит намеренно спроектированным, а не собранным из дефолтов.

**Что происходит без этого воркфлоу:**
Попросить Клода «создать страницу проекта» без этих скиллов → стандартная сетка карточек с шрифтом Inter и синим основным цветом. С тремя загруженными скиллами → Клод выбирает эстетическое направление, самобытную типографику, правильно структурирует контент, и результат ощущается сделанным специально для твоего проекта.

---

## visual-explainer vs frontend-slides

| | visual-explainer | frontend-slides |
|---|---|---|
| Формат | Одна страница с прокруткой | Слайды (один экран = один слайд) |
| Навигация | Липкая навигация, прокрутка | Клавиши / свайп / scroll-snap |
| Лучше для | Страниц проектов, дашбордов, отчётов, клиентских материалов | Выступлений, питчей, клиентских встреч |
| Поддержка диаграмм | Полная (Mermaid, Chart.js, таблицы) | Ограниченная (фокус на контент слайда) |

Оба выводят один `.html` файл. Выбирай по задаче: *поделиться страницей* (visual-explainer) или *презентовать слайды* (frontend-slides).

---

## Что включено в пакет

```
visual-explainer/
├── SKILL.md                        # Основные инструкции скилла
├── config.md                       # Твои настройки (создаётся при первом запуске)
├── templates/
│   ├── architecture.html           # Текстовая архитектура / редакционная структура
│   ├── mermaid-flowchart.html      # Блок-схемы, последовательности, диаграммы
│   └── data-table.html             # Таблицы данных, аудиты, сравнения
└── references/
    ├── css-patterns.md             # CSS-паттерны и защита от overflow
    ├── responsive-nav.md           # Многосекционная липкая навигация
    └── libraries.md                # Темизация Mermaid, Chart.js, anime.js, шрифты
```

---

## Авторство

Оригинальный скилл: **nicobailon** · [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) · MIT License

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

Расширен с фокусом на журналистику, медиа и академические исследования: **Алена Захарова** ([alenazaharovaux](https://github.com/alenazaharovaux))

---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
