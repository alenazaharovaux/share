# UX Audit

Run a full UX audit on any website. The skill crawls the site, checks 50 items across five blocks (Nielsen heuristics, conversion, content, technical quality, information architecture), and produces a prioritized report with evidence-based findings and fix recommendations. Built-in safeguards prevent hallucinated statistics, inflated severity ratings, and false claims about missing page elements.

## Installation

**macOS / Linux:**
```bash
cp -r ux-audit ~/.claude/skills/ux-audit
```

**Windows:**
```powershell
Copy-Item -Recurse ux-audit $env:USERPROFILE\.claude\skills\ux-audit
```

## Prerequisites

The skill needs a way to fetch website content. Options:

| Tool | Setup needed? | Quality | Notes |
|------|--------------|---------|-------|
| **Exa MCP** (recommended) | Yes — [setup guide](https://docs.exa.ai/reference/mcp) | Best | Tested and verified by the author |
| **WebFetch** | No — built into Claude Code | Good | Works out of the box, no setup |
| **WebSearch** | No — built into Claude Code | Basic | Works for simple page analysis |
| **Other MCP** | Depends | Varies | Any MCP server that can fetch page content |

The author developed and stress-tested this skill with Exa MCP. Other tools work but have not been tested — crawl depth and content quality may differ.

## Usage

Say any of these to Claude Code:

- "audit this site: example.com"
- "what's wrong with our landing page?"
- "review the UX of example.com"
- "check the forms on example.com"
- "why isn't this site converting?"

The skill adapts to your language — just talk to Claude as you normally would.

## What the audit covers

| Block | Items | What it checks |
|-------|-------|----------------|
| Nielsen heuristics | 10 | Feedback, consistency, error prevention, navigation |
| Conversion | 12 | CTAs, forms, trust signals, social proof, pricing |
| Content | 12 | Tone, SEO basics, readability, freshness |
| Technical | 8 | HTTPS, mobile, speed, broken links |
| Information architecture | 8 | Navigation depth, menu structure, sitemap |

## Built-in safeguards

The skill includes three protections discovered through [stress testing](https://github.com/alenazaharovaux/share/tree/main/skills/skill-stress-test) (12/12 pass rate under adversarial pressure):

1. **Crawl honesty** — distinguishes "not found in crawl data" from "absent on the site." Burger menus, popups, and JS-hidden elements often don't appear in crawls.
2. **No fabricated statistics** — never cites percentages "according to X Institute" without certainty. References established principles instead.
3. **Severity calibration** — a self-check step prevents inflating CRITICAL ratings. Each finding must pass three verification questions before the report is finalized.

## Extensions

After the audit, you can ask:

- **"Compare with competitors"** — quick audit of 2-3 competitor sites + comparison table
- **"Prepare a fix spec"** — technical specification grouped by priority
- **"Check mobile in detail"** — touch targets, font size, sticky elements, 3G speed
- **"Check accessibility"** — contrast, alt texts, focus indicators, ARIA, keyboard navigation

## Credits

By [Alena Zakharova](https://human2aimain.onrender.com/ru/), [Cloud Research](https://cloud-research.onrender.com/) (MIT).

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).

---

# UX Audit (RU)

Полный UX-аудит любого сайта. Скилл обходит сайт, проверяет 50 пунктов по пяти блокам (эвристики Нильсена, конверсия, контент, техника, информационная архитектура) и формирует отчёт с приоритизированными находками и рекомендациями. Встроенные защиты не дают галлюцинировать статистику, завышать серьёзность и делать ложные утверждения о «недостающих» элементах страницы.

## Установка

**macOS / Linux:**
```bash
cp -r ux-audit ~/.claude/skills/ux-audit
```

**Windows:**
```powershell
Copy-Item -Recurse ux-audit $env:USERPROFILE\.claude\skills\ux-audit
```

## Требования

Скиллу нужен способ получать содержимое веб-страниц. Варианты:

| Инструмент | Нужна настройка? | Качество | Заметки |
|------------|-----------------|----------|---------|
| **Exa MCP** (рекомендуется) | Да — [инструкция](https://docs.exa.ai/reference/mcp) | Лучшее | Проверено и протестировано автором |
| **WebFetch** | Нет — встроен в Claude Code | Хорошее | Работает из коробки |
| **WebSearch** | Нет — встроен в Claude Code | Базовое | Подходит для простого анализа |
| **Другой MCP** | Зависит от сервера | Разное | Любой MCP-сервер, способный получать контент страниц |

Автор разрабатывала и тестировала скилл с Exa MCP. Другие инструменты работают, но не проходили тестирование — глубина обхода и качество контента могут отличаться.

## Использование

Скажите Claude Code любую из фраз:

- «сделай аудит сайта example.com»
- «что не так с нашим лендингом?»
- «проверь UX на example.com»
- «посмотри формы на example.com»
- «почему сайт не конвертирует?»

Скилл подстраивается под ваш язык — говорите с Claude как обычно.

## Что проверяет аудит

| Блок | Пунктов | Что проверяет |
|------|---------|---------------|
| Эвристики Нильсена | 10 | Обратная связь, консистентность, предотвращение ошибок, навигация |
| Конверсия | 12 | CTA, формы, сигналы доверия, соцдоказательства, цены |
| Контент | 12 | Тон, SEO-основы, читаемость, актуальность |
| Техника | 8 | HTTPS, мобильность, скорость, битые ссылки |
| Информационная архитектура | 8 | Глубина навигации, структура меню, карта сайта |

## Встроенные защиты

Скилл включает три защиты, найденные через [стресс-тестирование](https://github.com/alenazaharovaux/share/tree/main/skills/skill-stress-test) (12/12 под давлением):

1. **Честность crawl'а** — различает «не найдено в данных обхода» и «на сайте отсутствует». Бургер-меню, попапы и JS-элементы часто не попадают в crawl.
2. **Без выдуманной статистики** — не цитирует проценты «по данным X института» без уверенности. Ссылается на общепринятые принципы.
3. **Калибровка серьёзности** — шаг самопроверки не даёт завышать CRITICAL. Каждая находка проходит три проверочных вопроса перед финализацией отчёта.

## Расширения

После аудита можно попросить:

- **«Сравни с конкурентами»** — экспресс-аудит 2-3 конкурентов + таблица сравнения
- **«Подготовь ТЗ»** — техническое задание, сгруппированное по приоритету
- **«Проверь мобилку подробнее»** — touch-targets, размер шрифта, sticky-элементы, скорость на 3G
- **«Проверь доступность»** — контраст, alt-тексты, фокус-индикаторы, ARIA, навигация с клавиатуры

## Автор

[Алена Захарова](https://human2aimain.onrender.com/ru/), [Cloud Research](https://cloud-research.onrender.com/) (MIT).

[Alena Zakharova](https://thehuman2ai.com/), [Thehuman2ai](https://thehuman2ai.com/) (MIT).
