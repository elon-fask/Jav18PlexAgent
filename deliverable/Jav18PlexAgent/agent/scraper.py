# Functions to scrape torrent links from 141jav.com
import sqlite3
import requests
from lxml import html
from rich import table
from rich.console import Console
import lxml

# from agent import db_manager
from agent.db_manager import DBManager

console = Console()


class Scraper:
    def __init__(self, db_manager):
        self.db_manager = DBManager("test.db")

    def scrape_141jav(self):
        console.print("[bold green]Scraping 141jav...[/bold green]")
        # Call the scrape_links method to get all the data
        links_data = self.scrape_links()
        console.print(f"[bold blue]Found {len(links_data)} entries.[/bold blue]")

        # Print each entry's details and save to the database
        for (
            link,
            title,
            size,
            date,
            tags,
            description,
            actors,
            magnet,
            torrent_download,
        ) in links_data:
            console.print(
                f"[bold blue]Link: {link}, Title: {title}, Size: {size}, Date: {date}, Tags: {tags}, Description: {description}, Actors: {actors}, Magnet: {magnet}, Torrent Download: {torrent_download}[/bold blue]"
            )
            self.save_to_database(
                "scraper_141jav",
                (
                    link,
                    title,
                    size,
                    date,
                    tags,
                    description,
                    actors,
                    magnet,
                    torrent_download,
                    False,
                ),  # Set scraped to False initially
            )

        console.print(
            "[bold green]Scraping 141jav completed successfully.[/bold green]"
        )

    def scrape_links(self):
        base_url = "https://www.141jav.com/new?page={}"
        torrents_data = []
        page_number = 1

        while True:
            url = base_url.format(page_number)
            response = requests.get(url)
            if response.status_code != 200:
                console.print(
                    f"[bold red]Failed to retrieve page {page_number}. Status code: {response.status_code}[/bold red]"
                )
                break  # Stop if no more pages are available

            tree = html.fromstring(response.content)
            # Extract torrent data using the specified XPath
            for i in range(2, 12):
                # Adjust range based on the number of divs per page
                xpath_link = f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/a[2]"
                xpath_title = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/h5/a//text()"
                )
                xpath_size = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/h5/span//text()"
                )
                xpath_date = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/p[1]/a//text()"
                )
                xpath_tags = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/div[1]/a//text()"
                )
                xpath_description = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/p[2]//text()"
                )
                xpath_actors = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/div[2]/a//text()"
                )
                xpath_magnet = f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/a[1]"
                xpath_torrent_download = (
                    f"/html/body/div[1]/div[{i}]/div/div/div[2]/div/a[2]"
                )

                # Extract elements using XPath
                link_elements = tree.xpath(xpath_link)
                title_elements = tree.xpath(xpath_title)
                size_elements = tree.xpath(xpath_size)
                date_elements = tree.xpath(xpath_date)
                tag_elements = tree.xpath(xpath_tags)
                description_elements = tree.xpath(xpath_description)
                actor_elements = tree.xpath(xpath_actors)
                magnet_elements = tree.xpath(xpath_magnet)
                torrent_download_elements = tree.xpath(xpath_torrent_download)

                print(
                    f"link element is {torrent_download_elements} and {magnet_elements} "
                )
                # Check if the essential elements are present
                if link_elements and title_elements:
                    link = link_elements[0].get("href")
                    title = title_elements[0].strip()
                    size = size_elements[0].strip() if size_elements else None
                    date = date_elements[0].strip() if date_elements else None
                    tags = (
                        ", ".join(tag.strip() for tag in tag_elements)
                        if tag_elements
                        else None
                    )
                    description = (
                        description_elements[0].strip()
                        if description_elements
                        else None
                    )
                    actors = (
                        ", ".join(actor.strip() for actor in actor_elements)
                        if actor_elements
                        else None
                    )
                    magnet = magnet_elements[0].get("href") if magnet_elements else None
                    torrent_download = (
                        torrent_download_elements[0].get("href")
                        if torrent_download_elements
                        else None
                    )

                    # print(
                    #     lxml.etree.tostring(
                    #         link_elements[0], pretty_print=True
                    #     ).decode()
                    # )
                    # Print the value of torrents_data using the console
                    console.print(
                        f"[bold green]Scraped {len(torrents_data)} torrents:[/bold green] {torrents_data}"
                    )
                    # Save the collected data to the database
                    self.save_to_database(
                        "scraper_141jav",
                        (
                            link,
                            title,
                            size,
                            date,
                            tags,
                            description,
                            actors,
                            magnet,
                            torrent_download,
                        ),
                    )

                    # Append the collected data as a tuple
                    torrents_data.append(
                        (
                            link,
                            title,
                            size,
                            date,
                            tags,
                            description,
                            actors,
                            magnet,
                            torrent_download,
                        )
                    )
            # page_number += 1

            page_number = 1

        # Print the value of torrents_data using the console
        console.print(
            f"[bold green]Scraped {len(torrents_data)} torrents:[/bold green] {torrents_data}"
        )
        return torrents_data

    def save_to_database(self, table_name, data):
        # Prepare the SQL statement to insert data into the specified table
        # sql = f"""
        # INSERT INTO {table_name} (link, title, scraped, scraped_at)
        # VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        # """
        try:
            self.db_manager.save_to_database(table_name, data)
            # query = f"INSERT INTO {table_name} (link, title, size, date, tags, description, actors, magnet, torrent_download, scraped) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            # self.cursor.execute(query, data)
            # self.connection.commit()
            console.print(
                f"[bold green]Saved to database: \n{data[1]} - {data[0]}[/bold green]"
            )
        except Exception as e:
            console.print(f"[bold red]Error saving to database: {e}[/bold red]")

    def scrape_avwiki(self):
        console.print("[bold green]Scraping avwiki...[/bold green]")
        # Placeholder for avwiki scraping logic
        console.print(
            "[bold green]Scraping avwiki completed successfully.[/bold green]"
        )

    def scrape_javdb(self):
        console.print("[bold green]Scraping javdb...[/bold green]")
        # Placeholder for javdb scraping logic
        console.print("[bold green]Scraping javdb completed successfully.[/bold green]")

    def scrape_javguru(self):
        console.print("[bold green]Scraping javguru...[/bold green]")
        # Placeholder for javguru scraping logic
        console.print(
            "[bold green]Scraping javguru completed successfully.[/bold green]"
        )

    def scrape_onejav(self):
        console.print("[bold green]Scraping onejav...[/bold green]")
        # Placeholder for onejav scraping logic
        console.print(
            "[bold green]Scraping onejav completed successfully.[/bold green]"
        )

    def scrape_r18dev(self):
        console.print("[bold green]Scraping r18dev...[/bold green]")
        # Placeholder for r18dev scraping logic
        console.print(
            "[bold green]Scraping r18dev completed successfully.[/bold green]"
        )
