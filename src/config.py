from datetime import datetime
from pathlib import Path


# ============================
# Base directories
# ============================
BASE_DIR = Path().cwd().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# ============================
# Execution date
# ============================
DATE = f"{datetime.now().date()}"

# ============================
# Browser settings
# ============================
HEADLESS = True

VIEWPORT = {
    "width": 1280,
    "height": 800,
}

# ============================
# Scraping settings
# ============================
URL = "https://charts.youtube.com/charts/TopSongs/global/weekly"

# Basic wait
DEFAULT_WAIT = 3000
RANDOMIZE = True
RANDOM_WAIT_MIN = 300
RANDOM_WAIT_MAX = 500

# scroll_to_bottom
SCROLL_PAUSE = 500

# auto_scroll
SCROLL_STEP = 300
SCROLL_DELAY = 500

# scroll_to_top
SCROLL_TOP_DELAY = 300
