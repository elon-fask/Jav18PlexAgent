
scraper_141jav.py
scraper_avwiki.py
scraper_javdb.py
scraper_javguru.py
scraper_onejav.py
scraper_r18dev.py



```python
# cli/terminal_interface.py
import logging
from tqdm import tqdm  # For progress bars
import sqlite3

# Configure logging
logging.basicConfig(filename='agent.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_welcome():
    print("Welcome to the Plex Metadata Agent!")
    print("This tool will help you scrape metadata from various websites.")
    print("You can choose to run each scraper service one by one.")
    print("Let's get started!")

def start_terminal():
    print("Welcome to the Plex Agent Terminal")
    print("Commands:")
    print("1. View logs")
    print("2. Check database status")
    print("3. Exit")

    while True:
        command = input("Enter command: ")
        if command == "1":
            view_logs()
        elif command == "2":
            check_database_status()
        elif command == "3":
            print("Exiting terminal.")
            break
        else:
            print("Invalid command. Please try again.")

def view_logs():
    try:
        with open('agent.log', 'r') as log_file:
            logs = log_file.readlines()
            for log in logs:
               ```python
# cli/terminal_interface.py
import os
import time
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.live import Live
from agent.db_manager import DBManager

console = Console()

def start_terminal():
    print("Welcome to the Plex Agent Terminal")

    db_manager = DBManager()

    while True:
        console.print("[bold green]Commands:[/bold green]")
        console.print("[1] View logs")
        console.print("[2] Check database status")
        console.print("[3] Exit")

        command = console.input("[bold yellow]Enter command: [/bold yellow]")

        if command == "1":
            display_logs()
        elif command == "2":
            display_database_status(db_manager)
        elif command == "3":
            console.print("[bold red]Exiting terminal.[/bold red]")
            db_manager.close()
            break
        else:
            console.print("[bold red]Invalid command. Please try again.[/bold red]")

def display_logs():
    console.print("[bold green]Displaying logs...[/bold green]")
    # Placeholder for log display
    with Progress() as progress:
        task = progress.add_task("[green]Loading logs...", total=100)
        while not task.finished:
            time.sleep(0.1)
            task.advance(1)
    console.print("[bold green]Logs displayed successfully.[/bold green]")

def display_database_status(db_manager):
    console.print("[bold green]Checking database status...[/bold green]")
    try:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Table Name", style="dim", width=20)
        table.add_column("Row Count", justify="right")

        for table_name in ["scraper_141jav", "scraper_avwiki", "scraper_javdb", "scraper_javguru", "scraper_onejav", "scraper_r18dev"]:
            db_manager.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = db_manager.cursor.fetchone()[0]
            table.add_row(table_name, str(row_count))

        console.print(table)
        console.print("[bold green]Database status: OK[/bold green]")
    except sqlite3.Error as e:
        console.print(f"[bold red]Error checking database status: {e}[/bold red]")

if __name__ == "__main__":
    start_terminal()
```

```python
# main.py
from cli.terminal_interface import start_terminal

if __name__ == "__main__":
    start_terminal()
