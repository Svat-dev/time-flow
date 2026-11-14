from datetime import datetime, timedelta

from models.activity import Activity
from services.activity_service import _row_to_activity_
from repositories.time_entry_repository import TimeEntryRepository


class TimerService:
    def __init__(self, repository: TimeEntryRepository):
        self.repository = repository

    def current(self) -> Activity | None:
        active = self.repository.get_active()
        if active is not None:
            return _row_to_activity_(active)

    def start(
        self, category_id: int, title: str, description: str | None = None
    ) -> int | None:
        if self.current() is not None:
            raise RuntimeError("Сначала завершите текущую активность")
        if not title.strip():
            raise ValueError("Укажите название активности")

        return self.repository.create(
            category_id,
            title.strip(),
            description,
            datetime.now(),
            None,
            "timer",
        )

    def stop(self) -> None:
        active = self.current()
        if active is None:
            return

        now = datetime.now()
        if now <= active.started_at:
            now = active.started_at + timedelta(seconds=1)

        self.repository.finish(active.id, now)

    def switch(
        self, category_id: int, title: str, description: str | None = None
    ) -> int | None:
        self.stop()
        return self.start(category_id, title, description)

    def elapsed_seconds(self) -> int:
        active = self.current()
        if active is None:
            return 0

        total_seconds = (datetime.now() - active.started_at).total_seconds()
        return max(0, int(total_seconds))
