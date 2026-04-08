# Levels of PMF — First Round Capital framework

**Источник:** First Round Capital, «The Levels of Product/Market Fit (& What to Focus on at Each)». Авторы — Todd Jackson, Brian Rothenberg, Carolyn Stein. Опубликовано в First Round Review.

**Зачем:** PMF — это не бинарное состояние «есть/нет», а лестница из 4 уровней. Каждый уровень требует разных метрик, разных приоритетов и разных типов работы. Команды часто думают что PMF либо есть, либо нет — и из-за этого делают неправильные действия (масштабируют преждевременно или сидят на достижимом уровне).

**Когда применяется:** Stage 9 (Metrics) после того как Sean Ellis и retention cohorts собраны, для определения **где именно** на лестнице находится продукт.

---

## 4 уровня

### Level 1 — Nascent PMF

**Что значит:** есть несколько early adopters, которым продукт реально полезен, но всё держится на ручной работе founder/команды. Нет повторяемого процесса acquisition. Retention сигналов недостаточно для статистики.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | <20% Sean Ellis Very disappointed (или ещё нет 40 ответов для замера) |
| Demand | 1-10 active users, ~0 organic growth, acquisition manual (founder outreach, friends) |
| Efficiency | Manual everything: onboarding, support, billing. Не масштабируется. |

**Что делать на этом уровне:**
- НЕ масштабировать
- НЕ поднимать большие раунды
- Глубинные интервью с этими 1-10 пользователями
- Делать concierge-уровень service (отвечать лично, исправлять bugs за час)
- Цель: понять для **кого** именно работает и **почему**

**Анти-паттерн:** запуск paid ads на этом уровне. Acquisition без retention = bucket с дырками.

---

### Level 2 — Developing PMF

**Что значит:** есть сигналы повторяемого спроса. Несколько cohorts retention начинают flatten (не падают к нулю). Sean Ellis между 25-40%. Word of mouth начался но слабый — 1-2 referrals в неделю.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis 25-40% Very disappointed на ≥40 ответах |
| Demand | Retention первых cohorts частично flatten, есть 1-2 organic referrals/week, growth неустойчивый |
| Efficiency | Часть процессов автоматизирована, но customer success всё ещё manual |

**Что делать на этом уровне:**
- Углубить понимание «Очень разочарован» сегмента (Superhuman PMF Engine)
- Сегментировать «Несколько разочарован» — что им мешает дойти до «Очень разочарован»
- Закрыть top-3 blockers из interviews
- Начать экспериментировать с acquisition channels, **но осторожно** — на этом уровне CAC обычно > LTV
- Цель: довести Sean Ellis до 40%+ через product improvements, не через переопределение метрики

**Анти-паттерн:** делать растущий roadmap features. На Level 2 нужны не features, а fit. Меньше нового, больше доделки того что есть.

---

### Level 3 — Strong PMF

**Что значит:** Sean Ellis ≥40%. Retention flatten на здоровом уровне (>40% consumer / >60% B2B / >25% high-frequency). Customers говорят что не могут жить без продукта. Organic word of mouth даёт измеримый channel. Команда чувствует «pull» — спрос обгоняет capacity.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis ≥40%, NPS ≥30, customers активно используют > 3 раз/неделю |
| Demand | Retention flatten, organic growth ≥20% MoM, есть waitlist или organic inbound, conversion trial→paid >25% |
| Efficiency | CAC payback <12 месяцев, LTV/CAC >3, support load растёт линейно а не экспоненциально |

**Что делать на этом уровне:**
- Можно scaling: paid acquisition с положительной экономикой
- Hire growth team (не раньше)
- Поднять Series A (если ещё нет)
- Стандартизация процессов (onboarding flows, support playbooks)
- Цель: расширить acquisition без потери satisfaction. Защитить Sean Ellis %, мониторить ежемесячно.

**Анти-паттерн:** перестать слушать пользователей. Переход к Level 3 — самый опасный момент для arrogance. Продолжать customer interviews ежемесячно.

---

### Level 4 — Extreme PMF

**Что значит:** редкое состояние. Нелинейный рост. Customers евангелизируют без подсказки. Supply (capacity, hiring, infrastructure) не успевает за demand. Press пишет сама. Конкуренты копируют. Sean Ellis часто >60%, retention curves почти горизонтальны.

**Signals:**

| Dimension | Indicator |
|-----------|-----------|
| Satisfaction | Sean Ellis >60%, customers буквально пишут unsolicited testimonials, NPS ≥50 |
| Demand | Нелинейный organic growth, длинные waitlists, СМИ пишут сами, копии в соцсетях |
| Efficiency | LTV/CAC >5, payback <6 месяцев, ограничение — supply, не demand |

