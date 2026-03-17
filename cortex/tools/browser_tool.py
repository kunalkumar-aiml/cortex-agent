from playwright.sync_api import sync_playwright


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            search_url = f"https://www.google.com/search?q={query}"
            page.goto(search_url)

            elements = page.query_selector_all("h3")

            for el in elements[:5]:
                results.append(el.inner_text())

            browser.close()

        return results
