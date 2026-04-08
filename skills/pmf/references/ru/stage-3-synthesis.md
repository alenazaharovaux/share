# Stage 3 — Synthesis

**Цель:** на основе market research сделать risk scoring, выявить риск-dimension, провести cross-fit analysis, обновить narrative до V2.

**Reads:** `narrative-v1.md`, `market-research.md`
**Writes:** `risk-prioritization.md`, `narrative-v2.md`

---

## Шаг 3.1 — Per-dimension analysis

Для каждой dimension зафиксировать:

1. **V1 hypothesis** — что было сформулировано в narrative-v1
2. **Evidence summary** — что показал рисёрч (analogs + antilogs)
3. **Confidence change** — V1 score → V2 score
4. **Update type:**
   - **Validated** — данные подтверждают, формулировка остаётся
   - **Refinement** — данные уточняют, минорные правки
   - **Pivot** — данные противоречат, нужна другая формулировка
   - **Reset** — данных нет или они опровергают полностью, нужна новая гипотеза
5. **V2 hypothesis** — обновлённая формулировка (если изменилась)

---

## Шаг 3.2 — Risk scoring

**Формула:**
```
Risk Score = (10 - Evidence Score) × Failure Impact
```

**Evidence Score** — насколько сильно данные подтверждают dimension (1-10).

**Failure Impact** — насколько катастрофично если эта dimension окажется неверной (1-4).

**Failure Impact defaults:**

| Dimension | Default Impact | Почему |
|-----------|---------------|---------|
| Problem to Solve | 4 (Critical) | Если нет проблемы — нет продукта. Восстановить невозможно |
| Business Model | 4 (Critical) | Если экономика не сходится — компания умрёт. Восстановить тяжело |
| Target Audience | 3 (High) | Можно перепозиционировать, но дорого |
| Growth Strategy | 3 (High) | Можно поменять каналы, но потеряется время |
| Timing / Why Now | 3 (High) | Если опоздал — поздно. Если рано — нужна выдержка |
| Value Proposition | 2 (Medium) | Можно переписать messaging, итеративно |
| Competitive Advantage | 2 (Medium) | Moat строится годами, важен в долгую, но не убивает на старте |

**Defaults можно перекалибровать** для конкретного продукта если есть основания. Например, для regulated industry Feasibility важнее Audience (regulatory failure = смерть).

**Risk Score Table:**

| Dimension | Evidence Score (1-10) | Failure Impact (1-4) | Risk Score | Rank |
|-----------|----------------------|----------------------|------------|------|
| Problem to Solve | 7 | 4 | 12 | 3 |
| Target Audience | 4 | 3 | 18 | 1 |
| Value Proposition | 6 | 2 | 8 | 5 |
| Competitive Advantage | 5 | 2 | 10 | 4 |
| Growth Strategy | 5 | 3 | 15 | 2 |
| Business Model | 8 | 4 | 8 | 5 |
| Timing / Why Now | 7 | 3 | 9 | 6 |

(Пример, не реальные числа)

**Riskiest dimension** = highest risk score. Если несколько одинаковых — выбрать с большим failure impact.

---

## Шаг 3.3 — Cross-fit analysis

Две обязательные проверки на согласованность между dimensions:

### Channel-Model Fit

**Question:** работают ли growth channels с business model?

**Конфликты-примеры:**
- Enterprise sales + freemium pricing → невозможно (sales rep требует deal $20K+ для оправдания salary)
- Cold outreach + low-ACV product ($10/мес) → CAC выше LTV
- Viral / WOM + high-touch onboarding → виральный канал тащит unqualified leads, перегружает onboarding
- SEO + new-category product → нет search volume, потому что аудитория ещё не знает что искать
- Paid ads + low gross margin → CAC всегда обгоняет
- Product-led growth + complex enterprise sales cycle → разные миры

**Если конфликт найден:** записать → Stage 4 fix или возврат к Stage 1

### Model-Market Fit

**Question:** работает ли business model для этой target audience?

