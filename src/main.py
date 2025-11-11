from config import URL, HEADLESS
from scraper.browser_manager import BrowserManager
from scraper.fetcher import Fetcher
from scraper.processor import Parser


with BrowserManager(headless=HEADLESS) as bm:
    fetcher = Fetcher(browser=bm)
    fetcher.fetch(URL, scroll=True)

    parser = Parser(browser=bm)
    songs = parser.parse_songs()
    print(songs)
