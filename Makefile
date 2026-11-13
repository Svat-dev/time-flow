UI_DIR = ui/windows

app-run:
	@python main.py

ui-generate:
	@pyside6-uic $(UI_DIR)/main_window.ui -o $(UI_DIR)/ui_main_window.py
