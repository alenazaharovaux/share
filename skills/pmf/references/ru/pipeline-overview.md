# PMF Pipeline Overview — карта переходов

State machine для скилла `pmf`. Каждая стадия читает артефакты предыдущих, пишет свои. Папка проекта — это и есть state machine.

## Базовый поток (happy path)

```
Stage 0 (Setup)
   ↓ создаёт 00_setup.md
Stage 1 (Hypothesis)
   ↓ создаёт narrative-v1.md
Stage 2 (Market Research)
   ↓ создаёт market-research.md
Stage 3 (Synthesis)
   ↓ создаёт risk-prioritization.md, narrative-v2.md
Stage 4 (Validate / DVF)
   ↓ создаёт assumptions-map.md, experiment-brief.md
Stage 5 (Interview Prep)
   ↓ создаёт interview-guide.md
Stage 6 [Field — вне скилла]
   ↓ пользователь заполняет interviews/notes/*.md
Stage 7 (Interview Synthesis)
   ↓ создаёт interview-synthesis.md, narrative-v3.md
Stage 8 [MVP Launch — вне скилла]
   ↓ пользователь запускает MVP
Stage 9 (Metrics)
   ↓ создаёт metrics-dashboard.md
Stage 10 (Iterate)
   ↓ создаёт iteration-changelog.md → возврат к нужной стадии
```

## Правила определения текущей стадии

Скилл проверяет файлы в папке проекта в порядке от поздних стадий к ранним. Первое совпадение = текущая стадия.

| Найден файл | Текущая стадия |
|-------------|----------------|
| `iteration-changelog.md` (последний) | Stage 10 — итерация (возврат к стадии указанной в changelog) |
| `metrics-dashboard.md` | Stage 9 done |
| `narrative-v3.md` + `interview-synthesis.md` | Stage 7 done → ожидание Stage 8 |
| ≥1 файл в `interviews/notes/` | Stage 6 (в процессе или завершено), готов к Stage 7 |
| `interview-guide.md` | Stage 5 done → ожидание Stage 6 |
| `assumptions-map.md` | Stage 4 done, готов к Stage 5 |
| `narrative-v2.md` + `risk-prioritization.md` | Stage 3 done, готов к Stage 4 |
| `market-research.md` | Stage 2 done, готов к Stage 3 |
| `narrative-v1.md` | Stage 1 done, готов к Stage 2 |
| `00_setup.md` | Stage 0 done, готов к Stage 1 |
| Папка пуста | Stage 0 |

## Возможные нелинейные переходы

PMF не всегда идёт по прямой. Скилл должен поддерживать возвраты и циклы:

### Возврат после Stage 3 (Synthesis)

| Условие | Действие |
|---------|----------|
| Overall confidence > 7 + есть конкретный риск-dimension | → Stage 4 (validate) или Stage 5 (interviews) |
| Overall confidence 4-7 | → Stage 4 обязателен |
| Overall confidence < 4 | → Возврат к Stage 1 (rethink hypothesis) или Stage 2 (больше рисёрча) |
| Cross-fit conflict обнаружен (Channel-Model или Model-Market) | → Возврат к Stage 1 для пересмотра конфликтующих dimensions |

### Возврат после Stage 4 (DVF)

| Условие | Действие |
|---------|----------|
| Эксперимент успешен | → Stage 5 (interviews для других риск-dimensions) |
| Эксперимент провален | → Stage 1 (рестарт dimension) или Stage 2 (рисёрч альтернатив) |
| Нужно больше данных | → Stage 2 (рисёрч) или сразу Stage 5-6 (интервью) |

### Возврат после Stage 7 (Interview Synthesis)

| Условие | Действие |
|---------|----------|
| Confidence повысился, гипотеза подтверждена | → Stage 8 (запуск MVP) |
| Confidence упал, нужны корректировки | → Stage 4 (новые assumptions) или Stage 1 (новая hypothesis) |
| Открылась новая риск-dimension | → Stage 4 для неё |
| Появилось предположение что нужен pivot | → Stage 1, явно зафиксировав почему |

### Возврат после Stage 9 (Metrics)

| Условие | Действие |
|---------|----------|
| PMF достигнут (Sean Ellis ≥40% + retention flatten + Level 3+) | → Out of scope (scale phase) |
| Промежуточный сигнал (Level 2) | → Stage 4 (новая итерация валидации) или Stage 7 (новый цикл интервью) |
| Слабый сигнал (Level 1, Sean Ellis <25%) | → Stage 1 (rethink) или Stage 2 (новый рисёрч) |

## Обработка состояний ожидания (Stage 6 и Stage 8)

Эти стадии — **вне скилла**. Скилл при возобновлении на них:

**Stage 6 (Field interviews):**
- Проверить наличие `interview-guide.md` → должен быть
- Проверить `interviews/notes/` — есть ли файлы?
  - 0 файлов → «жду заметки. Готов гайд: interview-guide.md. Сколько провёл уже?»
  - 1-14 файлов → «продолжай поле. Когда соберёшь ≥15 — переход к Stage 7. Провести синтез на текущих данных тоже можно, но менее надёжно»
  - 15+ файлов → «можно переходить к Stage 7. Готов?»
- Не предлагать «провести интервью за пользователя»

**Stage 8 (MVP launch):**
- Проверить `narrative-v3.md` → должен быть
- Сообщить «жду MVP. Когда соберёшь ~40 active users — Stage 9»
- Можно обсудить технические/продуктовые вопросы запуска как собеседник, но не «запустить MVP»

## Версионирование narrative

Narrative — центральный документ всего цикла. Версионируется на ключевых переходах:

| Версия | Когда создаётся | На основе чего |
|--------|----------------|----------------|
| **V1** | После Stage 1 | Initial hypothesis |
| **V2** | После Stage 3 | Market research данные |
| **V3** | После Stage 7 | Interview данные |
| **V4+** | После Stage 10, если итерация | Metrics + решения |

Каждая версия — отдельный файл (`narrative-v1.md`, `narrative-v2.md`, ...). НЕ перезаписывать предыдущие. В каждой новой версии — секция «Version History» с changelog.

## Файловые контракты между стадиями

Что каждая стадия читает и пишет:

| Stage | Reads | Writes |
|-------|-------|--------|
| 0 | — | `00_setup.md` |
| 1 | `00_setup.md` | `narrative-v1.md` |
| 2 | `narrative-v1.md` | `market-research.md` |
| 3 | `narrative-v1.md`, `market-research.md` | `risk-prioritization.md`, `narrative-v2.md` |
| 4 | `narrative-v2.md`, `risk-prioritization.md` | `assumptions-map.md`, `experiment-brief.md` |
| 5 | `narrative-v2.md`, `risk-prioritization.md`, `assumptions-map.md` | `interview-guide.md`, `interviews/note-template.md` |
| 7 | `narrative-v2.md`, `interviews/notes/*.md` | `interview-synthesis.md`, `narrative-v3.md` |
| 9 | `narrative-v3.md` | `metrics-dashboard.md` |
| 10 | `metrics-dashboard.md` + всё предыдущее | `iteration-changelog.md` |
