# Illustration Prompt Generator

Turn vague image requests into production-ready prompts for any AI image generator -- Midjourney, DALL-E, Flux, Stable Diffusion, or whatever comes next. The skill runs a 6-step interview (context, style, references, scene, colors, format) and outputs a structured prompt with 8 named blocks that generators interpret with minimal ambiguity.

## What makes it different from "just describing what you want"

Without this skill, you write "a nice illustration for my website" and get something generic. With illustration-prompt, you get a 150+ word structured prompt with exact HEX colors, named perspective, light direction, exclusion rules, and scale anchors -- so two different generators would produce recognizably similar results.

| Without skill | With skill |
|--------------|-----------|
| "A hero image for my website with some tech vibe" | 8-block structured prompt: SCENE, STYLE, OBJECTS, COLORS, ATMOSPHERE, EDGES, FORMAT, NEGATIVE |
| Generic colors, random composition | HEX codes from your project's palette, described light direction, explicit perspective |
| Looks like an illustration | Looks like YOUR illustration -- matches your design system, brand, and context |
| One shot, start over if wrong | Iterate by modifying specific blocks -- learn which block controls what |

## Installation

**macOS / Linux:**
```bash
cp -r illustration-prompt ~/.claude/skills/
```

**Windows:**
```powershell
xcopy illustration-prompt %USERPROFILE%\.claude\skills\illustration-prompt\ /E /I
```

No configuration needed. No dependencies. Works immediately after installation.

## How it works

### The 6-step interview

The skill walks through each step one at a time. If you're generating multiple images in the same session, it remembers your style, references, and palette -- and skips what's already established.

| Step | What it asks | Why it matters |
|------|-------------|----------------|
| 1. Context | Where will the image be used? (hero banner, card, social post, slide...) | Determines proportions, visual weight, and composition approach |
| 2. Style | Art style and detail level (voxel, isometric, watercolor, photorealism...) | Sets the rendering vocabulary for the entire prompt |
| 3. References | Share reference images with notes on what you like (optional -- can skip) | Anchors the style to concrete examples. Without them, the generator decides style details on its own |
| 4. Scene | What to depict -- the skill proposes 2-3 options based on context | Nails down specific objects, arrangement, and the story the image tells |
| 5. Colors | Palette, mood, lighting -- uses your project's brand colors if known | HEX codes, light direction, and mood descriptors that generators interpret consistently |
| 6. Format | Dimensions, aspect ratio, background type | Exact pixel size and background (transparent, solid color, or scene-filled) |

### The 8-block prompt

After the interview, the skill generates a structured prompt:

```
SCENE:      Overall composition, camera angle, element arrangement
STYLE:      Art style, detail level, rendering references
OBJECTS:    Every object -- position, size, visual features
COLORS:     HEX palette, color distribution, accent and shadow tones
ATMOSPHERE: Lighting direction, mood, depth, ambient effects
EDGES:      What happens at the borders -- fade, crop, vignette, island, bleed
FORMAT:     Width x Height, aspect ratio, background type
NEGATIVE:   What must NOT appear -- text, watermarks, unwanted elements
```

Each block can be modified independently when iterating.

### Built-in defaults (automatic)

The skill automatically applies protective rules in OBJECTS and NEGATIVE blocks for categories where AI generators consistently fail. These activate when the relevant element appears in the scene — no action needed from you.

| Category | What the skill does automatically | Why |
|----------|----------------------------------|-----|
| **Vehicles** | Transparent windows, closed doors, balanced proportions | Generators remove doors or render cutaway interiors |
| **Human figures** | "Five fingers on each hand," explicit hand poses, anatomically correct joints | Extra/fused fingers are the #1 generator failure |
| **Text** | Adds "no text, no letters" to NEGATIVE if user didn't request text; warns user if they did | Generators misspell even 2-word signs (as of March 2026) |
| **Counting (3+ identical objects)** | Describes each object individually with position, states exact count twice | Generators add or merge objects when count isn't explicit |

## Usage examples

Works for any visual asset. Triggers:

- `"I need an illustration for..."` -- starts the interview
- `"illustration prompt"` or `"prompt for image"` -- direct invocation
- `"write a prompt for a hero banner"` -- context-specific
- `"make me a picture"` or `"need a visual"` -- casual triggers
- `"generate an illustration prompt"` -- explicit

Works with ANY art style -- voxel art, isometric, flat, watercolor, photorealistic, 3D render, line art, collage, pixel art, and more.

## Works well with

- [frontend-design](../frontend-design/) -- design the page first, then generate illustrations that match
- [visual-explainer](../visual-explainer/) -- for diagrams and data visualizations (different from artistic illustrations)
- [brainstorming](../brainstorming/) -- if you're not sure what visual direction to take, brainstorm first

These are recommendations, not dependencies. Illustration Prompt works standalone.

## Credits

