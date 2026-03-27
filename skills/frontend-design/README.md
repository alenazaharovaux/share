# frontend-design

Create distinctive, production-grade web interfaces that look genuinely designed — not like generic AI output.

**by [Anthropic](https://anthropic.com)** · [official Claude Code plugin](https://github.com/anthropics/claude-code-skills) · Apache License 2.0

---

## What it does

`frontend-design` instructs Claude to commit to a bold aesthetic direction before writing a single line of code — choosing a conceptual tone (brutally minimal, maximalist, editorial, retro-futuristic, etc.), distinctive typography, a cohesive color system, and meaningful motion. The result: interfaces that are visually striking and memorable, not interchangeable.

Before/after:
- ❌ Without this skill: purple gradients, Inter font, predictable card layouts — the same look Claude produces by default
- ✅ With this skill: a clear aesthetic point-of-view, unexpected font pairings, depth through texture and motion, code that feels hand-crafted

---

## Installation

### ✅ Recommended: Official Plugin (Claude Code)

`frontend-design` is an **official Claude Code plugin** published by Anthropic.

**What is an official plugin?**
Claude Code has a built-in plugin system that lets you add skills, commands, and hooks from verified publishers. Plugins install automatically, update themselves, and don't require manual file management. Think of them as app store installs — but for Claude's capabilities.

**How to install frontend-design:**
1. Open Claude Code in your terminal
2. Type `/plugins` and press Enter (or open **Settings → Plugins**)
3. Search for **frontend-design**
4. Click **Install**

The skill activates whenever you ask Claude to build a web component, page, or application.

### Alternative: Copy the skill file manually

If you prefer to install just the skill file without the plugin system:

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/frontend-design
curl -o ~/.claude/skills/frontend-design/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-design/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\frontend-design"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-design/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\frontend-design\SKILL.md"
```

---

## Usage

Trigger when building any web UI:

- *"Build a landing page for my research project"*
- *"Create a card component for displaying interview results"*
- *"Design a dashboard that shows project metrics"*
- *"Make a presentation page for this client proposal"*
- *"Build a portfolio page"*

---

## How to use in the HTML page / presentation workflow

`frontend-design` is the **third step** — it elevates the aesthetics after the structure is in place:

```
1. brainstorming   → figure out structure, content, and goals
2. visual-explainer → generate the HTML page with data and diagrams
3. frontend-design  → elevate the visual quality and aesthetics
4.                 → "create the page"
```

**Why third?**
Visual structure and design quality are separate concerns. `visual-explainer` knows *what* to show and *how to organize it*. `frontend-design` knows *how to make it beautiful*. Loading both skills before saying "create the page" gives Claude the full picture — the result looks intentionally designed, not assembled from defaults.

**For presentations specifically (`frontend-slides`):**
```
1. brainstorming   → content and flow of the presentation
2. frontend-slides → create the slide deck
3. frontend-design  → (optional) push the aesthetics further
```

---

## What makes this different from just asking Claude to "make it look nice"

Without a dedicated instruction set, Claude defaults to:
- Inter or Roboto as the font
- A blue or purple primary color
- Standard card grids and hero sections
- The same layout patterns it has seen thousands of times

`frontend-design` breaks these defaults by enforcing a design thinking process: commit to a tone, choose a distinctive direction, and execute it with precision. Every interface should feel like it was designed for this specific context — not assembled from a template.

---

## Credits

Skill by **Anthropic** · [official Claude Code plugin](https://github.com/anthropics/claude-code-skills) · Apache License 2.0

Published here with attribution for reference. Primary installation: official plugin via Claude Code.

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

---

# frontend-design (RU)

Создаёт самобытные, продакшн-готовые веб-интерфейсы, которые выглядят по-настоящему спроектированными — а не как типичный AI-вывод.

**автор: [Anthropic](https://anthropic.com)** · [официальный плагин Claude Code](https://github.com/anthropics/claude-code-skills) · Apache License 2.0

---

## Что делает

`frontend-design` заставляет Клода выбрать смелое эстетическое направление до написания первой строки кода — определить концептуальный тон (брутально минималистичный, максималистский, редакционный, ретро-футуристический и т.д.), самобытную типографику, цельную цветовую систему и осмысленное движение. Результат: интерфейсы, которые запоминаются — а не все похожи друг на друга.

До/после:
- ❌ Без скилла: фиолетовые градиенты, шрифт Inter, предсказуемые карточки — типовой вывод Клода
- ✅ С скиллом: чёткая эстетическая позиция, неожиданные сочетания шрифтов, глубина через текстуры и движение, код, который кажется сделанным вручную

---

## Установка

### ✅ Рекомендуемый способ: официальный плагин (Claude Code)

`frontend-design` — **официальный плагин Claude Code**, опубликованный Anthropic.

**Что такое официальный плагин?**
Claude Code имеет встроенную систему плагинов, которая позволяет добавлять скиллы, команды и хуки от проверенных авторов. Плагины устанавливаются автоматически, обновляются сами и не требуют ручного управления файлами. Представь их как установку приложений из магазина — только для возможностей Клода.

**Как установить frontend-design:**
1. Открой Claude Code в терминале
2. Введи `/plugins` и нажми Enter (или зайди в **Настройки → Плагины**)
3. Найди **frontend-design**
4. Нажми **Установить**

Скилл активируется каждый раз, когда ты просишь Клода создать веб-компонент, страницу или приложение.

### Альтернатива: скопировать файл скилла вручную

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/frontend-design
curl -o ~/.claude/skills/frontend-design/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-design/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\frontend-design"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-design/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\frontend-design\SKILL.md"
```

---

## Использование

Вызывай при создании любого веб-интерфейса:

- *«Создай лендинг для моего исследовательского проекта»*
- *«Сделай карточку для отображения результатов интервью»*
- *«Спроектируй дашборд с метриками проекта»*
- *«Сделай страницу-презентацию для предложения клиенту»*
- *«Создай страницу портфолио»*

---

## Как использовать в связке для создания HTML-страниц и презентаций

`frontend-design` — это **третий шаг**: он поднимает эстетику после того, как структура готова:

```
1. brainstorming   → структура, содержание, цели
2. visual-explainer → HTML-страница с данными и схемами
3. frontend-design  → уровень визуального дизайна
4.                 → «создай страницу»
```

**Почему третий?**
Визуальная структура и качество дизайна — разные задачи. `visual-explainer` знает, *что* показывать и *как организовать* контент. `frontend-design` знает, *как сделать это красивым*. Загрузка обоих скиллов перед командой «создай страницу» даёт Клоду полную картину — результат выглядит намеренно спроектированным, а не собранным из дефолтов.

**Для презентаций (frontend-slides):**
```
1. brainstorming   → содержание и структура презентации
2. frontend-slides → создать слайды
3. frontend-design  → (опционально) поднять эстетику
```

---

## В чём отличие от «сделай покрасивее»

Без специального набора инструкций Клод по умолчанию использует:
- Inter или Roboto как шрифт
- Синий или фиолетовый основной цвет
- Стандартные сетки карточек и hero-секции
- Одни и те же паттерны компоновки из тысяч виденных примеров

`frontend-design` ломает эти дефолты, внедряя процесс дизайн-мышления: выбрать тон, определить самобытное направление и реализовать его с точностью. Каждый интерфейс должен ощущаться спроектированным для конкретного контекста — а не собранным из шаблона.

---

## Авторство

Скилл создан **Anthropic** · [официальный плагин Claude Code](https://github.com/anthropics/claude-code-skills) · Apache License 2.0

Опубликовано здесь с атрибуцией для справки. Основной способ установки: официальный плагин через Claude Code.

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
