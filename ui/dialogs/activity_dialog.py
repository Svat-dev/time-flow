from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QDateTimeEdit,
    QDialogButtonBox,
)
from PySide6.QtCore import QDateTime

from datetime import datetime, timedelta

from models.activity import Activity
from models.category import Category

Q_DATETIME_FORMAT = "yyyy-MM-dd HH:mm:ss"
ISO_FORMAT = "yyyy-MM-ddTHH:mm:ss"


class ActivityDialog(QDialog):
    def __init__(
        self, categories: list[Category], parent=None, entry: Activity | None = None
    ):
        super().__init__(parent)

        self.setWindowTitle("Редактировать запись" if entry else "Добавить запись")

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.title = QLineEdit(entry.title if entry else "")
        self.category = QComboBox()

        for c in categories:
            self.category.addItem(c.name, c.id)

        self.description = QTextEdit((entry.description or "") if entry else "")
        self.description.setMaximumHeight(80)

        self.start = QDateTimeEdit()
        self.end = QDateTimeEdit()

        for w in (self.start, self.end):
            w.setCalendarPopup(True)
            w.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        now = datetime.now()

        self.start.setDateTime(
            QDateTime.fromString(
                entry.started_at.isoformat().replace("T", " "), Q_DATETIME_FORMAT
            )
            if entry
            else QDateTime.fromSecsSinceEpoch(
                int((now - timedelta(hours=1)).timestamp())
            )
        )

        self.end.setDateTime(
            QDateTime.fromString(
                entry.ended_at.isoformat().replace("T", " "), Q_DATETIME_FORMAT
            )
            if entry and entry.ended_at
            else QDateTime.currentDateTime()
        )

        if entry:
            index = self.category.findData(entry.category_id)
            if index >= 0:
                self.category.setCurrentIndex(index)

        form.addRow("Название", self.title)
        form.addRow("Категория", self.category)
        form.addRow("Начало", self.start)
        form.addRow("Окончание", self.end)
        form.addRow("Описание", self.description)

        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def values(self):
        return (
            self.category.currentData(),
            self.title.text(),
            self.description.toPlainText().strip() or None,
            datetime.fromisoformat(self.start.dateTime().toString(ISO_FORMAT)),
            datetime.fromisoformat(self.end.dateTime().toString(ISO_FORMAT)),
        )
