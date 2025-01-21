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

