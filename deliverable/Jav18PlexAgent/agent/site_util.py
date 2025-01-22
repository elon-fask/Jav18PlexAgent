import requests
from lxml import html

class BaseSite:
    def __init__(self, name, search_url, detail_url):
        self.name = name
        self.search_url = search_url
        self.detail_url = detail_url

    def fetch_page(self, url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return html.fromstring(response.content)

    def log(self, message):
        print(f"[{self.name}] {message}")