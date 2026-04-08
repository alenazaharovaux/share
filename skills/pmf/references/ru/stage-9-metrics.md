# Stage 9 — Metrics

**Цель:** настроить пост-launch измерение PMF через 3 инструмента: Sean Ellis 40% survey, retention cohorts, First Round Levels of PMF.

**Reads:** `narrative-v3.md`
**Writes:** `metrics-dashboard.md`

---

## ⛔ Критичные правила Stage 9

1. **Скилл НЕ собирает данные.** Он создаёт template + инструкции по сбору. Сбор делает пользователь (минимум 40 ответов на Sean Ellis занимает недели).

2. **Sean Ellis распространять только на active users**, не на newsletter list. Active = реально использовали продукт ≥1 раз за последние 2 недели.

3. **Минимум 40 ответов на Sean Ellis.** Меньше — статистически бессмысленно.

4. **Retention анализировать когортами**, не общим средним. Общее среднее скрывает падение retention со временем.

5. **Использовать 3 инструмента вместе**, не один. Sean Ellis + retention + Levels — каждый освещает разный аспект.

---

## Шаг 9.1 — Прочитать narrative V3

Из narrative-v3.md извлечь:
- Final hypothesis (V3) — что будем измерять
- Target audience definition — кому распространять Sean Ellis
- Value proposition — для интерпретации Sean Ellis ответов
- Это нужно чтобы убедиться что метрики измеряют то что валидируем

---

## Шаг 9.2 — Sean Ellis Survey setup

**Полные инструкции:** `references/methodology.md` секция «Sean Ellis Survey».

**Quick reference:**

**Вопрос (точная формулировка):**
> «Как бы вы себя чувствовали, если бы больше не могли использовать [продукт]?»

**Варианты ответа:**
1. Очень разочарован (Very disappointed)
2. Несколько разочарован (Somewhat disappointed)
3. Не разочарован — это не очень полезно (Not disappointed)
4. Я больше не использую [продукт] (N/A)

**Threshold:** ≥40% выбравших «Очень разочарован» (исключая N/A) = есть PMF.

**Дистрибуция:**
- Только active users
- В контексте использования (in-product modal, email после ключевого действия)
- Не reminder massive blast

**Дополнительные вопросы (опциональные но желательные):**
- «Кому бы этот продукт больше всего пригодился?» (помогает уточнить target)
- «Какой главный benefit вы получаете?» (помогает уточнить value prop)
- «Что нужно улучшить?» (помогает приоритизировать roadmap)

**Минимум:** 40 ответов. Желательно 100+.

---

## Шаг 9.3 — Retention Cohorts setup

**Полные инструкции:** `references/methodology.md` секция «Retention Cohorts».

**Quick reference:**

**Что собирать:**
- Каждый user — дата first action + дата каждой следующей сессии (или ключевого действия)
- Cohort = пользователи зарегистрировавшиеся в одной неделе
- Track какой % cohort вернулся в неделю 2, 3, 4, 5, 8, 12

**Cohort table format:**

| Cohort | Week 1 | Week 2 | Week 3 | Week 4 | Week 8 | Week 12 |
|--------|--------|--------|--------|--------|--------|---------|
| Jan W1 | 100% | 60% | 50% | 45% | 42% | 40% |
| Jan W2 | 100% | 65% | 55% | 50% | 47% | 45% |
| ... | | | | | | |

**PMF signal:**
- **Healthy retention:** кривая выравнивается (flatten) на каком-то %, не падает к нулю
- **Unhealthy retention:** кривая монотонно падает, не stabilize
- **Strong PMF:** flatten на >40% для consumer / >60% для B2B / >25% для high-frequency

**Что определяет «active»:**
- B2B SaaS: ≥1 ключевое действие в неделю
- Consumer: ≥1 session в неделю или ≥3 в месяц
- High-frequency (соцсети, чаты): ≥1 в день или ≥3 в неделю
- Зависит от ожидаемой частоты использования

---

## Шаг 9.4 — First Round Levels of PMF

**Полные инструкции:** `references/methodology.md` секция «Levels of PMF».

**Quick reference (4 уровня):**

