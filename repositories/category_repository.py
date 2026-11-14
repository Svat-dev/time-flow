import sqlite3

from app.database import Database


class CategoryRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all(self, include_archived: bool = False) -> list[sqlite3.Row]:
        query = "SELECT * FROM categories"
        if not include_archived:
            query += " WHERE is_archived = 0"
        query += " ORDER BY name COLLATE NOCASE"

        return self.db.fetch_all(query)

    def get_by_id(self, category_id: str) -> sqlite3.Row:
        query = "SELECT * FROM categories WHERE id = ?"

        return self.db.fetch_one(query, (category_id,))

    def create(self, name: str, color: str, icon=None) -> int | None:
        query = "INSERT INTO categories (name, color, icon) VALUES(?, ?, ?)"
        params = (name, color, icon or None)

        cur = self.db.execute(query, params)

        self.db.commit()
        return cur.lastrowid

    def update(self, category_id: int, name: str, color: str, icon=None) -> None:
        query = "UPDATE categories SET name = ?, color = ?, icon = ? WHERE id = ?"
        params = (name, color, icon or None, category_id)

        self.db.execute(query, params)
        self.db.commit()

    def archive(self, category_id):
        query = "UPDATE categories SET is_archived = 1 WHERE id = ?"

        self.db.execute(query, (category_id,))
        self.db.commit()

    def restore(self, category_id):
        query = "UPDATE categories SET is_archived = 0 WHERE id = ?"

        self.db.execute(query, (category_id,))
        self.db.commit()
