# Stage 7 — Interview Synthesis

**Цель:** прочитать все заметки интервью, извлечь паттерны по каждой dimension, обновить confidence-скоры, эволюционировать narrative до V3.

**Reads:** `narrative-v2.md`, `interviews/notes/*.md`
**Writes:** `interview-synthesis.md`, `narrative-v3.md`

---

## ⛔ Правило изоляции (по образцу analyze-llm)

**Читать заметки по одной**, не пакетно. Между чтением заметок не смешивать данные. Это предотвращает «усреднение» паттернов и сохраняет конкретику.

Технически:
1. Прочитать все имена файлов в `interviews/notes/` (только список)
2. Для каждой заметки: открыть → извлечь паттерны → закрыть → перейти к следующей
3. **После** обработки всех заметок — синтез

Это похоже на правило в analyze-llm, но менее строгое (там вообще нельзя смотреть на других — здесь можно после обработки одной).

---

## Шаг 7.1 — Прочитать narrative V2 и assumptions-map

Контекст для синтеза:
- Из `narrative-v2.md` — текущие гипотезы по dimensions + V2 confidence
- Из `assumptions-map.md` — какие assumptions из Critical quadrant мы хотели валидировать
- Из `interview-guide.md` — coverage matrix (вопросы → assumptions)

---

## Шаг 7.2 — Per-interview extraction

Для каждой заметки в `interviews/notes/`:

1. **Прочитать одну заметку целиком** (не пропуская)
2. **Извлечь:**
   - Контекст респондента (1-2 предложения)
   - Признаки того что respondent typical / atypical для target
   - Quotes verbatim — не пересказ
   - Observations per dimension (только релевантные dimensions)
   - Surprises (то что неожиданно)
   - Quantitative signals (числа: время, деньги, частота)
3. **Записать в промежуточную таблицу** (в памяти или в черновике):

```markdown
| Resp ID | Dim 1 finding | Dim 2 finding | Surprise | Quant |
|---------|--------------|---------------|----------|-------|
| R001 | ... | ... | ... | ... |
```

4. **Закрыть заметку**, перейти к следующей

После всех заметок — переходить к синтезу.

---

## Шаг 7.3 — Pattern extraction per dimension

Для каждой dimension которую покрывали интервью:

1. **Pattern** — что в среднем говорят? (1-2 предложения)
2. **Supporting evidence** — N из M респондентов подтверждают (например «12 из 15»)
3. **Strength of pattern:**
   - **Strong** — 80%+ респондентов подтверждают, нет значимых противоречий
   - **Medium** — 50-80% подтверждают, есть нюансы
   - **Weak** — <50% или сильно разделены
4. **Key quotes** — 2-3 verbatim цитат лучших, с указанием respondent ID
5. **Confidence change:** V2 score → post-interview score
6. **Update type:** Validated / Refinement / Pivot / Reset

**Правило:** N supporting != true даже если 15 из 15. Если все 15 — близкие друзья founder'а и неподходящая аудитория — это не pattern, это echo chamber. Учитывать качество respondents, не только количество.

---

## Шаг 7.4 — Cross-dimensional insights

Паттерны спанящие несколько dimensions. Примеры:

- «Респонденты которые сильно жалуются на Problem (D1) — это те же кто **уже платит** за конкуренты (Business Model V validated). Те кто не жалуется — не платят. Это означает что **аудитория = paying customers**, а не general market.» (cross: Audience + Problem + Business Model)

- «Чем выше confidence в Value Proposition, тем меньше внимания к pricing. Респонденты которые видят value — спрашивают как купить, не сколько стоит.» (cross: Value Prop + Business Model)

- «Pattern timing: 11 из 15 респондентов начали искать решение последние 6 месяцев — после конкретного события (новый закон / новая модель GPT / новая платформа). Это validates Why Now с конкретной датой.» (cross: Timing + Problem)

Записать в отдельную секцию `## Cross-Dimensional Insights` в interview-synthesis.md.

---

## Шаг 7.5 — Surprises

Находки которые **противоречат** гипотезе или открывают новый угол. Это часто самое ценное из интервью.

**Типы surprises:**
- **Wrong assumption:** «Думали Y, оказалось X»
- **New segment:** «Появилась новая аудитория про которую мы не думали»
- **Hidden friction:** «Pain point про который мы не знали»
- **Workaround:** «Они уже решают это X-способом, который мы не учитывали»
- **Unexpected use case:** «Они хотят использовать это для Z, не для того что мы делали»

Записать каждый surprise + от какого respondent + что это значит для гипотезы.

