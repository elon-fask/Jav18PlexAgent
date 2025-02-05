import os
import time
import libtorrent as lt
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

console = Console()


def download_content_with_libtorrent(magnet_link, save_directory):
    """
    Downloads content using libtorrent from a magnet link.
    :param magnet_link: The magnet link to download.
    :param save_directory: The directory where the downloaded files will be saved.
    """
    os.makedirs(save_directory, exist_ok=True)  # Ensure the save directory exists

    # Initialize libtorrent session
    session = lt.session()
    session.listen_on(6881, 6891)

    # Add the magnet link to the session
    params = {
        "save_path": save_directory,
        "storage_mode": lt.storage_mode_t.storage_mode_sparse,
    }
    handle = lt.add_magnet_uri(session, magnet_link, params)

    console.print("[bold blue]Downloading metadata...[/bold blue]")
    while not handle.has_metadata():
        time.sleep(1)

    console.print(
        "[bold green]Metadata downloaded. Starting torrent download...[/bold green]"
    )

    # Start downloading the content
    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Downloading...", total=100)

        while handle.status().state != lt.torrent_status.seeding:
            status = handle.status()
            progress_percentage = status.progress * 100
            progress.update(task, completed=progress_percentage)
            time.sleep(1)

    console.print("[bold green]Download complete![/bold green]")


def start_download_process(magnet_link, save_directory):
    """
    Manages the full process of downloading content using libtorrent.
    :param magnet_link: The magnet link to download.
    :param save_directory: The directory where the downloaded files will be saved.
    """
    try:
        console.print("[bold green]Starting download process...[/bold green]")
        download_content_with_libtorrent(magnet_link, save_directory)
    except Exception as e:
        console.print(f"[bold red]Error during download process: {e}[/bold red]")


# def download_torrent_file(link, save_directory):
#     """
#     Downloads a torrent file from a given link and saves it in the specified directory.
#     """
#     os.makedirs(save_directory, exist_ok=True)  # Ensure directory exists
#     torrent_file_path = os.path.join(save_directory, os.path.basename(link))
#
#     response = requests.get(link, stream=True)
#     total_size = int(response.headers.get("content-length", 0))
#
#     with Progress() as progress:
#         task = progress.add_task(
#             "[cyan]Downloading Torrent File...[/cyan]", total=total_size
#         )
#
#         with open(torrent_file_path, "wb") as file:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     file.write(chunk)
#                     progress.update(task, advance=len(chunk))
#
#     return torrent_file_path
#
#
# def download_content_from_torrent(torrent_file_path):
#     """
#     Uses the torrent file to download content using Transmission.
#     """
#     # Connect to the Transmission daemon
#     client = transmissionrpc.Client(
#         "localhost",
#         port=9091,
#         user="transmission",
#         password="{0cf9bd1f0add576abf23368a7082a0a4f90257daG6zXsIdc",
#     )
#
#     console.print(f"[bold blue]Adding torrent: {torrent_file_path}[/bold blue]")
#
#     # Add the torrent file to Transmission
#     try:
#         client.add_torrent(torrent_file_path)
#         console.print(
#             f"[bold green]Torrent added successfully: {torrent_file_path}[/bold green]"
#         )
#     except Exception as e:
#         console.print(f"[bold red]Error adding torrent: {e}[/bold red]")
#
#
# def start_download_process(link, torrent_save_dir):
#     """
#     Manages the full process of downloading a torrent file and then adding it to Transmission.
#     """
#     try:
#         console.print("[bold green]Starting download process...[/bold green]")
#
#         # Step 1: Download the torrent file
#         # torrent_file_path = download_torrent_file(link, torrent_save_dir)
#         torrent_file_path = "DATA/torrentFiles/KING270.torrent"
#         # Step 2: Add the torrent to Transmission for downloading
#         download_content_from_torrent(torrent_file_path)
#
#     except Exception as e:
#         console.print(f"[bold red]Error during download process: {e}[/bold red]")