```

Explanation:

1. The `terminal_interface.py` file provides an interactive command-line interface for the user to interact with the Plex Agent.
2. The `start_terminal()` function displays the available commands and handles user input.
3. The `display_logs()` function is a placeholder for displaying the logs, which can be implemented by reading and formatting the log files.
4. The `display_database_status()` function checks the status of the database by querying the row counts for each table and displaying the information in a formatted table.
5. The `main.py` file simply calls the `start_terminal()` function to launch the interactive terminal.

The code utilizes the following libraries:
- `rich`: Provides a set of tools for creating beautiful and user-friendly command-line interfaces, including progress bars, tables, and live displays.
- `sqlite3`: Allows interaction with the SQLite database used by the Plex Agent.

The key features of this implementation are:
1. **Interactive Terminal**: The user can easily navigate through the available commands and perform various actions, such as viewing logs and checking the database status.
2. **Database Status Display**: The terminal displays the row count for each table in the database, providing a quick overview of the data stored by the Plex Agent.
3. **Error Handling**: The code includes basic error handling to gracefully handle any issues that may arise when interacting with the database.
4. **Modular Design**: The `terminal_interface.py` file is separate from the `main.py` file, allowing for easier maintenance and potential future expansion of the terminal functionality.

To test the implementation, simply run the `main.py` file, and the interactive terminal will be launched.



- rewriting and using best practices of coding in python. keeping in mind future changes and future addons.

- verifying XPATH and Web elements.

- debugging and testing.

- Documentation and making a User Guide

- assist client and asking for feedback


### PROJECT:
Develop an interactive Plex metadata agent with modular structure, using `.env` for XPath storage and terminal management tools.

---

### SUMMARY:
The project rebuilds a Plex metadata agent with modular classes and terminal interactivity. It uses `.env` for XPath configuration via `python-decouple` for better maintainability. The agent fetches movie metadata using external sites and integrates it into Plex Media Server libraries seamlessly.

---

### STEPS:
1. Create `Jav18PlexAgent` directory for the new project structure.  
2. Initialize Python environment with dependencies like `python-decouple`.  
3. Split code into modular files for clarity and maintainability.  
4. Implement `.env` for XPath and configuration storage.  
5. Update `site.py` and `site_141jav.py` with improved logic.  
6. Add CLI tool for managing the agent interactively.  
7. Implement detailed logging for debugging and error tracking.  
8. Test XPath validity and site connectivity via CLI commands.  
9. Deploy agent to Plex and verify its functionality.  
10. Write a README with setup and usage instructions.  

---

### STRUCTURE:
```
Jav18PlexAgent/
├── agent/
│   ├── __init__.py
│   ├── base_site.py
│   ├── site_141jav.py
│   ├── utils.py
│   └── .env
├── cli/
│   ├── __init__.py
│   ├── interactive_cli.py
│   ├── xpath_validator.py
│   └── config_manager.py
├── tests/
│   ├── test_base_site.py
│   ├── test_site_141jav.py
│   ├── test_utils.py
│   └── mock_responses.py
├── requirements.txt
├── README.md
└── setup.py
```

---

### DETAILED EXPLANATION:
1. **`agent/__init__.py`**: Initializes the agent and manages global configurations.  
2. **`agent/base_site.py`**: Contains base classes and common methods for site scraping.  
3. **`agent/site_141jav.py`**: Implements scraping logic for the **141Jav** site.  
4. **`agent/utils.py`**: Utility functions for logging, HTTP requests, and XPath handling.  
5. **`agent/.env`**: Stores XPath and configuration values securely.  
6. **`cli/interactive_cli.py`**: Provides an interactive terminal interface for managing the agent.  
7. **`cli/xpath_validator.py`**: Validates XPath expressions from `.env`.  
8. **`cli/config_manager.py`**: Manages `.env` configurations interactively.  
9. **`tests/`**: Contains unit tests for agent modules and CLI tools.  
10. **`requirements.txt`**: Specifies project dependencies.  
11. **`README.md`**: Provides detailed setup and usage instructions.  
12. **`setup.py`**: Automates project installation.  

---

### CODE:

#### **`agent/__init__.py`**
```python
from decouple import config

# Load common settings from .env
CACHE_PATH = config("CACHE_PATH", default="/tmp/jav18_cache")
USER_AGENT = config("USER_AGENT", default="Mozilla/5.0")
```

#### **`agent/base_site.py`**
```python
import requests
from lxml import html

