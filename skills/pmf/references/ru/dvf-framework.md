# DVF Framework — Desirability × Viability × Feasibility

**Источник:** David Bland & Alex Osterwalder, "Testing Business Ideas" (2019). Strategyzer.

**Зачем:** разложить риск-dimension на конкретные проверяемые assumptions по трём осям, чтобы знать **что именно валидировать** и в **каком порядке**.

**Когда применяется:** Stage 4 (Validate). Один раз на самую рискованную dimension из risk-prioritization. Может повторяться для второй и третьей рискованных dimension если эксперимент Stage 4 успешен.

---

## Три категории

### Desirability — «Хотят ли они это?»

Допущения **только про user needs, behavior, motivation**. Ничего про деньги, ничего про технику.

Что попадает сюда:
- Реальное поведение пользователей (как часто, в каком контексте, через какие workarounds)
- Severity проблемы (мешает или раздражает)
- Frequency (раз в день, раз в месяц, раз в год)
- Trigger (что запускает потребность)
- Желаемый результат (что они хотят, не что мы предлагаем)
- Готовность сменить текущее решение

Что НЕ попадает сюда:
- «Они купят это за $29» → Viability
- «Они любят красивый UI» → Desirability только если красота даёт им выгоду; иначе это Feasibility (мы можем сделать красиво)
- «Они захотят интеграцию с Slack» → Desirability только если интеграция решает работу; иначе это feature wishlist

**Тест на Desirability:** убираем продукт из формулировки. Остаётся ли проблема? Если нет — это не Desirability, это feature request.

### Viability — «Принесёт ли это деньги?»

Допущения **только про экономику, финансы, монетизацию**.

Что попадает сюда:
- Pricing model (subscription, one-time, freemium, usage-based)
- Willingness to pay на конкретной price point
- Conversion rates (visitor → trial → paid)
- CAC (customer acquisition cost) по каждому каналу
- LTV (lifetime value) и его драйверы
- Unit economics (gross margin, payback period)
- Размер рынка (TAM/SAM/SOM) если pre-launch
- Pricing power (можно ли поднимать цену)

**Тест на Viability:** убираем продукт из формулировки и заменяем на «решение этой проблемы». Остаётся ли финансовое утверждение? Если да — это Viability.

### Feasibility — «Можем ли мы это построить и поддерживать?»

Допущения про **operational + technical + regulatory** возможности.

Три подкатегории:

**Operational** — про команду и процессы:
- Хватит ли людей в команде
- Можем ли поддерживать N customers с текущим headcount
- Есть ли нужные навыки внутри команды
- Можем ли построить supply chain / distribution
- Сможем ли соблюдать SLA

**Technical** — про код и инфраструктуру:
- Существуют ли API/инструменты которые нам нужны
- Стабильны ли они достаточно для production
- Можем ли построить нужный latency / throughput / accuracy
- Хватит ли ML моделей нужного качества (для AI продуктов)
- Можем ли мигрировать существующих пользователей

**Regulatory** — про законы и compliance:
- Нужна ли лицензия (fintech, healthtech, education)
- Соответствуем ли GDPR / CCPA / HIPAA / AI Act
- Есть ли intellectual property риски (patents, trademarks)
- Можем ли работать на нужных территориях

---

## Regulatory sub-check

Для трёх типов продуктов regulatory становится **первоклассной** Feasibility, а не сноской:

| Product type | Минимум regulatory assumptions |
|--------------|-------------------------------|
| **AI / ML** | Data privacy для training data, AI Act если EU, copyright для outputs, model bias для регулируемых решений (hiring, credit, healthcare) |
| **Fintech** | Лицензирование (BaaS provider или своя), KYC/AML, PCI DSS если карты, локальные финансовые регуляторы |
| **Healthtech** | HIPAA если US, GDPR-medical если EU, FDA classification если medical device, telemedicine лицензирование по штатам/странам |

Если продукт попадает в категорию — регуляторные допущения **заменяют** часть operational/technical в трёх Feasibility, не добавляются сверху.

---

## 9 assumptions: 3+3+3

DVF разворачивает риск-dimension в **строго 9 assumptions, по 3 на категорию**.

Почему ровно 3:
- 1-2 — слишком мало, не покрывают все аспекты dimension
- 4-5 — слишком много, начинаются дубли и distractions
- 3 — заставляет приоритизировать самое важное в каждой категории

Почему сбалансированно (3+3+3) а не 5D + 2V + 2F:
- Несбалансированность маскирует пропущенные риски
- Если в Viability реально нет вопросов — значит вы переоцениваете уверенность в монетизации
- Если в Feasibility «всё легко» — значит вы не подумали о regulatory или scaling

Каждая assumption начинается с «I believe / Я считаю что» — это превращает мнение в проверяемое утверждение.

---

## DVF Tension Check

После генерации 9 assumptions ищем **самые большие конфликты между категориями**. Tensions = места где валидация одной категории убивает другую.

Типичные tensions:

| Tension | Пример |
|---------|--------|
| **Desirability vs Viability** | «Пользователи хотят бесплатно» vs «Нужен subscription для unit economics» |
| **Desirability vs Feasibility** | «Хотят real-time» vs «Технически возможен только batch» |
| **Viability vs Feasibility** | «$29/мес за план» vs «Cost to serve = $35/мес» |
| **Regulatory vs Desirability** | «Хотят анонимность» vs «KYC требует документы» |

