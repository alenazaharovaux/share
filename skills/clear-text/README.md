# Clear Text

Check any text written for people so that someone who reads it for the first time has no questions left: who is this about, what does this word mean, how do we know, where is it, why. The skill also builds HTML pages with a comment layer: you open the page in a browser, select a phrase, type or dictate a remark, and Claude fixes the page and adds new rules to the skill.

The skill comes in two versions with the same logic:

| Folder | Language | For texts in |
|--------|----------|--------------|
| `clear-text` | English | English |
| `ponyatnyj-tekst` | Russian | Russian |

The rules come from the author's comments on real texts: articles, research reports, interview findings, websites. Each rule is stored together with the comment it came from.

## Installation

Install the version for the language you write in. Run the commands from the `skills` folder of this repository.

**macOS / Linux:**
```bash
cp -r clear-text ~/.claude/skills/clear-text
cp -r ponyatnyj-tekst ~/.claude/skills/ponyatnyj-tekst
```

**Windows:**
```powershell
Copy-Item -Recurse clear-text $env:USERPROFILE\.claude\skills\clear-text
Copy-Item -Recurse ponyatnyj-tekst $env:USERPROFILE\.claude\skills\ponyatnyj-tekst
```

For Codex, copy the folder to `.agents/skills/` in your project.

## Usage

Say any of these to Claude Code:

- "clear text, check report.md"
- "make this text clearer"
- "make an HTML page about our onboarding flow"
- "I've commented" (after you have saved comments on a page)
- "go through my comments"

## What it does

**Clarity check.** Claude writes down the task of the text and its reader, then reads the text sentence by sentence and asks each one the questions from `references/questions.md`. Every spot where a reader would have a question is rewritten so the answer is in the sentence itself. Then `scripts/check_text.py` lists spots with suspicious signs: a sentence that starts with "It" or "This", a line number without a quote, an abbreviation without an explanation. The script only finds signs, and Claude checks each finding by eye.

**Comment pages.** Claude builds a designed HTML page and runs `scripts/add_comments_to_html.py`, which adds the comment layer on top without changing the design.

| Step | What happens |
|------|--------------|
| Page | A self-contained HTML file appears in your Downloads folder as `comments-<name>-<date-time>.html` |
| Comments | You select a phrase or hover over a paragraph and press "+ comment". Comments are kept in the browser |
| Save | "Save comments" downloads a `.json` file with the same name as the page |
| Review | You say "done". Claude finds the file, reads every comment and fixes the page |
| Learning | A new kind of reader question goes into `references/questions.md` with your quote. A good before → after pair goes into `references/examples.md` |

Claude looks for the comments file in Downloads, then on the Desktop, in Documents, in OneDrive folders and in the rest of your home folder, and asks for the path only if the file is nowhere to be found.

## The reader's questions

`references/questions.md` holds 16 questions. Each has a rule, an example and the comment it came from. A few of them:

| Question | Example of a fix |
|----------|------------------|
| Who or what is this about? | "The other question gives a different answer" → the question itself is quoted |
| How do we know? | "r03 talks about points in lines 14 and 42" → the lines are quoted |
| Where does it go? | "writes down what it fixed" → "writes it into the 'Check' column of the 'Findings' sheet" |
| Why? | "One action per link" → what goes missing from the findings without the rule |
| Could you make a slide from this paragraph? | Five rules in one paragraph → a table with an example for each |

## Dependencies

Python 3. No third-party libraries. If Python is missing, Claude will tell you to install it from python.org.

## Credits

By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT). The examples in the English version are translated from Russian.


---

# Понятный текст (RU)

Проверяет любой текст для людей так, чтобы у человека, который читает его впервые, не осталось вопросов: о ком это, что значит это слово, откуда это известно, где это лежит, почему так. Ещё навык собирает HTML-страницы со слоем комментариев: ты открываешь страницу в браузере, выделяешь фразу, пишешь или надиктовываешь замечание, а Claude исправляет страницу и дописывает в навык новые правила.

