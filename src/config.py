from datetime import datetime
from pathlib import Path


# ============================
# Base directories
# ============================
BASE_DIR = Path().cwd().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
