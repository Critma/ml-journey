# UNIX Commands Exercises — DS Track

## Требования

### Упражнение 00
- Скопировать `hh.json` в `ex00/`
- Убедиться, что файл содержит 20 вакансий Data Scientist в pretty-printed JSON

### Упражнение 01 — Преобразование JSON в CSV
- Файлы: `filter.jq`, `json_to_csv.sh`, `hh.csv`
- Задача: извлечь 5 столбцов (`id`, `created_at`, `name`, `has_test`, `alternate_url`) из JSON и сохранить в CSV
- Использовать `jq` с фильтром из отдельного файла

### Упражнение 02 — Сортировка файла
- Файлы: `sorter.sh`, `hh_sorted.csv`
- Задача: отсортировать CSV по `created_at` по убыванию, затем по `id` по возрастанию
- Сохранить заголовок в первой строке

### Упражнение 03 — Замена строк в файле
- Файлы: `cleaner.sh`, `hh_positions.csv`
- Задача: извлечь уровень позиции (Junior/Middle/Senior) из названия, заменить остальное на "-". Поддержка множественных уровней (Middle/Senior)
- CSV должен быть отсортирован как в ex02

### Упражнение 04 — Описательная статистика
- Файлы: `counter.sh`, `hh_uniq_positions.csv`
- Задача: посчитать количество уникальных значений в столбце `name`, отсортировать по убыванию

### Упражнение 05 — Разбиение и конкатенация
- Файлы: `partitioner.sh`, `concatenator.sh`
- Задача: разбить CSV по дате (из столбца `created_at`) на отдельные файлы, затем объединить обратно
- Результат должен совпадать с результатом ex03

## Результат

| Упражнение | Результат |
|------------|-----------|
| ex00 | `hh.json` — 20 вакансий Data Scientist |
| ex01 | `hh.csv` — 20 строк и заголовкок |
| ex02 | `hh_sorted.csv` — сортировка по дате по убыванию и id по возрастанию |
| ex03 | `hh_positions.csv` — извлечён уровень (Junior/Middle/Senior/-) |
| ex04 | `hh_uniq_positions.csv` — статистика по грейдам |
| ex05 | скрипты `partitioner.sh` и `concatenator.sh` |

## Технологии

- **jq** - json analyze
- **gawk\awk** - text processor
- **sort**

## Результат анализа файла

- **Junior**: 15 вакансий (75%)
- **Middle**: 1 вакансия (5%)
- **Senior**: 0 вакансий
- **- (не определено)**: 4 вакансии (20%)

---

**Структура каталога:**
```
ex00/
├── hh.json

ex01/
├── filter.jq
├── hh.csv
└── json_to_csv.sh

ex02/
├── hh_sorted.csv
└── sorter.sh

ex03/
├── cleaner.sh
└── hh_positions.csv

ex04/
├── counter.sh
└── hh_uniq_positions.csv

ex05/
├── concatenator.sh
├── partitioner.sh
```
