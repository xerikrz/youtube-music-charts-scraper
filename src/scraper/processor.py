import json

from scraper.browser_manager import BrowserManager


class Parser:
    def __init__(self, browser: BrowserManager):
        self.browser = browser

    def parse_songs(self) -> list[dict]:
        bm = self.browser
        page = bm.page

        container = page.locator("div.ytmc-chart-table-v2-container")
        if container.count() == 0:
            return []

        rows = page.locator("ytmc-entry-row.style-scope.ytmc-chart-table-v2")
        total = rows.count()

        songs = []

        for i in range(total):
            row = rows.nth(i)

            row.hover()

            # RANK
            rank = row.locator("#rank").inner_text().strip()

            # TITLE
            title = row.locator("#entity-title").inner_text().strip()

            # URL
            endpoint_raw = row.locator("#entity-title").get_attribute("endpoint")
            url = None
            if endpoint_raw:
                endpoint_json = json.loads(endpoint_raw)
                url = endpoint_json["urlEndpoint"]["url"]

            # THUMBNAIL
            thumbnail = row.locator("#thumbnail").get_attribute("src")

            # ARTISTS (varios)
            artist_nodes = row.locator("#artist-names .artistName")
            artists = [
                artist_nodes.nth(j).inner_text().strip()
                for j in range(artist_nodes.count())
            ]

            # Métricas crudas
            metrics = row.locator("div.metric.content.center")
            m = [metrics.nth(j).inner_text().strip() for j in range(metrics.count())]

            # Mapear métricas a nombres
            metrics_data = {
                "release_date": m[0] if len(m) > 0 else None,
                "last_week_position": m[1] if len(m) > 1 else None,
                "weeks_on_chart": m[2] if len(m) > 2 else None,
                "weekly_views": m[3] if len(m) > 3 else None,
            }

            songs.append(
                {
                    "rank": rank,
                    "title": title,
                    "url": url,
                    "artists": artists,
                    "thumbnail": thumbnail,
                    "metrics": metrics_data,
                }
            )

            bm.wait()

        return songs
