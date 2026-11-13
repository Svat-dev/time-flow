from PySide6.QtWidgets import QMainWindow

from ui.windows.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("TimeFlow")
