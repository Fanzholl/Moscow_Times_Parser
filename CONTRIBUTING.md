# Руководство по внесению вкладов

Спасибо за интерес к проекту.  
Проект небольшой, но открыт для идей, улучшений и исправлений.

## Как внести вклад

### 1) Форк
Сделайте fork репозитория и работайте в своей копии.

### 2) Создайте ветку
Используйте отдельную ветку для задачи:

```bash
git checkout -b feature/my-feature
````

или

```bash
git checkout -b fix/my-bugfix
```

### 3) Внесите изменения

Пишите понятно, избегайте лишних зависимостей.

### 4) Проверьте

Убедитесь, что изменения работают и не ломают существующую логику.

### 5) Коммиты

Рекомендуемые префиксы:

* `feat:` — новая функциональность
* `fix:` — исправление
* `docs:` — документация
* `refactor:` — рефакторинг

### 6) Pull Request

Создайте PR в `main` и опишите:

* что изменили
* почему
* как тестировали

При изменениях в CLI или UI можно приложить скриншоты/GIF.

---

## Стиль кода

* Пишите ясно и читаемо
* Аккуратные импорты
* Без мёртвого кода
* Понятные имена
* Python 3.10+

Типизация приветствуется, но не обязательна.

---

## Документация

Если добавляете новую функциональность — коротко опишите её в README.

---

## Сообщения об ошибках

Если нашли баг, укажите:

* краткое описание
* шаги воспроизведения
* ожидаемое поведение
* версию Python / ОС
* логи/скрин, если есть

---

## Идеи и предложения

Создайте Issue или черновик PR для обсуждения.

---

## Не нужно

* Тяжёлых зависимостей без веской причины
* Излишнего усложнения
* Ломающих изменений без аргументации

---

## Кратко

1. Форк
2. Ветка
3. Код
4. PR
5. Описание

Спасибо за вклад!

---

````markdown
# Contributing Guidelines

Thank you for your interest in contributing.  
This is a small project, but it is open to ideas, improvements, and bug fixes.

## How to Contribute

### 1) Fork
Fork the repository and work in your own copy.

### 2) Create a Branch
Use a dedicated branch for your change:

```bash
git checkout -b feature/my-feature
````

or

```bash
git checkout -b fix/my-bugfix
```

### 3) Make Changes

Keep the code clear and focused.
Avoid unnecessary dependencies.

### 4) Test

Ensure your changes run correctly and do not break existing behavior.

### 5) Commit

Recommended commit prefixes:

* `feat:` — new feature
* `fix:` — bug fix
* `docs:` — documentation
* `refactor:` — code restructuring

### 6) Pull Request

Open a PR into `main`, describing:

* what was changed
* why
* how it was tested

Include screenshots/GIFs for visual or CLI-related changes if helpful.

---

## Code Style

* Write clear, readable code
* Keep imports clean
* Remove dead code
* Use meaningful names
* Python 3.10+

Type hints are encouraged but not required.

---

## Documentation

If adding new functionality, update README with basic usage instructions.

---

## Reporting Issues

If reporting a bug, please include:

* short description
* reproduction steps
* expected behavior
* Python version / OS
* logs or screenshot if relevant

---

## Ideas & Suggestions

Open an Issue or draft PR to discuss proposals.

---

## Not Needed

* Heavy dependencies without strong justification
* Overcomplication
* Breaking changes without solid reasoning

---

## Summary

1. Fork
2. Branch
3. Code
4. Pull Request
5. Describe your change

Thank you for contributing.
