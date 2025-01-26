# cli/terminal_interface.py
import os
import time
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.live import Live
from tabulate import tabulate
from agent.db_manager import DBManager

console = Console()


def start_terminal(db_manager):
    console.print("Welcome to the Plex Agent Terminal")

    while True:
        console.print("[bold green]Commands:[/bold green]")
        console.print("[1] View logs")
        console.print("[2] Check database status")
        console.print("[3] Populate data (start scraping process)")
        console.print("[4] Exit")

        command = console.input("[bold yellow]Enter command: [/bold yellow]")

        if command == "1":
            display_logs()
        elif command == "2":
            display_database_status(db_manager)
        elif command == "3":
            start_scraping_process()
        elif command == "4":
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
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Table Name", style="dim", width=20)
        table.add_column("Row Count", justify="right")

        for table_name in [
            "scraper_141jav",
            "scraper_avwiki",
            "scraper_javdb",
            "scraper_javguru",
            "scraper_onejav",
            "scraper_r18dev",
        ]:
            db_manager.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = db_manager.cursor.fetchone()[0]
            table.add_row(table_name, str(row_count))

        console.print(table)
        console.print("[bold green]Database status: OK[/bold green]")
    except sqlite3.Error as e:
        console.print(f"[bold red]Error checking database status: {e}[/bold red]")


def start_scraping_process():
    console.print("[bold green]Starting scraping process...[/bold green]")
    services = [
        "scraper_141jav",
        "scraper_avwiki",
        "scraper_javdb",
        "scraper_javguru",
        "scraper_onejav",
        "scraper_r18dev",
    ]

    for service in services:
        console.print(f"[bold blue]Running service: {service}[/bold blue]")
        # Placeholder for actual scraping logic
        time.sleep(1)  # Simulate scraping time
        console.print(f"[bold green]{service} completed successfully.[/bold green]")
