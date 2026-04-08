# 7 Powers (Hamilton Helmer)

Долгосрочный competitive moat должен быть **одним** из этих 7. Не несколькими одновременно.

Из книги "7 Powers: The Foundations of Business Strategy" by Hamilton Helmer.

---

## 1. Scale Economies

**Определение:** себестоимость единицы падает с ростом объёма.

**Механизм:** fixed costs распределяются на больше units. R&D, manufacturing setup, customer support per user — всё дешевеет в пересчёте на одного customer.

**Примеры:**
- **Amazon** — logistics network: больше распредцентров → быстрее доставка → больше customers → больше объём → дешевле logistics на unit
- **Netflix** — content per subscriber: один сериал стоит одинаково для 1M или 100M зрителей
- **TSMC** — fab production: огромные капзатраты на фабрику amortized на миллиарды чипов

**Как проверить:** при удвоении объёма себестоимость единицы падает на X% (Henderson learning curve). Если нет — это не Scale Economies.

**Когда не работает:** в digital products где marginal cost ≈ 0 уже на маленьком масштабе (большинство SaaS не имеют scale economies в classic sense).

---

## 2. Network Economies

**Определение:** ценность для одного пользователя растёт с количеством других пользователей.

**Механизм:** Metcalfe's law — value of network ∝ N². Каждый новый пользователь увеличивает ценность для всех существующих.

**Примеры:**
- **Facebook / Telegram** — больше друзей → больше причин зайти
- **eBay / Avito** — больше продавцов → больше выбора → больше покупателей → больше продавцов
- **Airbnb** — больше hosts → больше locations → больше guests → больше hosts
- **Uber** — больше drivers → меньше wait time → больше riders → больше drivers

**Как проверить:** engagement растёт **нелинейно** с user count. Если пользователь добавляется без увеличения value для других — не network effect.

**Виды network effects:**
- **Direct** (Facebook) — друзья видят друг друга
- **Indirect / Two-sided** (Airbnb) — больше одной стороны помогает другой
- **Data network** (Google Search) — больше queries → лучше algorithms → больше queries

**Уязвимость:** multi-tenancy — если пользователи могут быть на нескольких сетях одновременно (Twitter + Threads + Bluesky), network effects слабеют.

---

## 3. Counter-Positioning

**Определение:** позиция которую incumbents **не могут скопировать** без угрозы своему core business.

**Механизм:** новая модель cannibalize existing revenue. Incumbents видят это, но скопировать = убить себя.

**Примеры:**
- **Vanguard vs Fidelity** — passive index funds vs active management. Fidelity не может полностью перейти на passive — они потеряют high-margin active management revenue.
- **Netflix mail vs Blockbuster stores** — Blockbuster видел Netflix, но переход на mail-only означал закрытие тысяч store с рентами и сотрудниками.
- **Roku vs Cable TV** — кабельщики не могли запустить cord-cutting service не уничтожив свою подписную базу.
- **Digital cameras vs Kodak film** — Kodak изобрёл digital, но боялся cannibalize film business. Опоздали.

**Как проверить:** что должны были бы caniballize incumbents чтобы скопировать? Если ответ «значительная часть текущего revenue» — counter-positioning есть.

**Сильнейшая Power в начале** — incumbents не реагируют пока не поздно.

---

## 4. Switching Costs

**Определение:** пользователю дорого/сложно/больно уйти к конкуренту.

**Механизм:** investment в текущее решение становится sunk cost при переходе. Время, данные, обучение, интеграции, привычки.

**Примеры:**
- **Salesforce** — данные клиентов, кастомные workflows, тренинг команды, интеграции с другими системами. Уход = месяцы работы.
- **Apple ecosystem** — iCloud photos, iMessage, Apple Watch, AirPods. Уход = переустановка всего.
- **ERP systems (SAP, Oracle)** — годы настройки бизнес-процессов под конкретную систему.
- **Git / GitHub** — история, issues, PRs, CI/CD pipelines, team workflow.
- **Slack** — история сообщений, integrations, channel structure, team habits.

**Виды switching costs:**
- **Financial** — досрочное расторжение, lost discounts
- **Procedural** — обучение, миграция данных, перенастройка
- **Relational** — relationships с support / vendor

**Как проверить:** что theoretically нужно сделать чтобы переключиться? Если >1 недели работы — switching cost есть. Если >1 месяца — strong.

---

## 5. Branding

