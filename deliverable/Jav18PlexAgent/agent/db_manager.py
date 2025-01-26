# agent/db_manager.py
import sqlite3
import os
from rich.console import Console


console = Console()


class DBManager:
    def __init__(self, db_path="DATA/plexagent.db"):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.initialize_database()

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

    def initialize_tables(self):
        # Create tables if they do not exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_141jav (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
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
            scraped BOOLEAN DEFAULT FALSE,
            metadata_scraped BOOLEAN DEFAULT FALSE,
            metadata TEXT,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_javdb (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            scraped BOOLEAN DEFAULT FALSE,
            metadata_scraped BOOLEAN DEFAULT FALSE,
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
            scraped BOOLEAN DEFAULT FALSE,
            metadata_scraped BOOLEAN DEFAULT FALSE,
            metadata TEXT,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_r18dev (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
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
