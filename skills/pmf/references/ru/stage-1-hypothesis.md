# Stage 1 — Hypothesis

**Цель:** превратить идею продукта в структурированную гипотезу по 7 PMF dimensions с честными confidence-скорами 1-10 для каждой и явной идентификацией риск-dimension.

**Reads:** `00_setup.md`
**Writes:** `narrative-v1.md`

---

## Шаг 1.1 — Прочитать setup

Из `00_setup.md` извлечь:
- Имя продукта
- Тип (B2C SaaS / B2B SaaS / Marketplace / DTC / Services / Internal / Other)
- Контекст организации (Zero-to-one / Established / Extension)
- Результаты Team Pre-Flight Check (3 ответа + risk flag)

Это влияет на дальнейший флоу Stage 1:
- B2B → multi-role handling (Decision Makers vs End Users)
- Marketplace → multi-role handling (Demand vs Supply)
- Established → переиспользование существующих каналов и аудиторий
- Zero-to-one → больше внимания к Timing (Why Now)

**Pre-flight результаты НЕ перепроводить** — они уже собраны в Stage 0 (`references/stage-0-setup.md`). Здесь только прочитать и учесть. Если `00_setup.md` отсутствует или Pre-Flight в нём не заполнен — вернуться к Stage 0, не пытаться домыслить.

---

## Шаг 1.2 — Перенос Pre-Flight в narrative

Pre-Flight результаты из `00_setup.md` будут включены в `narrative-v1.md` отдельной секцией (см. Шаг 1.6 — Document Generation, секция «Team Pre-Flight Check»). Они должны быть видимыми на всех последующих стадиях, поэтому не остаются только в setup-файле.

**Технически:** при сборке narrative скопировать секцию Team Pre-Flight Check из `00_setup.md` в narrative как есть. Если risk flag = Высокий — добавить в начало narrative явный warning блок «Team risk: высокий — учитывать при интерпретации dimensions ниже».

---

## Шаг 1.3 — Работа с 7 dimensions

Идти последовательно. На каждой dimension:
1. Показать «что хорошо выглядит» (примеры из `references/7-dimensions.md`)
2. Задать guided questions
3. Применить validation rules
4. Записать в narrative
5. Confidence 1-10

### 1.3.1 — Problem to Solve

**Outcome-Motivation Gap framework** — 3 вопроса:
1. **Что пользователи пытаются достичь?** (desired outcome — конкретный результат, не абстракция)
2. **Почему они этого хотят?** (motivation — что стоит за желанием)
3. **Почему они не могут это сделать сейчас?** (gap — что мешает; это и есть problem)

**Validation rules:**
- ⛔ Problem не должна упоминать ваш продукт или его features
- ⛔ Problem не «нет [нашего продукта]»
- ✅ Problem framed как obstacle, не как absence
- ✅ Конкретность: можно представить одного человека в этой ситуации

**Пример хорошо:** «Маленькие e-commerce продавцы тратят 4-6 часов в неделю на перенос заказов из 5 разных каналов в учётную систему вручную, потому что готовые интеграции существуют только для крупных игроков, а кодить их сами они не умеют»

**Пример плохо:** «Нет хорошего инструмента для синхронизации каналов продаж»

### 1.3.2 — Target Audience

**Вопросы:**
1. Defining attributes (2-3): что отличает эту аудиторию от соседних? Атрибут + конкретное значение.
2. **Now segment:** кто страдает прямо сейчас, готов платить, легко достижим?
3. **Future segments:** куда будете расширяться через 1-3 года?
4. Почему именно эта аудитория? Как она резонирует с другими dimensions (особенно value prop и growth)?

**Validation rules:**
- ⛔ Не «все женщины 25-45», не «все стартапы»
- ⛔ Defining attribute не «возраст» (это demographic, не behavior)
- ✅ Attribute = действие, ситуация, или болевая точка («продавцы 5+ каналов», «исследователи проводящие 10+ интервью в месяц»)
- ✅ Now segment явно отделён от Future

**Пример хорошо:**
- Now: продавцы 100-1000 заказов/мес из 3+ каналов одновременно (Wildberries + Ozon + свой сайт), оборот $5K-50K/мес, без штатного программиста
- Future 1: продавцы 10-100 заказов/мес (легче, но беднее)
- Future 2: enterprise 1000+ заказов/мес (тяжелее, но богаче, нужна интеграция с 1С)

### 1.3.3 — Value Proposition

**Ideal Homepage Approach:**
1. **Tagline** — одно предложение, **benefit-focused**, не feature-focused
2. **Sub-benefits** — 3-5 штук, тоже benefits

