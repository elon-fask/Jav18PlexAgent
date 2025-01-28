# agent/db_manager.py
import sqlite3
import os
from rich.console import Console


console = Console()


class DBManager:
    def __init__(self, db_path="test.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        # self.initialize_database()
        self.initialize_tables()

    def initialize_database(self):
        if not os.path.exists(self.db_path):
            console.print(
                "[bold yellow]Database does not exist. Creating a new database...[/bold yellow]"
            )
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            self.initialize_tables()
        else:
            console.print("[bold green]Database already exists.[/bold green]")
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

    def save_to_database(self, table_name, data):
        try:
            query = f"INSERT INTO {table_name} (link, title, size, date, tags, description, actors, magnet, torrent_download, scraped) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            print(f"Error saving to database: {e}")

    def initialize_tables(self):
        # Create tables if they do not exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_141jav (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_avwiki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_javdb (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_javguru (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_onejav (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_r18dev (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            title TEXT,
            size TEXT, -- Use TEXT for sizes to accommodate flexible formats (e.g., "1.5 GB")
            date DATETIME, -- Storing the date as DATETIME for better queries
            tags TEXT, -- A comma-separated list of tags
            description TEXT, -- Long descriptions
            actors TEXT, -- A comma-separated list of actors
            magnet TEXT, -- Magnet link for torrents
            torrent_download TEXT, -- URL for direct torrent download
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically store record creation time
            scraped BOOLEAN DEFAULT FALSE,
            torrent_link_scraped BOOLEAN DEFAULT FALSE,
            torrent_link TEXT,
            downloaded BOOLEAN DEFAULT FALSE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
