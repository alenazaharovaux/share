# Template — Metrics Dashboard

**Используется в:** Stage 9 (Metrics)
**Сохранять в:** `metrics-dashboard.md`
**Сопутствующие guides:** `references/stage-9-metrics.md`, `references/sean-ellis-survey.md`, `references/levels-of-pmf.md`

**Назначение:** template + инструкции для пост-launch измерения PMF через 3 инструмента: Sean Ellis 40% survey, retention cohorts, First Round Levels of PMF.

**⛔ Скилл НЕ собирает данные.** Создаёт template + инструкции. Сбор делает пользователь.

---

## Шаблон

```markdown
# Metrics Dashboard — [Product name]

**Date created:** YYYY-MM-DD
**Reads:** `narrative-v3.md`
**Status:** [Setup phase / Collection phase / Interpretation phase]

---

## What we are measuring

**Final hypothesis (V3):**
[Краткая формулировка того, что валидируем — из narrative-v3]

**Target audience for measurement:**
[Кто active users — из narrative-v3]

**Value proposition tested:**
[Главная formulation value prop — для интерпретации Sean Ellis ответов]

---

## 1. Sean Ellis Survey

**⛔ Не переписывать вопрос. Не менять порядок ответов.**

### Question (готовый для копирования)

**RU:**
> Как бы вы себя чувствовали, если бы больше не могли использовать [название продукта]?

**EN:**
> How would you feel if you could no longer use [product name]?

### Answer options

| # | RU | EN |
|---|----|----|
| 1 | Очень разочарован(а) | Very disappointed |
| 2 | Несколько разочарован(а) | Somewhat disappointed |
| 3 | Не разочарован(а) — это не очень полезно | Not disappointed — it isn't really that useful |
| 4 | Я больше не использую [продукт] | N/A — I no longer use [product] |

### Distribution rules

- **Только active users** (≥1 ключевое действие за последние 2 недели)
- **In-context** — после ключевого действия, не reminder massive blast
- **Random sample**, не cherry-picked

**Рекомендуемый канал:** [in-product modal / email через 1-2 часа после key action / другое]

### Optional follow-up questions

1. Кому бы этот продукт больше всего пригодился?
2. Какой главный benefit вы получаете?
3. Что нужно улучшить?

### Results table (заполняется пользователем)

| Date | Total responses | Very disappointed | Somewhat | Not disappointed | N/A | Score (excl N/A) |
|------|----------------|-------------------|----------|------------------|-----|------------------|
| YYYY-MM-DD | | | | | | % |
| YYYY-MM-DD | | | | | | % |

**Минимум 40 ответов для valid score.**

### Calculation

```
PMF score = Very disappointed / (Total - N/A) × 100%
```

### Interpretation

| Score | Status | Action |
|-------|--------|--------|
| <25% | No PMF | Stage 1 (rethink) |
| 25-40% | Developing | Stage 7 (interview synthesis на «Несколько разочарован») |
| 40-60% | Strong PMF | Scale через paid acquisition |
| >60% | Extreme PMF | Защита через 7 Powers, scaling supply |

---

## 2. Retention Cohorts

### Definition of «active» for this product

[Заполнить под тип продукта:]
- B2B SaaS: ≥1 ключевое действие в неделю
- Consumer: ≥1 session в неделю или ≥3 в месяц
- High-frequency: ≥1 в день или ≥3 в неделю

**Our definition:** [конкретно для этого продукта]

### Cohort table (заполняется пользователем)

| Cohort (week of signup) | Week 1 | Week 2 | Week 3 | Week 4 | Week 8 | Week 12 |
|------------------------|--------|--------|--------|--------|--------|---------|
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |
| [YYYY-MM-DD] | 100% | % | % | % | % | % |

### Where to get data

- [Указать инструмент: Mixpanel, Amplitude, custom DB query, etc.]
- [Конкретный SQL/event filter если применимо]

### Interpretation guide

**Healthy retention curve:**
- Падает в первые 1-2 недели, потом **flatten** (выравнивается)
- Strong PMF threshold:
  - Consumer: flatten на >40%
  - B2B: flatten на >60%
  - High-frequency: flatten на >25%

**Unhealthy retention curve:**
- Монотонно падает к 0% — продукт не цепляет
- «Smiley curve» (восстанавливается после месяца) — re-engagement работает, но изначальный onboarding слабый

---

## 3. Levels of PMF Assessment

| Level | Name | Satisfaction | Demand | Efficiency | Currently? |
|-------|------|--------------|--------|------------|-----------|
| 1 | **Nascent** | <20% или нет данных | 1-10 users, manual acq | Manual everything | [ ] |
| 2 | **Developing** | 25-40% Sean Ellis | Partial flatten, 1-2 referrals/wk | Mixed manual/auto | [ ] |
| 3 | **Strong** | ≥40% Sean Ellis | Flat retention, ≥20% MoM organic | LTV/CAC >3, payback <12mo | [ ] |
| 4 | **Extreme** | >60% Sean Ellis | Non-linear, supply-constrained | LTV/CAC >5, payback <6mo | [ ] |

**Rule:** общий уровень = минимум из трёх dimensions.

### Evidence per dimension

**Satisfaction:**
- [Что измерено: Sean Ellis %, NPS, retention rate]
- [Конкретные числа]

**Demand:**
- [Что измерено: growth rate, organic %, conversion rate, waitlist size]
- [Конкретные числа]

**Efficiency:**
- [Что измерено: CAC, LTV, payback period, support load]
- [Конкретные числа]

### Current assigned level

**Level:** [1/2/3/4]
**Bottleneck dimension:** [satisfaction/demand/efficiency]
**Why this level (1-2 фразы):**
[reasoning]

### What's needed to reach next level

[1-2 конкретных шага из levels-of-pmf.md table]

---

## Decision tree (Stage 10)

```
IF Level = Strong PMF and bottleneck = none:
  → Stage 10 (Iterate). Защита satisfaction, ускорение growth, начать строить power.
  
IF Level = Developing:
  → Stage 7 (Interview synthesis на «Несколько разочарован»). Закрыть top blockers.
  
IF Level = Nascent:
  → Stage 4 (Validate). Глубже валидировать assumptions через interviews + experiments.
  
IF Level = Extreme:
  → Outside PMF skill scope. Scaling, hiring, expansion.
```

---

## Flow notes

Stage 9 разворачивается во времени:

1. **Setup phase** (1 сессия со скиллом): создан этот dashboard + инструкции
2. **Collection phase** (4-12 недель, без скилла): пользователь собирает данные
3. **Interpretation phase** (1 сессия со скиллом): возврат с заполненным dashboard, скилл интерпретирует и рекомендует Stage 10

**Status now:** [Setup / Collection / Interpretation]

**Next checkpoint:** [когда планируется заполнить данные и вернуться]
```

---

## ⛔ Что НЕ делать при использовании этого шаблона

| Don't | Why |
|-------|-----|
| Симулировать данные | Скилл создаёт template, не данные. Цифры — от пользователя |
| Sean Ellis на newsletter list | Selection bias |
| <40 ответов считать как valid score | Статистический шум |
| Переписать Sean Ellis вопрос | Это уже не Sean Ellis |
| Общий retention rate без cohorts | Скрывает падение со временем |
| «Мы на Strong потому что revenue растёт» | Revenue ≠ fit. Растёт можно и через CAC > LTV |
| Self-assess Level без evidence | Wishful thinking |