**Что делать на этом уровне:**
- Scale supply: hiring, infrastructure, fundraising (Series B+)
- Защита от копирования: 7 Powers (см. `references/7-powers.md`)
- Подготовка к international expansion / adjacent markets
- Цель: не сломать культуру и качество в spike роста

**Примеры:** ChatGPT первые 2 месяца, Slack 2014, Zoom март 2020, Notion 2019, Linear 2021. Это редкие случаи, не норма.

**Анти-паттерн:** hire too fast, lose product quality, потерять culture. Большинство компаний которые получили Extreme PMF и провалились — провалились здесь, не в Level 1-3.

---

## 3 dimensions × 4 уровня = матрица оценки

Каждый уровень оценивается по 3 dimensions: **Satisfaction, Demand, Efficiency**. Команда не может быть на одном уровне в одной dimension и на другом в другой — это скорее всего самообман.

| Level | Satisfaction | Demand | Efficiency |
|-------|--------------|--------|------------|
| Nascent | <20% или нет данных | 1-10 users, manual acq | Manual everything |
| Developing | 25-40% Sean Ellis | Partial retention flatten, 1-2 referrals/wk | Mixed manual/auto |
| Strong | ≥40% Sean Ellis | Flat retention curve, organic growth ≥20% MoM | LTV/CAC >3, payback <12mo |
| Extreme | >60% Sean Ellis | Non-linear growth, supply-constrained | LTV/CAC >5, payback <6mo |

**Правило assessment:** уровень определяется по **минимальной** dimension. Если Satisfaction = Strong, а Demand = Developing, общий уровень = Developing. Самое слабое звено определяет реальное положение.

---

## Как assess level

**Шаг 1.** Собрать данные на 3 dimensions:
- Satisfaction: Sean Ellis (Stage 9, основной), NPS если есть
- Demand: retention cohorts, growth rate (MoM), conversion rate, organic %
- Efficiency: CAC, LTV, payback period, support load

**Шаг 2.** Для каждой dimension определить уровень по таблице выше.

**Шаг 3.** Общий уровень = минимум из трёх.

**Шаг 4.** Записать в `metrics-dashboard.md`:
- Текущий уровень
- Какая dimension = bottleneck
- Что нужно для перехода на следующий уровень (один-два конкретных шага)

---

## Что нужно для перехода уровня

| Текущий → Следующий | Главное изменение |
|---------------------|-------------------|
| Nascent → Developing | Сегментировать первых пользователей, найти повторяющийся pattern. Обычно 5-10 интервью в Stage 7 + iteration в Stage 4 |
| Developing → Strong | Закрыть top-3 blockers из «Несколько разочарован» сегмента. Поднять Sean Ellis с ~30% до ≥40% через product improvements |
| Strong → Extreme | Усилить power (см. 7 Powers), часто = network effects или counter-positioning. Невозможно усилием — продукт либо имеет potential к Extreme либо нет |

**Важно:** Strong PMF — это **достаточный** уровень для прибыльного бизнеса. Не каждый продукт может быть Extreme. Не нужно. Strong PMF = большинство успешных SaaS, marketplaces, B2B инструментов.

Extreme PMF — это venture-scale outcome, и он редкий. ~5% продуктов которые достигли Strong когда-либо доходят до Extreme.

---

## Common mis-assessments

| Ошибка | Как выглядит | Как избежать |
|--------|--------------|--------------|
| «Мы на Strong потому что 200 платящих» | Объём ≠ fit. 200 платящих с 10% retention = Nascent | Смотреть на retention curve, не на абсолютные числа |
| «Мы на Strong потому что Sean Ellis 45%» | Только satisfaction измерена | Все 3 dimensions обязательны |
| «Мы на Extreme потому что press пишет» | Hype ≠ retention | Press без retention = vanity. Что в retention cohorts? |
| «Мы на Developing потому что доход растёт» | Growth ≠ fit. Можно расти через CAC > LTV | Смотреть на unit economics |
| «Мы на Nascent уже год» | Может быть signs developing скрыты внутри сегмента | Сегментировать users — может в одном сегменте уже Strong, в других Nascent |
| «Мы на Strong но Sean Ellis 25%» | Самообман через переопределение | Не переопределять threshold. 40% не для красоты |

---

## Связь со Stage 10 (Iterate)

Уровень определяет **следующий action**:

- **Nascent → Stage 4** (Validate): глубже валидировать assumptions через interviews, не запускать новые features
- **Developing → Stage 7** (Interview synthesis): углубить понимание сегмента «Очень разочарован» и blockers «Несколько разочарован»
- **Strong → Stage 10** (Iterate): защищать satisfaction, усиливать growth каналы, начать строить power
- **Extreme → outside scope of PMF skill**: scaling, hiring, expansion — уже не PMF задача

Это decision tree автоматически создаётся в `metrics-dashboard.md` (см. `references/template-metrics-dashboard.md`).
