# Stage 2 — Market Research

**Цель:** найти аналоги (успешные компании которые валидируют ту или иную dimension вашей гипотезы) и антилоги (известные провалы из-за проблем с этой dimension) для каждой из 7 dimensions.

**Reads:** `narrative-v1.md`
**Writes:** `market-research.md`

---

## ⛔ Критичные правила Stage 2

1. **Никаких subagents.** Поиск делается прямыми вызовами `mcp__exa__web_search_exa` (приоритет) или `WebSearch` (fallback). В основной сессии. Memory rule: запрет агентов для контентных задач.

2. **Пользователь видит каждый поиск.** Не прятать процесс. Пользователь может вмешаться с уточнением, и это полезно.

3. **Можно разбить на 2 захода.** Если контекст переполняется или пользователь устал — запомнить где остановились и продолжить в следующей сессии. Это нормально для месячного цикла.

4. **Ключевое правило:** аналог = компания которая **успешно валидировала эту dimension в реальных условиях**. Не «тоже работает в этой нише», а «доказала что **именно эта dimension** работает».

---

## Шаг 2.1 — Прочитать narrative-v1

Из narrative-v1 извлечь:
- Тип продукта (для adaptive threshold)
- 7 dimensions с их формулировками
- Confidence-скоры (риск-dimensions исследовать тщательнее)
- Riskiest dimension (приоритет)

---

## Шаг 2.2 — Adaptive threshold

**Что считается аналогом** (revenue-floor):

| Тип рынка | Threshold |
|-----------|-----------|
| Mature SaaS / e-commerce / marketplace / fintech | $10M+ revenue ИЛИ 100K+ paying users |
| Emerging (AI, web3, новые категории) | $1M+ ARR ИЛИ 10K+ active users |
| Hardware | $5M+ revenue ИЛИ 50K+ units sold |

**Что считается антилогом:**
- Получил funding ($500K+) и закрылся
- Был известен (упоминания в TechCrunch, Crunchbase, профессиональных СМИ) и закрылся
- Pivot был публично объяснён через провал в этой конкретной dimension
- Acquihire после провала ≠ exit (это закрытие)

---

## Шаг 2.3 — Search strategies на 7 dimensions

Для каждой dimension — конкретные query-стратегии. Делать 2-3 поиска на dimension.

### Dimension 1: Problem to Solve

**Что ищем:**
- Компании которые решили **тот же класс проблемы** (не обязательно в той же нише) и преуспели
- Компании которые попытались решить эту проблему, но провалились

**Search queries (примеры):**
- `"[problem class]" startup raised funding acquired`
- `"[problem class]" YC company unicorn`
- `"[problem class]" startup shutdown failed reasons`
- Exa semantic: «companies that solved [vivid problem description]»

**Что записать:**
- Аналог: компания + revenue/users + год founded + что именно валидировало эту dimension
- Антилог: компания + funding raised + причина провала (документированная)

### Dimension 2: Target Audience

**Что ищем:**
- Компании которые успешно построили продукт для **той же демографии/поведенческой группы**
- Компании которые промахнулись с аудиторией (broad vs narrow, wrong segment)

**Search queries:**
- `"[audience description]" SaaS market size`
- `"[audience description]" startup CAC payback`
- `"[audience description]" startup pivot wrong target`
- Exa: «companies that successfully serve [specific audience]»

**Что записать:**
- Аналог: компания + аудитория + retention/CAC если известны
- Антилог: компания + почему промахнулись с аудиторией

### Dimension 3: Value Proposition

**Что ищем:**
- Компании с **похожей структурой value prop** (tagline + benefits structure)
- Компании которые провалились из-за невнятного value prop или features-focused messaging

**Search queries:**
- `"[main benefit]" SaaS positioning success`
- `"[similar value prop]" startup growth trajectory`
- `startup failure feature creep no clear value prop`

**Что записать:**
- Аналог: компания + tagline + почему value prop работает
- Антилог: компания + чем value prop был размытым

### Dimension 4: Competitive Advantage

**Что ищем:**
- Компании которые построили моат на **той же из 7 Powers**
- Компании которые думали что у них есть Power, но её не оказалось

**Search queries:**
- `"[power name]" startup moat success [industry]`
- `"network effects" SaaS company growth`
- `"first mover advantage" startup failed lost market`
- `"counter-positioning" startup incumbent unable to copy`

**Что записать:**
- Аналог: компания + какая Power + как именно компаундинг работает
- Антилог: компания + ложная Power + что её не защитило

### Dimension 5: Growth Strategy

**Что ищем:**
- Компании с похожей growth-стратегией (короткий + длинный срок)
- Компании которые провалились из-за **неработающего growth channel**

**Search queries:**
- `"[channel name]" SaaS startup first 1000 users`
- `"product-led growth" startup playbook examples`
- `"paid acquisition" startup CAC too high failed`
- `"viral coefficient" startup growth examples`

