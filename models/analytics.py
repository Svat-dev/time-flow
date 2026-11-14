from dataclasses import dataclass


@dataclass
class CategoryAnalytics:
    category_id: int
    name: str
    color: str
    seconds: int


@dataclass
class DayAnalytics:
    total_seconds: int
    activity_count: int
    categories: list[CategoryAnalytics]
    top_category: CategoryAnalytics | None
