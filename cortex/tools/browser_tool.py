from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.goto(f"https://www.google.com/search?q={query}")

            page.wait_for_timeout(3000)

            html = page.content()

            soup = BeautifulSoup(html, "html.parser")

            for h in soup.find_all("h3")[:15]:

                results.append(h.text)

            browser.close()

        return results
