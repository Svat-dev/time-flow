from PySide6.QtWidgets import QApplication

from app.database import Database
from app.styles import load_stylesheet
from ui.windows.main_window import MainWindow


class Application:
    def __init__(self, app: QApplication) -> None:
        self.app = app
        self.main_window: MainWindow | None = None

    def run(self) -> None:
        with Database() as db:
            db.initialize_database()

        load_stylesheet(self.app)

        self.main_window = MainWindow()
        self.main_window.show()
