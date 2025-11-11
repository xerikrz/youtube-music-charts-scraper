from config import URL, HEADLESS
from scraper.browser_manager import BrowserManager
from scraper.fetcher import Fetcher


with BrowserManager(headless=HEADLESS) as bm:
    fetcher = Fetcher(browser=bm)
    fetcher.fetch(URL, scroll=True)
