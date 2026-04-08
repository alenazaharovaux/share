# Template — Risk Prioritization

**Используется в:** Stage 3 (Synthesis)
**Сохранять в:** `risk-prioritization.md`
**Сопутствующий guide:** `references/stage-3-synthesis.md`

**Назначение:** превратить findings из market research в numerical risk score для каждой dimension и определить **самую рискованную dimension** для Stage 4 (Validate).

---

## Шаблон

```markdown
# Risk Prioritization — [Product name]

**Date:** YYYY-MM-DD
**Reads:** `narrative-v1.md`, `market-research.md`
**Writes:** этот файл + `narrative-v2.md` (обновлённый)

---

## Risk scoring formula

**Risk score = Failure impact × Uncertainty**

- **Failure impact (1–5):** если эта dimension окажется неверной, насколько катастрофичны последствия
  - 5 = продукт мёртв, нельзя адаптировать
  - 4 = major pivot нужен
  - 3 = значительная переделка
  - 2 = адаптация в рамках текущего курса
  - 1 = косметика

- **Uncertainty (1–5):** насколько мы НЕ знаем правильный ответ
  - 5 = только мнение команды, ноль данных
  - 4 = indirect evidence из аналогов
  - 3 = одна точка данных или соц.доказательство
  - 2 = несколько подтверждений с разных источников
  - 1 = strong evidence из interviews / measured data

**Risk score range:** 1 (min) до 25 (max).

---

## Failure impact defaults (если не уверен)

| Dimension | Default impact | Reasoning |
|-----------|---------------|-----------|
| 1. Customer | 5 | Wrong audience = всё остальное бессмысленно |
| 2. Problem | 5 | No problem = no product |
| 3. Why now | 3 | Wrong timing — можно подождать или ускорить |
| 4. Why us | 3 | Можно нанять / приобрести capability |
| 5. Solution | 4 | Solution shape можно итерировать, но дорого |
| 6. Distribution | 4 | Без channel нет growth |
| 7. Business model | 4 | Pricing итерируется, но базовая модель тяжело |
| 8. Power | 2 | Long-term, не fatal в первые 1-2 года |

---

## Risk table

| # | Dimension | V1 formulation (краткая) | Failure impact (1-5) | Uncertainty (1-5) | Risk score | Top reason for uncertainty |
|---|-----------|--------------------------|---------------------|-------------------|------------|---------------------------|
| 1 | Customer | [одна фраза] | | | | [почему uncertainty высокая] |
| 2 | Problem | | | | | |
| 3 | Why now | | | | | |
| 4 | Why us | | | | | |
| 5 | Solution | | | | | |
| 6 | Distribution | | | | | |
| 7 | Business model | | | | | |
| 8 | Power | | | | | |

**Sort by Risk score descending.** Самая рискованная — наверху.

---

## Cross-fit checks

После scoring проверить пересечения dimensions — иногда отдельные dimensions выглядят safe, но их комбинация — нет.

### Channel × Business Model fit

**Вопрос:** соответствует ли cost-per-acquisition в выбранном канале target unit economics?

| Channel | Typical CAC range | Compatible с pricing $X? |
|---------|-------------------|--------------------------|
| Cold outreach | $20-200 | [yes/no] |
| Paid search | $50-300 | |
| Content marketing | $10-100 (long-term) | |
| Partnerships | $0-50 | |

Если channel CAC > LTV margin → cross-fit risk высокий, добавить +1 к Risk score Distribution.

### Solution × Customer fit

**Вопрос:** соответствует ли solution shape реальному поведению customer?

- Если customer = enterprise но solution = self-serve sign-up → mismatch
- Если customer = consumer но solution = manual onboarding → mismatch
- Если customer = mobile-first но solution = desktop-only → mismatch

Если mismatch выявлен → +1 к Risk score Solution.

### Why now × Distribution fit

**Вопрос:** working ли каналы которые мы выбрали, в данный момент рыночного цикла?

- Если Why now = «AI стал доступен» но Distribution = «cold email» → channel не использует timing
- Если Why now = «новый закон обязывает X» но Distribution = «content marketing» → channel слишком медленный для urgency

---

## Riskiest dimension

**Selected for Stage 4:** [имя dimension]

**Risk score:** [число]

**Why this is the riskiest:**
[2-3 фразы о том, что именно неизвестно и почему impact высокий]

**What Stage 4 will validate:**
[Какой главный вопрос Stage 4 разрешит]

---

## Updates to narrative

**Dimensions to revise in narrative-v2:**

| Dimension | What changes |
|-----------|--------------|
| [Dim 1] | [как переформулировать после research] |
| [Dim 2] | |

**Persona divides to add:**
- [новые исключения которые увидели в research]

**New evidence sections:**
- [какие dimensions получили Strong evidence]

---

## Decision tree (что делать дальше)

```
IF top 1 risk score ≥ 16:
  → Critical risk. Stage 4 (Validate) is mandatory before any further investment.
  
IF top 1 risk score 10-15:
  → Significant risk. Stage 4 recommended, but можно начать Stage 5 (Interview Prep) параллельно.
  
IF top 1 risk score 6-9:
  → Manageable risk. Можно идти сразу в Stage 5 (Interview Prep), пропустив Stage 4.
  
IF top 1 risk score ≤ 5:
  → Low risk overall. Подозрение на overconfidence. Перепроверить uncertainty scores.
```
```

---

## Common mistakes

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Все scores = 3 | «Среднее везде» | 1-5 — заставлять себя дифференцировать |
| Failure impact = 1 для всех | Мы думаем всё можно адаптировать | 5 dimensions из 8 имеют default ≥3 — это не случайность |
| Uncertainty = 1 для favorite dimensions | Wishful thinking | Если evidence не из interviews/measurement, не ставить 1 |
| Skip cross-fit | Пары dimensions не проверены | Cross-fit обязателен — там часто скрытые риски |
| Outsource decision Stage 4 vs 5 | «Не знаю, идти ли в validate или в interviews» | Использовать decision tree |
