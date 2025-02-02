import time
from rich.console import Console
import os
import requests
import transmissionrpc
from rich.progress import Progress

console = Console()


def download_torrent_file(link, save_directory):
    """
    Downloads a torrent file from a given link and saves it in the specified directory.
    """
    os.makedirs(save_directory, exist_ok=True)  # Ensure directory exists
    torrent_file_path = os.path.join(save_directory, os.path.basename(link))

    response = requests.get(link, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with Progress() as progress:
        task = progress.add_task(
            "[cyan]Downloading Torrent File...[/cyan]", total=total_size
        )

        with open(torrent_file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress.update(task, advance=len(chunk))

    return torrent_file_path


def download_content_from_torrent(torrent_file_path):
    """
    Uses the torrent file to download content using Transmission.
    """
    # Connect to the Transmission daemon
    client = transmissionrpc.Client(
        "localhost",
        port=9091,
        user="transmission",
        password="{0cf9bd1f0add576abf23368a7082a0a4f90257daG6zXsIdc",
    )

    console.print(f"[bold blue]Adding torrent: {torrent_file_path}[/bold blue]")

    # Add the torrent file to Transmission
    try:
        client.add_torrent(torrent_file_path)
        console.print(
            f"[bold green]Torrent added successfully: {torrent_file_path}[/bold green]"
        )
    except Exception as e:
        console.print(f"[bold red]Error adding torrent: {e}[/bold red]")


def start_download_process(link, torrent_save_dir):
    """
    Manages the full process of downloading a torrent file and then adding it to Transmission.
    """
    try:
        console.print("[bold green]Starting download process...[/bold green]")

        # Step 1: Download the torrent file
        # torrent_file_path = download_torrent_file(link, torrent_save_dir)
        torrent_file_path = "DATA/torrentFiles/KING270.torrent"
        # Step 2: Add the torrent to Transmission for downloading
        download_content_from_torrent(torrent_file_path)

    except Exception as e:
        console.print(f"[bold red]Error during download process: {e}[/bold red]")
