# Stage 4 — Validate / DVF

**Цель:** взять самую рискованную dimension из risk-prioritization, разложить её на 9 assumptions по DVF (Desirability × Viability × Feasibility), приоритизировать через 2×2 (importance × evidence), спроектировать эксперимент для самой рискованной assumption.

**Reads:** `narrative-v2.md`, `risk-prioritization.md`
**Writes:** `assumptions-map.md`, `experiment-brief.md`

**Методология:** David Bland, "Testing Business Ideas". Полное описание DVF — `references/dvf-framework.md`.

---

## ⛔ Терминология

В Stage 4 используем **«assumption»** / **«допущение»**, не «hypothesis» / «гипотеза».

**Почему:** методологически в DVF фреймворке assumption — это конкретное проверяемое утверждение «I believe X». Hypothesis — это более крупная конструкция (вся dimension это hypothesis). Stage 4 разворачивает hypothesis в 9 assumptions для конкретной dimension.

Не смешивать. В narrative — hypothesis. В assumptions-map — assumption.

---

## ⛔ Тон

Calm, coaching. Без восклицательных знаков. Без драматизации. Не задавать clarifying questions перед генерацией — сразу генерировать первый draft, потом уточнять.

---

## Шаг 4.1 — Прочитать риск-dimension

Из `risk-prioritization.md` извлечь:
- Имя riskiest dimension
- V2 формулировку этой dimension из narrative-v2
- Risk score + reasoning
- Какие данные уже есть (из market research)

---

## Шаг 4.2 — Extract: 9 assumptions

Декомпозировать риск-dimension на 9 assumptions, по 3 на каждую DVF-категорию.

### Desirability assumptions (3 шт)

**Что это:** допущения про user needs ТОЛЬКО. Ничего про деньги, ничего про то можно ли это построить.

**Формат:** «Я считаю что [пользователи / сегмент] [действие / отношение / поведение]»

**Примеры:**
- «Я считаю что маленькие e-commerce продавцы тратят 4-6 часов в неделю на ручной перенос заказов»
- «Я считаю что эти продавцы готовы попробовать новый инструмент если он экономит хотя бы 2 часа в неделю»
- «Я считаю что эти продавцы предпочитают табличный интерфейс CRM-подобному»

### Viability assumptions (3 шт)

**Что это:** допущения про деньги ТОЛЬКО. Pricing, willingness to pay, unit economics, LTV, CAC, costs.

**Формат:** «Я считаю что [финансовое утверждение]»

**Примеры:**
- «Я считаю что эти продавцы готовы платить $29/мес за этот инструмент»
- «Я считаю что CAC через cold outreach будет $150 при LTV $500»
- «Я считаю что 30% trial users converted в paid в первые 14 дней»

### Feasibility assumptions (3 шт)

**Что это:** допущения про operational + technical + regulatory.

**Формат:** «Я считаю что мы можем [построить / запустить / соблюсти]»

**Примеры:**
- **Operational:** «Я считаю что мы можем поддерживать 100 customers с командой из 2 человек»
- **Technical:** «Я считаю что API маркетплейсов стабильны достаточно для real-time sync»
- **Regulatory:** «Я считаю что хранение данных продаж не требует специальной лицензии»

### Regulatory sub-check

Если product type из setup = AI / fintech / healthtech → автоматически добавить хотя бы 1-2 regulatory assumptions в Feasibility:

- AI: data privacy, model compliance, AI Act если EU
- Fintech: лицензирование, KYC/AML, payment processing
- Healthtech: HIPAA / GDPR-medical, FDA если US, ML medical device classification

Это **не дополнительные** assumptions — они **внутри** 3 Feasibility, заменяя operational/technical если regulatory важнее.

### DVF Tension Check

После генерации 9 assumptions — посмотреть на **самые большие конфликты между категориями**:

