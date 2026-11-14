import sys

from PySide6.QtWidgets import QApplication

from app.application import Application


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("TimeFlow")
    app.setOrganizationName("TimeFlow")

    Application(app).run()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