У навыка две версии с одинаковой логикой:

| Папка | Язык навыка | Для текстов на |
|-------|-------------|----------------|
| `clear-text` | английский | английском |
| `ponyatnyj-tekst` | русский | русском |

Правила выросли из комментариев автора к реальным текстам: статьям, отчётам исследований, выводам интервью, сайтам. Каждое правило хранится вместе с комментарием, из которого оно появилось.

## Установка

Ставь версию для языка, на котором пишешь. Команды запускай из папки `skills` этого репозитория.

**macOS / Linux:**
```bash
cp -r ponyatnyj-tekst ~/.claude/skills/ponyatnyj-tekst
cp -r clear-text ~/.claude/skills/clear-text
```

**Windows:**
```powershell
Copy-Item -Recurse ponyatnyj-tekst $env:USERPROFILE\.claude\skills\ponyatnyj-tekst
Copy-Item -Recurse clear-text $env:USERPROFILE\.claude\skills\clear-text
```

Для Codex скопируй папку в `.agents/skills/` своего проекта.

## Как пользоваться

Скажи Claude Code что-нибудь из этого:

- «понятный текст, проверь report.md»
- «сделай этот текст понятнее»
- «подними HTML про наш онбординг»
- «комментарии готовы» (после того как комментарии на странице сохранены)
- «разбери мои комментарии»

## Что он делает

**Проверка на понятность.** Claude записывает задачу текста и его читателя, потом читает текст по одному предложению и задаёт каждому вопросы из `references/voprosy.md`. Каждое место, где у читателя возник бы вопрос, переписывается так, чтобы ответ был в самом предложении. Потом `scripts/check_text.py` выдаёт список мест с подозрительными признаками: предложение начинается с «Это» или «Он», номер строки стоит без цитаты, сокращение не расшифровано. Программа только находит признаки, каждую находку Claude проверяет глазами.

**Страницы с комментариями.** Claude собирает HTML-страницу с дизайном и запускает `scripts/add_comments_to_html.py`: программа добавляет поверх слой комментариев и дизайн не меняет.

| Шаг | Что происходит |
|-----|----------------|
| Страница | В папке «Загрузки» появляется самостоятельный HTML-файл `kommentarii-<имя>-<дата-время>.html` |
| Комментарии | Выделяешь фразу или наводишь мышь на абзац и нажимаешь «+ комментарий». Комментарии хранятся в браузере |
| Сохранение | «Сохранить комментарии» скачивает файл `.json` с тем же именем, что у страницы |
| Разбор | Пишешь «готово». Claude находит файл, читает каждый комментарий и исправляет страницу |
| Обучение | Новый вид вопроса читателя ложится в `references/voprosy.md` с твоей цитатой. Удачная пара «было → стало» ложится в `references/primery.md` |

Файл комментариев Claude ищет в «Загрузках», потом на рабочем столе, в «Документах», в папках OneDrive и в остальной домашней папке. Путь он спрашивает, только если файла нигде нет.

## Вопросы читателя

В `references/voprosy.md` 16 вопросов. У каждого есть правило, пример и комментарий, из которого он вырос. Несколько из них:

| Вопрос | Пример правки |
|--------|---------------|
| О ком или о чём это? | «Другой вопрос даёт другой ответ» → сам вопрос приведён цитатой |
| Откуда это известно? | «У r03 про баллы есть строки 14 и 42» → строки приведены цитатами |
| Где это и куда? | «записывает, что исправил» → «записывает в колонку „Проверка“ листа „Выводы“» |
| Почему так? | «Одно действие в одной связке» → что пропадёт из выводов без этого правила |
| Можно ли сделать по абзацу слайд? | Пять правил в одном абзаце → таблица с примером на каждое |

## Зависимости

Python 3. Сторонние библиотеки не нужны. Если Python нет, Claude подскажет поставить его с python.org.

## Благодарности

Автор: [Алёна Захарова](https://github.com/alenazaharovaux) (MIT). Примеры в английской версии переведены с русского.