- Desirability says «они хотят X» + Viability says «но они не платят за X»
- Desirability says «они любят простоту» + Feasibility says «но простота требует backend сложности»
- Viability says «$29/мес работает» + Desirability says «они привыкли к бесплатным инструментам»

Записать 1-2 предложения о самом большом DVF tension в `assumptions-map.md`. Это часто = riskiest assumption.

---

## Шаг 4.3 — Map: 2×2 importance × evidence

Расположить 9 assumptions на матрице:

```
        High Importance
              |
    [Critical]| [Sweet spot]
   weak       |       strong
  evidence ---+--- evidence
  [Distraction]| [Solid]
              |
        Low Importance
```

**Quadrants:**

| Quadrant | Что значит | Действие |
|----------|------------|----------|
| **Critical** (high importance + weak evidence) | Самые рискованные. Без валидации продукт умрёт. | Тестировать первыми |
| **Sweet spot** (high importance + strong evidence) | Подтверждены. | Не трогать, использовать как опору |
| **Solid** (low importance + strong evidence) | Подтверждены, но не критичны. | Не тратить время |
| **Distraction** (low importance + weak evidence) | Не критичны и нет данных. | Игнорировать пока что |

**Importance scale:**
- **High:** если assumption неверна → продукт не работает / экономика не сходится / нельзя построить
- **Low:** если assumption неверна → можно адаптировать без катастрофы

**Evidence scale:**
- **Strong:** есть данные из market research, существующих пользователей, аналогов
- **Weak:** нет данных, только предположение

**Запись в assumptions-map.md** — таблица 9 строк с колонками:
- Assumption text (verbatim)
- Category (D/V/F)
- Importance (high/low)
- Evidence (strong/weak)
- Quadrant
- Notes

**После размещения** — выделить **1-3 assumption из Critical quadrant** как кандидатов на эксперимент.

---

## Шаг 4.4 — Test: experiment brief

Для **самой рискованной assumption** из Critical quadrant — спроектировать эксперимент.

**Experiment types** (стандартные, использовать только эти названия):

| Type | Что делает | Когда применять |
|------|-----------|-----------------|
| **Customer Interview** | Глубинное интервью с целевой аудиторией | Desirability assumptions, понимание behavior |
| **Smoke Test** | Landing page + ad → измеряем интерес (sign-ups) до того как продукт построен | Desirability + Viability (intent to pay) |
| **Concierge** | Делаем работу руками для 5-10 customers, симулируя продукт | Feasibility + Desirability в комплексе |
| **Survey** | Структурированный опрос на масштабе | Desirability + Viability (willingness to pay) |
| **Prototype** | Кликабельный прототип без real backend | Desirability (UX) + Feasibility (нужен ли backend) |
| **Landing Page** | Полная landing page с CTA | Demand validation, price testing |

**Не выдумывать новые типы.** Стандартный набор покрывает 95% случаев.

### Структура experiment brief

```markdown
## Experiment Brief

**Assumption:** [verbatim из assumptions-map.md]

**What we'll learn:** [что именно подтвердится или опровергнется]

**Experiment type:** [один из 6 стандартных]

**How to run:**
1. [шаг 1]
2. [шаг 2]
3. [шаг 3]

**How to measure:**
- **Success signal:** [конкретный threshold] — если этот результат, assumption подтверждена
- **Failure signal:** [конкретный threshold] — если этот результат, assumption опровергнута
- **Inconclusive:** [что между signals] — если этот результат, эксперимент нужно повторить или редизайнить

**Estimated effort:** [часы / дни]

**Remaining uncertainty:** [что эксперимент НЕ покажет, нужны другие методы]
```

**Пример:**