**Validation rules:**
- ⛔ Features («интеграции с 5 маркетплейсами»)
- ⛔ Generic («лучше, быстрее, дешевле»)
- ✅ Benefits («перестаёшь терять заказы из-за ручного переноса»)
- ✅ Specific («4-6 часов в неделю обратно у тебя»)

**Пример хорошо:**
- Tagline: «Все ваши заказы из всех маркетплейсов в одной таблице — без программиста и без ручного труда»
- Sub-benefits:
  1. Никаких пропущенных заказов из-за переключения вкладок
  2. Освобождается 4-6 часов в неделю
  3. Готовый отчёт для бухгалтера в один клик
  4. Работает с Wildberries, Ozon, Я.Маркет, AliExpress, своим сайтом
  5. Никакого кода — настройка за 15 минут

### 1.3.4 — Competitive Advantage

**Долгосрочный moat:** один из 7 Powers (Helmer). Полное описание — `references/7-powers.md`.

Краткий список:
1. **Scale Economies** — себестоимость падает с ростом
2. **Network Economies** — ценность для пользователя растёт с количеством других пользователей
3. **Counter-Positioning** — позиция которую incumbents не могут скопировать без угрозы своему бизнесу
4. **Switching Costs** — пользователю дорого/сложно уйти к конкуренту
5. **Branding** — пользователи готовы платить премию за бренд
6. **Cornered Resource** — эксклюзивный доступ к ключевому ресурсу
7. **Process Power** — операционное превосходство которое сложно скопировать

**Вопросы:**
1. Какая из 7 Powers будет вашим долгосрочным moat?
2. Почему именно эта Power будет работать в вашем контексте?
3. Что вам нужно сделать чтобы её построить?

**Plus краткий competitive landscape:**
- **Direct competitors:** кто делает то же самое для той же аудитории
- **Indirect competitors:** кто решает ту же проблему другим способом
- **Underserved segments:** где конкуренты недостаточно покрывают рынок

**Validation:**
- ⛔ «У нас лучшая команда» — не Power
- ⛔ «Мы первые» — не Power (first-mover advantage редко устойчив)
- ⛔ «У нас уникальная технология» — не Power, если нет patent moat или process advantage
- ✅ Конкретный механизм компаундинга

### 1.3.5 — Growth Strategy

**Два горизонта:**

**Short-term traction** — как получить первых 1K пользователей / 10 customers:
- Какие каналы работают для маленьких объёмов? (cold outreach, founder communities, content, partnerships)
- Что **не** работает на этом масштабе (paid ads обычно слишком дороги без оптимизированной воронки)

**Long-term sustainable** — как масштабироваться до 100K+:
- Какие каналы выдержат масштаб? (paid ads с оптимизированным CAC, viral loops, SEO content engine, sales team)
- Они должны быть **другими** чем short-term (это нормально)

**Validation:**
- ⛔ Short-term = long-term (пример ошибки: «cold outreach» — не масштабируется)
- ⛔ «Мы будем вирусными» без конкретного механизма
- ✅ Каждый канал имеет конкретный owner / cost model / expected CAC

### 1.3.6 — Business Model

**Business equation** (формула зависит от типа продукта):

| Тип | Формула |
|-----|---------|
| B2B SaaS | LTV > 3× CAC, payback < 12 months |
| Freemium B2C | Free→Paid conversion × ARPU > CAC |
| Marketplace | (Take rate × GMV) > Cost-to-serve both sides |
| DTC | (LTV × Repeat rate) > CAC + COGS + ops |

**Что зафиксировать:**
- **Revenue streams** — откуда деньги
- **Pricing** — модель + конкретный price point + обоснование
- **LTV estimate** — оценка
- **Cost structure** — fixed vs variable
- **Path to profitability** — как LTV растёт быстрее CAC со временем

**Validation:**
- ⛔ «Будет реклама / freemium / премиум» без чисел
- ⛔ Pricing скопирован у конкурента без проверки на свою аудиторию
- ✅ Конкретные оценки даже если грубые («LTV ~$500 на основе X»)

### 1.3.7 — Timing / Why Now

**Два вопроса:**
1. **Что изменилось?** — конкретный сдвиг (технология, поведение, регуляция, экономика)
2. **Почему именно сейчас?** Не год назад и не через 3 года?
   - Что было невозможно/нерентабельно раньше?
   - Что закрывает окно возможности позже?

**Validation:**
- ⛔ «Нам кажется что рынок созрел» — не timing
- ⛔ «AI hype» — это не timing, это шум
- ✅ Конкретный triggering event («GPT-4 сделал перевод дешевле в 100 раз», «новый закон о маркировке пришёл с 2025», «поколение Z вышло на рынок труда массово»)
- ✅ Window опционально объяснимо («окно закроется когда incumbents адаптируются — оценочно 2-3 года»)

