# Template — Interview Synthesis

**Используется в:** Stage 7 (Interview Synthesis)
**Сохранять в:** `interview-synthesis.md` + `narrative-v3.md` (обновлённый narrative)
**Сопутствующий guide:** `references/stage-7-interview-synthesis.md`

**Назначение:** свести findings из 15+ интервью в patterns, surprises, обновлённую формулировку narrative и обновлённую риск-карту.

---

## ⛔ Правила синтеза

1. **Изоляция чтения по одной заметке.** Не загружать все интервью одновременно — паттерны искажаются. Читать по одной, выписывать citations + observations, потом сводить.
2. **Минимум 15 интервью.** Меньше = отдельные мнения, не паттерны.
3. **Pattern = ≥3 респондента сказали что-то похожее.** Меньше — это outlier, отметить как surprise.
4. **Surprises обязательны.** Если синтез не нашёл ничего неожиданного, это значит вы услышали то, что хотели услышать. Перечитать.
5. **Loop detection:** если паттерны полностью совпадают с V2 narrative — interviews ничего не дали, проверить leading questions.

---

## Шаблон

```markdown
# Interview Synthesis — [Product name]

**Date:** YYYY-MM-DD
**Reads:** все интервью из `interviews/notes/*.md`
**Writes:** этот файл + `narrative-v3.md`
**Number of interviews:** [N]
**Date range:** [first] – [last]

---

## Coverage

| Segment | Planned | Actual | Notes |
|---------|---------|--------|-------|
| Primary segment | 12-15 | [N] | |
| Adjacent segment 1 | 3-5 | [N] | |
| Adjacent segment 2 | 3-5 | [N] | |
| Non-target (control) | 2-3 | [N] | |
| **TOTAL** | 20-28 | [N] | |

**Минимум met?** [yes/no — если <15 общее, синтез слабый]

---

## Patterns

Каждый pattern должен:
- Появиться у ≥3 респондентов
- Иметь конкретные quotes (не пересказ)
- Быть привязан к dimension(s)

### Pattern 1: [короткое название]

**Dimension(s):** [Customer / Problem / Solution / Distribution / Business model]

**Description:**
[1-2 параграфа: что именно общего нашли]

**Quotes (минимум 3):**
- «[verbatim quote]» — [respondent ID, segment]
- «[verbatim quote]» — [respondent ID, segment]
- «[verbatim quote]» — [respondent ID, segment]

**Frequency:** [сколько респондентов из N]

**Strength:** [Strong / Moderate / Weak]
- Strong: 7+ из 15 чётко артикулировали это
- Moderate: 4-6 артикулировали
- Weak: 3 артикулировали + ещё несколько косвенно

**Implication for narrative:**
[Как этот pattern меняет narrative-v2 → v3]

---

### Pattern 2: [...]

[Та же структура]

---

### Pattern 3-N: [...]

[Минимум 3 паттерна, обычно 5-8]

---

## Surprises

Surprises — неожиданные находки которые не были в narrative-v2.

### Surprise 1: [короткое название]

**What was unexpected:**
[Что не предполагали]

**Where it appeared:**
- «[quote]» — [respondent ID]
- «[quote]» — [respondent ID]

**Why it matters:**
[Implication для narrative или для risk map]

**Confidence:**
[Strong / Moderate / Weak — сколько респондентов поддерживают этот surprise]

---

### Surprise 2-N: [...]

**Минимум 2 surprises.** Если меньше — leading questions и/или confirmation bias. Перечитать заметки.

---

## Anti-patterns / disconfirmed assumptions

Что мы предполагали в narrative-v2, но интервью НЕ подтвердили:

| Assumption (V2) | What interviews showed | Action |
|-----------------|----------------------|--------|
| [например: «target users тратят 4-6 часов»] | «На самом деле 1-2 часа» | Пересмотреть problem severity |
| | | |

---

## Persona refinement

После 15+ интервью персона должна стать конкретнее.

**V2 persona:** [как было]
**V3 persona:** [как стало после интервью]

**New persona divides:**
- ✗ [новая категория исключения, выявленная в интервью]

**Different sub-segments inside primary segment:**
[Если интервью показали что внутри сегмента есть 2-3 разные группы с разными needs — описать]

---

## Updated risk map

| Dimension | V2 risk score | V3 risk score | Why changed |
|-----------|---------------|---------------|-------------|
| 1. Customer | [X] | [Y] | [interviews подтвердили / опровергли / уточнили] |
| 2. Problem | | | |
| 3. Why now | | | |
| 4. Why us | | | |
| 5. Solution | | | |
| 6. Distribution | | | |
| 7. Business model | | | |
| 8. Power | | | |

**New riskiest dimension (для следующего цикла):** [имя]

---

## Recommendations for narrative-v3

**What to rewrite:**
- Customer section: [conкретно что менять]
- Problem section: [...]
- Solution section: [...]

**New visceral quotes to include:**
- «[quote]» — для Problem section
- «[quote]» — для Solution section

**What to remove:**
- [feature/claim/assumption который интервью не поддержали]

---

## Decision tree (что делать дальше)

```
IF patterns mostly confirm V2 narrative AND ≥3 surprises found:
  → Strong validation. Write narrative-v3 with refinements. Move to Stage 8 (MVP).
  
IF patterns mostly confirm BUT 0-1 surprises:
  → Suspicion of confirmation bias. Re-read interviews with fresh eyes OR run 5 more with different recruiter.
  
IF patterns disconfirm V2 in 2-3 dimensions:
  → Significant pivot needed. Rewrite narrative-v3 with major changes. Return to Stage 3 (synthesis) with new risk map.
  
IF patterns disconfirm V2 in 4+ dimensions:
  → Hypothesis broken. Return to Stage 1 (Hypothesis) with learnings.
```
```

---

## Common mistakes

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Загрузка всех интервью одновременно | Patterns кажутся очевидными сразу | Изоляция: одна заметка → выписать → следующая |
| Pattern на 1-2 респондентах | «У нас уже 5 паттернов после 5 интервью» | ≥3 респондентов на pattern, минимум 15 интервью |
| 0 surprises | Wishful thinking | Перечитать с фокусом на «что не вписывается» |
| Pattern = пересказ команды | «Мы знали что они скажут это» | Использовать verbatim quotes, не парафраз |
| Игнор adjacent segments | Только primary | Adjacent дают persona divides |
| Skip risk map update | Старый risk map после новых данных | Обязательно обновить scores |
