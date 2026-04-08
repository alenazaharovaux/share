# 7 Powers (Hamilton Helmer)

A long-term competitive moat must be **one** of these 7. Not several at once.

From the book *7 Powers: The Foundations of Business Strategy* by Hamilton Helmer.

---

## 1. Scale Economies

**Definition:** unit cost falls as volume grows.

**Mechanism:** fixed costs are spread over more units. R&D, manufacturing setup, customer support per user — all of it gets cheaper per customer.

**Examples:**
- **Amazon** — logistics network: more distribution centers → faster delivery → more customers → more volume → cheaper logistics per unit
- **Netflix** — content per subscriber: one show costs the same for 1M or 100M viewers
- **TSMC** — fab production: huge capex on a fab amortized across billions of chips

**How to verify:** when volume doubles, unit cost falls by X% (Henderson learning curve). If not — it is not Scale Economies.

**When it does not work:** in digital products where marginal cost ≈ 0 even at small scale (most SaaS does not have scale economies in the classic sense).

---

## 2. Network Economies

**Definition:** the value to one user grows with the number of other users.

**Mechanism:** Metcalfe's law — value of network ∝ N². Every new user increases the value to all existing ones.

**Examples:**
- **Facebook / Telegram** — more friends → more reasons to log in
- **eBay / Avito** — more sellers → more selection → more buyers → more sellers
- **Airbnb** — more hosts → more locations → more guests → more hosts
- **Uber** — more drivers → less wait time → more riders → more drivers

**How to verify:** engagement grows **non-linearly** with user count. If a user is added without increasing value for others — not a network effect.

**Types of network effects:**
- **Direct** (Facebook) — friends see each other
- **Indirect / Two-sided** (Airbnb) — more of one side helps the other
- **Data network** (Google Search) — more queries → better algorithms → more queries

**Vulnerability:** multi-homing — if users can be on several networks at once (Twitter + Threads + Bluesky), network effects weaken.

---

## 3. Counter-Positioning

**Definition:** a position incumbents **cannot copy** without harming their core business.

**Mechanism:** the new model cannibalizes existing revenue. Incumbents see it, but copying = killing themselves.

**Examples:**
- **Vanguard vs Fidelity** — passive index funds vs active management. Fidelity cannot fully move to passive — they would lose high-margin active management revenue.
- **Netflix mail vs Blockbuster stores** — Blockbuster saw Netflix, but moving to mail-only meant closing thousands of stores with rent and staff.
- **Roku vs Cable TV** — cable companies could not launch a cord-cutting service without destroying their subscription base.
- **Digital cameras vs Kodak film** — Kodak invented digital, but feared cannibalizing the film business. They were too late.

**How to verify:** what would incumbents have to cannibalize to copy? If the answer is "a significant share of current revenue" — counter-positioning is real.

**Strongest Power early on** — incumbents do not react until it is too late.

---

## 4. Switching Costs

**Definition:** it is expensive/complex/painful for the user to leave for a competitor.

**Mechanism:** investment in the current solution becomes a sunk cost on switching. Time, data, training, integrations, habits.

**Examples:**
- **Salesforce** — customer data, custom workflows, team training, integrations with other systems. Leaving = months of work.
- **Apple ecosystem** — iCloud photos, iMessage, Apple Watch, AirPods. Leaving = reinstalling everything.
- **ERP systems (SAP, Oracle)** — years of business-process tuning to a specific system.
- **Git / GitHub** — history, issues, PRs, CI/CD pipelines, team workflow.
- **Slack** — message history, integrations, channel structure, team habits.

**Types of switching costs:**
- **Financial** — early termination, lost discounts
- **Procedural** — training, data migration, reconfiguration
- **Relational** — relationships with support / vendor

**How to verify:** what would theoretically be needed to switch? If > 1 week of work — switching cost exists. If > 1 month — strong.

---

## 5. Branding

**Definition:** users are willing to pay a premium for the brand (durable preference, not temporary).

