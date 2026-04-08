# Template — Market Research

**Используется в:** Stage 2 (Research)
**Сохранять в:** `market-research.md` в папке проекта
**Сопутствующий guide:** `references/stage-2-research.md`

**Назначение:** результат desk research по 7 dimensions. Содержит analogs (что работает на похожих рынках) и antilogs (что НЕ работает и почему).

---

## Шаблон

```markdown
# Market Research — [Product name]

**Date:** YYYY-MM-DD
**Reads:** narrative-v1.md
**Riskiest dimensions to research first:** [список dimensions из V1 narrative с Weak evidence]

---

## Methodology

**Sources used:**
- [Web searches: 10-30 запросов через WebSearch]
- [Industry reports: ссылки]
- [Competitor websites: ссылки]
- [Academic / case studies: ссылки]
- [Customer reviews / G2 / Capterra / app stores]

**⛔ No subagents.** Search через WebSearch / Exa напрямую, чтобы сохранять контекст находок.

---

## Dimension 1 — Customer

**What we wanted to learn:**
[Конкретные вопросы от V1 narrative]

**Analogs (companies that succeeded with similar customer):**

| Company | Customer segment | Key insight | Source |
|---------|-----------------|-------------|--------|
| [Company A] | [Segment] | [Что они узнали о customer] | [URL] |
| [Company B] | | | |

**Antilogs (companies that failed or pivoted away from this customer):**

| Company | Why didn't work | Source |
|---------|----------------|--------|
| [Company X] | [Что не сработало с этой аудиторией] | [URL] |

**Updated understanding:**
[1-2 параграфа: как изменилось понимание customer после research]

**Evidence level:** [Weak → Indirect / Indirect → Strong]

---

## Dimension 2 — Problem

**What we wanted to learn:**
[Конкретные вопросы]

**Analogs (problem confirmed in similar form):**

| Source | Problem evidence | Quote / data point |
|--------|-----------------|--------------------|
| [Reddit thread X] | [people complaining about Y] | [quote] |
| [Industry report] | [N% of segment experiences this] | [data] |

**Antilogs (problem doesn't exist as we framed it):**

| Source | Counter-evidence |
|--------|-----------------|
| [Source] | [почему проблема может быть преувеличена / решена] |

**Updated formulation:**
[Visceral формулировка проблемы после research]

**Frequency / severity refined:**
- Frequency: [data]
- Severity: [data]

**Evidence level:**

---

## Dimension 3 — Why now

**What changed (1-3 years ago):**
- [Технологическое изменение 1] — [источник]
- [Рыночное изменение 2] — [источник]
- [Регуляторное изменение 3] — [источник]
- [Поведенческое изменение 4] — [источник]

**Why these enable the product now (not 3 years ago):**
[Конкретное reasoning]

**Evidence level:**

---

## Dimension 4 — Why us

**Competitor landscape:**

| Competitor | Position | Distinctive capability | Weakness |
|-----------|----------|----------------------|----------|
| [Comp 1] | [Direct/Indirect] | | |
| [Comp 2] | | | |
| [Comp 3] | | | |

**Where we'd differentiate:**
[Где у нас есть unique angle, который другие не закрывают]

**Adjacent skills / experience our team has that competitors don't:**
[Конкретно]

**Evidence level:**

---

## Dimension 5 — Solution shape

**Analogs (similar solutions that worked):**

| Solution | What they built | How users adopted | Lesson |
|---------|----------------|-------------------|--------|
| [Solution A] | [shape] | [adoption pattern] | [insight] |

**Antilogs (similar solutions that failed):**

| Solution | What they built | Why didn't work | Lesson |
|---------|----------------|-----------------|--------|
| [Solution X] | | | |

**Solution shape refinement:**
[Что мы меняем в нашей формулировке решения после research]

**Evidence level:**

---

## Dimension 6 — Distribution

**Analogs (channels that worked for similar products):**

| Company | Channel | Key metric | Source |
|---------|---------|-----------|--------|
| [Comp A] | [channel] | [CAC / conversion / scale] | |

**Antilogs (channels that DIDN'T work):**

| Company | Failed channel | Why | Source |
|---------|---------------|-----|--------|
| | | | |

**Channel hypothesis update:**
[Какие каналы убираем, какие добавляем после research]

**Evidence level:**

---

## Dimension 7 — Business model

**Pricing benchmarks:**

| Competitor | Plan | Price | What's included | Source |
|-----------|------|-------|-----------------|--------|
| [Comp 1] | [Starter / Pro / Enterprise] | $X/mo | [features] | |

**Unit economics from analogs:**
- ARPU range: [data]
- LTV/CAC ratios in similar products: [data]
- Payback period typical: [data]

**Pricing model patterns in this space:**
[Какие модели работают: subscription / usage-based / commission / etc.]

**Pricing hypothesis update:**
[Как изменилась наша гипотеза price point после research]

**Evidence level:**

---

## Cross-dimension findings

**Key surprises (≥3):**
1. [Surprise 1: что не ожидали узнать]
2. [Surprise 2]
3. [Surprise 3]

**Confirmed assumptions (which dimensions stayed strong):**
- [Dimension X — confirmed because Y]

**Disconfirmed assumptions (which dimensions need rethinking):**
- [Dimension X — disconfirmed because Y]

**New questions emerged (что нужно дальше валидировать):**
- [Question 1 — для interviews]
- [Question 2 — для experiment]

---

## Sources index

| # | Source | Type | URL | Used in dimensions |
|---|--------|------|-----|-------------------|
| 1 | [Title] | [Web / Report / Reddit / etc.] | [URL] | [1, 2, 5] |
| 2 | | | | |

**Минимум 10 сверенных источников.** Если меньше — research недостаточен.
```

---

## Filling guidance

- **Time-box research:** 2-4 часа на dimension. Не уходить в кроличью нору.
- **Threshold for «enough»:** когда новые поиски дают повторение того же. Это сигнал что насытились.
- **Equal coverage:** все 7 dimensions, не только Customer + Problem (самая частая ошибка).
- **Antilogs обязательны:** без antilogs research = wishful thinking. Минимум 1 antilog на dimension.
- **Concrete sources:** не «по данным интернета», а конкретный URL + дата.
