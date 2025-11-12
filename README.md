# YouTube Music Charts Scraper

This project is a **Web Scraping** tool designed to extract data from YouTube Music's global weekly charts ([charts.youtube.com](https://charts.youtube.com/charts/TopSongs/global/weekly)). It uses **Playwright** to simulate real browser interaction, ensuring reliable extraction of dynamically loaded content.

---

## ✨ Features

- **Technology:** Uses Playwright to handle dynamic and asynchronous web pages, with direct execution in Colab or Kaggle notebooks.  
- **Metrics extraction:**  
  - Song ranking  
  - Title  
  - Artists  
  - Video URL  
  - YouTube-specific metrics (weekly views, weeks on the chart)  
- **Browser management:** `BrowserManager` handles initialization, viewport configuration, and safe browser closure.  
- **Structured output:** Exports data in **CSV** and **JSON** formats ready for analysis.  
- **Human-like behavior simulation:** Includes random pauses and simulated scrolling to reduce blocks.

---

## 💻 Project Structure

```
.
├── pyproject.toml
├── README.md
├── requirements.txt
├── uv.lock
├── src/
│   ├── config.py                 # Configuration (URLs, Playwright settings, paths)
│   ├── main.py                   # Entry point and workflow orchestrator
│   └── scraper/
│       ├── __init__.py           # Scraper package initializer
│       ├── browser_manager.py    # Browser handling (start, close, wait, scroll)
│       ├── fetcher.py            # Navigation and scrolling on the target URL
│       ├── processor.py          # Extract song information
│       └── exporter.py           # Export to CSV and JSON
└── data/                          # Directory for generated output files
```

---

## ⚙️ Key Technologies

- **Language:** Python 3.11  
- **Scraping/Automation:** Playwright (Chromium headless)  
- **Data analysis:** Standard Python modules (`json`, `csv`)  
- **Path and date management:** `pathlib`, `datetime`

---

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.11  
- pip  

### 📥 Installation

#### Step 1: Clone the repository and create a virtual environment

```bash
git clone https://github.com/xerikrz/youtube-music-charts-scraper.git
cd youtube-music-charts-scraper
python3 -m .venv venv
source .venv/bin/activate
```

---

#### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

#### Step 3: Install Playwright binaries

```bash
playwright install chromium
```

---

### ▶️ Usage

Run the scraper and generate output files:

```bash
cd src/
python3 main.py
```

The files `youtube_charts_[DATE].csv` and `youtube_charts_[DATE].json` will be saved in the `data/` directory.

---

### 🚀 Deployment and Automation

This project features **automatic deployment via GitHub Actions**, optimized for weekly scraping and cache management. Deployment runs on a dedicated **`deploy` branch**, which also stores the generated data.

#### Deployment Features

- **Deploy branch (`deploy`)**:  
  - Automatic execution every Sunday at 23:59.  
  - The scraper runs and the resulting CSV and JSON files are **saved directly in the `deploy` branch**, keeping the main and development branches clean.  

- **Cache optimization:**  
  - Caches dependencies and partial results to reduce execution time on repeated runs.  

- **Development branch (`develop`)**:  
  - Allows testing changes and running the scraper without affecting the deploy branch.  

---

### 🔄 Execution Flow (Pipeline)

1. **Browser initialization:** `BrowserManager` starts Chromium in headless mode with the configured viewport.  
2. **Navigation and scrolling:** `Fetcher` navigates to the configured URL (`https://charts.youtube.com/charts/TopSongs/global/weekly`) and simulates scrolling to load dynamic content.  
3. **Processing (Parsing):** `Processor` analyzes the page:  
   - Iterates over each row (`ytmc-entry-row`)  
   - Extracts ranking, title, artists, video URL, and thumbnail  
   - Collects additional metrics (release date, previous position)  
   - Adds random pauses between songs  
4. **Exporting:**  
   - `CSVExporter` → `data/youtube_charts_[DATE].csv`  
   - `JSONExporter` → `data/youtube_charts_[DATE].json`

---

### 📄 Configuration

Main variables are in `src/config.py`:

| Variable      | Description                                   | Default value                           |
|---------------|-----------------------------------------------|----------------------------------------|
| `URL`         | URL of the chart to scrape                    | `TopSongs/global/weekly`               |
| `HEADLESS`    | Run browser without visible interface         | `True`                                 |
| `VIEWPORT`    | Simulated browser window size                 | `1280x800`                             |
| `RANDOMIZE`   | Enable random wait times between actions      | `True`                                 |
| `FILEPATH_CSV`| Path and filename for CSV output              | `data/youtube_charts_[DATE].csv`      |

---

### 🛑 Warning

Web scraping should be performed responsibly. Excessive usage can overload the target site and result in IP blocks. Pauses implemented in `browser_manager.py` help mitigate this risk.