**Определение:** пользователи готовы платить премию за бренд (durable preference, не temporary).

**Механизм:** бренд снижает perceived risk (известный = safe), даёт identity/status, создаёт affective preference.

**Примеры:**
- **Apple** — премия за iPhone vs equivalent Android (~$300 разница, та же hardware quality)
- **Tiffany & Co** — diamonds той же quality stoять дешевле без коробки
- **Hermès** — Birkin bag vs equivalent quality leather bag (10×+ markup)
- **Coca-Cola** — vs generic cola (blind tests show people can't tell difference, branded tests show preference)
- **Rolex** — vs equivalent quality watches (5-10× markup)

**Как проверить:** ценовая премия vs commodity equivalent. Если >20% — branding есть. Если >50% — strong.

**Опасность:** branding одна из самых сложных Powers. Строится десятилетиями. Легко разрушается одним скандалом.

---

## 6. Cornered Resource

**Определение:** эксклюзивный доступ к ключевому ресурсу.

**Механизм:** ресурс необходим для продукта, конкуренты не могут получить тот же.

**Виды ресурсов:**
- **Human talent** — Pixar (Steve Jobs assembled unique team), DeepMind early
- **Physical asset** — De Beers diamonds (mines), oil reserves, prime real estate
- **IP / Patents** — pharma blockbusters, специфические технологические патенты
- **License / Regulatory** — taxi medallion (NYC), exclusive distribution agreements
- **Data** — proprietary datasets для ML (например, медицинские записи десятилетий)
- **Contracts** — long-term exclusive supplier deals

**Примеры:**
- **Pixar** — десятилетие работы Lasseter с командой создало unique creative process. Конкурентам не достать этих людей.
- **OpenAI ранний доступ к training data** до того как все стали зачищать robots.txt
- **Pharma patents** — 20 лет монополии на molecule

**Как проверить:** конкуренты не могут получить тот же ресурс ни за какие деньги, или это потребует years to replicate.

**Опасность:** многие думают что у них cornered resource, но это просто early lead который конкуренты догонят.

---

## 7. Process Power

**Определение:** операционное превосходство которое требует years of refinement и сложно скопировать даже зная the secret.

**Механизм:** оптимизированные процессы накапливаются итеративно, organizational knowledge не передаётся документами.

**Примеры:**
- **Toyota TPS (Toyota Production System)** — Toyota открыто делится TPS уже 50 лет. Конкуренты копируют. Toyota всё равно остаётся самой эффективной. Process power.
- **TSMC** — yield rate на самых advanced nodes на 5-10% выше чем у Samsung и Intel. Знают как, остальные не могут повторить.
- **Walmart logistics** — десятилетия оптимизации supply chain. Конкуренты копировали приёмы, всё равно не догнали costs.
- **Amazon AWS** — эффективность data center operations накопленная за 15+ лет.
- **Costco** — buying power + operational efficiency дают consistent 15% margin advantage над Sam's Club.

**Как проверить:** компания имеет measurably лучшие операционные метрики (yield, defect rate, cost per unit, throughput) чем все конкуренты years подряд, несмотря на attempts to copy.

**Сложно построить:** процессы — это organizational learning. Не покупается, не нанимается, не описывается в книгах. Нужны years of compounding small improvements.

---

## Правило выбора Power

**Один из 7. Не несколько.** Если у вас «несколько» — обычно это значит что вы переоцениваете. Один сильный moat лучше трёх слабых.

**Не путать Power с advantage:**
- **Advantage** — что-то лучше у вас сейчас
- **Power** — что-то что **нельзя скопировать** в долгую

«У нас лучший UX» — advantage, не Power. UX копируется за 6 месяцев.

**Когда какая Power подходит:**

| Тип продукта | Чаще всего работает |
|-------------|---------------------|
| Marketplace / Social | Network Economies |
| Enterprise SaaS | Switching Costs |
| Consumer brand | Branding |
| Platform / OS | Network Economies + Switching Costs |
| Hardware (semi, manufacturing) | Scale Economies или Process Power |
| Pharma / Biotech | Cornered Resource (patents) |
| Tech disruption (DTC, fintech) | Counter-Positioning |
| Operational complexity (logistics, services) | Process Power |
| Resource extraction | Cornered Resource |

**В Stage 1** выбрать одну Power и явно объяснить почему именно она будет работать. В Stage 4 (Validate) проверить assumption что эта Power реально достижима.
