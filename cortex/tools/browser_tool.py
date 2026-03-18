import requests
from bs4 import BeautifulSoup


class BrowserTool:

    def search_google(self, query):

        url = f"https://www.google.com/search?q={query}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        results = []

        for g in soup.select("div.tF2Cxc")[:5]:

            title = g.select_one("h3")

            if title:
                results.append(title.text)

        return results
