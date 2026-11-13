# Пояснительная бригада · Explainer Crew

**[English below](#english)**

Навык для Codex и Claude Code объясняет сложные термины и названия инструментов в стиле, который вы выбрали сами: «Игра престолов», «Бригада», рассказ Чехова, химические элементы или любой другой. Все объяснённые слова копятся в личный глоссарий — одну HTML-страницу, которую можно переслать.

## Как объясняет

Каждый термин в три части:
1. **История в вашем стиле** — чтобы понять и запомнить.
2. **Просто** — одна-две фразы обычным языком.
3. **Пример** — где вы это встретите в работе.

Ниже — ссылка на источник. Названия инструментов и свежие термины агент проверяет поиском в интернете. Если ничего не нашёл, так и пишет и объяснение не выдумывает.

## Что внутри

```
poyasnitelnaya-brigada/
├── SKILL.md                    инструкция агенту: режимы и порядок шагов
├── INSTALL-AGENT.md            инструкция по установке для агента
├── references/
│   ├── stili.md                как писать в стиле, правила точности, примеры на 4 стилях
│   └── primer-termina.md       формат записи термина
└── scripts/
    ├── build_glossary.py       собирает страницу глоссария
    └── read_comments.py        переводит сохранённые комментарии в список
```

## Установка

Откройте Codex или Claude Code в любой папке и напишите агенту:

> Установи навык по ссылке https://github.com/alenazaharovaux/share/tree/main/skills/poyasnitelnaya-brigada по файлу INSTALL-AGENT.md

Агент скопирует навык в личную папку навыков (`~/.agents/skills/` в Codex, `~/.claude/skills/` в Claude Code), проверит Python 3 и, если его нет, предложит поставить. Сторонние библиотеки не нужны.

## Как запускать

Навык включается только по слову «бригада». На обычное «объясни» агент отвечает как всегда.

- Первый раз: «пояснительная бригада». Агент спросит стиль.
- Одно слово: «бригада, что такое RAG».
- Транскрипт или файл: «бригада, найди все термины и инструменты в <файл>». Агент покажет список, вы назовёте номера знакомых слов, остальные он объяснит.
- Сменить стиль: «бригада, смени стиль на Чехова». Старые объяснения останутся как были.
- Открыть глоссарий: «бригада, открой глоссарий».

## Глоссарий и комментарии

Данные лежат в папке `poyasnitelnaya-brigada` в домашней папке. Страница — `Загрузки/poyasnitelnaya-brigada.html`. Свежие слова на ней сверху, есть поиск и фильтр по темам.

На странице выделите слово или фразу, или наведите мышь на блок и нажмите «+ комментарий». Напишите вопрос, «удали» или «знаю это слово». Нажмите «Сохранить комментарии» и скажите агенту «бригада, я оставил(а) комментарии». Агент ответит на вопросы прямо в глоссарии, уберёт лишнее и обновит страницу.

---

## English

A Codex and Claude Code skill that explains hard terms and tool names in a style you choose: *Game of Thrones*, a Russian crime drama, a Chekhov short story, the periodic table, or anything else. Every term gets a story in your style, a plain one-line definition, a real-life example and a source link. Tool names and recent terms are checked with a web search; if nothing reliable is found, the skill says so instead of inventing an explanation.

Works on a single term ("бригада, что такое RAG") or a whole transcript: the agent lists candidate terms, you mark the ones you already know, it explains the rest. All terms collect on one HTML glossary page (newest first, search, topic filter) with a comment layer: select text, ask a question or write "delete", save, and tell the agent — it answers in the glossary and rebuilds the page.

The skill and its texts are in Russian. Triggered only by the word «бригада».

**Install:** ask your agent to install it from this folder following `INSTALL-AGENT.md`. Requires Python 3, no third-party packages.

By [Alena Zakharova](https://github.com/alenazaharovaux) · MIT
