# Entry point for the Plex Agent application
from agent.scraper import scrape_links
from agent.downloader import download_torrent
from agent.db_manager import initialize_db, check_recorded
from cli.terminal_interface import start_terminal


def main():
    initialize_db()  # Set up the SQLite database
    while True:
        links = scrape_links()  # Scrape links from defined websites
        for link in links:
            if not check_recorded(link):  # Check if link is already recorded
                download_torrent(link)  # Download the torrent file
        start_terminal()  # Start the interactive terminal interface


if __name__ == "__main__":
    main()
