# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setMinimumSize(QSize(1100, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rootLayout = QHBoxLayout(self.centralwidget)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(220, 0))
        self.sidebar.setMaximumSize(QSize(220, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(20, 28, 20, 20)
        self.brandName = QLabel(self.sidebar)
        self.brandName.setObjectName(u"brandName")

        self.sidebarLayout.addWidget(self.brandName)

        self.topSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.topSpacer)

        self.navCaption = QLabel(self.sidebar)
        self.navCaption.setObjectName(u"navCaption")

        self.sidebarLayout.addWidget(self.navCaption)

        self.todayButton = QPushButton(self.sidebar)
        self.todayButton.setObjectName(u"todayButton")
        self.todayButton.setCheckable(True)
        self.todayButton.setChecked(True)

        self.sidebarLayout.addWidget(self.todayButton)

        self.analyticsButton = QPushButton(self.sidebar)
        self.analyticsButton.setObjectName(u"analyticsButton")

        self.sidebarLayout.addWidget(self.analyticsButton)

        self.historyButton = QPushButton(self.sidebar)
        self.historyButton.setObjectName(u"historyButton")

        self.sidebarLayout.addWidget(self.historyButton)

        self.middleSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.middleSpacer)

        self.manageCaption = QLabel(self.sidebar)
        self.manageCaption.setObjectName(u"manageCaption")

        self.sidebarLayout.addWidget(self.manageCaption)

        self.settingsButton = QPushButton(self.sidebar)
        self.settingsButton.setObjectName(u"settingsButton")

        self.sidebarLayout.addWidget(self.settingsButton)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.bottomSpacer)

        self.profileName = QLabel(self.sidebar)
        self.profileName.setObjectName(u"profileName")

        self.sidebarLayout.addWidget(self.profileName)


        self.rootLayout.addWidget(self.sidebar)

        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.mainLayout = QVBoxLayout(self.mainContent)
        self.mainLayout.setSpacing(18)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(34, 26, 34, 28)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.pageTitle = QLabel(self.mainContent)
        self.pageTitle.setObjectName(u"pageTitle")

        self.titleLayout.addWidget(self.pageTitle)

        self.dateLabel = QLabel(self.mainContent)
        self.dateLabel.setObjectName(u"dateLabel")

        self.titleLayout.addWidget(self.dateLabel)


        self.headerLayout.addLayout(self.titleLayout)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.addEntryButton = QPushButton(self.mainContent)
        self.addEntryButton.setObjectName(u"addEntryButton")

        self.headerLayout.addWidget(self.addEntryButton)


        self.mainLayout.addLayout(self.headerLayout)

        self.summaryLayout = QHBoxLayout()
        self.summaryLayout.setSpacing(14)
        self.summaryLayout.setObjectName(u"summaryLayout")
        self.trackedCard = QFrame(self.mainContent)
        self.trackedCard.setObjectName(u"trackedCard")
        self.trackedLayout = QVBoxLayout(self.trackedCard)
        self.trackedLayout.setObjectName(u"trackedLayout")
        self.trackedCaption = QLabel(self.trackedCard)
        self.trackedCaption.setObjectName(u"trackedCaption")

        self.trackedLayout.addWidget(self.trackedCaption)

        self.trackedValue = QLabel(self.trackedCard)
        self.trackedValue.setObjectName(u"trackedValue")

        self.trackedLayout.addWidget(self.trackedValue)

        self.trackedHint = QLabel(self.trackedCard)
        self.trackedHint.setObjectName(u"trackedHint")

        self.trackedLayout.addWidget(self.trackedHint)


        self.summaryLayout.addWidget(self.trackedCard)

        self.activitiesCard = QFrame(self.mainContent)
        self.activitiesCard.setObjectName(u"activitiesCard")
        self.activitiesLayout = QVBoxLayout(self.activitiesCard)
        self.activitiesLayout.setObjectName(u"activitiesLayout")
        self.activitiesCaption = QLabel(self.activitiesCard)
        self.activitiesCaption.setObjectName(u"activitiesCaption")

        self.activitiesLayout.addWidget(self.activitiesCaption)

        self.activitiesValue = QLabel(self.activitiesCard)
        self.activitiesValue.setObjectName(u"activitiesValue")

        self.activitiesLayout.addWidget(self.activitiesValue)

        self.activitiesHint = QLabel(self.activitiesCard)
        self.activitiesHint.setObjectName(u"activitiesHint")

        self.activitiesLayout.addWidget(self.activitiesHint)


        self.summaryLayout.addWidget(self.activitiesCard)

        self.topCategoryCard = QFrame(self.mainContent)
        self.topCategoryCard.setObjectName(u"topCategoryCard")
        self.topCategoryLayout = QVBoxLayout(self.topCategoryCard)
        self.topCategoryLayout.setObjectName(u"topCategoryLayout")
        self.topCategoryCaption = QLabel(self.topCategoryCard)
        self.topCategoryCaption.setObjectName(u"topCategoryCaption")

        self.topCategoryLayout.addWidget(self.topCategoryCaption)

        self.topCategoryValue = QLabel(self.topCategoryCard)
        self.topCategoryValue.setObjectName(u"topCategoryValue")

        self.topCategoryLayout.addWidget(self.topCategoryValue)

        self.topCategoryHint = QLabel(self.topCategoryCard)
        self.topCategoryHint.setObjectName(u"topCategoryHint")

        self.topCategoryLayout.addWidget(self.topCategoryHint)


        self.summaryLayout.addWidget(self.topCategoryCard)


        self.mainLayout.addLayout(self.summaryLayout)

        self.bodyLayout = QHBoxLayout()
        self.bodyLayout.setSpacing(16)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.timelineCard = QFrame(self.mainContent)
        self.timelineCard.setObjectName(u"timelineCard")
        self.timelineCardLayout = QVBoxLayout(self.timelineCard)
        self.timelineCardLayout.setObjectName(u"timelineCardLayout")
        self.timelineCardLayout.setContentsMargins(20, 18, 20, 18)
        self.timelineHeader = QHBoxLayout()
        self.timelineHeader.setObjectName(u"timelineHeader")
        self.timelineTitle = QLabel(self.timelineCard)
        self.timelineTitle.setObjectName(u"timelineTitle")

        self.timelineHeader.addWidget(self.timelineTitle)

        self.filterSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.timelineHeader.addItem(self.filterSpacer)

        self.categoryFilter = QComboBox(self.timelineCard)
        self.categoryFilter.addItem("")
        self.categoryFilter.setObjectName(u"categoryFilter")

        self.timelineHeader.addWidget(self.categoryFilter)


        self.timelineCardLayout.addLayout(self.timelineHeader)

        self.timelinePlaceholder = QFrame(self.timelineCard)
        self.timelinePlaceholder.setObjectName(u"timelinePlaceholder")
        self.timelinePlaceholder.setMinimumSize(QSize(0, 390))
        self.placeholderLayout = QVBoxLayout(self.timelinePlaceholder)
        self.placeholderLayout.setObjectName(u"placeholderLayout")
        self.timelineHint = QLabel(self.timelinePlaceholder)
        self.timelineHint.setObjectName(u"timelineHint")
        self.timelineHint.setAlignment(Qt.AlignCenter)

        self.placeholderLayout.addWidget(self.timelineHint)


        self.timelineCardLayout.addWidget(self.timelinePlaceholder)


        self.bodyLayout.addWidget(self.timelineCard)

        self.rightColumn = QWidget(self.mainContent)
        self.rightColumn.setObjectName(u"rightColumn")
        self.rightColumn.setMinimumSize(QSize(270, 0))
        self.rightColumn.setMaximumSize(QSize(310, 16777215))
        self.rightColumnLayout = QVBoxLayout(self.rightColumn)
        self.rightColumnLayout.setObjectName(u"rightColumnLayout")
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.timerCard = QFrame(self.rightColumn)
        self.timerCard.setObjectName(u"timerCard")
        self.timerLayout = QVBoxLayout(self.timerCard)
        self.timerLayout.setObjectName(u"timerLayout")
        self.timerLayout.setContentsMargins(18, 18, 18, 18)
        self.timerTitle = QLabel(self.timerCard)
        self.timerTitle.setObjectName(u"timerTitle")

        self.timerLayout.addWidget(self.timerTitle)

        self.timerActivityName = QLabel(self.timerCard)
        self.timerActivityName.setObjectName(u"timerActivityName")

        self.timerLayout.addWidget(self.timerActivityName)

        self.timerCategory = QLabel(self.timerCard)
        self.timerCategory.setObjectName(u"timerCategory")

        self.timerLayout.addWidget(self.timerCategory)

        self.timerValue = QLabel(self.timerCard)
        self.timerValue.setObjectName(u"timerValue")
        self.timerValue.setAlignment(Qt.AlignCenter)

        self.timerLayout.addWidget(self.timerValue)

        self.timerButtonsLayout = QHBoxLayout()
        self.timerButtonsLayout.setObjectName(u"timerButtonsLayout")
        self.stopTimerButton = QPushButton(self.timerCard)
        self.stopTimerButton.setObjectName(u"stopTimerButton")

        self.timerButtonsLayout.addWidget(self.stopTimerButton)

        self.switchTimerButton = QPushButton(self.timerCard)
        self.switchTimerButton.setObjectName(u"switchTimerButton")

        self.timerButtonsLayout.addWidget(self.switchTimerButton)


        self.timerLayout.addLayout(self.timerButtonsLayout)


        self.rightColumnLayout.addWidget(self.timerCard)

        self.categoriesCard = QFrame(self.rightColumn)
        self.categoriesCard.setObjectName(u"categoriesCard")
        self.categoriesLayout = QVBoxLayout(self.categoriesCard)
        self.categoriesLayout.setObjectName(u"categoriesLayout")
        self.categoriesLayout.setContentsMargins(18, 18, 18, 18)
        self.categoriesTitle = QLabel(self.categoriesCard)
        self.categoriesTitle.setObjectName(u"categoriesTitle")

        self.categoriesLayout.addWidget(self.categoriesTitle)


        self.rightColumnLayout.addWidget(self.categoriesCard)

        self.rightSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightColumnLayout.addItem(self.rightSpacer)


        self.bodyLayout.addWidget(self.rightColumn)


        self.mainLayout.addLayout(self.bodyLayout)


        self.rootLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TimeFlow", None))
        self.brandName.setText(QCoreApplication.translate("MainWindow", u"\u25f7  TimeFlow", None))
        self.navCaption.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0411\u041e\u0427\u0415\u0415 \u041f\u0420\u041e\u0421\u0422\u0420\u0410\u041d\u0421\u0422\u0412\u041e", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"\u25f7   \u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.analyticsButton.setText(QCoreApplication.translate("MainWindow", u"\u25a5   \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"\u25a6   \u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.manageCaption.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0418\u041b\u041e\u0416\u0415\u041d\u0418\u0415", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"\u2699   \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.profileName.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.dateLabel.setText("")
        self.addEntryButton.setText(QCoreApplication.translate("MainWindow", u"\uff0b  \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.trackedCaption.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u041f\u0418\u0421\u0410\u041d\u041e \u0421\u0415\u0413\u041e\u0414\u041d\u042f", None))
        self.trackedValue.setText(QCoreApplication.translate("MainWindow", u"0 \u043c\u0438\u043d", None))
        self.trackedHint.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0442\u0451\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.activitiesCaption.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041a\u0422\u0418\u0412\u041d\u041e\u0421\u0422\u0415\u0419", None))
        self.activitiesValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.activitiesHint.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u0435\u043d\u044c", None))
        self.topCategoryCaption.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u041d\u041e\u0412\u041d\u0410\u042f \u041a\u0410\u0422\u0415\u0413\u041e\u0420\u0418\u042f", None))
        self.topCategoryValue.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.topCategoryHint.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430 \u043d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.timelineTitle.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0440\u043e\u043d\u043e\u043b\u043e\u0433\u0438\u044f \u0434\u043d\u044f", None))
        self.categoryFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))

        self.timelineHint.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0448\u043a\u0430\u043b\u0430", None))
        self.timerTitle.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.timerActivityName.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.timerCategory.setText("")
        self.timerValue.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.stopTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.switchTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.categoriesTitle.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c", None))
    # retranslateUi

