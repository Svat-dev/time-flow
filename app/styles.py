from os import path
from PySide6.QtWidgets import QApplication

STYLES_DIR = path.join("resources", "styles")


def load_stylesheet(app: QApplication) -> None:
    filename = path.join(STYLES_DIR, "dark.qss")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"stylesheet file '{filename}' not found")