---

## Шаг 7.6 — Updated Risk Assessment

Сравнить confidence до и после интервью:

```markdown
| Dimension | Pre-Interview | Post-Interview | Change | Status |
|-----------|---------------|----------------|--------|--------|
| Problem to Solve | 6 | 8 | +2 | Validated |
| Target Audience | 5 | 4 | -1 | Refined (segment narrowed) |
| Value Proposition | 5 | 7 | +2 | Validated |
| Competitive Advantage | 5 | 5 | 0 | Unchanged |
| Growth Strategy | 4 | 3 | -1 | At risk |
| Business Model | 6 | 8 | +2 | Validated |
| Timing / Why Now | 7 | 9 | +2 | Validated |
```

**Loop detection:** если confidence упала для какой-то dimension в V3 vs V2 → флаг + рекомендация:
- Drop для риск-dimension которую валидировали → возврат к Stage 4 (новые assumptions) или Stage 1 (rethink)
- Drop для не-критичной dimension → возможно, можно продолжать с пониженной оценкой
- Drop для нескольких dimensions → возврат к Stage 1, проверить гипотезу целиком

---

## Шаг 7.7 — Update narrative V2 → V3

Создать `narrative-v3.md`:
- Дата обновлена, version V3
- Version History: «V3: After Field Interviews (date)» с changelog
- Каждая dimension: новая формулировка (если изменилась) + post-interview confidence
- Если есть **new segment** или **wrong assumption** — явно отметить
- Validation Status table обновлена evidence-data из интервью
- Recommended next step (decision tree ниже)

**НЕ перезаписывать V2.** V3 — отдельный файл.

---

## Шаг 7.8 — Decision tree после Stage 7

| Условие | Recommended next |
|---------|------------------|
| Все ключевые assumptions validated, confidence высок (avg >7) | Stage 8 (запуск MVP) |
| Confidence повысился, но риск-dimension всё ещё weak | Stage 4 для другой риск-dimension или больше интервью с другим segment |
| Confidence упал в какой-то dimension | Stage 4 (новые assumptions) или Stage 1 (rethink dimension) |
| Появилась новая риск-dimension которую не валидировали | Stage 4 для неё |
| Wrong assumption на critical dimension | Stage 1 (pivot этой dimension) |
| Wrong assumption на 2+ critical dimensions | Stage 1 (полный rethink hypothesis, возможно reset) |

Записать в `interview-synthesis.md` и в narrative-v3.md.

---

## Шаг 7.9 — Создание interview-synthesis.md

По шаблону `references/template-interview-synthesis.md`. Должен содержать:

1. Метаданные (дата, count interviews, narrative version V2 → V3)
2. Summary (one-sentence key finding + overall confidence change)
3. Per-Dimension Patterns (1-7 секций, каждая с pattern + evidence + quotes + confidence change)
4. Cross-Dimensional Insights
5. Surprises
6. Updated Risk Assessment table
7. Loop detection notes
8. Recommended next steps

---

## Quality gates Stage 7

- [ ] Все заметки прочитаны (изоляция: по одной)
- [ ] Per-dimension patterns с supporting evidence count
- [ ] Strength of pattern (strong/medium/weak) для каждой
- [ ] Key quotes verbatim, с respondent ID
- [ ] Cross-dimensional insights отдельной секцией
- [ ] Surprises явно перечислены
- [ ] Updated Risk Assessment table заполнена
- [ ] Confidence delta для каждой dimension рассчитана
- [ ] Loop detection: если есть drops — флаг
- [ ] narrative-v3.md создан как отдельный файл
- [ ] Recommended next step соответствует decision tree

---

## Common pitfalls Stage 7

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Чтение заметок пакетно | Все 15 в один контекст | По одной — изоляция |
| Усреднение паттернов | «В среднем говорят...» | Конкретные числа: N из M, key quotes |
| Игнор surprises | Только то что вписывается | Surprises = самое ценное, отдельная секция |
| Echo chamber pattern | 15 из 15 = strong, но все знакомые | Учитывать качество respondents |
| Отсутствие confidence drops | Все confidence только растут | Если данные противоречат — drop обязателен |
| Цитаты переписаны | «Респонденты в целом сказали что...» | Verbatim в кавычках |
| Pivot всего | Reset на 2+ dimensions подряд | Возврат к Stage 1 целиком, не локальные правки |
| narrative V3 = narrative V2 | Confidence обновлены, формулировки нет | Если pattern strong → формулировка должна обновиться (refinement) |
