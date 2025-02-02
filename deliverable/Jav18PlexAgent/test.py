import time
from rich.console import Console
import os
import requests
import transmissionrpc
from rich.progress import Progress

import libtorrent as lt

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
    try:
        client = transmissionrpc.Client(
            "localhost",
            port=9091,
            user="transmission",
            password="transmission",
        )
        client.get_torrents()  # Attempt to fetch the list of torrents
        print("Connected to Transmission daemon successfully!")
        console.print(f"[bold blue]Adding torrent: {torrent_file_path}[/bold blue]")

        # Add the torrent file to Transmission
        try:
            client.add_torrent(torrent_file_path)
            console.print(
                f"[bold green]Torrent added successfully: {torrent_file_path}[/bold green]"
            )
        except Exception as e:
            console.print(f"[bold red]Error adding torrent: {e}[/bold red]")

    except transmissionrpc.TransmissionError as e:
        print(f"Error connecting to Transmission daemon: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def start_download_process(link, torrent_save_dir):
    """
    Manages the full process of downloading a torrent file and then adding it to Transmission.
    """
    try:
        console.print("[bold green]Starting download process...[/bold green]")

        # Step 1: Download the torrent file
        torrent_file_path = download_torrent_file(link, torrent_save_dir)

        # Step 2: Add the torrent to Transmission for downloading
        download_content_from_torrent(torrent_file_path)

    except Exception as e:
        console.print(f"[bold red]Error during download process: {e}[/bold red]")


def torrent_downloader(torrent_magnet_link, params):
    ses = lt.session()
    handle = lt.add_magnet_uri(ses, torrent_magnet_link, params)
    console.print("[bold green] Downloading metadata... [/bold green]")


if __name__ == "__main__":
    print("heheh")
    # start_download_process(
    #     "https://www.141jav.com/download/KING270.torrent", "DATA/mp4"
    # )

    ses = lt.session()
    params = {"save_path": "DATA/mp4"}
    link = "magnet:?xt=urn:btih:753f1ed712dd2967f2874c7fb8f838dca0f8c512&dn=%2B%2B%2B%20%5BFHD%5D%20KING-270%20%E7%B7%8F%E9%A1%8D100%E4%B8%87%E5%86%86%EF%BC%81%EF%BC%81%E3%81%8A%E5%B9%B4%E7%8E%89%E4%BA%89%E5%A5%AA%E3%83%81%E3%82%AD%E3%83%81%E3%82%AD%E6%A5%B5%E5%A4%AA%E3%83%87%E3%82%A3%E3%83%AB%E3%83%89%E6%A4%85%E5%AD%90%E5%8F%96%E3%82%8A%E3%82%B2%E3%83%BC%E3%83%A0%EF%BC%81%20%E9%9F%B3%E6%A5%BD%E6%AD%A2%E3%81%BE%E3%81%A3%E3%81%9F%E3%82%89%E3%83%9E%E3%80%87%E3%82%B3%E3%81%AB%E3%83%87%E3%82%A3%E3%83%AB%E3%83%89%E3%82%92%E6%8C%BF%E5%85%A5%EF%BC%813%E5%88%86%E9%96%93%E8%85%B0%E3%82%92%E6%8C%AF%E3%81%A3%E3%81%A6%E6%BD%AE%E3%82%92%E5%90%B9%E3%81%91%E3%81%9F%E3%82%89%E3%82%AF%E3%83%AA%E3%82%A2%EF%BC%81%20%E5%A4%B1%E6%95%97%E3%81%97%E3%81%9F%E3%82%89%E5%8D%B3%E3%83%8F%E3%83%A1%E4%B8%AD%E5%87%BA%E3%81%97%E7%BD%B0%E3%82%B2%E3%83%BC%E3%83%A0%EF%BC%81%E4%BA%88%E9%81%B8%E7%B7%A8&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
    handle = lt.add_magnet_uri(ses, link, params)

    print("downloading metadata...")
    while not handle.has_metadata():
        time.sleep(1)
    print("got metadata, starting torrent download...")
    while handle.status().state != lt.torrent_status.seeding:
        print("%d %% done" % (handle.status().progress * 100))
        time.sleep(1)
    print("finished")
