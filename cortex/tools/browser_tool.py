import requests
from bs4 import BeautifulSoup


class BrowserTool:

    def search_google(self, query):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        url = f"https://www.google.com/search?q={query}"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for h in soup.select("h3")[:15]:
            results.append(h.text)

        return results
