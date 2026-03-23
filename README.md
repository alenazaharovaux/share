# Share

Shared knowledge, tools, and skills for Claude Code.

## Skills

Ready-to-use skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Copy any skill folder to `~/.claude/skills/` to install.

| Skill | What it does |
|-------|-------------|
| [triage-finding](skills/triage-finding/) | Quickly assess links, posts, articles, and YouTube videos — explains what it is, maps to your projects, recommends action |
| [tool-scout](skills/tool-scout/) | Find the right tools (services, MCP servers, AI models, libraries) before building from scratch. Quick scan or deep dive |
| [skill-stress-test](skills/skill-stress-test/) | TDD philosophy for skill quality — pressure scenarios, rationalization tables, RED-GREEN-REFACTOR cycle applied to documentation. From [superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) by Jesse Vincent (MIT) |
| [skill-lab](skills/skill-lab/) | Full-cycle skill creation tooling — eval runner, grader agents, browser-based review viewer, benchmark aggregation, description optimizer. Official [Anthropic plugin](https://github.com/anthropics/claude-code-plugins) (Apache 2.0) |
| [ai-writing-detox](skills/ai-writing-detox/) | Kill the patterns that make readers think "AI wrote this" — banned words, staccato fragments, corporate jargon, fake enthusiasm. The trust filter |
| [newsroom-style](skills/newsroom-style/) | AP Style enforcement — attribution ("said" not "stated"), numbers, dates, ledes under 35 words, pre-publish checklist. The editorial baseline |
| [story-pitch](skills/story-pitch/) | Five pitch templates (news, feature, investigation, op-ed, freelance query) plus the "so what" test and angle development tools |
| [newsletter-publishing](skills/newsletter-publishing/) | Launch and run email newsletters — content strategy, responsive HTML templates, subscriber management, deliverability, A/B testing, platform comparison |
| [academic-writing](skills/academic-writing/) | Full academic lifecycle — research design, literature review, IMRaD structure, peer review responses, NSF/NIH grant proposals, journal selection |
| [writing-guru](skills/writing-guru/) | Narrative strategy before writing — 25 base narratives, 204 compounds, 3-lens algorithm. Turns "write about X" into a structured map with sample leads. Based on the Periodic Table of Narratives by [Arseniy Popov](https://t.me/votposmotrim) |
| [ux-audit](skills/ux-audit/) | 50-item UX audit across 5 blocks (Nielsen heuristics, conversion, content, technical, IA). Prioritized report with safeguards against hallucinated stats and inflated severity. Stress-tested 12/12. By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |

Writing skills (ai-writing-detox through academic-writing) are based on [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) by Joe Amditis — MIT license.

### HTML pages & presentations

Skills for building client-facing HTML pages, dashboards, and presentations. Use together: `brainstorming` → `visual-explainer` → `frontend-design` → "create the page".

| Skill | What it does |
|-------|-------------|
| [brainstorming](skills/brainstorming/) | Turn rough ideas into approved designs through structured dialogue — before any code is written. Hard gate: no implementation without a design. From [superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) by Jesse Vincent (MIT) |
| [frontend-design](skills/frontend-design/) | Instructs Claude to commit to a bold aesthetic direction — distinctive typography, cohesive color system, meaningful motion — before writing code. Official Anthropic plugin (Apache 2.0) |
| [frontend-slides](skills/frontend-slides/) | Zero-dependency HTML slide decks with animations and 12 aesthetic presets. Every slide fits exactly one screen. Can convert PowerPoint files. By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |
| [visual-explainer](skills/visual-explainer/) | Generates styled HTML pages for architecture diagrams, data tables, timelines, dashboards, and investigation maps. Never falls back to ASCII art. Adapted from [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT), extended for journalism and research |
| [illustration-prompt](skills/illustration-prompt/) | 6-step interview → structured 8-block prompt for any AI image generator (Midjourney, DALL-E, Flux, Stable Diffusion). HEX colors, named perspectives, vehicle defaults, iterative refinement. By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |

### Development workflow

| Skill | What it does |
|-------|-------------|
| [adr](skills/adr/) | Log architecture decisions as you work — what you chose, why, and what you rejected. One Markdown file per project, ~1 minute per entry. Designed for solo developers and small teams. By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |

## Prompts

Universal prompt collections that work with any LLM — not tied to Claude Code.

| Playbook | What it does |
|----------|-------------|
| [diary-research-playbook](prompts/diary-research-playbook/) | 13 prompts for analyzing qualitative diary studies: entry analysis, pattern detection, interview prep, monitoring cards, synthesis, narrative portraits, business case studies, and interview guide review. By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |

## Other Resources

- [How to customize using superpowers](how-to-customize-using-superpowers.md)

---

# Share (RU)

Общие знания, инструменты и скиллы для Claude Code.

## Скиллы

Готовые скиллы для [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Чтобы установить, скопируй папку скилла в `~/.claude/skills/`.

| Скилл | Что делает |
|-------|-----------|
| [triage-finding](skills/triage-finding/) | Быстро оценивает ссылки, посты, статьи и YouTube-видео — объясняет суть, сопоставляет с проектами, рекомендует действие |
| [tool-scout](skills/tool-scout/) | Находит инструменты (сервисы, MCP, нейронки, библиотеки) прежде чем писать с нуля. Быстрый скан или глубокий разбор |
| [skill-stress-test](skills/skill-stress-test/) | TDD-философия качества скиллов — сценарии давления, таблицы рационализаций, цикл RED-GREEN-REFACTOR для документации. Из [superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) от Jesse Vincent (MIT) |
| [skill-lab](skills/skill-lab/) | Полный конвейер создания скиллов — раннер тестов, агенты-грейдеры, вьюер ревью в браузере, агрегация бенчмарков, оптимизатор описаний. Официальный [плагин Anthropic](https://github.com/anthropics/claude-code-plugins) (Apache 2.0) |
| [ai-writing-detox](skills/ai-writing-detox/) | Убивает паттерны, по которым читатель опознаёт ИИ-текст — запрещённые слова, рубленые фрагменты, корпоративный жаргон. Фильтр доверия |
| [newsroom-style](skills/newsroom-style/) | Стандарты AP Style — атрибуция ("said", не "stated"), числа, даты, лиды до 35 слов, чеклист перед публикацией. Редакционный baseline |
| [story-pitch](skills/story-pitch/) | Пять шаблонов питчей (новость, фичер, расследование, колонка, фриланс) + тест «ну и что?» и развитие угла подачи |
| [newsletter-publishing](skills/newsletter-publishing/) | Запуск и ведение рассылки — стратегия, HTML-шаблоны, подписчики, доставляемость, A/B-тесты, сравнение платформ |
| [academic-writing](skills/academic-writing/) | Весь академический цикл — дизайн исследования, литобзор, структура IMRaD, ответы рецензентам, гранты NSF/NIH, выбор журнала |
| [writing-guru](skills/writing-guru/) | Нарративная стратегия перед написанием — 25 нарративов, 204 соединения, алгоритм 3 линз. Превращает "напиши про X" в карту с семплами лидов. На основе Периодической таблицы нарративов [Арсения Попова](https://t.me/votposmotrim) |
| [ux-audit](skills/ux-audit/) | UX-аудит по 50 пунктам в 5 блоках (эвристики Нильсена, конверсия, контент, техника, ИА). Приоритизированный отчёт с защитой от галлюцинаций и завышения серьёзности. Стресс-тест 12/12. Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT) |

Скиллы для текстов (от ai-writing-detox до academic-writing) основаны на [jamditis/claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) от Joe Amditis — лицензия MIT.

### HTML-страницы и презентации

Скиллы для создания клиентских HTML-страниц, дашбордов и презентаций. Используй в связке: `brainstorming` → `visual-explainer` → `frontend-design` → «создай страницу».

| Скилл | Что делает |
|-------|-----------|
| [brainstorming](skills/brainstorming/) | Превращает сырые идеи в согласованные дизайны через структурированный диалог — до написания кода. Жёсткий запрет: без одобрения дизайна реализации не будет. Из [superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) от Jesse Vincent (MIT) |
| [frontend-design](skills/frontend-design/) | Заставляет Клода выбрать смелое эстетическое направление — самобытная типографика, цельная цветовая система, осмысленное движение — до написания кода. Официальный плагин Anthropic (Apache 2.0) |
| [frontend-slides](skills/frontend-slides/) | HTML-слайды без зависимостей с анимациями и 12 эстетическими пресетами. Каждый слайд точно вписывается в экран. Умеет конвертировать PowerPoint. Автор: [Alena Zakharova](https://github.com/alenazaharovaux) (MIT) |
| [visual-explainer](skills/visual-explainer/) | Генерирует стилизованные HTML-страницы для архитектурных схем, таблиц данных, таймлайнов, дашбордов и карт расследований. Никогда не использует ASCII-арт. Адаптирован из [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT), расширен для журналистики и исследований |
| [illustration-prompt](skills/illustration-prompt/) | Интервью из 6 шагов → структурированный промпт из 8 блоков для любого AI-генератора (Midjourney, DALL-E, Flux, Stable Diffusion). HEX-цвета, перспектива, дефолты для транспорта, итеративная доработка. Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT) |

### Рабочий процесс

| Скилл | Что делает |
|-------|-----------|
| [adr](skills/adr/) | Фиксирует архитектурные решения по ходу работы — что выбрали, почему и что отвергли. Один Markdown-файл на проект, ~1 минута на запись. Для соло-разработчиков и небольших команд. Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT) |

## Промпты

Универсальные коллекции промптов, работающие с любым LLM — не привязаны к Claude Code.

| Playbook | Что делает |
|----------|-----------|
| [diary-research-playbook](prompts/diary-research-playbook/) | 13 промптов для анализа качественных дневниковых исследований: анализ записей, поиск паттернов, подготовка к интервью, карточки мониторинга, синтез, нарративные портреты, бизнес-статьи, ревью гайда интервью. Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT) |

## Другие материалы

- [How to customize using superpowers](how-to-customize-using-superpowers.md)
