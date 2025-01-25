# Handles SQLite database operations
import sqlite3


def initialize_db():
    # Create a new SQLite database or connect to existing
    conn = sqlite3.connect("DATA/torrents.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS torrents
                      (id INTEGER PRIMARY KEY, link TEXT, recorded BOOLEAN)""")
    conn.commit()
    conn.close()


def check_recorded(link):
    # Check if the link is already recorded in the database
    conn = sqlite3.connect("DATA/torrents.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torrents WHERE link=?", (link,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
