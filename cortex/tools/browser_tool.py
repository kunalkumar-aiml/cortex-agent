from playwright.sync_api import sync_playwright


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Use DuckDuckGo HTML version (stable for scraping)
            url = f"https://duckduckgo.com/html/?q={query}"

            page.goto(url)

            page.wait_for_timeout(3000)

            elements = page.locator("a.result__a")

            count = elements.count()

            for i in range(min(count, 5)):
                text = elements.nth(i).inner_text()
                results.append(text)

            browser.close()

        return results
