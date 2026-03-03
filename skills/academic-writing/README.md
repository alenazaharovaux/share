# academic-writing

A Claude Code skill that guides you through the entire academic lifecycle — from forming a research question to responding to peer reviewers. Not just writing style: it covers methodology, literature search strategy, citation management, grant proposals, journal selection, and the politics of getting published.

No configuration needed — works out of the box.

## Installation

**macOS / Linux:**
```bash
cp -r academic-writing ~/.claude/skills/academic-writing
```

**Windows:**
```powershell
Copy-Item -Recurse academic-writing $env:USERPROFILE\.claude\skills\academic-writing
```

## Usage

Say any of these to Claude Code:

- "help me write a research paper"
- "structure my literature review"
- "write a grant proposal"
- "respond to reviewer comments"
- "help me choose a journal"
- "check my paper for common problems"

## What's inside

**Research design** — FINER criteria (Feasible, Interesting, Novel, Ethical, Relevant) for evaluating your question. A table of question types — descriptive, comparative, correlational, causal, exploratory. A progressive narrowing method (see example below).

**Literature review strategy** — Database selection by field: Web of Science and Scopus for multidisciplinary work, PubMed for health, ERIC for education, SSRN for social sciences. Boolean search templates, inclusion/exclusion criteria, search trail documentation.

**Citation management** — BibTeX entry templates. Citation context patterns: introducing concepts, supporting claims, contrasting sources, direct quotation. Integration notes for Zotero, Mendeley, and EndNote. APA 7, MLA 9, Chicago 17, Harvard, IEEE, Vancouver.

**IMRaD paper structure** — Templates for each section. Abstract in five moves (background, purpose, methods, results, conclusions). Introduction in funnel structure. Methods framed around reproducibility. Results vs. Discussion clearly separated.

**Academic writing style** — Tense by section (past for methods/results, present for established knowledge). Hedging language. Transitions by rhetorical function. Paragraph structure: topic sentence → evidence → connection.

**Common problems** — Wordiness with before/after fixes. Weak passive constructions. Vague language replaced with specific citations and effect sizes.

**Peer review** — Full response letter template: point-by-point format with page/line references. When to agree, negotiate, or push back — with ready phrases for each.

**Grant proposals (NSF/NIH)** — Specific Aims page template. Full structure for Significance, Innovation, and Approach. Budget justification: personnel, equipment, supplies, travel, indirect costs.

**Journal selection** — Quality and fit indicators. Predatory journal red flags. Cover letter template with suggested reviewers.

**Research ethics** — Human subjects, data management, authorship, conflict of interest. Fabrication, falsification, plagiarism definitions. P-hacking, HARKing, salami slicing — what to avoid.

**Productivity** — Daily writing routine, large project breakdown, overcoming blocks, tool recommendations.

## Example: research question refinement

```
Draft 1: "How does social media affect politics?"
Draft 2: "How does Twitter use affect political polarization?"
Draft 3: "How does exposure to partisan Twitter accounts affect
         political attitude polarization among US adults?"
Draft 4: "Does increased exposure to ideologically homogeneous Twitter
         feeds increase affective polarization among politically
         engaged US adults aged 18-35?"
```

Each iteration adds population, mechanism, direction, and measurability — without losing the original research impulse.

## Works well with

- [ai-writing-detox](../ai-writing-detox/) — strips AI-generated patterns from academic prose before submission

## Credits

From [academic-writing](https://github.com/jamditis/claude-skills-journalism) by [Joe Amditis](https://github.com/jamditis) — MIT license.

---

# academic-writing (RU)

Скилл для Claude Code, который ведёт через весь академический цикл — от формулировки вопроса до ответов рецензентам. Не только стиль: методология, поиск литературы, управление источниками, гранты, выбор журнала и практика публикации.

Конфигурация не нужна — работает сразу.

## Установка

```bash
cp -r academic-writing ~/.claude/skills/academic-writing
```

## Использование

- «помоги написать научную статью»
- «структурируй литобзор»
- «напиши грантовую заявку»
- «ответь на замечания рецензентов»
- «помоги выбрать журнал»

## Что внутри

**Дизайн исследования** — критерии FINER, типы вопросов, метод последовательного сужения (от расплывчатого к точному за 4 шага).

**Литобзор** — базы данных по дисциплинам, булев поиск, критерии включения/исключения.

**Цитирование** — BibTeX, контексты цитирования, 6 стилей (APA, MLA, Chicago, Harvard, IEEE, Vancouver).

**Структура статьи (IMRaD)** — шаблоны для каждого раздела, аннотация в 5 движений, лид-воронка во введении.

**Ответ рецензентам** — полный шаблон письма: постатейный формат со ссылками на страницы. Когда согласиться, когда оспорить — с готовыми фразами.

**Гранты (NSF/NIH)** — шаблон Specific Aims, структура Significance/Innovation/Approach, обоснование бюджета.

**Выбор журнала** — индикаторы качества, красные флаги хищных журналов, шаблон cover letter.

## Пример: уточнение вопроса

```
Черновик 1: «Как соцсети влияют на политику?»
Черновик 2: «Как Twitter влияет на политическую поляризацию?»
Черновик 3: «Как контакт с партийными аккаунтами в Twitter влияет
             на поляризацию взглядов среди взрослых в США?»
Черновик 4: «Ведёт ли увеличение контакта с идеологически однородными
             лентами к росту аффективной поляризации среди политически
             активных американцев 18-35 лет?»
```

## Хорошо работает вместе с

- [ai-writing-detox](../ai-writing-detox/) — убирает ИИ-маркеры из академического текста перед сдачей

## Авторство

Из [academic-writing](https://github.com/jamditis/claude-skills-journalism) от [Joe Amditis](https://github.com/jamditis) — лицензия MIT.
