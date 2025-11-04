# Moscow Times News Parser

Небольшой скрипт на Python, который парсит свежие новости с раздела  
**https://www.moscowtimes.ru/news**  
и сохраняет их в текстовые файлы, сгруппированные по дате.

## 📌 Что делает скрипт

- Открывает страницу новостей The Moscow Times
- Извлекает:
  - дату публикации
  - время
  - заголовок
  - ссылку на новость
- Группирует новости по дате (в формате `ДД.ММ.ГГГГ`)
- Сохраняет их в текстовые файлы (`./news/articles-<date>.txt`)
- Дублирует результат в консоль
- Создаёт директорию `./news`, если её нет

Скрипт работает **на Playwright**, запускает Chromium в headless-режиме.

---

## 🧰 Технологии

- Python 3.10+
- Playwright
- Регулярные выражения
- OS / filesystem API

---

Мить, без лишнего — правлю блок **Установка** под **UV**.
Вставляй это вместо pip-версии.

---

## 📦 Установка

### 1) Создать окружение и установить зависимости через **uv**

```bash
# создать виртуальное окружение (опционально)
uv venv
source .venv/bin/activate
```

```bash
# установить Playwright
uv pip install playwright
```

```bash
# установить браузеры (Chromium)
playwright install chromium
```

> **Важно:** `playwright install` ставит бинарники браузера — это не Python-зависимости, поэтому оно вызывается отдельно.

---

## ✅ Итоговый быстрый набор

```bash
git clone https://github.com/Fanzholl/Moscow_Times_Parser
cd Moscow_Times_Parser

uv venv
source .venv/bin/activate

uv pip install playwright
playwright install chromium
```

---

# Moscow Times News Parser

A small Python script that scrapes fresh news from
**[https://www.moscowtimes.ru/news](https://www.moscowtimes.ru/news)**
and saves them into text files grouped by date.

## 📌 What the script does

* Opens the Moscow Times news page
* Extracts:

  * publication date
  * time
  * title
  * link
* Groups news by date (`DD.MM.YYYY`)
* Saves them to text files (`./news/articles-<date>.txt`)
* Prints extracted data to console
* Creates `./news` directory if it does not exist

The script uses **Playwright** and runs Chromium in headless mode.

---

## 🧰 Tech Stack

* Python 3.10+
* Playwright
* Regular expressions
* OS / filesystem API

---

## 📦 Installation

### 1) Create a virtual environment & install dependencies via **uv**

```bash
# create virtual environment (optional)
uv venv
source .venv/bin/activate
```

```bash
# install Playwright
uv pip install playwright
```

```bash
# install browsers (Chromium)
playwright install chromium
```

> **Note:** `playwright install` downloads browser binaries —
> it is not a Python dependency so it must be installed separately.

---

## ✅ Quick Setup

```bash
git clone https://github.com/Fanzholl/Moscow_Times_Parser
cd Moscow_Times_Parser

uv venv
source .venv/bin/activate

uv pip install playwright
playwright install chromium
```

---

## ✈️ Telegram: **[blacksunder](https://t.me/blacksunder)**
## 📧 Mail: **[whiteparser@icloud.com](mailto:whiteparser@icloud.com)**


