# verify-sources

A Claude Code skill that checks sources with a program. Each statement of a report is written to `claims.json` together with its source and a verbatim quote. The program opens every source, looks for the quote in its text and checks that every number from the statement is in both the quote and the source. For DOIs it reads metadata from doi.org and abstracts from Europe PMC, OpenAlex, Crossref and Semantic Scholar. The result is `verification.md` with lists: confirmed, partly confirmed, number not confirmed, quote not found, source not read. A fresh session then opens the unconfirmed sources itself and writes `review.md`.

Use it on its own to check a finished report, a literature review or someone else's methodology. It is also a required part of [desk-research](../desk-research/): that skill collects the quotes, this one checks them. To run desk research, install both skills into the same skills folder.

## Why

In the author's [KINEMETRIC experiment](https://kinemetric.vercel.app/) six models wrote a literature review. All 60 links were live, and one model invented all the content around them and wrote "everything checked via PubMed" without opening a single source. A live link proves nothing, and a phrase like "all checked" counts only when a verification file stands behind it.

## Installation

Open Claude Code or Codex in any folder and send the agent this message:

> Install the verify-sources skill from https://github.com/alenazaharovaux/share following skills/verify-sources/INSTALL-AGENT.md

The agent asks whether to add desk-research as well, downloads the folders, puts them into your personal skills folder, checks Python and, in Codex, turns on internet access for scripts. You do not need to look for any folders yourself.

<details>
<summary>Manual install</summary>

Run the commands from the `skills` folder of this repository.

**macOS / Linux:**
```bash
cp -r desk-research ~/.claude/skills/desk-research
cp -r verify-sources ~/.claude/skills/verify-sources
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse desk-research $env:USERPROFILE\.claude\skills\desk-research
Copy-Item -Recurse verify-sources $env:USERPROFILE\.claude\skills\verify-sources
```

For Codex, copy both folders to `~/.agents/skills/`.
</details>

## First run

No setup questions. The skill needs Python 3.8+ and internet access for scripts. In Codex, enable it once in `~/.codex/config.toml`: `[sandbox_workspace_write]` → `network_access = true`. Without it the program cannot open any source.

## Usage

- "verify sources in report.md"
- "check the quotes and numbers in this literature review"
- "did the agent invent any sources?"
- "проверь источники в отчёте"

## Dependencies

Python 3.8+, standard library only. The `check_counts.py` script that compares counts between the report and `claims.json` lives in desk-research.

The skill and its texts are in Russian. Claude talks to you in your language.

By [Alena Zakharova](https://github.com/alenazaharovaux) · MIT

---

# verify-sources (RU)

Навык Claude Code проверяет источники программой. Каждое утверждение отчёта записывается в `claims.json` вместе с источником и дословной цитатой. Программа открывает каждый источник, ищет цитату в его тексте и проверяет, что каждое число из утверждения есть и в цитате, и в источнике. Для DOI она берёт метаданные из doi.org и аннотации из Europe PMC, OpenAlex, Crossref и Semantic Scholar. Итог — файл `verification.md` со списками: подтверждено, подтверждено частично, число не подтверждено, цитата не найдена, источник не прочитан. Потом новая сессия сама открывает неподтверждённые источники и пишет `review.md`.

Навык можно запускать отдельно, чтобы проверить готовый отчёт, обзор литературы или чужую методологию. Ещё он обязательная часть навыка [desk-research](../desk-research/): тот собирает цитаты, этот их проверяет. Для кабинетного исследования поставьте оба навыка в одну папку навыков.

## Зачем

В [эксперименте KINEMETRIC](https://kinemetric.vercel.app/) автора навыка шесть моделей писали обзор литературы. Все 60 ссылок оказались живыми. Одна модель выдумала всё содержание вокруг них и написала «всё проверено через PubMed», не открыв ни одного источника. Живая ссылка ничего не доказывает. Фраза «всё проверено» считается, только если за ней стоит файл проверки.

## Установка

Откройте Claude Code или Codex в любой папке и напишите агенту:

> Установи навык verify-sources из https://github.com/alenazaharovaux/share по файлу skills/verify-sources/INSTALL-AGENT.md

Агент спросит, ставить ли заодно desk-research, сам скачает папки, положит их в вашу папку навыков, проверит Python, а в Codex включит интернет для программ. Искать папки самим не нужно.

<details>
<summary>Установка вручную</summary>

Команды запускаются из папки `skills` этого репозитория.

**macOS / Linux:**
```bash
cp -r desk-research ~/.claude/skills/desk-research
cp -r verify-sources ~/.claude/skills/verify-sources
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse desk-research $env:USERPROFILE\.claude\skills\desk-research
Copy-Item -Recurse verify-sources $env:USERPROFILE\.claude\skills\verify-sources
```

Для Codex скопируйте обе папки в `~/.agents/skills/`.
</details>

## Первый запуск

Вопросов при первом запуске нет. Нужны Python 3.8 или новее и интернет для скриптов. В Codex интернет включают один раз в `~/.codex/config.toml`: `[sandbox_workspace_write]` → `network_access = true`. Без этой строки программа не откроет ни одного источника.

## Как запускать

- «проверь источники в report.md»
- «сверь цитаты и цифры в этом обзоре»
- «не выдумал ли агент источники»
- «verify sources»

## Что нужно установить

Python 3.8 или новее, только стандартная библиотека. Скрипт `check_counts.py`, который сверяет числа между отчётом и `claims.json`, лежит в desk-research.

Навык и его тексты на русском. С вами Claude говорит на вашем языке.

Автор — [Алёна Захарова](https://github.com/alenazaharovaux) · MIT