| Level | Name | Signals |
|-------|------|---------|
| 1 | **Nascent** | Несколько early adopters, manual everything, no clear retention signal yet |
| 2 | **Developing** | Есть некоторые сигналы (Sean Ellis 25-40%, retention partially flatten, 1-2 word-of-mouth referrals/week), но не устойчивые |
| 3 | **Strong** | Sean Ellis ≥40%, retention flatten на здоровом уровне, organic WOM growth, customers cannot live without |
| 4 | **Extreme** | Нелинейный рост, ажиотаж, customers евангелизируют без подсказки, supply не успевает за demand |

**Каждый уровень определяется по 3 signals:**
- **Satisfaction** — Sean Ellis %, NPS, retention rate
- **Demand** — growth rate (organic), waitlist если есть, conversion rate
- **Efficiency** — CAC payback, LTV/CAC ratio, support load

**Записать в metrics-dashboard.md:** какой уровень сейчас, что нужно для следующего, evidence для каждого signal.

---

## Шаг 9.5 — Создать metrics-dashboard.md

По шаблону `references/templates.md` секция «Metrics Dashboard».

Структура:
1. Метаданные (дата, narrative version V3+)
2. **Sean Ellis Survey:**
   - Текст вопроса (готовый для копирования в форму)
   - Инструкции по дистрибуции
   - Таблица результатов (заполняется пользователем)
   - Калькуляция % Very disappointed
   - Interpretation
3. **Retention Cohorts:**
   - Definition of «active» для этого продукта
   - Cohort table template (5-10 строк)
   - Чем заполнять (где брать данные)
   - Interpretation guide (flatten / fall)
4. **Levels of PMF Assessment:**
   - 4 строки (по уровню) с критериями + checkbox + evidence
   - Финальный assigned level
5. **Recommended next** (decision tree из stage-10):
   - PMF achieved → scale
   - Promising signals → iterate (Stage 4 или Stage 7)
   - Weak signals → rethink (Stage 1)

---

## Шаг 9.6 — Flow

**Не one-shot.** Stage 9 разворачивается во времени:

1. **Setup phase** (1 сессия со скиллом): создать metrics-dashboard.md template + инструкции
2. **Collection phase** (4-12 недель, без скилла): пользователь собирает данные сам
3. **Interpretation phase** (1 сессия со скиллом): пользователь возвращается с заполненным metrics-dashboard, скилл интерпретирует и рекомендует Stage 10

При возобновлении Stage 9: проверить заполнен ли metrics-dashboard.md (есть ли числа а не плейсхолдеры). Если нет — продолжаем ждать. Если да — переход к интерпретации.

---

## Quality gates Stage 9

- [ ] Sean Ellis вопрос в формулировке Sean Ellis (не переписан)
- [ ] Дистрибуция явно ограничена active users
- [ ] Минимум 40 ответов прописан как требование
- [ ] Cohort table структура правильная (cohort × weeks)
- [ ] «Active» definition подходит для типа продукта
- [ ] Levels of PMF — 4 строки с конкретными signals
- [ ] Decision tree связывает результаты с Stage 10
- [ ] Skill НЕ симулирует и НЕ выдумывает данные сам

---

## Common pitfalls Stage 9

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Sean Ellis на newsletter list | 5% Very disappointed | Дистрибуция только active users |
| <40 ответов | «У нас 12 ответов, всё ок» | Подождать. <40 = шум |
| Переписать Sean Ellis вопрос | «Какова вероятность что вы порекомендуете...» | Это NPS, не Sean Ellis. Использовать оригинальную формулировку |
| Общий retention rate | «У нас 50% retention» | Когортно. 50% — это среднее за месяц или за всё время? |
| Только Sean Ellis без retention | 45% Very disappointed = «есть PMF» | Sean Ellis fooled by selection bias. Retention cohort обязателен |
| «Мы на Level 3» без evidence | Wishful thinking | Каждый уровень требует evidence на 3 signals |
| Ranking пользователей по revenue для Sean Ellis | «Мы спросили top 10%» | Дистрибуция random sample active users, не cherry-picked |
| Retention 7 дней vs 30 дней путаница | «Retention 80%» (за день) | Указать window: D1, D7, D30, W4, M3 |
| Скилл генерирует фальшивые данные | «Допустим Sean Ellis 47%» | Скилл создаёт template, не данные. Данные — от пользователя |
