from playwright.sync_api import sync_playwright


class BrowserTool:

    def search_google(self, query):

        results = []

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            search_url = f"https://www.google.com/search?q={query}"
            page.goto(search_url)

            page.wait_for_selector("h3")

            titles = page.locator("h3")

            count = titles.count()

            for i in range(min(count, 5)):
                text = titles.nth(i).inner_text()
                if text:
                    results.append(text)

            browser.close()

        return results
