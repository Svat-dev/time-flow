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
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setSpacing(12)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(20, 28, 20, 20)
        self.brandLayout = QHBoxLayout()
        self.brandLayout.setObjectName(u"brandLayout")
        self.brandMark = QLabel(self.sidebar)
        self.brandMark.setObjectName(u"brandMark")

        self.brandLayout.addWidget(self.brandMark)

        self.brandName = QLabel(self.sidebar)
        self.brandName.setObjectName(u"brandName")

        self.brandLayout.addWidget(self.brandName)

        self.brandSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.brandLayout.addItem(self.brandSpacer)


        self.sidebarLayout.addLayout(self.brandLayout)

        self.sidebarTopSpacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarTopSpacer)

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
        self.analyticsButton.setCheckable(True)

        self.sidebarLayout.addWidget(self.analyticsButton)

        self.historyButton = QPushButton(self.sidebar)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setCheckable(True)

        self.sidebarLayout.addWidget(self.historyButton)

        self.sidebarMiddleSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarMiddleSpacer)

        self.manageCaption = QLabel(self.sidebar)
        self.manageCaption.setObjectName(u"manageCaption")

        self.sidebarLayout.addWidget(self.manageCaption)

        self.settingsButton = QPushButton(self.sidebar)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setCheckable(True)

        self.sidebarLayout.addWidget(self.settingsButton)

        self.sidebarBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarBottomSpacer)

        self.profileCard = QFrame(self.sidebar)
        self.profileCard.setObjectName(u"profileCard")
        self.profileCard.setFrameShape(QFrame.StyledPanel)
        self.profileLayout = QHBoxLayout(self.profileCard)
        self.profileLayout.setObjectName(u"profileLayout")
        self.avatarLabel = QLabel(self.profileCard)
        self.avatarLabel.setObjectName(u"avatarLabel")
        self.avatarLabel.setMinimumSize(QSize(36, 36))
        self.avatarLabel.setMaximumSize(QSize(36, 36))
        self.avatarLabel.setAlignment(Qt.AlignCenter)

        self.profileLayout.addWidget(self.avatarLabel)

        self.profileTextLayout = QVBoxLayout()
        self.profileTextLayout.setObjectName(u"profileTextLayout")
        self.profileName = QLabel(self.profileCard)
        self.profileName.setObjectName(u"profileName")

        self.profileTextLayout.addWidget(self.profileName)

        self.profileSubtitle = QLabel(self.profileCard)
        self.profileSubtitle.setObjectName(u"profileSubtitle")

        self.profileTextLayout.addWidget(self.profileSubtitle)


        self.profileLayout.addLayout(self.profileTextLayout)


        self.sidebarLayout.addWidget(self.profileCard)


        self.rootLayout.addWidget(self.sidebar)

        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.mainLayout = QVBoxLayout(self.mainContent)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(34, 26, 34, 28)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerTitleLayout = QVBoxLayout()
        self.headerTitleLayout.setObjectName(u"headerTitleLayout")
        self.pageTitle = QLabel(self.mainContent)
        self.pageTitle.setObjectName(u"pageTitle")

        self.headerTitleLayout.addWidget(self.pageTitle)

        self.dateLabel = QLabel(self.mainContent)
        self.dateLabel.setObjectName(u"dateLabel")

        self.headerTitleLayout.addWidget(self.dateLabel)


        self.headerLayout.addLayout(self.headerTitleLayout)

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
        self.trackedCard.setFrameShape(QFrame.StyledPanel)
        self.trackedCardLayout = QVBoxLayout(self.trackedCard)
        self.trackedCardLayout.setObjectName(u"trackedCardLayout")
        self.trackedCaption = QLabel(self.trackedCard)
        self.trackedCaption.setObjectName(u"trackedCaption")

        self.trackedCardLayout.addWidget(self.trackedCaption)

        self.trackedValue = QLabel(self.trackedCard)
        self.trackedValue.setObjectName(u"trackedValue")

        self.trackedCardLayout.addWidget(self.trackedValue)

        self.trackedHint = QLabel(self.trackedCard)
        self.trackedHint.setObjectName(u"trackedHint")

        self.trackedCardLayout.addWidget(self.trackedHint)


        self.summaryLayout.addWidget(self.trackedCard)

        self.activitiesCard = QFrame(self.mainContent)
        self.activitiesCard.setObjectName(u"activitiesCard")
        self.activitiesCard.setFrameShape(QFrame.StyledPanel)
        self.activitiesCardLayout = QVBoxLayout(self.activitiesCard)
        self.activitiesCardLayout.setObjectName(u"activitiesCardLayout")
        self.activitiesCaption = QLabel(self.activitiesCard)
        self.activitiesCaption.setObjectName(u"activitiesCaption")

        self.activitiesCardLayout.addWidget(self.activitiesCaption)

        self.activitiesValue = QLabel(self.activitiesCard)
        self.activitiesValue.setObjectName(u"activitiesValue")

        self.activitiesCardLayout.addWidget(self.activitiesValue)

        self.activitiesHint = QLabel(self.activitiesCard)
        self.activitiesHint.setObjectName(u"activitiesHint")

        self.activitiesCardLayout.addWidget(self.activitiesHint)


        self.summaryLayout.addWidget(self.activitiesCard)

        self.topCategoryCard = QFrame(self.mainContent)
        self.topCategoryCard.setObjectName(u"topCategoryCard")
        self.topCategoryCard.setFrameShape(QFrame.StyledPanel)
        self.topCategoryCardLayout = QVBoxLayout(self.topCategoryCard)
        self.topCategoryCardLayout.setObjectName(u"topCategoryCardLayout")
        self.topCategoryCaption = QLabel(self.topCategoryCard)
        self.topCategoryCaption.setObjectName(u"topCategoryCaption")

        self.topCategoryCardLayout.addWidget(self.topCategoryCaption)

        self.topCategoryValue = QLabel(self.topCategoryCard)
        self.topCategoryValue.setObjectName(u"topCategoryValue")

        self.topCategoryCardLayout.addWidget(self.topCategoryValue)

        self.topCategoryHint = QLabel(self.topCategoryCard)
        self.topCategoryHint.setObjectName(u"topCategoryHint")

        self.topCategoryCardLayout.addWidget(self.topCategoryHint)


        self.summaryLayout.addWidget(self.topCategoryCard)


        self.mainLayout.addLayout(self.summaryLayout)

        self.bodyLayout = QHBoxLayout()
        self.bodyLayout.setSpacing(16)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.timelineCard = QFrame(self.mainContent)
        self.timelineCard.setObjectName(u"timelineCard")
        self.timelineCard.setFrameShape(QFrame.StyledPanel)
        self.timelineCardLayout = QVBoxLayout(self.timelineCard)
        self.timelineCardLayout.setSpacing(14)
        self.timelineCardLayout.setObjectName(u"timelineCardLayout")
        self.timelineCardLayout.setContentsMargins(20, 18, 20, 18)
        self.timelineHeaderLayout = QHBoxLayout()
        self.timelineHeaderLayout.setObjectName(u"timelineHeaderLayout")
        self.timelineTitle = QLabel(self.timelineCard)
        self.timelineTitle.setObjectName(u"timelineTitle")

        self.timelineHeaderLayout.addWidget(self.timelineTitle)

        self.timelineHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.timelineHeaderLayout.addItem(self.timelineHeaderSpacer)

        self.categoryFilter = QComboBox(self.timelineCard)
        self.categoryFilter.addItem("")
        self.categoryFilter.addItem("")
        self.categoryFilter.addItem("")
        self.categoryFilter.addItem("")
        self.categoryFilter.setObjectName(u"categoryFilter")

        self.timelineHeaderLayout.addWidget(self.categoryFilter)


        self.timelineCardLayout.addLayout(self.timelineHeaderLayout)

        self.timelinePlaceholder = QFrame(self.timelineCard)
        self.timelinePlaceholder.setObjectName(u"timelinePlaceholder")
        self.timelinePlaceholder.setMinimumSize(QSize(0, 390))
        self.timelinePlaceholder.setFrameShape(QFrame.StyledPanel)
        self.timelinePlaceholderLayout = QVBoxLayout(self.timelinePlaceholder)
        self.timelinePlaceholderLayout.setSpacing(0)
        self.timelinePlaceholderLayout.setObjectName(u"timelinePlaceholderLayout")
        self.timelineHint = QLabel(self.timelinePlaceholder)
        self.timelineHint.setObjectName(u"timelineHint")
        self.timelineHint.setAlignment(Qt.AlignCenter)

        self.timelinePlaceholderLayout.addWidget(self.timelineHint)

        self.timelineHint2 = QLabel(self.timelinePlaceholder)
        self.timelineHint2.setObjectName(u"timelineHint2")
        self.timelineHint2.setAlignment(Qt.AlignCenter)

        self.timelinePlaceholderLayout.addWidget(self.timelineHint2)


        self.timelineCardLayout.addWidget(self.timelinePlaceholder)


        self.bodyLayout.addWidget(self.timelineCard)

        self.rightColumn = QWidget(self.mainContent)
        self.rightColumn.setObjectName(u"rightColumn")
        self.rightColumn.setMinimumSize(QSize(270, 0))
        self.rightColumn.setMaximumSize(QSize(310, 16777215))
        self.rightColumnLayout = QVBoxLayout(self.rightColumn)
        self.rightColumnLayout.setSpacing(14)
        self.rightColumnLayout.setObjectName(u"rightColumnLayout")
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.timerCard = QFrame(self.rightColumn)
        self.timerCard.setObjectName(u"timerCard")
        self.timerCard.setFrameShape(QFrame.StyledPanel)
        self.timerCardLayout = QVBoxLayout(self.timerCard)
        self.timerCardLayout.setSpacing(12)
        self.timerCardLayout.setObjectName(u"timerCardLayout")
        self.timerCardLayout.setContentsMargins(18, 18, 18, 18)
        self.timerTitle = QLabel(self.timerCard)
        self.timerTitle.setObjectName(u"timerTitle")

        self.timerCardLayout.addWidget(self.timerTitle)

        self.timerActivityName = QLabel(self.timerCard)
        self.timerActivityName.setObjectName(u"timerActivityName")

        self.timerCardLayout.addWidget(self.timerActivityName)

        self.timerCategory = QLabel(self.timerCard)
        self.timerCategory.setObjectName(u"timerCategory")

        self.timerCardLayout.addWidget(self.timerCategory)

        self.timerValue = QLabel(self.timerCard)
        self.timerValue.setObjectName(u"timerValue")
        self.timerValue.setAlignment(Qt.AlignCenter)

        self.timerCardLayout.addWidget(self.timerValue)

        self.timerButtonsLayout = QHBoxLayout()
        self.timerButtonsLayout.setObjectName(u"timerButtonsLayout")
        self.stopTimerButton = QPushButton(self.timerCard)
        self.stopTimerButton.setObjectName(u"stopTimerButton")

        self.timerButtonsLayout.addWidget(self.stopTimerButton)

        self.switchTimerButton = QPushButton(self.timerCard)
        self.switchTimerButton.setObjectName(u"switchTimerButton")

        self.timerButtonsLayout.addWidget(self.switchTimerButton)


        self.timerCardLayout.addLayout(self.timerButtonsLayout)


        self.rightColumnLayout.addWidget(self.timerCard)

        self.categoriesCard = QFrame(self.rightColumn)
        self.categoriesCard.setObjectName(u"categoriesCard")
        self.categoriesCard.setFrameShape(QFrame.StyledPanel)
        self.categoriesCardLayout = QVBoxLayout(self.categoriesCard)
        self.categoriesCardLayout.setSpacing(12)
        self.categoriesCardLayout.setObjectName(u"categoriesCardLayout")
        self.categoriesCardLayout.setContentsMargins(18, 18, 18, 18)
        self.categoriesTitle = QLabel(self.categoriesCard)
        self.categoriesTitle.setObjectName(u"categoriesTitle")

        self.categoriesCardLayout.addWidget(self.categoriesTitle)

        self.devCategoryLayout = QHBoxLayout()
        self.devCategoryLayout.setObjectName(u"devCategoryLayout")
        self.devDot = QLabel(self.categoriesCard)
        self.devDot.setObjectName(u"devDot")

        self.devCategoryLayout.addWidget(self.devDot)

        self.devName = QLabel(self.categoriesCard)
        self.devName.setObjectName(u"devName")

        self.devCategoryLayout.addWidget(self.devName)

        self.devSpacer = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.devCategoryLayout.addItem(self.devSpacer)

        self.devTime = QLabel(self.categoriesCard)
        self.devTime.setObjectName(u"devTime")

        self.devCategoryLayout.addWidget(self.devTime)


        self.categoriesCardLayout.addLayout(self.devCategoryLayout)

        self.devProgress = QProgressBar(self.categoriesCard)
        self.devProgress.setObjectName(u"devProgress")
        self.devProgress.setValue(49)
        self.devProgress.setTextVisible(False)

        self.categoriesCardLayout.addWidget(self.devProgress)

        self.studyCategoryLayout = QHBoxLayout()
        self.studyCategoryLayout.setObjectName(u"studyCategoryLayout")
        self.studyDot = QLabel(self.categoriesCard)
        self.studyDot.setObjectName(u"studyDot")

        self.studyCategoryLayout.addWidget(self.studyDot)

        self.studyName = QLabel(self.categoriesCard)
        self.studyName.setObjectName(u"studyName")

        self.studyCategoryLayout.addWidget(self.studyName)

        self.studySpacer = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.studyCategoryLayout.addItem(self.studySpacer)

        self.studyTime = QLabel(self.categoriesCard)
        self.studyTime.setObjectName(u"studyTime")

        self.studyCategoryLayout.addWidget(self.studyTime)


        self.categoriesCardLayout.addLayout(self.studyCategoryLayout)

        self.studyProgress = QProgressBar(self.categoriesCard)
        self.studyProgress.setObjectName(u"studyProgress")
        self.studyProgress.setValue(29)
        self.studyProgress.setTextVisible(False)

        self.categoriesCardLayout.addWidget(self.studyProgress)

        self.restCategoryLayout = QHBoxLayout()
        self.restCategoryLayout.setObjectName(u"restCategoryLayout")
        self.restDot = QLabel(self.categoriesCard)
        self.restDot.setObjectName(u"restDot")

        self.restCategoryLayout.addWidget(self.restDot)

        self.restName = QLabel(self.categoriesCard)
        self.restName.setObjectName(u"restName")

        self.restCategoryLayout.addWidget(self.restName)

        self.restSpacer = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.restCategoryLayout.addItem(self.restSpacer)

        self.restTime = QLabel(self.categoriesCard)
        self.restTime.setObjectName(u"restTime")

        self.restCategoryLayout.addWidget(self.restTime)


        self.categoriesCardLayout.addLayout(self.restCategoryLayout)

        self.restProgress = QProgressBar(self.categoriesCard)
        self.restProgress.setObjectName(u"restProgress")
        self.restProgress.setValue(21)
        self.restProgress.setTextVisible(False)

        self.categoriesCardLayout.addWidget(self.restProgress)


        self.rightColumnLayout.addWidget(self.categoriesCard)

        self.rightColumnSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightColumnLayout.addItem(self.rightColumnSpacer)


        self.bodyLayout.addWidget(self.rightColumn)


        self.mainLayout.addLayout(self.bodyLayout)


        self.rootLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TimeFlow", None))
        self.brandMark.setText(QCoreApplication.translate("MainWindow", u"\u25f7", None))
        self.brandName.setText(QCoreApplication.translate("MainWindow", u"TimeFlow", None))
        self.navCaption.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0411\u041e\u0427\u0415\u0415 \u041f\u0420\u041e\u0421\u0422\u0420\u0410\u041d\u0421\u0422\u0412\u041e", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"\u25f7   \u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.analyticsButton.setText(QCoreApplication.translate("MainWindow", u"\u25a5   \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"\u25a6   \u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.manageCaption.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0418\u041b\u041e\u0416\u0415\u041d\u0418\u0415", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"\u2699   \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.avatarLabel.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.profileName.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.profileSubtitle.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430, 6 \u043d\u043e\u044f\u0431\u0440\u044f 2026", None))
        self.addEntryButton.setText(QCoreApplication.translate("MainWindow", u"\uff0b  \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.trackedCaption.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u041f\u0418\u0421\u0410\u041d\u041e \u0421\u0415\u0413\u041e\u0414\u041d\u042f", None))
        self.trackedValue.setText(QCoreApplication.translate("MainWindow", u"4 \u0447 32 \u043c\u0438\u043d", None))
        self.trackedHint.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 24 \u0447\u0430\u0441\u043e\u0432", None))
        self.activitiesCaption.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041a\u0422\u0418\u0412\u041d\u041e\u0421\u0422\u0415\u0419", None))
        self.activitiesValue.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.activitiesHint.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u0435\u043d\u044c", None))
        self.topCategoryCaption.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u041d\u041e\u0412\u041d\u0410\u042f \u041a\u0410\u0422\u0415\u0413\u041e\u0420\u0418\u042f", None))
        self.topCategoryValue.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.topCategoryHint.setText(QCoreApplication.translate("MainWindow", u"2 \u0447 15 \u043c\u0438\u043d \u00b7 49%", None))
        self.timelineTitle.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0440\u043e\u043d\u043e\u043b\u043e\u0433\u0438\u044f \u0434\u043d\u044f", None))
        self.categoryFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.categoryFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.categoryFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0451\u0431\u0430", None))
        self.categoryFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u044b\u0445", None))

        self.timelineHint.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0448\u043a\u0430\u043b\u0430 00:00\u201324:00", None))
        self.timelineHint2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u044d\u0442\u043e\u0442 \u0431\u043b\u043e\u043a \u043d\u0430 TimelineWidget", None))
        self.timerTitle.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.timerActivityName.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u043d\u0430\u0434 TimeFlow", None))
        self.timerCategory.setText(QCoreApplication.translate("MainWindow", u"\u25cf  \u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.timerValue.setText(QCoreApplication.translate("MainWindow", u"01:24:36", None))
        self.stopTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.switchTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.categoriesTitle.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c", None))
        self.devDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.devName.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.devTime.setText(QCoreApplication.translate("MainWindow", u"2 \u0447 15 \u043c", None))
        self.studyDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.studyName.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0451\u0431\u0430", None))
        self.studyTime.setText(QCoreApplication.translate("MainWindow", u"1 \u0447 20 \u043c", None))
        self.restDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.restName.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u044b\u0445", None))
        self.restTime.setText(QCoreApplication.translate("MainWindow", u"57 \u043c\u0438\u043d", None))
    # retranslateUi

