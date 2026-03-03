# newsletter-publishing

A Claude Code skill for journalists and researchers who want to build direct relationships with their audience. Covers everything from content strategy and HTML templates to deliverability, analytics, and platform selection — so you can launch and run a newsletter without reinventing the wheel. Newsletters give you what algorithms do not: direct access to your reader.

No configuration needed — works out of the box.

## Installation

**macOS / Linux:**
```bash
cp -r newsletter-publishing ~/.claude/skills/newsletter-publishing
```

**Windows:**
```powershell
Copy-Item -Recurse newsletter-publishing $env:USERPROFILE\.claude\skills\newsletter-publishing
```

## Usage

Say any of these to Claude Code:

- "help me create a newsletter"
- "design an email template"
- "improve my open rates"
- "plan a content calendar"
- "set up email authentication"
- "which newsletter platform should I use"

## What's inside

**Content strategy framework** — A fillable document: name, tagline, target reader, content pillars, voice/tone sliders (formal ↔ conversational), and six-month success metrics.

**Issue structure template** — Subject line, preview text, opening hook, main story (300-600 words), secondary items, recurring section, and footer with unsubscribe links.

**Responsive HTML email template** — Production-ready HTML with dark mode support, mobile breakpoint at 480px, table-based layout for email client compatibility, and `{{placeholder}}` variables.

**Subscriber management** — Python dataclasses for Subscriber and NewsletterIssue, list hygiene workflow (flags inactive after 180 days), re-engagement campaign. Segmentation by engagement tier, interest tags, and acquisition source.

**Subject line optimization + A/B testing** — Formulas for news and analysis newsletters. Python function that splits a test group, sends two variants, and routes the remainder to the winner after 4 hours.

**Deliverability** — DNS record templates for SPF, DKIM, and DMARC. Pre-send checklists: content (no spam triggers, text-to-image ratio) and technical (from address, reply-to, preheader, alt text).

**Analytics dashboard** — Open rate, click rate, click-to-open, unsubscribe rate with journalism benchmarks:

| Metric | Good | Excellent |
|--------|------|-----------|
| Open rate | 40% | 55% |
| Click rate | 4% | 8% |
| Unsubscribe rate | < 0.5% | — |

### Platform comparison

| Platform | Best for | Key feature |
|----------|----------|-------------|
| **Substack** | Writer-first | Built-in payments |
| **Ghost** | Publishers | Full CMS included |
| **beehiiv** | Growth | Referral tools |
| **Buttondown** | Developers | Markdown native |
| **ConvertKit** | Creators | Automation |
| **Mailchimp** | Small orgs | Easy templates |

**Legal compliance** — CAN-SPAM (US) and GDPR (EU) checklists in fillable markdown format.

## Works well with

- [ai-writing-detox](../ai-writing-detox/) — strip AI patterns before the issue goes out
- [newsroom-style](../newsroom-style/) — apply editorial standards to newsletter copy

## Credits

From [newsletter-publishing](https://github.com/jamditis/claude-skills-journalism) by [Joe Amditis](https://github.com/jamditis) — MIT license.

---

# newsletter-publishing (RU)

Скилл для Claude Code — для журналистов и исследователей, которые хотят выстроить прямую связь с аудиторией. Рассылка даёт то, чего не даёт алгоритм: прямой доступ к читателю. Покрывает контент-стратегию, HTML-шаблоны, управление подписчиками, доставляемость, аналитику и выбор платформы.

Конфигурация не нужна — работает сразу.

## Установка

```bash
cp -r newsletter-publishing ~/.claude/skills/newsletter-publishing
```

## Использование

- «помоги создать рассылку»
- «сделай шаблон письма»
- «улучши open rate»
- «спланируй контент-календарь»
- «как настроить SPF и DKIM»
- «какую платформу выбрать для рассылки»

## Что внутри

**Контент-стратегия** — шаблон: название, слоган, аудитория, контентные столбы, тон, метрики.

**Шаблон выпуска** — тема, превью, хук, основной материал, рубрика, футер.

**HTML-шаблон** — адаптивный, тёмная тема, мобильный брейкпоинт, переменные-плейсхолдеры.

**Управление подписчиками** — Python-классы, очистка базы, сегментация, реактивация.

**A/B-тестирование** — формулы тем для новостных рассылок, Python-функция split-теста.

**Доставляемость** — SPF, DKIM, DMARC, чеклисты перед отправкой.

**Аналитика** — бенчмарки: open rate 40% (хорошо), 55% (отлично).

**Платформы** — Substack, Ghost, beehiiv, Buttondown, ConvertKit, Mailchimp — сравнительная таблица.

**Юридика** — CAN-SPAM (США) и GDPR (ЕС).

## Хорошо работает вместе с

- [ai-writing-detox](../ai-writing-detox/) — убрать ИИ-паттерны перед отправкой выпуска
- [newsroom-style](../newsroom-style/) — применить стандарты к тексту рассылки

## Авторство

Из [newsletter-publishing](https://github.com/jamditis/claude-skills-journalism) от [Joe Amditis](https://github.com/jamditis) — лицензия MIT.
