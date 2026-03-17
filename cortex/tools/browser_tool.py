from playwright.sync_api import sync_playwright


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            search_url = f"https://www.google.com/search?q={query}"
            page.goto(search_url)

            page.wait_for_timeout(2000)

            elements = page.locator("h3")

            count = elements.count()

            for i in range(min(5, count)):
                results.append(elements.nth(i).inner_text())

            browser.close()

        return results
