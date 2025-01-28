# run.py
from agent import db_manager
from cli.terminal_interface import start_terminal
from agent.db_manager import DBManager


def main():
    db_manager = DBManager("test.db")
    start_terminal(db_manager)
    db_manager.close()


def run():
    db_manager = DBManager("test.db")
    start_terminal(db_manager)

    db_manager.close()


if __name__ == "__main__":
    # main()
    run()
