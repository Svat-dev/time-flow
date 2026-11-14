from __future__ import annotations

from datetime import date
from typing import TypeVar

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QBoxLayout,
    QComboBox,
    QFrame,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QWidget,
)

from app.database import Database

from services.activity_service import ActivityService
from services.analytics_service import AnalyticsService
from services.category_service import CategoryService
from services.timer_service import TimerService

from ui.dialogs.activity_dialog import ActivityDialog
from ui.dialogs.category_dialog import CategoryDialog
from ui.windows.ui_main_window import Ui_MainWindow
from ui.widgets.timeline_widget import TimelineWidget

WidgetType = TypeVar("WidgetType", bound=QWidget)


def format_duration(seconds: int | float) -> str:
    hours, remainder = divmod(max(0, int(seconds)), 3600)
    minutes = remainder // 60

    if hours:
        return f"{hours} ч {minutes} мин"

    return f"{minutes} мин"


class MainWindow(QMainWindow):
    def __init__(
        self,
        db: Database,
        category_service: CategoryService,
        activity_service: ActivityService,
        timer_service: TimerService,
        analytics_service: AnalyticsService,
    ) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db
        self.categories = category_service
        self.activities = activity_service
        self.timer = timer_service
        self.analytics = analytics_service

        self.timeline: TimelineWidget
        self.start_button: QPushButton

        self._install_timeline()
        self._connect_signals()
        self.refresh_all()

        self.clock = QTimer(self)
        self.clock.timeout.connect(self.refresh_live)
        self.clock.start(1000)

    def _get_widget(
        self,
        name: str,
        expected_type: type[WidgetType],
    ) -> WidgetType:
        widget = getattr(self.ui, name, None)

        if widget is None:
            raise RuntimeError(
                f"Не найден обязательный виджет '{name}' " "в main_window.ui"
            )

        if not isinstance(widget, expected_type):
            raise TypeError(
                f"Виджет '{name}' должен иметь тип "
                f"{expected_type.__name__}, "
                f"получен {type(widget).__name__}"
            )

        return widget

    def _get_layout(self, widget: QWidget, name: str) -> QBoxLayout:
        layout = widget.layout()

        if layout is None:
            raise RuntimeError(
                f"У виджета '{name}' отсутствует layout. " "Проверьте main_window.ui."
            )

        if not isinstance(layout, QBoxLayout):
            raise TypeError(
                f"Layout виджета '{name}' должен быть QBoxLayout, "
                f"получен {type(layout).__name__}"
            )

        return layout

    def _get_ui_layout(self, name: str) -> QBoxLayout:
        layout = getattr(self.ui, name, None)

        if layout is None:
            raise RuntimeError(
                f"Не найден обязательный layout '{name}' " "в main_window.ui"
            )

        if not isinstance(layout, QBoxLayout):
            raise TypeError(
                f"Объект '{name}' должен быть QBoxLayout, "
                f"получен {type(layout).__name__}"
            )

        return layout

    def _install_timeline(self) -> None:
        placeholder = self._get_widget("timelinePlaceholder", QFrame)
        timeline_card = self._get_widget("timelineCard", QFrame)

        parent = placeholder.parentWidget()

        if parent is None:
            raise RuntimeError("timelinePlaceholder не имеет родительского виджета")

        parent_layout = self._get_layout(
            parent,
            "родитель timelinePlaceholder",
        )

        placeholder_index = parent_layout.indexOf(placeholder)

        if placeholder_index < 0:
            raise RuntimeError("timelinePlaceholder отсутствует в родительском layout")

        parent_layout.removeWidget(placeholder)
        placeholder.deleteLater()

        self.timeline = TimelineWidget(timeline_card)
        parent_layout.insertWidget(placeholder_index, self.timeline)

        self.start_button = QPushButton("Запустить", self)

        timer_buttons_layout = self._get_ui_layout("timerButtonsLayout")
        timer_buttons_layout.insertWidget(0, self.start_button)

        self.start_button.clicked.connect(lambda: self._start_prompt(switch=False))

        self.timeline.entry_selected.connect(self.edit_activity)

    def _connect_signals(self) -> None:
        self._get_widget("addEntryButton", QPushButton).clicked.connect(
            self.add_activity
        )

        self._get_widget("todayButton", QPushButton).clicked.connect(self.refresh_all)

        self._get_widget("analyticsButton", QPushButton).clicked.connect(
            self.show_analytics
        )

        self._get_widget("historyButton", QPushButton).clicked.connect(
            self.show_history
        )

        self._get_widget("settingsButton", QPushButton).clicked.connect(
            self.manage_categories
        )

        self._get_widget("categoryFilter", QComboBox).currentIndexChanged.connect(
            self.refresh_timeline
        )

        self._get_widget("stopTimerButton", QPushButton).clicked.connect(
            self.stop_timer
        )

        self._get_widget("switchTimerButton", QPushButton).clicked.connect(
            self.switch_timer
        )

    def refresh_all(self) -> None:
        self._get_widget("dateLabel", QLabel).setText(date.today().strftime("%d.%m.%Y"))

        self.refresh_filter()
        self.refresh_timeline()
        self.refresh_analytics()
        self.refresh_timer()

    def refresh_filter(self) -> None:
        combo = self._get_widget("categoryFilter", QComboBox)
        selected_category_id = combo.currentData()

        previous_signals_state = combo.blockSignals(True)

        try:
            combo.clear()
            combo.addItem("Все категории", None)

            for category in self.categories.list_categories():
                combo.addItem(
                    category.name,
                    category.id,
                )

            selected_index = combo.findData(selected_category_id)
            combo.setCurrentIndex(max(0, selected_index))

        finally:
            combo.blockSignals(previous_signals_state)

    def refresh_timeline(self) -> None:
        category_id = self._get_widget(
            "categoryFilter",
            QComboBox,
        ).currentData()

        self.timeline.set_entries(
            self.activities.list_for_day(date.today()),
            date.today(),
            category_id,
        )

    def refresh_analytics(self) -> None:
        stats = self.analytics.for_day(date.today())

        self._get_widget("trackedValue", QLabel).setText(
            format_duration(stats.total_seconds)
        )

        self._get_widget("trackedHint", QLabel).setText("Учтённое время")

        self._get_widget("activitiesValue", QLabel).setText(str(stats.activity_count))

        self._get_widget("activitiesHint", QLabel).setText("Записей за день")

        top_category = stats.top_category

        self._get_widget("topCategoryValue", QLabel).setText(
            top_category.name if top_category else "—"
        )

        self._get_widget("topCategoryHint", QLabel).setText(
            format_duration(top_category.seconds) if top_category else "Пока нет данных"
        )

        categories_card = self._get_widget(
            "categoriesCard",
            QFrame,
        )

        categories_layout = self._get_layout(
            categories_card,
            "categoriesCard",
        )

        while categories_layout.count() > 1:
            item = categories_layout.takeAt(1)

            if item is None:
                continue

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()
                continue

            child_layout = item.layout()

            if child_layout is not None:
                while child_layout.count():
                    child_item = child_layout.takeAt(0)

                    if child_item is None:
                        continue

                    child_widget = child_item.widget()

                    if child_widget is not None:
                        child_widget.deleteLater()

        total_seconds = max(1, stats.total_seconds)

        for category in stats.categories:
            row = QWidget(categories_card)
            row_layout = QBoxLayout(
                QBoxLayout.Direction.TopToBottom,
                row,
            )
            row_layout.setContentsMargins(0, 3, 0, 3)

            line_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)

            name_label = QLabel(f"●  {category.name}", row)
            name_label.setStyleSheet(f"color: {category.color};")

            time_label = QLabel(
                format_duration(category.seconds),
                row,
            )

            line_layout.addWidget(name_label)
            line_layout.addStretch()
            line_layout.addWidget(time_label)

            row_layout.addLayout(line_layout)

            progress_bar = QProgressBar(row)
            progress_bar.setTextVisible(False)
            progress_bar.setMaximum(100)
            progress_bar.setValue(round(category.seconds * 100 / total_seconds))

            progress_bar.setStyleSheet(
                "QProgressBar::chunk {"
                f"background-color: {category.color};"
                "border-radius: 4px;"
                "}"
            )

            row_layout.addWidget(progress_bar)
            categories_layout.addWidget(row)

    def refresh_timer(self) -> None:
        active_entry = self.timer.current()
        is_running = active_entry is not None

        stop_button = self._get_widget(
            "stopTimerButton",
            QPushButton,
        )

        switch_button = self._get_widget(
            "switchTimerButton",
            QPushButton,
        )

        stop_button.setEnabled(is_running)
        switch_button.setEnabled(is_running)

        self.start_button.setVisible(not is_running)

        activity_name = self._get_widget(
            "timerActivityName",
            QLabel,
        )

        category_label = self._get_widget(
            "timerCategory",
            QLabel,
        )

        timer_value = self._get_widget(
            "timerValue",
            QLabel,
        )

        if active_entry is None:
            activity_name.setText("Нет активной активности")
            category_label.setText("")
            timer_value.setText("00:00:00")
            return

        activity_name.setText(active_entry.title)

        category_label.setText(f"●  {active_entry.category_name}")

        elapsed_seconds = self.timer.elapsed_seconds()

        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        timer_value.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def refresh_live(self) -> None:
        active_entry = self.timer.current()

        self.refresh_timer()

        if active_entry is not None:
            self.refresh_timeline()
            self.refresh_analytics()

    def manage_categories(self) -> None:
        settings_button = self._get_widget(
            "settingsButton",
            QPushButton,
        )

        menu = QMenu(self)

        add_action = menu.addAction("Добавить категорию")
        menu.addSeparator()

        editable_categories = {}
        archived_categories = {}

        active_categories = self.categories.list_categories()

        all_categories = self.categories.list_categories(include_archived=True)

        for category in active_categories:
            action = menu.addAction(f"Изменить: {category.name}")
            editable_categories[action] = category

        menu.addSeparator()

        for category in active_categories:
            action = menu.addAction(f"Архивировать: {category.name}")
            archived_categories[action] = category

        for category in all_categories:
            if category.is_archived:
                action = menu.addAction(f"Восстановить: {category.name}")
                archived_categories[action] = category

        chosen_action = menu.exec(
            settings_button.mapToGlobal(settings_button.rect().bottomLeft())
        )

        if chosen_action is None:
            return

        try:
            if chosen_action == add_action:
                dialog = CategoryDialog(self)

                if dialog.exec():
                    self.categories.create(*dialog.values())

            elif chosen_action in editable_categories:
                category = editable_categories[chosen_action]
                dialog = CategoryDialog(self, category)

                if dialog.exec():
                    self.categories.update(
                        category.id,
                        *dialog.values(),
                    )

            elif chosen_action in archived_categories:
                category = archived_categories[chosen_action]

                if category.is_archived:
                    self.categories.restore(category.id)
                else:
                    self.categories.archive(category.id)

        except Exception as error:
            QMessageBox.warning(
                self,
                "Ошибка",
                str(error),
            )

        self.refresh_all()

    def add_activity(self) -> None:
        categories = self.categories.list_categories()

        if not categories:
            QMessageBox.information(
                self,
                "Категории",
                "Сначала создайте категорию.",
            )
            self.manage_categories()
            return

        dialog = ActivityDialog(categories, self)

        if not dialog.exec():
            return

        try:
            self.activities.create_manual(*dialog.values())
            self.refresh_all()

        except Exception as error:
            QMessageBox.warning(
                self,
                "Ошибка",
                str(error),
            )

    def edit_activity(self, entry_id: int) -> None:
        entry = self.db.fetch_one(
            "SELECT * FROM time_entries WHERE id = ?",
            (entry_id,),
        )

        if entry is None:
            raise RuntimeError(f"Запись активности с id={entry_id} не найдена")

        if entry["ended_at"] is None:
            return

        dialog = ActivityDialog(
            self.categories.list_categories(),
            self,
            entry,
        )

        if dialog.exec():
            try:
                self.activities.update(
                    entry_id,
                    *dialog.values(),
                )
                self.refresh_all()

            except Exception as error:
                QMessageBox.warning(
                    self,
                    "Ошибка",
                    str(error),
                )

            return

        answer = QMessageBox.question(
            self,
            "Удалить запись?",
            "Удалить выбранную активность?",
        )

        if answer == QMessageBox.StandardButton.Yes:
            try:
                self.activities.delete(entry_id)
                self.refresh_all()

            except Exception as error:
                QMessageBox.warning(
                    self,
                    "Ошибка",
                    str(error),
                )

    def _start_prompt(self, switch: bool = False) -> None:
        categories = self.categories.list_categories()

        if not categories:
            QMessageBox.information(
                self,
                "Категории",
                "Сначала создайте категорию.",
            )
            self.manage_categories()
            return

        title, title_confirmed = QInputDialog.getText(
            self,
            "Активность",
            "Название активности:",
        )

        if not title_confirmed or not title.strip():
            return

        category_names = [category.name for category in categories]

        category_name, category_confirmed = QInputDialog.getItem(
            self,
            "Категория",
            "Выберите категорию:",
            category_names,
            0,
            False,
        )

        if not category_confirmed:
            return

        selected_category = next(
            (category for category in categories if category.name == category_name),
            None,
        )

        if selected_category is None:
            raise RuntimeError(f"Не удалось найти категорию '{category_name}'")

        try:
            if switch:
                self.timer.switch(
                    selected_category.id,
                    title.strip(),
                )
            else:
                self.timer.start(
                    selected_category.id,
                    title.strip(),
                )

        except Exception as error:
            QMessageBox.warning(
                self,
                "Ошибка",
                str(error),
            )

        self.refresh_all()

    def stop_timer(self) -> None:
        try:
            self.timer.stop()
            self.refresh_all()

        except Exception as error:
            QMessageBox.warning(
                self,
                "Ошибка",
                str(error),
            )

    def switch_timer(self) -> None:
        self._start_prompt(switch=True)

    # ------------------------------------------------------------------
    # Разделы приложения
    # ------------------------------------------------------------------

    def show_analytics(self) -> None:
        stats = self.analytics.for_day(date.today())

        lines = [
            f"Всего: {format_duration(stats.total_seconds)}",
            f"Активностей: {stats.activity_count}",
        ]

        lines.extend(
            f"{category.name}: " + f"{format_duration(category.seconds)}"
            for category in stats.categories
        )

        QMessageBox.information(
            self,
            "Статистика за сегодня",
            "\n".join(lines),
        )

    def show_history(self) -> None:
        QMessageBox.information(
            self,
            "История",
            "История по датам пока не реализована.",
        )
