# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI import Mainwin


class Ui_login(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 70, 251, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.id_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.id_label)
        self.psw_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.psw_label.setFont(font)
        self.psw_label.setObjectName("psw_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.psw_label)
        self.id_text = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.id_text.setFont(font)
        self.id_text.setObjectName("id_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_text)
        self.psw_text = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.psw_text.setFont(font)
        self.psw_text.setObjectName("psw_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.psw_text)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.login_btn.setObjectName("login_btn")
        
        #self.login_btn.clicked.connect(self.login_btn_act)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id_label.setText(_translate("MainWindow", "帳號"))
        self.psw_label.setText(_translate("MainWindow", "密碼"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        
class Mainlogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainlogin, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login_btn_act)
        
    def act(self):
        self.ui.login_btn_act
        
    def login_btn_act(self):
        self.hide()
        self.m = Mainwin()
        self.m.show()
        
if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mainlogin()

    #ui.__init__
    ui.show()
    sys.exit(app.exec_()) 