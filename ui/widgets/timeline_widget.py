from datetime import datetime, time, timedelta
from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
)
from PySide6.QtGui import QBrush, QPen, QColor, QFont
from PySide6.QtCore import Signal

from datetime import date

from models.activity import Activity


class TimelineWidget(QGraphicsView):
    entry_selected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.graphics_scene = QGraphicsScene(self)
        self.setScene(self.graphics_scene)
        self.setMinimumHeight(390)

        self.day: date = datetime.now().date()
        self.entries: list[Activity] = []

        self.setBackgroundBrush(QBrush(QColor("#151922")))

    def set_entries(
        self,
        entries: list[Activity],
        day: date | None = None,
        category_id: int | None = None,
    ):
        self.entries = entries
        if day:
            self.day = day

        self.draw(category_id)

    def draw(self, category_id: int | None = None):
        self.graphics_scene.clear()

        left, top, width, height = 56, 16, 680, 340
        self.graphics_scene.setSceneRect(0, 0, width + left + 10, height + 40)

        for hour in range(25):
            y = top + hour * height / 24
            self.graphics_scene.addLine(
                left, y, left + width, y, QPen(QColor("#303746"), 1)
            )

            if hour < 24:
                label = self.graphics_scene.addText(f"{hour:02d}:00")
                label.setDefaultTextColor(QColor("#929aaa"))
                label.setFont(QFont("Arial", 8))
                label.setPos(5, y - 8)

        start_day = datetime.combine(self.day, time.min)
        end_day = start_day + timedelta(days=1)

        for row in self.entries:
            if category_id is not None and row.category_id != category_id:
                continue

            a = max(row.started_at, start_day)
            raw_end = row.ended_at if row.ended_at else datetime.now()
            b = min(raw_end, end_day)

            if b <= a:
                continue

            y1 = top + (a - start_day).total_seconds() / 86400 * height
            y2 = top + (b - start_day).total_seconds() / 86400 * height

            rect = QGraphicsRectItem(left + 3, y1, width - 8, max(5, y2 - y1 - 2))
            rect.setBrush(QBrush(QColor(row.category_color)))
            rect.setPen(QPen(QColor("#111318"), 1))
            rect.setData(0, row.id)

            self.graphics_scene.addItem(rect)
            if y2 - y1 > 17:
                label = self.graphics_scene.addText(row.title)
                label.setDefaultTextColor(QColor("#111318"))
                label.setFont(QFont("Arial", 8, QFont.Weight.Bold))
                label.setPos(left + 8, y1 + 1)

        now = datetime.now()
        if now.date() == self.day:
            y = top + (now - start_day).total_seconds() / 86400 * height
            self.graphics_scene.addLine(
                left, y, left + width, y, QPen(QColor("#f87171"), 2)
            )

    def mousePressEvent(self, event):
        item = self.itemAt(event.position().toPoint())
        while item is not None and item.data(0) is None:
            item = item.parentItem()

        if item is not None and item.data(0) is not None:
            self.entry_selected.emit(int(item.data(0)))

        super().mousePressEvent(event)
