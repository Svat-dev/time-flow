import sqlite3

from datetime import date
from app.database import Database


class TimeEntryRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_active(self) -> sqlite3.Row | None:
        query = """
            SELECT e.*, c.name AS category_name, c.color AS category_color
            FROM time_entries e
            JOIN categories c ON c.id = e.category_id
            WHERE e.ended_at IS NULL
            LIMIT 1
        """

        return self.db.fetch_one(query)

    def get_by_id(self, entry_id: int):
        query = "SELECT * FROM time_entries WHERE id = ?"

        return self.db.fetch_one(query, (entry_id,))

    def get_for_day(self, day: date) -> list[sqlite3.Row]:
        start, end = f"{day}T00:00:00", f"{day}T23:59:59.999999"

        query = """
            SELECT e.*, c.name AS category_name, c.color AS category_color
            FROM time_entries e
            JOIN categories c ON c.id = e.category_id
            WHERE (
                e.started_at <= ?
                AND COALESCE(e.ended_at, datetime('now', 'localtime')) >= ?
            )
            ORDER BY e.started_at
        """

        return self.db.fetch_all(
            query,
            (end, start),
        )

    def get_all_between(self, start: date, end: date) -> list[sqlite3.Row]:
        query = """
            SELECT e.*, c.name AS category_name, c.color AS category_color
            FROM time_entries e
            JOIN categories c ON c.id = e.category_id
            WHERE (
                e.started_at < ?
                AND COALESCE(e.ended_at, ?) > ?
            )
            ORDER BY e.started_at
        """

        return self.db.fetch_all(
            query,
            (end, end, start),
        )

    def create(
        self,
        category_id: int,
        title: str,
        description: str | None,
        started_at: date,
        ended_at: date | None,
        source: str,
    ) -> int | None:
        query = """
            INSERT INTO time_entries(category_id, title, description, started_at, ended_at, source)
            VALUES(?, ?, ?, ?, ?, ?)
        """
        params = (category_id, title, description, started_at, ended_at, source)

        cur = self.db.execute(
            query,
            params,
        )

        self.db.commit()
        return cur.lastrowid

    def finish(self, entry_id: int, ended_at: date) -> None:
        query = "UPDATE time_entries SET ended_at = ? WHERE id = ? AND ended_at IS NULL"
        params = (ended_at, entry_id)

        self.db.execute(
            query,
            params,
        )
        self.db.commit()

    def update(
        self,
        entry_id: int,
        category_id: int,
        title: str,
        description: str | None,
        started_at: date,
        ended_at: date,
    ) -> None:
        query = "UPDATE time_entries SET category_id = ?,title = ?,description = ?,started_at = ?,ended_at = ? WHERE id = ?"
        params = (category_id, title, description, started_at, ended_at, entry_id)

        self.db.execute(
            query,
            params,
        )
        self.db.commit()

    def delete(self, entry_id: int) -> None:
        query = "DELETE FROM time_entries WHERE id=?"

        self.db.execute(query, (entry_id,))
        self.db.commit()