- **Skill:** [Alena Zakharova](https://github.com/alenazaharovaux)
- [Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

# Генератор промптов для иллюстраций (RU)

Превращает расплывчатые запросы на изображения в точные промпты для любого AI-генератора -- Midjourney, DALL-E, Flux, Stable Diffusion и всего, что появится дальше. Скилл проводит интервью из 6 шагов (контекст, стиль, референсы, сцена, цвета, формат) и выдает структурированный промпт из 8 именованных блоков.

## Чем отличается от "просто описать что хочешь"

| Без скилла | Со скиллом |
|------------|-----------|
| "Красивая картинка для сайта с технологичным настроением" | Структурированный промпт из 8 блоков: SCENE, STYLE, OBJECTS, COLORS, ATMOSPHERE, EDGES, FORMAT, NEGATIVE |
| Случайные цвета и композиция | HEX-коды из палитры проекта, описанное направление света, явная перспектива |
| Выглядит как иллюстрация | Выглядит как ВАША иллюстрация -- совпадает с дизайн-системой и брендом |
| Один выстрел, не понравилось -- начинай сначала | Итерация по отдельным блокам -- учишься, какой блок за что отвечает |

## Установка

**macOS / Linux:**
```bash
cp -r illustration-prompt ~/.claude/skills/
```

**Windows:**
```powershell
xcopy illustration-prompt %USERPROFILE%\.claude\skills\illustration-prompt\ /E /I
```

Не нужна настройка. Нет зависимостей. Работает сразу после установки.

## Как работает

### Интервью из 6 шагов

Скилл проходит по каждому шагу по очереди. При генерации нескольких картинок в одной сессии запоминает стиль, референсы и палитру, пропуская то, что уже известно.

| Шаг | Что спрашивает | Зачем |
|-----|---------------|-------|
| 1. Контекст | Где будет использоваться? (баннер, карточка, соцсеть, слайд...) | Определяет пропорции, визуальный вес и подход к композиции |
| 2. Стиль | Стиль и уровень детализации (воксель, изометрия, акварель, фотореализм...) | Задает визуальный словарь для промпта |
| 3. Референсы | Картинки-примеры с пометками, что нравится (необязательно -- можно пропустить) | Привязывает стиль к конкретным примерам. Без них генератор сам решает детали стиля |
| 4. Сцена | Что изобразить -- скилл предлагает 2-3 варианта | Фиксирует объекты, расположение и историю |
| 5. Цвета | Палитра, настроение, освещение -- использует бренд-цвета проекта | HEX-коды, направление света, дескрипторы настроения |
| 6. Формат | Размеры, соотношение сторон, тип фона | Точный размер в пикселях и фон (прозрачный, цвет, заполненная сцена) |

### Промпт из 8 блоков

```
SCENE:      Общая композиция, угол камеры, расположение элементов
STYLE:      Стиль, детализация, визуальные референсы
OBJECTS:    Каждый объект -- позиция, размер, ключевые черты
COLORS:     HEX-палитра, распределение цветов, акценты и тени
ATMOSPHERE: Направление света, настроение, глубина, эффекты
EDGES:      Что происходит на границах -- затухание, обрез, виньетка, остров
FORMAT:     Ширина x Высота, соотношение сторон, тип фона
NEGATIVE:   Что НЕ должно появиться -- текст, водяные знаки, лишние элементы
```

Каждый блок можно менять независимо при итерациях.

### Встроенные дефолты (автоматические)

Скилл автоматически добавляет защитные правила в блоки OBJECTS и NEGATIVE для категорий, где генераторы стабильно ошибаются. Активируются при появлении соответствующего элемента в сцене.

| Категория | Что скилл делает автоматически | Почему |
|-----------|-------------------------------|--------|
| **Транспорт** | Прозрачные окна, закрытые двери, сбалансированные пропорции | Генераторы убирают двери или рисуют cutaway |
| **Люди** | «Пять пальцев на каждой руке», явная поза рук, анатомически корректные суставы | Лишние/сросшиеся пальцы — ошибка №1 генераторов |
| **Текст** | Добавляет «no text, no letters» в NEGATIVE, если текст не нужен; предупреждает, если нужен | Генераторы не умеют писать даже два слова (на март 2026) |
| **Подсчёт (3+ одинаковых объектов)** | Описывает каждый объект отдельно с позицией, дублирует точное число | Генераторы добавляют или сливают объекты, если число не указано явно |

## Примеры использования

- `"мне нужна иллюстрация для..."` -- запуск интервью
- `"illustration prompt"` или `"промпт для картинки"` -- прямой вызов
- `"напиши промпт для баннера"` -- с контекстом
- `"сделай мне картинку"` или `"нужен визуал"` -- неформальные триггеры
- `"need an image"` / `"generate an illustration prompt"` -- английские триггеры

Работает с ЛЮБЫМ стилем -- воксель-арт, изометрия, флэт, акварель, фотореализм, 3D, лайн-арт, коллаж, пиксель-арт и другие.

## Работает в связке с

- [frontend-design](../frontend-design/) -- сначала дизайн страницы, потом иллюстрации под него
- [visual-explainer](../visual-explainer/) -- для диаграмм и визуализации данных (другая задача)
- [brainstorming](../brainstorming/) -- если не уверены в визуальном направлении, начните с брейншторма

Это рекомендации, не зависимости. Скилл работает автономно.

## Авторство

- **Скилл:** [Алена Захарова](https://github.com/alenazaharovaux)
- [Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
