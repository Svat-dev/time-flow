from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Activity:
    id: int
    category_id: int
    category_name: str
    category_color: str
    title: str
    description: str | None
    started_at: datetime
    ended_at: datetime | None
    source: Literal["timer", "manual"]
    created_at: datetime
    updated_at: datetime
