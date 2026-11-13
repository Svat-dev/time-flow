import os

from PySide6.QtWidgets import QApplication

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES_DIR = os.path.join(BASE_DIR, "resources", "styles")


def load_stylesheet(app: QApplication) -> None:
    filename = os.path.join(STYLES_DIR, "dark.qss")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())
    except OSError as error:
        print(f"Не удалось загрузить стили {filename}: {error}")
