from config import URL, HEADLESS, FILEPATH_CSV, FILEPATH_JSON
from scraper.browser_manager import BrowserManager
from scraper.fetcher import Fetcher
from scraper.processor import Parser
from scraper.exporter import CSVExporter, JSONExporter


with BrowserManager(headless=HEADLESS) as bm:
    fetcher = Fetcher(browser=bm)
    fetcher.fetch(URL, scroll=True)

    parser = Parser(browser=bm)
    songs = parser.parse_songs()

    csv_exporter = CSVExporter()
    json_exporter = JSONExporter()

    csv_exporter.export(songs, FILEPATH_CSV)
    json_exporter.export(songs, FILEPATH_JSON)
