# main.py
import sqlite3
from cli.terminal_interface import display_welcome
from agent.db_manager import DBManager

if __name__ == "__main__":
    display_welcome()
    db_manager = DBManager()
    # The database and tables are initialized in the DBManager constructor
    db_manager.close()