**Конфликты-примеры:**
- Subscription SaaS + малые e-commerce продавцы (не привыкли платить за софт ежемесячно)
- High pricing + студенты / молодые специалисты
- Marketplace take rate 15%+ + low-margin commodity goods
- Pay-per-use + аудитория которая хочет предсказуемый бюджет
- Annual contract + аудитория с 6-месячным runway
- Self-serve + аудитория без технической экспертизы (нужен sales support)

**Если конфликт найден:** аналогично — записать и принять решение.

---

## Шаг 3.4 — Update narrative V1 → V2

Создать `narrative-v2.md` на основе `narrative-v1.md` + изменения:

**Обязательные изменения в V2:**
- Дата обновлена
- Version: V2
- В Version History — секция «V2: After Market Research (date)» с changelog (что именно изменилось vs V1)
- Каждая dimension: обновлённая формулировка + новый confidence score
- Если update type = Pivot или Reset — явно отметить «PIVOTED» / «RESET» рядом с dimension
- Validation Status table обновлена: actual evidence (не пусто как в V1)
- Recommended next step: «Stage 4 (Validate) для риск-dimension: [name]» или «Stage 5 (Interviews)» если confidence уже высок

**НЕ перезаписывать narrative-v1.md.** V2 — отдельный файл. V1 остаётся для истории и сравнения.

---

## Шаг 3.5 — Создание risk-prioritization.md

По шаблону `references/template-risk-prioritization.md`. Должен содержать:

1. Метаданные (дата, narrative version)
2. Evidence sources (market research, optional expert notes)
3. Risk Scoring Table (формула + 7 строк)
4. Riskiest Dimension section (имя + объяснение)
5. Cross-Fit Analysis (Channel-Model, Model-Market)
6. Per-Dimension Analysis (V1 hypothesis → evidence → confidence change → update type → V2 hypothesis)
7. Recommended Next Steps (decision tree ниже)

---

## Шаг 3.6 — Decision tree (что делать после Stage 3)

| Условие | Recommended next |
|---------|------------------|
| Overall confidence > 7 + есть конкретная риск-dimension | Stage 4 (validate riskiest) или сразу Stage 5 (interviews) если уверенность в DVF assumptions есть |
| Overall confidence 5-7 | Stage 4 обязателен |
| Overall confidence < 5 | Возврат к Stage 1 (rethink) или Stage 2 (больше рисёрча) |
| Cross-fit конфликт обнаружен | Возврат к Stage 1 для пересмотра конфликтующих dimensions |
| Pivot/Reset на одной dimension | Локальный возврат: переформулировать эту dimension в V2, потом продолжать |
| Pivot/Reset на 2+ dimensions | Полный возврат к Stage 1 |

Записать рекомендацию в `risk-prioritization.md` и предложить пользователю.

---

## Quality gates Stage 3

- [ ] Все 7 dimensions имеют evidence score
- [ ] Все 7 dimensions имеют failure impact (default или скорректированный с обоснованием)
- [ ] Risk Score рассчитан для каждой
- [ ] Riskiest dimension явно идентифицирована
- [ ] Update type (Validated/Refinement/Pivot/Reset) указан для каждой
- [ ] Cross-Fit Analysis обе проверки сделаны (Channel-Model + Model-Market)
- [ ] Narrative V2 создан как отдельный файл (не перезапись V1)
- [ ] Version History в V2 содержит changelog
- [ ] Recommended next step соответствует decision tree

---

## Common pitfalls Stage 3

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Перезаписать V1 | narrative-v1.md теряется | V2 — отдельный файл |
| Не упасть в confidence когда данные противоречат | V2 confidence ≥ V1 для всех dimensions | Если данные противоречат — confidence ДОЛЖЕН упасть |
| Skip cross-fit analysis | Только risk scoring | Cross-fit обязателен — там часто прячутся фатальные конфликты |
| Default impact без обоснования | Просто скопировал | Если перекалибровал — объяснить почему |
| Riskiest = первая в списке | Без расчёта | Считать формулу для каждой и выбирать highest |
| Pivot всего сразу | «Все dimensions нужно переделать» | Скорее всего Reset на 2+ dimensions = сигнал что нужен Stage 1, а не локальные правки |
| Игнор confidence change | V1 → V2 без явных дельт | Каждая dimension должна показать confidence delta + причину |
