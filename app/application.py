import os
import subprocess

from PySide6.QtWidgets import QApplication, QMessageBox

from app.database import Database
from app.styles import load_stylesheet

from repositories.category_repository import CategoryRepository
from repositories.time_entry_repository import TimeEntryRepository

from services.category_service import CategoryService
from services.activity_service import ActivityService
from services.timer_service import TimerService
from services.analytics_service import AnalyticsService

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UI_FILE = os.path.join(BASE_DIR, "ui", "windows", "ui_main_window.py")


class Application:
    def __init__(self, app: QApplication):
        self.app = app
        self.db = Database()
        self.main_window = None

    def run(self):
        if not os.path.exists(UI_FILE):
            result = subprocess.run(
                ["pyside6-uic", "ui/windows/main_window.ui", "-o", UI_FILE],
                capture_output=True,
                text=True,
            )
            if result.returncode:
                QMessageBox.critical(
                    None,
                    "Ошибка UI",
                    result.stderr
                    or "Не удалось сгенерировать Python-код из main_window.ui",
                )
                raise RuntimeError("Run `make ui-generate` after installing PySide6")
        from ui.windows.main_window import MainWindow

        self.db.connect()
        self.db.initialize_database()

        category_repo = CategoryRepository(self.db)
        entry_repo = TimeEntryRepository(self.db)

        self.main_window = MainWindow(
            self.db,
            CategoryService(category_repo),
            ActivityService(entry_repo),
            TimerService(entry_repo),
            AnalyticsService(entry_repo),
        )

        load_stylesheet(self.app)

        self.app.aboutToQuit.connect(self.db.disconnect)
        self.main_window.show()
