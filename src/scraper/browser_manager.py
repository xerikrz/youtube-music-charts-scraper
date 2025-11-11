from playwright.sync_api import (
    sync_playwright,
    Browser,
    BrowserContext,
    Page,
    Playwright,
)
import random

from config import (HEADLESS, VIEWPORT)


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

        # Add viewport from config
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
