# agent/db_manager.py
import sqlite3


class DBManager:
    def __init__(self, db_path="DATA/torrents.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.initialize_tables()

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
        self.connection.close()
