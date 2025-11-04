import re
import os
from collections import defaultdict
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.moscowtimes.ru/news", timeout=30000)
        page.wait_for_load_state("domcontentloaded")

        title = page.title()
        print(f"Page is loaded. Its title is: {title}\n")

        page.wait_for_selector(".article-excerpt-default--news", timeout=10000)
        articles = page.locator(".article-excerpt-default--news")
        articles_count = articles.count()

        summary = defaultdict(list)

        for i in range(articles_count):
            article = articles.nth(i)
            href = article.locator("a").get_attribute("href") or ""

            match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", href)
            if match:
                y, m, d = match.groups()
                date = f"{d}.{m}.{y}"
            else:
                date = "—"

            time = article.locator("span").nth(0).text_content().strip()
            title = article.locator("span").nth(1).text_content().strip().replace("\xa0", " ")

            summary[date].append({
                "time": time,
                "title": title,
                "href": href
            })

        browser.close()

        os.makedirs("./news", exist_ok=True)

        for date, news in summary.items():
            file_path = f"./news/articles-{date}.txt"

            # запись
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"=== Новости за {date} ===\n\n")
                for article in news:
                    file.write(f"[{article['time']}] {article['title']}\n{article['href']}\n\n")

            # чтение
            with open(file_path, "r", encoding="utf-8") as file:
                file_summary = file.read()
                print(file_summary)

            print(f"✅ {len(news)} новостей сохранено\n")


if __name__ == "__main__":
    main()
