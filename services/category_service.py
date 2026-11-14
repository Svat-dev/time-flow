import re
import sqlite3

from datetime import datetime

from models.category import Category
from repositories.category_repository import CategoryRepository

COLOR_RE = re.compile(r"^#[0-9a-fA-F]{6}$")


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    @staticmethod
    def validate(name: str, color: str):
        if not name.strip():
            raise ValueError("Название категории не может быть пустым")
        if len(name.strip()) > 100:
            raise ValueError("Название не должно превышать 100 символов")
        if not COLOR_RE.fullmatch(color):
            raise ValueError("Цвет должен быть в формате HEX (#ffffff)")

    def list_categories(self, include_archived: bool = False) -> list[Category]:
        return list(map(_row_to_category_, self.repository.get_all(include_archived)))

    def create(self, name: str, color: str = "#8b5cf6", icon=None) -> int | None:
        self.validate(name, color)
        return self.repository.create(name.strip(), color, icon)

    def update(self, category_id: int, name: str, color: str, icon=None) -> None:
        self.validate(name, color)
        self.repository.update(category_id, name.strip(), color, icon)

    def archive(self, category_id: str) -> None:
        self.repository.archive(category_id)

    def restore(self, category_id: str) -> None:
        self.repository.restore(category_id)


def _row_to_category_(row: sqlite3.Row) -> Category:
    return Category(
        id=row["id"],
        name=row["name"],
        color=row["color"],
        icon=row["icon"],
        created_at=datetime.fromisoformat(row["created_at"]),
        is_archived=bool(row["is_archived"]),
    )
