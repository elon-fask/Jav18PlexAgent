# main.py
from cli.erminal_interface import start_terminal
from .db_manager import DBManager


def main():
    db_manager = DBManager()
    start_terminal(db_manager)
    db_manager.close()


if __name__ == "__main__":
    main()
