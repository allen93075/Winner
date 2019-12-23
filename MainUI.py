# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI(donotpush).ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from webcrawler import webcrawler,link

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Products_area = QtWidgets.QDockWidget(self.splitter)
        self.Products_area.setAutoFillBackground(False)
        self.Products_area.setFloating(False)
        self.Products_area.setObjectName("Products_area")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.product = QtWidgets.QComboBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product.sizePolicy().hasHeightForWidth())
        self.product.setSizePolicy(sizePolicy)
        self.product.setEditable(False)
        self.product.setMaxVisibleItems(100)
        self.product.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.product.setObjectName("product")
        self.product.addItem("")
        self.horizontalLayout.addWidget(self.product)
        self.algorithm = QtWidgets.QComboBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm.sizePolicy().hasHeightForWidth())
        self.algorithm.setSizePolicy(sizePolicy)
        self.algorithm.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.horizontalLayout.addWidget(self.algorithm)
        self.period = QtWidgets.QComboBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.period.sizePolicy().hasHeightForWidth())
        self.period.setSizePolicy(sizePolicy)
        self.period.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.period.setObjectName("period")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.horizontalLayout.addWidget(self.period)
        self.pushButton_sentout = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_sentout.setAutoDefault(False)
        self.pushButton_sentout.setDefault(False)
        self.pushButton_sentout.setFlat(False)
        self.pushButton_sentout.setObjectName("pushButton_sentout")
        self.horizontalLayout.addWidget(self.pushButton_sentout)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.Products_area.setWidget(self.dockWidgetContents)
        self.product_status = QtWidgets.QDockWidget(self.splitter)
        self.product_status.setObjectName("product_status")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.listView_2 = QtWidgets.QListView(self.dockWidgetContents_2)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_4.addWidget(self.listView_2, 1, 0, 1, 1)
        self.product_status.setWidget(self.dockWidgetContents_2)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.Kbar_area = QtWidgets.QDockWidget(self.splitter_2)
        self.Kbar_area.setObjectName("Kbar_area")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.columnView = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.columnView.setObjectName("K_Line")
        self.gridLayout_5.addWidget(self.columnView, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.Kbar_area.setWidget(self.dockWidgetContents_3)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 357))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title5.setObjectName("title5")
        self.gridLayout_2.addWidget(self.title5, 4, 0, 1, 1)
        self.title1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title1.setObjectName("title1")
        self.gridLayout_2.addWidget(self.title1, 0, 0, 1, 1)
        self.title2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title2.setObjectName("title2")
        self.gridLayout_2.addWidget(self.title2, 1, 0, 1, 1)
        self.title4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title4.setObjectName("title4")
        self.gridLayout_2.addWidget(self.title4, 3, 0, 1, 1)
        self.title3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title3.setObjectName("title3")
        self.gridLayout_2.addWidget(self.title3, 2, 0, 1, 1)
        self.link1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.link1.setObjectName("link1")
        self.gridLayout_2.addWidget(self.link1, 0, 1, 1, 1)
        self.link2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.link2.setObjectName("link2")
        self.gridLayout_2.addWidget(self.link2, 1, 1, 1, 1)
        self.link3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.link3.setObjectName("link3")
        self.gridLayout_2.addWidget(self.link3, 2, 1, 1, 1)
        self.link4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.link4.setObjectName("link4")
        self.gridLayout_2.addWidget(self.link4, 3, 1, 1, 1)
        self.link5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.link5.setObjectName("link5")
        self.gridLayout_2.addWidget(self.link5, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLSTM = QtWidgets.QAction(MainWindow)
        self.actionLSTM.setObjectName("actionLSTM")
        self.actionrm_6hk4gj4 = QtWidgets.QAction(MainWindow)
        self.actionrm_6hk4gj4.setObjectName("actionrm_6hk4gj4")
        self.menu_2.addAction(self.actionLSTM)
        self.menu_2.addAction(self.actionrm_6hk4gj4)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "時間"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名稱"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "開盤價"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "高點"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "低點"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "收盤價"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "成交量"))
        self.product.setCurrentText(_translate("MainWindow", "商品..."))
        self.product.setItemText(0, _translate("MainWindow", "商品..."))
        self.algorithm.setItemText(0, _translate("MainWindow", "演算法..."))
        self.period.setItemText(0, _translate("MainWindow", "時間線"))
        self.period.setItemText(1, _translate("MainWindow", "10分鐘"))
        self.period.setItemText(2, _translate("MainWindow", "30分鐘"))
        self.period.setItemText(3, _translate("MainWindow", "60分鐘"))
        self.pushButton_sentout.setText(_translate("MainWindow", "送出"))
        self.lineEdit_2.setText(_translate("MainWindow", "走勢圖..."))
        self.lineEdit.setText(_translate("MainWindow", "K棒圖"))
        self.title5.setText(_translate("MainWindow", "TextLabel"))
        self.title1.setText(_translate("MainWindow", "OAO"))
        self.title2.setText(_translate("MainWindow", "TextLabel"))
        self.title4.setText(_translate("MainWindow", "TextLabel"))
        self.title3.setText(_translate("MainWindow", "TextLabel"))
        self.link1.setText(_translate("MainWindow", "TextLabel"))
        self.link2.setText(_translate("MainWindow", "TextLabel"))
        self.link3.setText(_translate("MainWindow", "TextLabel"))
        self.link4.setText(_translate("MainWindow", "TextLabel"))
        self.link5.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "歷史回測"))
        self.menu_2.setTitle(_translate("MainWindow", "交易策略模組"))
        self.menu_3.setTitle(_translate("MainWindow", "策略管理模組"))
        self.menu_4.setTitle(_translate("MainWindow", "資金管理"))
        self.menu_5.setTitle(_translate("MainWindow", "績效評估"))
        self.menu_6.setTitle(_translate("MainWindow", "下單機"))
        self.actionLSTM.setText(_translate("MainWindow", "LSTM"))
        self.actionrm_6hk4gj4.setText(_translate("MainWindow", "決策樹"))


class Mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainwin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.link1.setOpenExternalLinks(True)
        self.ui.link2.setOpenExternalLinks(True)
        self.ui.link3.setOpenExternalLinks(True)
        self.ui.link4.setOpenExternalLinks(True)
        self.ui.link5.setOpenExternalLinks(True)



    def web(self,a=[]):
        self.ui.title1.setText(a[0])
        self.ui.title2.setText(a[1])
        self.ui.title3.setText(a[2])
        self.ui.title4.setText(a[3])
        self.ui.title5.setText(a[4])

    def link(self,b=[]):
        self.ui.link1.setText(("<a href=\""+ b[0] +"\">"+b[0]))
        self.ui.link2.setText(("<a href=\"" + b[1] + "\">"+b[1]))
        self.ui.link3.setText(("<a href=\"" + b[2] + "\">"+b[2]))
        self.ui.link4.setText(("<a href=\"" + b[3] + "\">"+b[3]))
        self.ui.link5.setText(("<a href=\"" + b[4] + "\">"+b[4]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mainwin()
    ui.web(webcrawler())
    ui.link(link())
    ui.show()
    sys.exit(app.exec_())