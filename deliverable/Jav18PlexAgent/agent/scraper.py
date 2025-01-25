# Functions to scrape torrent links from 141jav.com
import requests
from lxml import html


def scrape_links():
    base_url = "https://www.141jav.com/new?page={}"
    links = []
    page_number = 1

    while True:
        url = base_url.format(page_number)
        response = requests.get(url)
        if response.status_code != 200:
            break  # Stop if no more pages are available

        tree = html.fromstring(response.content)
        # Extract links using the specified XPath
        for i in range(1, 12):  # Adjust range based on the number of divs per page
            xpath = f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/a[2]"
            elements = tree.xpath(xpath)
            if elements:
                links.append(
                    elements[0].get("href")
                )  # Append the href attribute of the link

        page_number += 1

    return links
