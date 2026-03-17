from playwright.sync_api import sync_playwright


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            search_url = f"https://duckduckgo.com/?q={query}"
            page.goto(search_url)

            page.wait_for_timeout(3000)

            links = page.locator("a")

            count = links.count()

            for i in range(min(count, 20)):
                text = links.nth(i).inner_text()

                if text and len(text) > 20:
                    results.append(text)

                if len(results) >= 5:
                    break

            browser.close()

        return results
