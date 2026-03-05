# brainstorming

Turn rough ideas into fully formed designs — before writing a single line of code.

**by [Jesse Vincent](https://github.com/jessevondoom)** · [superpowers plugin](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

---

## What it does

`brainstorming` guides Claude through a structured dialogue before any implementation begins. It asks clarifying questions one at a time, proposes 2–3 approaches with trade-offs, then produces a written design document and hands off to the `writing-plans` skill. **No code is written until the design is approved** — this is enforced as a hard gate.

Before/after:
- ❌ *"Build me a dashboard"* → Claude writes code immediately, misses the real requirements, you spend hours on revisions
- ✅ *"Build me a dashboard"* → brainstorming asks 4–6 targeted questions, presents a design, gets approval, then implementation begins

---

## Installation

### ✅ Recommended: Official Plugin (Claude Code)

`brainstorming` is part of the **superpowers** plugin — an official plugin available in Claude Code's plugin marketplace.

**What is an official plugin?**
Claude Code has a built-in plugin system that lets you add skills, commands, and automated hooks from verified publishers. Plugins install automatically, update themselves, and don't require manual file management. Think of them as app store installs for Claude.

**How to install superpowers:**
1. Open Claude Code in your terminal
2. Type `/plugins` and press Enter (or open **Settings → Plugins**)
3. Search for **superpowers**
4. Click **Install**

`brainstorming` will be available immediately after installation, along with other superpowers skills like `writing-plans`, `systematic-debugging`, and `test-driven-development`.

### Alternative: Copy the skill file manually

If you prefer to install just this skill without the full superpowers plugin:

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/brainstorming
curl -o ~/.claude/skills/brainstorming/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/brainstorming/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\brainstorming"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/brainstorming/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\brainstorming\SKILL.md"
```

---

## Usage

Trigger brainstorming before any creative or implementation task:

- *"Let's brainstorm a new feature"*
- *"I want to build a user dashboard — help me think it through"*
- *"Brainstorm how to structure this API"*
- *"I have an idea for a newsletter layout — let's design it"*
- *"/brainstorm"*

**Important:** This skill has a hard gate — it will NOT write any code until a design is approved. This is intentional.

---

## How to use in the HTML page / presentation workflow

This skill is the **first step** when building any page, site, or presentation with Claude:

```
1. brainstorming   → figure out structure, content, and goals
2. visual-explainer → generate the HTML page with data and diagrams
3. frontend-design  → elevate the visual quality and aesthetics
4.                 → "create the page"
```

**Why start here?**
People often can't articulate what they want until they see the wrong version. `brainstorming` extracts the real requirements through dialogue — what the page is for, who reads it, what story it tells — before any code is written. This prevents the most common source of rework.

---

## Dependencies

- **writing-plans** — brainstorming always hands off to this skill to create the implementation plan. Also part of the superpowers plugin.

---

## Credits

Skill by **Jesse Vincent** · [superpowers plugin](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

Published here with attribution for reference. Primary installation: superpowers plugin via Claude Code.

---

---

# brainstorming (RU)

Превращает сырые идеи в продуманные дизайны — до написания единой строки кода.

**автор: [Jesse Vincent](https://github.com/jessevondoom)** · [плагин superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

---

## Что делает

`brainstorming` проводит структурированный диалог с Клодом до начала любой реализации. Задаёт уточняющие вопросы по одному, предлагает 2–3 подхода с компромиссами, затем создаёт письменный дизайн-документ и передаёт управление скиллу `writing-plans`. **Код пишется только после одобрения дизайна** — это жёсткий запрет.

До/после:
- ❌ *«Сделай мне дашборд»* → Клод сразу пишет код, промахивается с требованиями, ты часами переделываешь
- ✅ *«Сделай мне дашборд»* → brainstorming задаёт 4–6 точечных вопросов, показывает дизайн, получает одобрение, и только потом начинается реализация

---

## Установка

### ✅ Рекомендуемый способ: официальный плагин (Claude Code)

`brainstorming` входит в плагин **superpowers** — официальный плагин, доступный в магазине плагинов Claude Code.

**Что такое официальный плагин?**
Claude Code имеет встроенную систему плагинов, которая позволяет добавлять скиллы, команды и хуки от проверенных авторов. Плагины устанавливаются автоматически, обновляются сами и не требуют ручного управления файлами. Представь их как установку приложений из магазина — только для Клода.

**Как установить superpowers:**
1. Открой Claude Code в терминале
2. Введи `/plugins` и нажми Enter (или зайди в **Настройки → Плагины**)
3. Найди **superpowers**
4. Нажми **Установить**

`brainstorming` будет доступен сразу после установки вместе с другими скиллами superpowers: `writing-plans`, `systematic-debugging`, `test-driven-development` и другими.

### Альтернатива: скопировать файл скилла вручную

**macOS / Linux:**
```bash
mkdir -p ~/.claude/skills/brainstorming
curl -o ~/.claude/skills/brainstorming/SKILL.md \
  https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/brainstorming/SKILL.md
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\brainstorming"
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/alenazaharovaux/share/main/skills/brainstorming/SKILL.md" `
  -OutFile "$env:USERPROFILE\.claude\skills\brainstorming\SKILL.md"
```

---

## Использование

Вызывай brainstorming перед любой творческой или технической задачей:

- *«Давай продумаем новую фичу»*
- *«Хочу построить дашборд — помоги разобраться»*
- *«Brainstorm структуру этого API»*
- *«У меня есть идея для макета рассылки — давай проработаем»*
- *«/brainstorm»*

**Важно:** У скилла жёсткий запрет — он НЕ пишет код до одобрения дизайна. Это сделано намеренно.

---

## Как использовать в связке для создания страниц и презентаций

Это **первый шаг** при создании любой HTML-страницы, сайта или презентации с Клодом:

```
1. brainstorming   → структура, содержание, цели
2. visual-explainer → HTML-страница с данными и схемами
3. frontend-design  → уровень визуального дизайна
4.                 → «создай страницу»
```

**Зачем начинать здесь?**
Люди часто не могут сформулировать, чего хотят, пока не увидят неправильную версию. `brainstorming` извлекает реальные требования через диалог — для чего страница, кто её читает, какую историю она рассказывает — прежде чем написан хоть один тег. Это устраняет главный источник переработок.

---

## Зависимости

- **writing-plans** — brainstorming всегда передаёт управление этому скиллу для создания плана реализации. Тоже входит в плагин superpowers.

---

## Авторство

Скилл создан **Jesse Vincent** · [плагин superpowers](https://github.com/jessevondoom/superpowers-for-claude-code) · MIT License

Опубликовано здесь с атрибуцией для справки. Основной способ установки: плагин superpowers через Claude Code.

---

*Опубликовано в [alenazaharovaux/share](https://github.com/alenazaharovaux/share)*