**Что записать:**
- Аналог: компания + конкретный канал + цифры (CAC, viral coefficient, conversion)
- Антилог: компания + канал который не сработал + почему

### Dimension 6: Business Model

**Что ищем:**
- Компании с похожей моделью монетизации в той же категории
- Компании которые провалились из-за business model (несовпадение pricing/audience/cost)

**Search queries:**
- `"[pricing model]" SaaS company unit economics`
- `"freemium" startup conversion rate examples`
- `"marketplace take rate" successful examples`
- `startup failed unit economics LTV CAC`

**Что записать:**
- Аналог: компания + конкретные числа (LTV, CAC, payback, gross margin)
- Антилог: компания + почему числа не сходились

### Dimension 7: Timing / Why Now

**Что ищем:**
- Компании которые попали в окно technology/behavior/regulation shift
- Компании которые опоздали или пришли слишком рано

**Search queries:**
- `"[triggering event]" startup founded year`
- `"first to market" startup failed too early`
- `"perfect timing" startup case study`
- `Bill Gross "single biggest reason" timing`
- Exa: «companies that succeeded because of timing [shift description]»

**Что записать:**
- Аналог: компания + какой shift + почему именно тогда (а не раньше)
- Антилог: компания + почему опоздала или пришла рано

---

## Шаг 2.4 — Запись в market-research.md

После каждой dimension сразу записывать в `market-research.md` (создать в начале Stage 2 по шаблону `references/template-market-research.md`). Не накапливать в памяти.

Структура per-dimension в market-research.md:

```markdown
### Dimension N: [Название]

**Analogs:**
1. **[Company]** — [revenue/users] — founded [year]
   - **Что валидирует:** [конкретный аспект этой dimension]
   - **Evidence:** [что мы знаем — ссылка / цитата]
   - **Relevance:** [насколько применимо к нашему контексту 1-5]

2. ...

**Antilogs:**
1. **[Company]** — raised [amount] — closed [year]
   - **Failure mode:** [как именно провалились в этой dimension]
   - **Evidence:** [источник / цитата]
   - **Lesson:** [что из этого полезно нам]

**Patterns observed:** [что повторяется среди аналогов]
**Counter-patterns:** [что повторяется среди антилогов]

**Confidence change:** [V1 score] → [updated score]
**Status:** Validated / Needs more research / At risk
```

---

## Шаг 2.5 — Cross-dimension themes

После всех 7 dimensions — выделить паттерны которые **спанят несколько dimensions**:

- Аналоги которые валидируют 3+ dimensions одновременно (это «similar deals» — наиболее ценные референсы)
- Антилоги где провал в одной dimension потащил другие (это показывает sequencing рисков)
- Несовместимость между dimensions у конкурентов (это намёки на competitive gap для нас)

Записать в секцию `## Cross-Dimension Themes` в market-research.md.

---

## Шаг 2.6 — Risk prioritization (preview)

Не делать полный risk scoring (это Stage 3) — но в конце market-research.md дать preview:

```markdown
## Preview: dimensions at risk after research

| Dimension | V1 Confidence | Post-research Confidence | Status |
|-----------|---------------|--------------------------|--------|
| ...       | ...           | ...                      | ...    |

**Riskiest after research:** [name]
**Recommended next:** Stage 3 (Synthesis) для полного risk scoring
```

---

## Quality gates Stage 2

- [ ] Все 7 dimensions исследованы
- [ ] На каждую dimension минимум 3 аналога и 2 антилога (или явно отмечено что их нет)
- [ ] Аналоги соответствуют threshold (не «стартап с 10 пользователями»)
- [ ] Антилоги документированы (не слухи)
- [ ] Confidence обновлён для каждой dimension
- [ ] Cross-dimension themes выделены
- [ ] Sources cited (не голословные утверждения)
- [ ] Контекст-aware: 2010 analog ≠ 2026 market — отмечено где это релевантно

---

## Common pitfalls Stage 2

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Аналог не валидирует именно эту dimension | «Это похожий продукт» | Сформулировать конкретно: какую dimension эта компания доказывает |
| Антилог = слухи | «Я слышал что они закрылись» | Найти подтверждение (статья, Crunchbase, объявление) |
| Игнорирование antilogs | Только success stories | Антилоги ценнее: они показывают где грабли |
| Контекст не учтён | «Facebook сделал так в 2007» | Отметить: что было правдой в 2007 ≠ сейчас |
| Cherry-picking | Только то что подтверждает гипотезу | Искать антилоги с тем же усердием что и аналоги |
| Поиск в одном источнике | Только Crunchbase | Diversify: TechCrunch, ProductHunt, IndieHackers, Twitter, Reddit |
| Запуск агента «сделай рисёрч за меня» | Агент пишет содержательное | Поиск в основной сессии. Каждый запрос — пользователь видит |
| Не записывать сразу | Накапливать всё в памяти, потом писать | Записывать после каждой dimension. Иначе потеряется |