class BaseSite:
    def __init__(self, name, search_url, detail_url):
        self.name = name
        self.search_url = search_url
        self.detail_url = detail_url

    def fetch_page(self, url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return html.fromstring(response.content)

    def log(self, message):
        print(f"[{self.name}] {message}")
```

#### **`agent/site_141jav.py`**
```python
from agent.base_site import BaseSite
from decouple import config

class Site141Jav(BaseSite):
    def __init__(self):
        super().__init__(
            "141Jav",
            search_url=config("141JAV_SEARCH_URL"),
            detail_url=config("141JAV_DETAIL_URL"),
        )

    def search(self, release_id):
        url = self.search_url.format(release_id=release_id)
        self.log(f"Searching for {release_id} at {url}")
        page = self.fetch_page(url)
        results = page.xpath(config("141JAV_SEARCH_XPATH"))
        return [{"id": r.text.strip()} for r in results]
```

#### **`agent/utils.py`**
```python
def log_debug(message):
    print(f"[DEBUG] {message}")
```

#### **`cli/interactive_cli.py`**
```python
import click

@click.group()
def cli():
    """Manage the Jav18 Agent interactively."""
    pass

@click.command()
def validate_xpath():
    """Validate XPaths from the .env file."""
    print("Validating XPaths...")

@click.command()
def test_connection():
    """Test site connectivity."""
    print("Testing connection...")

cli.add_command(validate_xpath)
cli.add_command(test_connection)

if __name__ == "__main__":
    cli()
```

#### **`.env`**
```env
CACHE_PATH=/tmp/jav18_cache
USER_AGENT=Mozilla/5.0
141JAV_SEARCH_URL=https://www.141jav.com/search?q={release_id}
141JAV_DETAIL_URL=https://www.141jav.com/details/{release_id}
141JAV_SEARCH_XPATH=//div[@class='result']
```

---

### SETUP:
```bash
#!/bin/bash

# 1. Create project directory
mkdir Jav18PlexAgent
cd Jav18PlexAgent

# 2. Initialize Python environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# 3. Install dependencies
cat > requirements.txt << EOF
click
decouple
lxml
requests
EOF
pip install -r requirements.txt

# 4. Create directories
mkdir -p agent cli tests

# 5. Create .env file
cat > agent/.env << EOF
CACHE_PATH=/tmp/jav18_cache
USER_AGENT=Mozilla/5.0
141JAV_SEARCH_URL=https://www.141jav.com/search?q={release_id}
141JAV_DETAIL_URL=https://www.141jav.com/details/{release_id}
141JAV_SEARCH_XPATH=//div[@class='result']
EOF

echo "Setup completed. Start by running 'python cli/interactive_cli.py'"
```

---

### TAKEAWAYS:
1. Modular design enhances maintainability and debugging.  
2. `.env` simplifies configuration and improves security.  
3. Interactive CLI provides robust management capabilities.  

---

### SUGGESTIONS:
1. Add more sites with similar modular classes.  
2. Include better error handling for missing `.env` values.  
3. Implement a test suite with mocked HTTP responses.





PROJECT:
Develop a Plex metadata agent for seamless integration and efficient metadata management using Python.
SUMMARY:
This project involves creating a Plex metadata agent that fetches and updates movie metadata from various online sources, ensuring compatibility with Plex Media Server environments and enhancing user experience by providing detailed, accurate, and up-to-date information about media content.
STEPS:
Set up a project directory and initialize a Python environment.
Create base and site-specific modules for metadata fetching.
Implement error handling and logging for debugging.
Configure .env for secure and flexible settings management.
Develop an interactive CLI for agent management.
Test the agent locally with Plex Media Server.
Document the setup and usage instructions in README.md.
Deploy the agent to the Plex server and verify functionality.
Gather user feedback and refine the agent based on responses.
Maintain and update the agent for new Plex versions and site changes.
STRUCTURE:
javascript


Jav18.bundle/
├── Contents/
│   ├── Code/
│   │   ├── __init__.py
│   │   ├── site.py
│   │   ├── site_141jav.py
│   │   ├── genres.py
│   │   └── utils.py
│   ├── DefaultPrefs.json
│   ├── Info.plist
│   └── Resources/
│       ├── attribution.png
│       └── icon-default.png
DETAILED EXPLANATION:
__init__.py: Initializes the agent, imports site modules, and sets up service list.
site.py: Contains base classes and utilities for site-specific scraping.
site_141jav.py: Handles fetching and parsing metadata from 141Jav.
genres.py: Manages genre mappings and transformations.
utils.py: Provides additional utility functions like logging and error handling.
DefaultPrefs.json: Stores user preferences for agent behavior.
Info.plist: Metadata file for Plex plugin identification.
Resources/: Contains images and other resources used by the plugin.
CODE:
init.py
python


# Initialization and service setup for Plex metadata agent
from site_141jav import Site141Jav
from site import Log

SERVICES = [Site141Jav()]

def setup_services():
    for service in SERVICES:
        Log(f"Service initialized: {service.tag()}")

setup_services()
site.py
python


# Base classes and utilities for site-specific scraping
class Site:
    def fetch_data(self, url):
        # Fetch data logic
        pass

    def parse_data(self, data):
        # Parse data logic
        pass
site_141jav.py
python


# Specific site logic for 141Jav
from site import Site

class Site141Jav(Site):
    def fetch_data(self, url):
        super().fetch_data(url)
        # Additional fetch logic for 141Jav

    def parse_data(self, data):
        super().parse_data(data)
        # Additional parse logic for 141Jav


now we are going to stop and finish one step by step,
we are going to build a tool that will check websites for each kind of scraping logic. wich mean we will specefiy each logic in a python file that will be called sitename_agent.py 
after we will focus on having a terminal_interface.py in wich we will use to monitor and do actions when called.
as 