Tension часто **указывает на самую рискованную assumption** — это место где продукт может развалиться, даже если все три категории по отдельности подтверждены.

Записывается в `assumptions-map.md` одним абзацем.

---

## 2×2 Matrix: Importance × Evidence

Когда 9 assumptions готовы, размещаем их на матрице:

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

**Importance scale:**
- **High** = если assumption неверна, продукт ломается. Невозможно адаптировать без major pivot.
- **Low** = если assumption неверна, можно адаптироваться. Не fatal.

**Evidence scale:**
- **Strong** = есть данные из market research, существующих пользователей, аналогов с конкретными числами
- **Weak** = только мнение команды, indirect evidence или ничего

**4 quadrant:**

| Quadrant | Что делать |
|----------|-----------|
| **Critical** (High imp + Weak ev) | Тестировать **первым**. Здесь главный риск. |
| **Sweet spot** (High imp + Strong ev) | Не трогать, использовать как опору |
| **Solid** (Low imp + Strong ev) | Пропустить, экономить ресурсы |
| **Distraction** (Low imp + Weak ev) | Игнорировать. Распространённая ошибка — увлечься этим квадрантом «потому что интересно» |

Цель квадранта — **выбрать 1–3 assumption из Critical** для эксперимента в Шаге 4.4.

---

## 6 стандартных типов экспериментов

David Bland каталогизировал ~44 эксперимента. Для PMF skill используется **6 базовых**, которые покрывают 95% случаев на ранних стадиях:

| Type | Что делает | Стоимость | Best for |
|------|-----------|-----------|----------|
| **Customer Interview** | Глубинное интервью (45–60 мин) с целевой аудиторией | Время, нет $ | Desirability, понимание behavior |
| **Survey** | Структурированный опрос на масштабе | $0–$200 на дистрибуцию | Desirability + Viability (willingness to pay) |
| **Smoke Test** | Landing page + ad → измеряем интерес (sign-ups) до того как продукт построен | $200–$1000 на ads | Desirability + Viability (intent) |
| **Landing Page** | Полная landing с CTA, ценой, фичами | $200–$2000 | Demand validation, price testing |
| **Prototype** | Кликабельный прототип без real backend (Figma, Framer) | Время, нет $ | UX desirability + technical feasibility check |
| **Concierge** | Делаем работу руками для 5–10 customers, симулируя продукт | Время команды, нет $ | Полный комплекс D+V+F на малом масштабе |

**Не выдумывать новые типы.** «Mini-pilot», «Discovery sprint», «Soft launch» — не эксперименты, это размытые термины. Если ничего не подходит — пересобрать формулировку assumption так, чтобы стандартный тип сработал.

---

## Связь с другими фреймворками

**Lean Startup (Eric Ries):** DVF — это конкретизация Build–Measure–Learn. «Build» в Lean — это не обязательно код, это experiment. DVF говорит **что именно** строить как experiment.

**Design Thinking (IDEO):** DVF использует ту же триаду «Desirable / Viable / Feasible» которую IDEO предложил в 2009. Bland добавил к ней systematic testing (assumptions map + experiment library).

**Jobs-to-be-Done:** JTBD питает Desirability assumptions — «job to be done» это и есть формулировка need. JTBD не покрывает V и F.

**Customer Development (Steve Blank):** Customer Discovery в его модели = Stage 4 + Stage 5 + Stage 6 в PMF skill. DVF — это как структурировать что валидировать в Customer Discovery.

---

## Common mistakes

| Ошибка | Почему происходит | Как избежать |
|--------|-------------------|--------------|
| Все 9 assumptions в Desirability | Команда продуктовая, думает только про users | Жёстко 3+3+3, без исключений |
| Viability assumptions = «мы сможем монетизировать» | Слишком абстрактно | Конкретный price point, конкретный channel, конкретный CAC |
| Feasibility = «мы это построим» | Игнорирует технические unknowns | Декомпозировать на operational/technical/regulatory |
| Assumption начинается с «нужно» | «Нужно сделать integration» | Это feature, не assumption. «I believe users won't adopt without integration» |
| Все assumptions в Sweet spot после maps | Wishful thinking | Если 9/9 в Sweet spot — Stage 4 не нужен; пересмотреть importance, обычно это самообман |
| Пропуск 2×2 → сразу experiment | Лень или спешка | 2×2 защищает от теста не-критичной assumption |
| Customer Interview как тест Viability | «Спросим хотят ли они платить» | Interview не валидирует pricing — люди врут об этом. Используй Smoke Test или Landing Page |

---

## Когда DVF не работает

DVF предполагает что вы знаете кто целевая аудитория и какую проблему решаете. Если ни того ни другого нет — Stage 4 преждевременен. Вернись в Stage 1 (Hypothesis) и проработай 7 dimensions сначала.

DVF также не подходит для **deep tech R&D** где Feasibility — основной риск на годы вперёд (квантовые компьютеры, biotech). Там нужен другой фреймворк (Technology Readiness Levels).

Для всего остального в B2B SaaS, consumer apps, marketplaces, AI products — DVF покрывает.
