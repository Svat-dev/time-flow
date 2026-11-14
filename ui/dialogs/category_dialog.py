from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QDialogButtonBox,
    QColorDialog,
    QPushButton,
)
from PySide6.QtGui import QColor

from utils.color import random_hex_color
from models.category import Category


class CategoryDialog(QDialog):
    def __init__(self, parent=None, category: Category | None = None):
        super().__init__(parent)

        self.setWindowTitle("Изменить категорию" if category else "Новая категория")

        self.color = category.color if category else random_hex_color()

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.name = QLineEdit(category.name if category else "")
        self.icon = QLineEdit((category.icon or "") if category else "")

        self.color_button = QPushButton(self.color)
        self.color_button.clicked.connect(self.pick_color)

        form.addRow("Название", self.name)
        form.addRow("Иконка (необязательно)", self.icon)
        form.addRow("Цвет", self.color_button)

        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def pick_color(self):
        color = QColorDialog.getColor(QColor(self.color), self)
        if color.isValid():
            self.color = color.name()
            self.color_button.setText(self.color)

    def values(self):
        return self.name.text(), self.color, self.icon.text().strip() or None
