from PySide6.QtWidgets import QApplication

from app.database import initialize_database
from app.styles import load_stylesheet


class Application:
    def __init__(self, app: QApplication) -> None:
        self.app = app

    def run(self) -> None:
        initialize_database()

        load_stylesheet(self.app)

