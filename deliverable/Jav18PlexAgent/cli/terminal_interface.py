# cli/terminal_interface.py
import os
import time
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.live import Live
from tabulate import tabulate
from agent import db_manager
from agent.db_manager import DBManager
from agent.scraper import Scraper

from agent.downloader import start_download_process
import sqlite3

console = Console()

# Define default directories
DEFAULT_TORRENT_DIR = "DATA/torrentFiles"
DEFAULT_CONTENT_DIR = "DATA/mp4"


def start_terminal(db_manager):
    console.print("Welcome to the Plex Agent Terminal")

    while True:
        console.print("[bold green]Commands:[/bold green]")
        console.print("[1] View logs")
        console.print("[2] Check database status")
        console.print("[3] Populate data (start scraping process)")
        console.print("[4] Download content")
        console.print("[0] Exit")

        command = console.input("[bold yellow]Enter command: [/bold yellow]")

        if command == "1":
            display_logs()
        elif command == "2":
            display_database_status(db_manager)
        elif command == "3":
            start_scraping_process(db_manager)
        elif command == "4":
            while True:  # Ensure a non-empty torrent URL
                torrent_url = console.input(
                    "[bold blue]Enter torrent link (required): [/bold blue]"
                ).strip()
                if torrent_url:
                    break
                console.print("[bold red]Torrent link cannot be empty![/bold red]")

            # Ask for save directories, use default if nothing is entered
            torrent_save_dir = console.input(
                f"[bold blue]Enter folder to save torrent files (default: {DEFAULT_TORRENT_DIR}): [/bold blue]"
            ).strip()
            content_save_dir = console.input(
                f"[bold blue]Enter folder to save downloaded content (default: {DEFAULT_CONTENT_DIR}): [/bold blue]"
            ).strip()

            # Use defaults if user input is empty
            torrent_save_dir = (
                torrent_save_dir if torrent_save_dir else DEFAULT_TORRENT_DIR
            )
            content_save_dir = (
                content_save_dir if content_save_dir else DEFAULT_CONTENT_DIR
            )

            # Ensure directories exist
            os.makedirs(torrent_save_dir, exist_ok=True)
            os.makedirs(content_save_dir, exist_ok=True)

            start_download_process(torrent_url, torrent_save_dir)
        elif command == "0":
            console.print("[bold red]Exiting terminal.[/bold red]")
            break
        else:
            console.print("[bold red]Invalid command. Please try again.[/bold red]")


def display_logs():
    console.print("[bold green]Displaying logs...[/bold green]")
    # Placeholder for log display
    with Progress() as progress:
        task = progress.add_task("[green]Loading logs...", total=100)
        while not task.finished:
            time.sleep(0.1)
            task.advance(1)
    console.print("[bold green]Logs displayed successfully.[/bold green]")


def display_database_status(db_manager):
    console.print("[bold green]Checking database status...[/bold green]")
    try:
        # Step 1: Display table row counts
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Table Name", style="dim", width=20)
        table.add_column("Row Count", justify="right")

        # List of all table names
        table_names = [
            "scraper_141jav",
            "scraper_avwiki",
            "scraper_javdb",
            "scraper_javguru",
            "scraper_onejav",
            "scraper_r18dev",
        ]

        # Display row counts for all tables
        for table_name in table_names:
            db_manager.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = db_manager.cursor.fetchone()[0]
            table.add_row(table_name, str(row_count))

        console.print(table)

        # Step 2: Display detailed table contents
        for table_name in table_names:
            console.print(f"\n[bold blue]Contents of {table_name}:[/bold blue]")

            # Fetch column names dynamically
            db_manager.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [info[1] for info in db_manager.cursor.fetchall()]  # Column names

            # Query all rows from the table
            db_manager.cursor.execute(f"SELECT * FROM {table_name}")
            rows = db_manager.cursor.fetchall()

            # Print the table using tabulate if there are rows
            if rows:
                print(tabulate(rows, headers=columns, tablefmt="grid"))
            else:
                console.print(
                    f"[italic]No data available in {table_name} table.[/italic]"
                )

        console.print("[bold green]Database status: OK[/bold green]")
    except sqlite3.Error as e:
        console.print(f"[bold red]Error checking database status: {e}[/bold red]")


def start_scraping_process(db_manager):
    console.print("[bold green]Starting scraping process...[/bold green]")

    services = [
        "scraper_141jav",
        "scraper_avwiki",
        "scraper_javdb",
        "scraper_javguru",
        "scraper_onejav",
        "scraper_r18dev",
    ]
    scraper = Scraper(db_manager)
    for service in services:
        console.print(f"[bold blue]Running service: {service}[/bold blue]")

        # Ask user if they want to skip the service
        skip = console.input(
            "[bold yellow]Do you want to skip this service? (y/n): [/bold yellow]"
        )
        if skip.lower() == "y":
            console.print(f"[bold red]Skipping service: {service}[/bold red]")
            continue

        if service == "scraper_141jav":
            scraper.scrape_141jav()
        elif service == "scraper_avwiki":
            scraper.scrape_avwiki()
        elif service == "scraper_javdb":
            scraper.scrape_javdb()
        elif service == "scraper_javguru":
            scraper.scrape_javguru()
        elif service == "scraper_onejav":
            scraper.scrape_onejav()
        elif service == "scraper_r18dev":
            scraper.scrape_r18dev()
        else:
            console.print(
                f"[bold green]{service} is a placeholder service. Skipping...[/bold green]"
            )

        console.print(f"[bold green]{service} completed successfully.[/bold green]")
        time.sleep(1)  # Simulate scraping time
