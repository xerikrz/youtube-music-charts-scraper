from scraper.browser_manager import BrowserManager


class Fetcher:
    def __init__(self, browser: BrowserManager):
        self.browser = browser

    def fetch(self, url: str, scroll: bool = False) -> None:
        bm = self.browser

        try:
            bm.page.goto(url)

            if scroll:
                bm.wait()
                bm.auto_scroll()
                bm.wait()
                bm.scroll_to_top()
                bm.wait()

        except Exception:
            print("Error al cargar la página")
            return None
