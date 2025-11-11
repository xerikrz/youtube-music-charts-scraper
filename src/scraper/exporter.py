import csv
import json
from pathlib import Path


class CSVExporter:
    def export(self, songs: list[dict], filepath: str):
        filepath = Path(filepath)

        filepath.parent.mkdir(parents=True, exist_ok=True)

        rows = []
        for s in songs:
            rows.append(
                {
                    "rank": s["rank"],
                    "title": s["title"],
                    "url": s["url"],
                    "artists": ", ".join(s["artists"]),
                    "thumbnail": s["thumbnail"],
                    "release_date": s["metrics"].get("release_date"),
                    "last_week_position": s["metrics"].get("last_week_position"),
                    "weeks_on_chart": s["metrics"].get("weeks_on_chart"),
                    "weekly_views": s["metrics"].get("weekly_views"),
                }
            )

        fieldnames = list(rows[0].keys()) if rows else []

        with filepath.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


class JSONExporter:
    def export(self, songs: list[dict], filepath: str):
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(songs, f, ensure_ascii=False, indent=4)