```markdown
**Assumption:** «Маленькие e-commerce продавцы готовы платить $29/мес за инструмент синхронизации заказов»

**What we'll learn:** Подтвердить willingness to pay на конкретной price point. Не пользовательский интерес (это desirability), а готовность открыть кошелёк.

**Experiment type:** Smoke Test

**How to run:**
1. Создать landing page с описанием продукта (3-5 benefits, screenshot mockup, social proof placeholder)
2. На странице — Pricing block с одним планом $29/мес. Кнопка «Start free trial» ведёт на форму (email + Stripe Checkout без charge — pre-authorize только)
3. Запустить $200 cold ads на FB / IG таргетированных на e-commerce продавцов в RU/UA/CIS

**How to measure:**
- **Success:** ≥3% landing → trial sign-up + ≥30% trial → entered card details. Если 100 visitors дали 3 sign-ups и 1 entered card details — pass
- **Failure:** <1% landing → trial OR <10% trial → entered card details
- **Inconclusive:** что между → редизайнить landing copy и повторить

**Estimated effort:** 8-12 часов на создание landing + 1 неделя на сбор данных

**Remaining uncertainty:** Эксперимент покажет интент, но не retention. Retention нужен Concierge experiment с 5-10 пользователями minimum.
```

---

## Шаг 4.5 — Cross-loop

Если эксперимент требует **больше данных** перед запуском (например, нужно знать конкретный pricing competitors) — рекомендовать локальный возврат к Stage 2 (research) для одной точки данных. Не возвращаться целиком, только по одному вопросу.

Если эксперимент **успешен** → переход к Stage 5 (Interview Prep) для других риск-dimensions, или сразу к Stage 8 (если всё валидировано).

Если эксперимент **провален** → возврат к Stage 1 для переосмысления этой dimension (Pivot или Reset).

---

## Quality gates Stage 4

- [ ] Терминология выдержана: «assumption» везде, не «hypothesis»
- [ ] 9 assumptions = ровно 3 на каждую категорию (Desirability, Viability, Feasibility)
- [ ] Каждая assumption начинается с «I believe...» / «Я считаю что...»
- [ ] Desirability assumptions ТОЛЬКО про user needs (нет про деньги или backend)
- [ ] Viability assumptions ТОЛЬКО про финансы
- [ ] Feasibility assumptions про operational/technical/regulatory
- [ ] Regulatory sub-check сделан для AI/fintech/healthtech продуктов
- [ ] DVF tension записан (1-2 предложения)
- [ ] 2×2 map создана, все 9 размещены в quadrants
- [ ] Critical quadrant выделен (1-3 assumptions кандидатов)
- [ ] Experiment brief сделан для 1 самой рискованной
- [ ] Experiment type — один из 6 стандартных, не выдуманный
- [ ] Success/failure signals имеют конкретные thresholds (не «будет много sign-ups»)
- [ ] Estimated effort указан

---

## Common pitfalls Stage 4

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Терминология «hypothesis» в Stage 4 | Смешано с narrative | Только «assumption» |
| Desirability содержит pricing | «Они хотят это за $29/мес» | Это Viability. Desirability — только хотят/не хотят |
| Viability содержит UX | «Они купят если дизайн красивый» | Это Desirability |
| 9 assumptions не сбалансированы | 5 D + 2 V + 2 F | Должно быть строго 3+3+3 |
| Все assumptions в Sweet spot | «У нас всё подтверждено» | Если все подтверждены — Stage 4 не нужен. Скорее всего underestimated importance |
| Distraction исследуется | Тратить время на low importance + weak evidence | Skip. Важны только Critical |
| Experiment без quantitative threshold | «Будет много интереса» | Конкретные числа: ≥3%, ≥10 sign-ups, etc. |
| Кастомный experiment type | «Mini-pilot», «Discovery sprint» | Только 6 стандартных. Если не подходит — переформулировать |
| Перепрыгнуть Map → сразу Test | Без 2×2 | Map нужен чтобы выбрать ПРАВИЛЬНУЮ assumption для теста, иначе тест на не-критичной |
| Игнор regulatory для AI | Skip Feasibility regulatory | Для AI обязательно: data privacy, AI Act, copyright |
