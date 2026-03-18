import requests
from bs4 import BeautifulSoup


class BrowserTool:

    def search_google(self, query):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # force latest results
        query = query + " 2025 2026 latest laptop specs"

        url = f"https://www.google.com/search?q={query}&num=10"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for g in soup.select("div.g"):

            title = g.select_one("h3")
            desc = g.select_one("span")

            if title:
                text = title.text

                # remove old models
                if "2021" in text or "2022" in text or "2023" in text:
                    continue

                results.append(text)

        return results[:10]
