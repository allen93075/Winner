# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_UI_for_edit.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 638)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 365, 543))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title3.setObjectName("title3")
        self.gridLayout_2.addWidget(self.title3, 2, 0, 1, 1)
        self.title1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title1.setObjectName("title1")
        self.gridLayout_2.addWidget(self.title1, 0, 0, 1, 1)
        self.title4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title4.setEnabled(True)
        self.title4.setObjectName("title4")
        self.gridLayout_2.addWidget(self.title4, 3, 0, 1, 1)
        self.title5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title5.setObjectName("title5")
        self.gridLayout_2.addWidget(self.title5, 4, 0, 1, 1)
        self.title2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title2.setObjectName("title2")
        self.gridLayout_2.addWidget(self.title2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(140, 70, 231, 261))
        font = QtGui.QFont()
        font.setFamily("AGA Arabesque")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu_Strategy = QtWidgets.QMenu(self.menubar)
        self.menu_Strategy.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu_Strategy.setObjectName("menu_Strategy")
        self.menuTurtle = QtWidgets.QMenu(self.menu_Strategy)
        self.menuTurtle.setObjectName("menuTurtle")
        self.menuMoveAverage = QtWidgets.QMenu(self.menu_Strategy)
        self.menuMoveAverage.setObjectName("menuMoveAverage")
        self.menuRangeBreak = QtWidgets.QMenu(self.menu_Strategy)
        self.menuRangeBreak.setObjectName("menuRangeBreak")
        self.menu_AI = QtWidgets.QMenu(self.menubar)
        self.menu_AI.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu_AI.setObjectName("menu_AI")
        self.menu_Reports = QtWidgets.QMenu(self.menubar)
        self.menu_Reports.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu_Reports.setObjectName("menu_Reports")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRF_2 = QtWidgets.QAction(MainWindow)
        self.actionRF_2.setObjectName("actionRF_2")
        self.actionDT_2 = QtWidgets.QAction(MainWindow)
        self.actionDT_2.setObjectName("actionDT_2")
        self.actionLSTM_2 = QtWidgets.QAction(MainWindow)
        self.actionLSTM_2.setObjectName("actionLSTM_2")
        self.actionMLP_2 = QtWidgets.QAction(MainWindow)
        self.actionMLP_2.setObjectName("actionMLP_2")
        self.actionMulticharts = QtWidgets.QAction(MainWindow)
        self.actionMulticharts.setObjectName("actionMulticharts")
        self.actionTurtle30k = QtWidgets.QAction(MainWindow)
        self.actionTurtle30k.setObjectName("actionTurtle30k")
        self.actionTurtle60k = QtWidgets.QAction(MainWindow)
        self.actionTurtle60k.setObjectName("actionTurtle60k")
        self.actionMA_Original = QtWidgets.QAction(MainWindow)
        self.actionMA_Original.setObjectName("actionMA_Original")
        self.actionRangeBreak_Original = QtWidgets.QAction(MainWindow)
        self.actionRangeBreak_Original.setObjectName("actionRangeBreak_Original")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutMC = QtWidgets.QAction(MainWindow)
        self.actionAboutMC.setObjectName("actionAboutMC")
        self.actionPowerLanguage_Editor = QtWidgets.QAction(MainWindow)
        self.actionPowerLanguage_Editor.setObjectName("actionPowerLanguage_Editor")
        self.actionAdaboost = QtWidgets.QAction(MainWindow)
        self.actionAdaboost.setObjectName("actionAdaboost")
        self.menuTurtle.addAction(self.actionTurtle30k)
        self.menuTurtle.addAction(self.actionTurtle60k)
        self.menuMoveAverage.addAction(self.actionMA_Original)
        self.menuRangeBreak.addAction(self.actionRangeBreak_Original)
        self.menu_Strategy.addAction(self.menuTurtle.menuAction())
        self.menu_Strategy.addAction(self.menuMoveAverage.menuAction())
        self.menu_Strategy.addAction(self.menuRangeBreak.menuAction())
        self.menu_AI.addAction(self.actionRF_2)
        self.menu_AI.addAction(self.actionDT_2)
        self.menu_AI.addAction(self.actionLSTM_2)
        self.menu_AI.addAction(self.actionMLP_2)
        self.menu_AI.addAction(self.actionAdaboost)
        self.menuOpen.addAction(self.actionMulticharts)
        self.menuOpen.addAction(self.actionPowerLanguage_Editor)
        self.menu_About.addAction(self.actionAbout)
        self.menu_About.addAction(self.actionAboutMC)
        self.menubar.addAction(self.menu_Strategy.menuAction())
        self.menubar.addAction(self.menu_AI.menuAction())
        self.menubar.addAction(self.menu_Reports.menuAction())
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title3.setText(_translate("MainWindow", "TextLabel"))
        self.title1.setText(_translate("MainWindow", "TextLabel"))
        self.title4.setText(_translate("MainWindow", "TextLabel"))
        self.title5.setText(_translate("MainWindow", "TextLabel"))
        self.title2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menu_Strategy.setTitle(_translate("MainWindow", "交易策略"))
        self.menuTurtle.setTitle(_translate("MainWindow", "海龜"))
        self.menuMoveAverage.setTitle(_translate("MainWindow", "移動均線"))
        self.menuRangeBreak.setTitle(_translate("MainWindow", "區間突破"))
        self.menu_AI.setTitle(_translate("MainWindow", "AI"))
        self.menu_Reports.setTitle(_translate("MainWindow", "績效報告"))
        self.menuOpen.setTitle(_translate("MainWindow", "開啟"))
        self.menu_About.setTitle(_translate("MainWindow", "關於"))
        self.actionRF_2.setText(_translate("MainWindow", "隨機森林(RF)"))
        self.actionDT_2.setText(_translate("MainWindow", "決策樹(DT)"))
        self.actionLSTM_2.setText(_translate("MainWindow", "長短期記憶(LSTM)"))
        self.actionMLP_2.setText(_translate("MainWindow", "多層感知器(MLP)"))
        self.actionMulticharts.setText(_translate("MainWindow", "Multicharts"))
        self.actionTurtle30k.setText(_translate("MainWindow", "海龜30k策略集"))
        self.actionTurtle60k.setText(_translate("MainWindow", "海龜60k策略集"))
        self.actionMA_Original.setText(_translate("MainWindow", "移動均線策略集"))
        self.actionRangeBreak_Original.setText(_translate("MainWindow", "區間突破策略集"))
        self.actionAbout.setText(_translate("MainWindow", "關於我們"))
        self.actionAboutMC.setText(_translate("MainWindow", "關於Multicharts"))
        self.actionPowerLanguage_Editor.setText(_translate("MainWindow", "PowerLanguage Editor"))
        self.actionAdaboost.setText(_translate("MainWindow", "自適應增強(Adaboost)"))
