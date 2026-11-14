from dataclasses import dataclass
from datetime import datetime


@dataclass
class Category:
    id: int
    name: str
    color: str
    icon: str
    created_at: datetime
    is_archived: bool
