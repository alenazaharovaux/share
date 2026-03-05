# frontend-slides

Create stunning, animation-rich HTML presentations that run in any browser — no PowerPoint, no build tools, no dependencies.

**by [Alena Zakharova](https://github.com/alenazaharovaux)** · MIT License

---

## What it does

`frontend-slides` generates self-contained single-file HTML presentations with smooth animations, keyboard/touch/scroll navigation, and a unique aesthetic for each deck. Every slide fits exactly one screen — no scrolling within slides, ever. It can build from scratch, from your notes, or convert an existing PowerPoint file.

Before/after:
- ❌ Exporting PowerPoint to PDF and sending a static file
- ✅ A live HTML presentation that opens in any browser, looks custom-designed, and navigates like a real slideshow

Key features:
- **Zero dependencies** — one `.html` file, works offline
- **Show, don't tell** — generates 3 style previews from your mood preferences before committing to a design
- **12 aesthetic presets** — Bold Signal, Dark Botanical, Neon Cyber, Paper & Ink, Swiss Modern, and more
- **PPT conversion** — extracts content and images from `.pptx` files
- **Viewport fitting** — every slide guaranteed to fit the screen with responsive `clamp()` typography

---

## Installation

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/frontend-slides
curl -o ~/.claude/skills/frontend-slides/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-slides/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\frontend-slides"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-slides/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\frontend-slides\SKILL.md"
```

---

## Usage

- *"Create a pitch deck for my research project"*
- *"Convert my slides.pptx to a web presentation"*
- *"Build a 10-slide talk about AI tools for journalists"*
- *"I need a presentation for a client meeting — help me design it"*
- *"Make a conference talk slide deck, Dark Botanical style"*

---

## How to use in the presentation workflow

`frontend-slides` is the **core tool** for slide-format presentations. Combined with `brainstorming` for structure and `frontend-design` for extra aesthetic polish:

```
1. brainstorming    → figure out content, structure, and audience
2. frontend-slides  → generate the HTML slide deck with style previews
3. frontend-design  → (optional) push the aesthetics even further
```

**frontend-slides vs visual-explainer:**

| | frontend-slides | visual-explainer |
|---|---|---|
| Format | Slides (one screen = one slide) | Single scrollable page |
| Navigation | Keyboard / swipe / scroll-snap | Sticky nav, scrolling sections |
| Best for | Talks, pitches, client presentations | Project pages, dashboards, reports |
| Output | One `.html` file | One `.html` file |

Both work well for client-facing deliverables. Choose based on whether you want to *present* (slides) or *share a page* (visual-explainer).

---

## Available style presets

| Preset | Vibe | Best for |
|--------|------|----------|
| Bold Signal | Confident, high-impact | Pitch decks, keynotes |
| Electric Studio | Clean, professional | Agency presentations |
| Creative Voltage | Energetic, retro-modern | Creative pitches |
| Dark Botanical | Elegant, sophisticated | Premium brands |
| Notebook Tabs | Editorial, organized | Reports, reviews |
| Pastel Geometry | Friendly, approachable | Product overviews |
| Neon Cyber | Futuristic, techy | Tech startups |
| Terminal Green | Developer-focused | Dev tools, APIs |
| Swiss Modern | Minimal, precise | Corporate, data |
| Paper & Ink | Literary, thoughtful | Storytelling |

---

## Dependencies

- **python-pptx** (optional) — only needed for PowerPoint conversion: `pip install python-pptx`

---

## Credits

Skill by **Alena Zakharova** ([alenazaharovaux](https://github.com/alenazaharovaux)) · MIT License

---

---

# frontend-slides (RU)

Создаёт эффектные HTML-презентации с анимациями — работают в любом браузере без PowerPoint, сборщиков и зависимостей.

**автор: [Alena Zakharova](https://github.com/alenazaharovaux)** · MIT License

---

## Что делает

`frontend-slides` генерирует самодостаточные однофайловые HTML-презентации с плавными анимациями, навигацией по клавиатуре/свайпу/скроллу и уникальной эстетикой для каждого проекта. Каждый слайд точно вписывается в один экран — никакой прокрутки внутри слайдов, никогда. Умеет создавать с нуля, из заметок или конвертировать существующие PowerPoint-файлы.

До/после:
- ❌ Экспорт PowerPoint в PDF и отправка статичного файла
- ✅ Живая HTML-презентация, открывается в любом браузере, выглядит как авторский дизайн, навигация как в настоящем слайдшоу

Ключевые особенности:
- **Ноль зависимостей** — один `.html` файл, работает офлайн
- **Покажи, а не рассказывай** — генерирует 3 стилевых превью по твоим настроениям, прежде чем выбрать дизайн
- **12 эстетических пресетов** — Bold Signal, Dark Botanical, Neon Cyber, Paper & Ink, Swiss Modern и другие
- **Конвертация PPT** — извлекает контент и изображения из `.pptx` файлов
- **Вписывание в экран** — каждый слайд гарантированно помещается на экране с адаптивной `clamp()` типографикой

---

## Установка

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/frontend-slides
curl -o ~/.claude/skills/frontend-slides/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-slides/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\frontend-slides"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/frontend-slides/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\frontend-slides\SKILL.md"
```

---

## Использование

- *«Создай питч-дек для моего исследовательского проекта»*
- *«Конвертируй мой slides.pptx в веб-презентацию»*
- *«Сделай 10 слайдов про AI-инструменты для журналистов»*
- *«Нужна презентация для встречи с клиентом — помоги спроектировать»*
- *«Сделай слайды для конференции в стиле Dark Botanical»*

---

## Как использовать в связке для создания презентаций

`frontend-slides` — **основной инструмент** для слайдовых презентаций. В сочетании с `brainstorming` для структуры и `frontend-design` для дополнительной эстетики:

```
1. brainstorming    → содержание, структура, аудитория
2. frontend-slides  → HTML-слайды с выбором стиля по превью
3. frontend-design  → (опционально) поднять эстетику ещё выше
```

**frontend-slides vs visual-explainer:**

| | frontend-slides | visual-explainer |
|---|---|---|
| Формат | Слайды (один экран = один слайд) | Одна страница с прокруткой |
| Навигация | Клавиши / свайп / scroll-snap | Липкая навигация, прокрутка |
| Лучше для | Выступлений, питчей, клиентских встреч | Страниц проектов, дашбордов, отчётов |
| Вывод | Один `.html` файл | Один `.html` файл |

Оба хорошо работают для клиентских материалов. Выбирай по задаче: *презентовать* (слайды) или *поделиться страницей* (visual-explainer).

---

## Доступные пресеты стилей

| Пресет | Настроение | Лучше для |
|--------|-----------|-----------|
| Bold Signal | Уверенный, высокое воздействие | Питч-деки, keynotes |
| Dark Botanical | Элегантный, утончённый | Премиальные бренды |
| Neon Cyber | Футуристичный, технологичный | Технологические стартапы |
| Paper & Ink | Литературный, задумчивый | Сторителлинг |
| Swiss Modern | Минималистичный, точный | Корпоратив, данные |

---

## Зависимости

- **python-pptx** (опционально) — только для конвертации PowerPoint: `pip install python-pptx`

---

## Авторство

Скилл создан **Алена Захарова** ([alenazaharovaux](https://github.com/alenazaharovaux)) · MIT License

---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
