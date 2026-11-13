from os import path
from PySide6.QtWidgets import QApplication

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

STYLES_DIR = path.join(BASE_DIR, "resources", "styles")


def load_stylesheet(app: QApplication) -> None:
    filename = path.join(STYLES_DIR, "dark.qss")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"stylesheet file '{filename}' not found")