**Mechanism:** the brand reduces perceived risk (known = safe), gives identity/status, creates affective preference.

**Examples:**
- **Apple** — premium for an iPhone vs an equivalent Android (~$300 difference, same hardware quality)
- **Tiffany & Co** — diamonds of the same quality cost less without the box
- **Hermès** — Birkin bag vs an equivalent quality leather bag (10×+ markup)
- **Coca-Cola** — vs generic cola (blind tests show people can't tell, branded tests show preference)
- **Rolex** — vs equivalent quality watches (5-10× markup)

**How to verify:** price premium vs commodity equivalent. If > 20% — branding exists. If > 50% — strong.

**Risk:** branding is one of the hardest Powers. Built over decades. Easily destroyed by a single scandal.

---

## 6. Cornered Resource

**Definition:** exclusive access to a key resource.

**Mechanism:** the resource is necessary for the product, competitors cannot get the same one.

**Resource types:**
- **Human talent** — Pixar (Steve Jobs assembled a unique team), early DeepMind
- **Physical asset** — De Beers diamonds (mines), oil reserves, prime real estate
- **IP / Patents** — pharma blockbusters, specific technology patents
- **License / Regulatory** — taxi medallion (NYC), exclusive distribution agreements
- **Data** — proprietary datasets for ML (e.g. decades of medical records)
- **Contracts** — long-term exclusive supplier deals

**Examples:**
- **Pixar** — a decade of Lasseter's work with the team built a unique creative process. Competitors cannot get those people.
- **OpenAI's early access to training data** before everyone started locking robots.txt
- **Pharma patents** — 20 years of monopoly on a molecule

**How to verify:** competitors cannot get the same resource for any amount of money, or it would take years to replicate.

**Risk:** many think they have a cornered resource, but it is just an early lead competitors will catch up to.

---

## 7. Process Power

**Definition:** operational superiority that requires years of refinement and is hard to copy even if you know the secret.

**Mechanism:** optimized processes accumulate iteratively, organizational knowledge does not transfer through documents.

**Examples:**
- **Toyota TPS (Toyota Production System)** — Toyota has openly shared TPS for 50 years. Competitors copy. Toyota still remains the most efficient. Process power.
- **TSMC** — yield rate on the most advanced nodes is 5-10% higher than Samsung and Intel. They know how, the others cannot replicate.
- **Walmart logistics** — decades of supply chain optimization. Competitors copied the techniques, still did not catch up to the costs.
- **Amazon AWS** — data center operations efficiency built up over 15+ years.
- **Costco** — buying power + operational efficiency give a consistent 15% margin advantage over Sam's Club.

**How to verify:** the company has measurably better operational metrics (yield, defect rate, cost per unit, throughput) than all competitors for years in a row, despite attempts to copy.

**Hard to build:** processes are organizational learning. Cannot be bought, cannot be hired, cannot be written down in a book. Years of compounding small improvements are needed.

---

## The rule for picking a Power

**One of the 7. Not several.** If you have "several" — usually it means you are overestimating. One strong moat is better than three weak ones.

**Do not confuse a Power with an advantage:**
- **Advantage** — something you do better right now
- **Power** — something that **cannot be copied** long term

"We have the best UX" is an advantage, not a Power. UX is copied in 6 months.

**When each Power fits:**

| Product type | Most often works |
|-------------|---------------------|
| Marketplace / Social | Network Economies |
| Enterprise SaaS | Switching Costs |
| Consumer brand | Branding |
| Platform / OS | Network Economies + Switching Costs |
| Hardware (semi, manufacturing) | Scale Economies or Process Power |
| Pharma / Biotech | Cornered Resource (patents) |
| Tech disruption (DTC, fintech) | Counter-Positioning |
| Operational complexity (logistics, services) | Process Power |
| Resource extraction | Cornered Resource |

**In Stage 1**, pick one Power and explain explicitly why it will work. In Stage 4 (Validate) check the assumption that this Power is actually achievable.
