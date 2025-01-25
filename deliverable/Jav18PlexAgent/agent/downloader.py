# Manages downloading of torrent files and content
import os
import requests
from torrentp import Torrent


def download_content(link, save_directory):
    # Download the torrent file
    response = requests.get(link)
    torrent_file_path = os.path.join(save_directory, os.path.basename(link))

    with open(torrent_file_path, "wb") as file:
        file.write(response.content)

    # Download the content using the torrent file
    torrent = Torrent(torrent_file_path)
    torrent.download(
        save_path=save_directory
    )  # Specify the directory for downloaded content
