from datetime import date, datetime, time, timedelta

from repositories.time_entry_repository import TimeEntryRepository
from models.analytics import CategoryAnalytics, DayAnalytics


class AnalyticsService:
    def __init__(self, repository: TimeEntryRepository) -> None:
        self.repository = repository

    def for_day(self, day: date | str) -> DayAnalytics:
        target = date.fromisoformat(day) if isinstance(day, str) else day

        start = datetime.combine(target, time.min)
        end = start + timedelta(days=1)

        rows = self.repository.get_all_between(start, end)

        totals: dict[int, CategoryAnalytics] = {}

        total = 0
        count = 0
        now = datetime.now()

        for row in rows:
            started_at = datetime.fromisoformat(row["started_at"])

            ended_at = (
                datetime.fromisoformat(row["ended_at"]) if row["ended_at"] else now
            )

            a = max(started_at, start)
            b = min(ended_at, end)

            seconds = max(0, int((b - a).total_seconds()))

            if not seconds:
                continue

            category_id = row["category_id"]

            if category_id not in totals:
                totals[category_id] = CategoryAnalytics(
                    category_id=category_id,
                    name=row["category_name"],
                    color=row["category_color"],
                    seconds=0,
                )

            totals[category_id].seconds += seconds

            total += seconds
            count += 1

        categories = sorted(
            totals.values(),
            key=lambda category: category.seconds,
            reverse=True,
        )

        return DayAnalytics(
            total_seconds=total,
            activity_count=count,
            categories=categories,
            top_category=categories[0] if categories else None,
        )