**Bill Gross research:** timing — топ-1 фактор успеха стартапов (важнее команды, идеи, бизнес-модели и финансирования). Не пропускать эту dimension.

---

## Шаг 1.4 — Multi-role handling

Если из setup известно что продукт **B2B** или **Marketplace** — пройти dimensions второй раз для второй роли:

**B2B SaaS:**
- Decision Makers (кто платит) ≠ End Users (кто пользуется)
- Их Problem, Value Prop и Audience могут быть разными
- Pricing работает на DM, retention — на EU

**Marketplace:**
- Demand side (покупатели) ≠ Supply side (продавцы)
- Каждая сторона = отдельная audience с отдельными dimensions
- Chicken-and-egg problem явно отметить в Growth Strategy

**Один и тот же narrative-v1.md** содержит обе роли — отдельными секциями.

---

## Шаг 1.5 — Confidence Assessment

После проработки всех 7 (или 14 для multi-role) dimensions — оценить confidence 1-10 для каждой:

| Score | Что значит |
|-------|-----------|
| 9-10 | Подкреплено сильными данными или личным опытом, маловероятно ошибиться |
| 7-8 | Есть основания, но требуется валидация |
| 5-6 | Логично, но без данных. Гипотеза. |
| 3-4 | Слабая гипотеза, много неизвестных |
| 1-2 | Гадание |

**В V1 confidence обычно 4-6 для большинства dimensions.** 9-10 в V1 — красный флаг (overconfidence).

**Идентификация riskiest:**
- Самая низкая confidence
- Если несколько с одинаковой — та у которой Failure Impact выше (см. defaults в `references/stage-3-synthesis.md`)

Записать: **«Riskiest dimension: [name] (confidence: X/10, impact: Y)»**

---

## Шаг 1.6 — Document Generation

**Спросить пользователя:**
- Структурный или прозаический формат?
  - Структурный (`template-narrative.md`) — для собственной работы и команды, легче обновлять
  - Прозаический (`template-narrative-prose.md`) — для стейкхолдеров и инвесторов

Загрузить шаблон, заполнить, сохранить как `narrative-v1.md` в папке проекта.

Обязательные секции:
1. Метаданные (продукт, тип, контекст, дата, версия V1)
2. Version History (для V1: «Initial hypothesis»)
3. Team Pre-Flight Check (с risk flag)
4. 1-7 dimensions
5. Validation Status table (7 строк, для V1 confidence + «riskiest» отметка, evidence пусто)
6. Recommended next step: «Stage 2 (Market Research) для риск-dimension в первую очередь»

---

## Quality gates Stage 1

Перед закрытием stage 1:

- [ ] Все 7 dimensions проработаны (не «забыли про Timing»)
- [ ] Problem не упоминает продукт
- [ ] Audience имеет 2-3 defining attributes (не demographics)
- [ ] Value prop = benefits, не features
- [ ] Competitive Advantage = одна из 7 Powers с обоснованием
- [ ] Growth: short-term ≠ long-term, оба с конкретикой
- [ ] Business model имеет хотя бы грубые оценки чисел
- [ ] Timing — конкретный triggering event
- [ ] Confidence записан для каждой dimension
- [ ] Riskiest явно идентифицирована
- [ ] Multi-role handled (если B2B или Marketplace)
- [ ] Team pre-flight check сделан

---

## Common pitfalls Stage 1

| Ошибка | Симптом | Фикс |
|--------|---------|------|
| Solution-framed problem | «Нашего продукта нет» | Сформулировать что мешает пользователю независимо от вашего продукта |
| Audience = demographic | «Женщины 25-45» | Найти **поведенческий** атрибут |
| Features in value prop | «Интеграция с 5 маркетплейсами» | Переформулировать в benefit: «Не надо переключать вкладки» |
| Generic competitive advantage | «Лучшая команда» | Один из 7 Powers с конкретным механизмом |
| Same channel short+long | «SEO» в обоих горизонтах | Разделить: что работает на 100 пользователях vs 100K |
| Pricing без обоснования | «$29/мес — стандарт» | Откуда $29? Что подтверждает что аудитория заплатит? |
| Timing = «AI everywhere» | Generic hype | Конкретный triggering event |
| Confidence 9-10 в V1 | «Мы уверены» | Снизить. V1 — это гипотеза, не факт |
| Игнор multi-role в B2B | Один набор dimensions | Decision Makers ≠ End Users — два набора |
| Skip team pre-flight | «У нас всё ок» | 3 вопроса всё равно задать — это контекст |
