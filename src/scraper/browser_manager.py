from playwright.sync_api import (
    sync_playwright,
    Browser,
    BrowserContext,
    Page,
    Playwright,
)
import random

from config import (
    HEADLESS,
    DEFAULT_WAIT,
    RANDOMIZE,
    RANDOM_WAIT_MIN,
    RANDOM_WAIT_MAX,
    SCROLL_PAUSE,
    SCROLL_STEP,
    SCROLL_DELAY,
    SCROLL_TOP_DELAY,
)


class BrowserManager:
    def __init__(
        self,
        headless: bool = HEADLESS,
        headers: dict | None = None,
        cookies: dict | None = None,
    ):
        self.headless = headless
        self.headers = headers
        self.cookies = cookies

        self.playwright: Playwright | None = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)

        context_kwargs = {}

        if self.headers:
            context_kwargs["extra_http_headers"] = self.headers

        if self.cookies:
            context_kwargs["storage_state"] = {"cookies": self.cookies, "origins": []}

        if VIEWPORT:
            context_kwargs["viewport"] = VIEWPORT

        self.context = self.browser.new_context(**context_kwargs)
        self.page = self.context.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def wait(
        self,
        seconds: float = DEFAULT_WAIT,
        *,
        randomize: bool = RANDOMIZE,
        min: float = RANDOM_WAIT_MIN,
        max: float = RANDOM_WAIT_MAX,
    ):
        if randomize:
            duration = random.uniform(min, max)
        else:
            duration = seconds

        self.page.wait_for_timeout(duration)

    def scroll_to_bottom(self, pause: float = SCROLL_PAUSE):
        while True:
            prev_height = self.page.evaluate("document.body.scrollHeight")
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            self.page.wait_for_timeout(pause)
            new_height = self.page.evaluate("document.body.scrollHeight")
            if new_height == prev_height:
                break

    def auto_scroll(self, step: int = SCROLL_STEP, delay: float = SCROLL_DELAY):
        scroll_height = self.page.evaluate("document.body.scrollHeight")
        current_pos = 0

        while current_pos < scroll_height:
            self.page.evaluate(f"window.scrollBy(0, {step})")
            current_pos += step
            self.page.wait_for_timeout(delay)
            scroll_height = self.page.evaluate("document.body.scrollHeight")

    def scroll_to_top(self, delay: float = SCROLL_TOP_DELAY):
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(delay)
