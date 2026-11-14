import sqlite3

from datetime import date, datetime

from models.activity import Activity
from repositories.time_entry_repository import TimeEntryRepository


class ActivityService:
    def __init__(self, repository: TimeEntryRepository):
        self.repository = repository

    @staticmethod
    def validate(title: str, started_at: date, ended_at: date):
        if not title.strip():
            raise ValueError("Название активности не может быть пустым")
        if len(title.strip()) > 100:
            raise ValueError("Название не должно превышать 100 символов")
        if ended_at <= started_at:
            raise ValueError("Время окончания должно быть позже времени начала")

    def list_for_day(self, day: date) -> list[Activity]:
        return list(map(_row_to_activity_, self.repository.get_for_day(day)))

    def create_manual(
        self,
        category_id: int,
        title: str,
        description: str | None,
        started_at: date,
        ended_at: date,
    ):
        self.validate(title, started_at, ended_at)
        return self.repository.create(
            category_id, title.strip(), description, started_at, ended_at, "manual"
        )

    def update(
        self,
        entry_id: int,
        category_id: int,
        title: str,
        description: str | None,
        started_at: date,
        ended_at: date,
    ):
        self.validate(title, started_at, ended_at)
        self.repository.update(
            entry_id, category_id, title.strip(), description, started_at, ended_at
        )

    def delete(self, entry_id):
        self.repository.delete(entry_id)


def _row_to_activity_(row: sqlite3.Row) -> Activity:
    return Activity(
        id=row["id"],
        category_id=row["category_id"],
        category_name=row["category_name"],
        category_color=row["category_color"],
        title=row["title"],
        description=row["description"],
        started_at=datetime.fromisoformat(row["started_at"]),
        ended_at=(
            datetime.fromisoformat(row["ended_at"])
            if row["ended_at"] is not None
            else None
        ),
        source=row["source"],
        created_at=datetime.fromisoformat(row["created_at"]),
        updated_at=datetime.fromisoformat(row["updated_at"]),
    )
