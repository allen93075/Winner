# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from webcrawler import webcrawler


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Kbar_area = QtWidgets.QDockWidget(self.centralwidget)
        self.Kbar_area.setObjectName("Kbar_area")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.listView = QtWidgets.QListView(self.dockWidgetContents_3)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.Kbar_area.setWidget(self.dockWidgetContents_3)
        self.gridLayout.addWidget(self.Kbar_area, 2, 0, 1, 2)
        self.Products_area = QtWidgets.QDockWidget(self.centralwidget)
        self.Products_area.setAutoFillBackground(False)
        self.Products_area.setFloating(False)
        self.Products_area.setObjectName("Products_area")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.product = QtWidgets.QComboBox(self.dockWidgetContents)
        self.product.setEditable(False)
        self.product.setObjectName("product")
        self.product.addItem("")
        self.horizontalLayout.addWidget(self.product)
        self.algorithm = QtWidgets.QComboBox(self.dockWidgetContents)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.horizontalLayout.addWidget(self.algorithm)
        self.comboBox_3 = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.pushButton_sentout = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_sentout.setAutoDefault(False)
        self.pushButton_sentout.setDefault(True)
        self.pushButton_sentout.setFlat(False)
        self.pushButton_sentout.setObjectName("pushButton_sentout")
        self.horizontalLayout.addWidget(self.pushButton_sentout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.Products_area.setWidget(self.dockWidgetContents)
        self.gridLayout.addWidget(self.Products_area, 0, 0, 1, 1)
        self.product_status = QtWidgets.QDockWidget(self.centralwidget)
        self.product_status.setObjectName("product_status")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.listView_2 = QtWidgets.QListView(self.dockWidgetContents_2)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_2.addWidget(self.listView_2)
        self.product_status.setWidget(self.dockWidgetContents_2)
        self.gridLayout.addWidget(self.product_status, 0, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 465, 368))
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
        self.gridLayout.addWidget(self.scrollArea, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
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
        self.lineEdit.setText(_translate("MainWindow", "K棒圖"))
        self.product.setCurrentText(_translate("MainWindow", "商品..."))
        self.product.setItemText(0, _translate("MainWindow", "商品..."))
        self.algorithm.setItemText(0, _translate("MainWindow", "演算法..."))
        self.pushButton_sentout.setText(_translate("MainWindow", "送出"))
        self.lineEdit_2.setText(_translate("MainWindow", "走勢圖..."))
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

    def web(self,b = []):
        self.ui.title1.setText(b[0])
        self.ui.title2.setText(b[1])
        self.ui.title3.setText(b[2])
        self.ui.title4.setText(b[3])
        self.ui.title5.setText(b[4])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mainwin()
    ui.web(webcrawler())
    ui.show()
    sys.exit(app.exec_())
