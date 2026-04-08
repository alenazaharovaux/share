# Template — Narrative (Structured)

**Используется в:** Stage 1 (V1), Stage 3 (V2), Stage 7 (V3)
**Сохранять в:** `narrative-v1.md`, `narrative-v2.md`, `narrative-v3.md` (отдельные файлы, не перезапись)
**Сопутствующий guide:** `references/narrative-writing-guide.md`

---

```markdown
# Narrative — [Product name]

**Version:** V[1/2/3]
**Date:** YYYY-MM-DD
**Stage source:** [Stage 1 Hypothesis / Stage 3 Synthesis / Stage 7 Interview Synthesis]
**Author:** [имя]

---

## Executive summary (≤200 слов)

[Кто этот продукт для. Какую боль снимает. Чем отличается от текущих решений. 3 параграфа максимум. Visceral, не abstract.]

---

## 1. Customer

**Primary segment:**
[Конкретный сегмент: кто, где, с каким контекстом. Не «занятые люди», а «продавцы 1-3 маркетплейсов в РФ с оборотом 0.5-5 млн ₽/мес».]

**Persona divides (кого исключаем):**
- ✗ [Сегмент 1] — [почему не подходит, одной фразой]
- ✗ [Сегмент 2] — [почему не подходит]
- ✗ [Сегмент 3] — [почему не подходит]

**Evidence:** [Strong / Indirect / Weak] — [источник: market research / interviews / только мнение]

---

## 2. Problem

**Visceral formulation:**
[Проблема с временем, местом, контекстом, числами, реальными workarounds. Эмоциональная, конкретная.]

**Frequency:** [сколько раз в день/неделю/месяц возникает]
**Severity:** [мешает работать / раздражает / nice-to-have]
**Current workarounds:** [как они решают это сейчас — конкретные инструменты, процессы]
**Cost of current state:** [сколько часов/денег/энергии тратят на workarounds]

**Evidence:** [Strong / Indirect / Weak] — [источник]

---

## 3. Why now

**What changed in the world / market / technology in the last 1–3 years that makes this product possible/needed now?**

[Конкретные изменения. Не «AI стал доступен», а «GPT-4 API подешевел в 10x в 2024, что сделало per-request экономику рентабельной для consumer use cases».]

**Evidence:** [Strong / Indirect / Weak]

---

## 4. Why us

**Unique insight or founder-market fit:**
[Что команда знает / умеет / видит, чего другие не видят. Не «нам нравится эта область», а «founder работал 5 лет в этой индустрии и видел эту проблему лично».]

**Distinctive capability:**
[Технология / data / network / опыт, который трудно скопировать]

**Evidence:** [Strong / Indirect / Weak]

---

## 5. Solution shape

**What the product does (benefits, not features):**
[Как меняется день пользователя из-за продукта. Видимый результат, а не feature list.]

**Core experience in one sentence:**
«[Пользователь] [действие] [результат] за [время], используя [главный механизм]»

**Key benefits (3-5):**
1. [benefit 1] — что меняется в жизни пользователя
2. [benefit 2]
3. [benefit 3]

**Out of scope (что НЕ делаем):**
- [feature 1] — почему не нужен сейчас
- [feature 2]

**Evidence:** [Strong / Indirect / Weak]

---

## 6. Distribution / Channel

**Hypothesis 1 (primary channel):**
[Конкретный канал. Например: «cold outreach в Telegram сообщества продавцов на маркетплейсах» а не «social media marketing».]

**Why this channel:**
[Почему здесь target audience и почему сообщение сработает]

**Hypothesis 2 (backup channel):**
[Второй конкретный канал]

**Flywheel sketch:**
```
[event] → [event] → [event] → loop back
```
[Описать 1 потенциальный flywheel: как одна успешная итерация создаёт условия для следующей]

**Evidence:** [Strong / Indirect / Weak]

---

## 7. Business model

**Pricing model:** [subscription / one-time / freemium / usage-based / commission]
**First hypothesis price point:** [конкретное число]
**Why this number:** [reasoning — competitor benchmarks, value-based, cost-plus, etc.]

**Unit economics first guess:**
- ARPU: [число]
- CAC (target): [число]
- LTV (target): [число]
- Payback period: [месяцев]
- Gross margin: [%]

**Revenue model assumptions:**
- [assumption 1]
- [assumption 2]

**Evidence:** [Strong / Indirect / Weak]

---

## 8. Defensibility / Power (+1)

**Which of the 7 Powers (Hamilton Helmer) is most applicable:**
[Scale Economies / Network Economies / Counter-positioning / Switching Costs / Branding / Cornered Resource / Process Power]

**How it builds over time:**
[Конкретный механизм накопления power. Не «у нас будет moat», а «каждый новый пользователь добавляет данные в shared dataset, который улучшает рекомендации для всех — network effect».]

**When this power kicks in:**
[На каком уровне traction defensibility становится реальной — обычно после Strong PMF]

**Evidence:** [Strong / Indirect / Weak]

---

## Validation status table

| Dimension | Evidence level | Top risk | Notes |
|-----------|---------------|----------|-------|
| 1. Customer | Strong/Indirect/Weak | [риск] | [одна строка] |
| 2. Problem | | | |
| 3. Why now | | | |
| 4. Why us | | | |
| 5. Solution | | | |
| 6. Distribution | | | |
| 7. Business model | | | |
| 8. Power | | | |

**Riskiest dimension:** [имя dimension]
**Why riskiest:** [одна-две фразы]

---

## What changed from previous version (для V2 и V3)

**V1 → V2 changes:**
- [Что изменилось в Customer]
- [Что изменилось в Problem]
- [...]

**Evidence updates:**
- [Какая dimension получила Strong evidence]
- [Какая всё ещё Weak]
```

---

## Notes for filling

- **V1**: писать без давления, заполнить всё что знаете, явно отметить Weak evidence
- **V2**: после market research — обновить evidence levels, добавить competitor analogs/antilogs в Validation table
- **V3**: после field interviews — переписать Customer и Problem на языке пользователей с реальными цитатами в комментариях

**Размер:**
- V1: 600-1000 слов
- V2: 800-1200 слов
- V3: 1000-1500 слов

Если меньше — недостаточно конкретики. Если больше — детали уходят в research/interview docs, не в narrative.
