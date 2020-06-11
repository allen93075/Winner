import subprocess
import sys, os, webbrowser
import pandas as pd
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QAction
from webcrawler import webcrawler, link , article
from Menu import About_US
from New_UI_for_edit import Ui_MainWindow
from LSTM_call import LSTM
from RF_call import RF
from Adaboost_call import AdaboostUI
from BigBar_Strategies_call import BigBar_Strategies
from MLP_UI_call import MLPUI
from MoveAverage_Strategies_call import MoveAverage_Strategies
from RangeBreak_Strategies_call import RangeBreak_Strategies
from Turtle30k_Strategies_call import Turtle30k_Strategies
from CCI_Strategies_call import CCI_Strategies
from Read_txt_call import ReadTXT
from LSTM_controll_call import LSTMcall
from useRF_call import useRF

class Mainwin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stack1 = QtWidgets.QWidget()
        self.ui.stack1 = LSTM()
        #self.ui.stack1.__init__()
        self.ui.stack1.setObjectName("LSTM_UI")
        self.ui.stackedWidget.addWidget(self.ui.stack1)  # widget_index = 2
        self.ui.stack3 = QtWidgets.QWidget()
        self.ui.stack3 = MLPUI()
        #self.ui.stack3.__init__()
        self.ui.stack3.setObjectName("MLP")
        self.ui.stackedWidget.addWidget(self.ui.stack3) # widget_index = 3
        self.ui.stack4 = QtWidgets.QWidget()
        self.ui.stack4.setObjectName("ADAboost")
        self.ui.stack4 = AdaboostUI()
        self.ui.stackedWidget.addWidget(self.ui.stack4) # widget_index = 4
        self.ui.stack5 = QtWidgets.QTableWidget()
        self.ui.stack5.setObjectName("Turtle30k")
        self.ui.stack5 = Turtle30k_Strategies()
        self.ui.stackedWidget.addWidget(self.ui.stack5)  # widget_index = 5
        self.ui.stack6 = QtWidgets.QTableWidget()
        self.ui.stack6.setObjectName("MoveAverage")
        self.ui.stack6 = MoveAverage_Strategies()
        self.ui.stackedWidget.addWidget(self.ui.stack6)  # widget_index = 6
        self.ui.stack7 = QtWidgets.QTableWidget()
        self.ui.stack7.setObjectName("RangeBreak")
        self.ui.stack7 = RangeBreak_Strategies()
        self.ui.stackedWidget.addWidget(self.ui.stack7)  # widget_index = 7
        self.ui.stack8 = QtWidgets.QTableWidget()
        self.ui.stack8.setObjectName("BigBar")
        self.ui.stack8 = BigBar_Strategies()
        self.ui.stackedWidget.addWidget(self.ui.stack8)  # widget_index = 8
        self.ui.stack9 = QtWidgets.QWidget()
        self.ui.stack9 = useRF()
        self.ui.stack9.setObjectName("Randomforest")
        self.ui.stackedWidget.addWidget(self.ui.stack9)  # widget_index = 9
        self.ui.stack10 = QtWidgets.QWidget()
        self.ui.stack10.setObjectName("LSTM_controll")
        self.ui.stack10 = LSTMcall()
        self.ui.stackedWidget.addWidget(self.ui.stack10)  # widget_index = 10
        self.ui.stack11 = QtWidgets.QWidget()
        self.ui.stack11.setObjectName("Performance")
        self.ui.stack11 = ReadTXT()
        self.ui.stackedWidget.addWidget(self.ui.stack11)  # widget_index = 11
        self.ui.stack12 = QtWidgets.QWidget()
        self.ui.stack12.setObjectName("CCI")
        self.ui.stack12 = CCI_Strategies()
        self.ui.stackedWidget.addWidget(self.ui.stack12)  # widget_index = 12
        self.ui.stack13 = RF()
        self.ui.stackedWidget.addWidget(self.ui.stack13) # widget_index = 13
        self.resize(800, 600)

        self.ui.actionMLP_2.triggered.connect(self.callMLP)

        self.ui.actionAdaboost.triggered.connect(self.callAdaboost)

        self.ui.actionLSTM_2.triggered.connect(self.callLSTM)
        self.ui.actionReports.triggered.connect(self.callPerformance)
        self.ui.actionAbout.triggered.connect(self.callAboutus)
        self.ui.actionAboutMC.triggered.connect(self.callAboutMC)
        self.ui.actionMulticharts.triggered.connect(self.callMC)
        self.ui.actionPowerLanguage_Editor.triggered.connect(self.OpenPLEditor)
        self.ui.actionTurtle30k.triggered.connect(self.callTurtle30k)
        self.ui.actionMA_Original.triggered.connect(self.callMA)
        self.ui.actionRangeBreak_Original.triggered.connect(self.callRangeBreak)
        self.ui.actionRF_2.triggered.connect(self.callRF)
        self.ui.actionBigBar_Original.triggered.connect(self.callBigBar)
        self.ui.actionLSTM.triggered.connect(self.call_LSTMcontroll)
        self.ui.actionCCI_Original.triggered.connect(self.callCCI)
        self.ui.actionRF.triggered.connect(self.call_RFcontroll)
        self.ui.title1.setOpenExternalLinks(True)
        self.ui.title2.setOpenExternalLinks(True)
        self.ui.title3.setOpenExternalLinks(True)
        self.ui.title4.setOpenExternalLinks(True)
        self.ui.title5.setOpenExternalLinks(True)
        #   MainWindow Title
        self.setWindowTitle('期貨贏家機器人')
        self.statusBar().showMessage('歡迎使用期貨贏家機器人！')

    # def web(self, a=[]):
    #     self.ui.title1.setText(a[0])
    #     self.ui.title2.setText(a[1])
    #     self.ui.title3.setText(a[2])
    #     self.ui.title4.setText(a[3])
    #     self.ui.title5.setText(a[4])

    def link(self, b=[], a=[],c=[]):
        self.ui.title1.setText(("<a href=\"" + b[0] + "\">\n" + a[0]))
        self.ui.title2.setText(("<a href=\"" + b[1] + "\">\n" + a[1]))
        self.ui.title3.setText(("<a href=\"" + b[2] + "\">\n" + a[2]))
        self.ui.title4.setText(("<a href=\"" + b[3] + "\">\n" + a[3]))
        self.ui.title5.setText(("<a href=\"" + b[4] + "\">\n" + a[4]))
        self.ui.article1.setText(c[0])
        self.ui.article2.setText(c[1])
        self.ui.article3.setText(c[2])
        self.ui.article4.setText(c[3])
        self.ui.article5.setText(c[4])

    def callLSTM(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        print(self.ui.stackedWidget.count())
        print(self.ui.stackedWidget.currentIndex())
        print(self.ui.stackedWidget.currentWidget().objectName())
        print(self.ui.stackedWidget.currentWidget())
        print(self.ui.stackedWidget.indexOf(self.ui.stack1))

    def callRF(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def callMC(self):
        # self.call = os.system(
        #     'open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [2].app"')
        # self.statusBar().showMessage('正在開起Multicharts主程式')
        commend = '"C:\Program Files\TS Support\MultiCharts64\MultiCharts64.exe"'
        p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def OpenPLEditor(self):
        # self.call = os.system(
        #     'open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/PowerLanguage Editor.app"')
        # self.statusBar().showMessage('正在開起PowerLanguage Editor')
        commend = '"C:\Program Files\TS Support\MultiCharts64\PLEditor.exe"'
        p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


    def callAboutMC(self):
        webbrowser.open("https://www.multicharts.com.tw/characteristic.aspx")
        self.statusBar().showMessage('正在開起網頁')

    def callAboutus(self):
        self.callAboutus = About_US()
        self.callAboutus.show()
        self.statusBar().showMessage('開啟關於我們')

    def callTurtle30k(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.statusBar().showMessage('開啟海龜策略集')

    def callMA(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.statusBar().showMessage('開啟移動均線策略集')

    def callRangeBreak(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        self.statusBar().showMessage('開啟區間突破策略集')

    def callCCI(self):
        self.ui.stackedWidget.setCurrentIndex(12)
        self.statusBar().showMessage('開啟CCI策略集')

    def callAdaboost(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    def callMLP(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def callBigBar(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        self.statusBar().showMessage('開啟BigBar策略集')

    def callPerformance(self):
        self.ui.stackedWidget.setCurrentIndex(11)
        self.statusBar().showMessage('開啟績效報告')

    def call_LSTMcontroll(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def call_RFcontroll(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def BackHome(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.statusBar().showMessage('返回主頁')

    # def SetHomebutton(self):
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap('Homebtnicon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #     self.ui.BackHome_button.setIcon(icon)
    #     self.ui.BackHome_button.setIconSize(QtCore.QSize(30, 30))
    #     self.ui.BackHome_button.setAutoRepeatDelay(200)
    #
    # def SetMCbutton(self):
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap('multicharts_logo_big.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #     self.ui.MCcall_button.setIcon(icon)
    #     self.ui.MCcall_button.setIconSize(QtCore.QSize(30, 30))
    #     # self.ui.MCcall_button.setAutoRepeatDelay(200)
    #
    # def SetPLbutton(self):
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap('PLlogo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #     self.ui.PLcall_button.setIcon(icon)
    #     self.ui.PLcall_button.setIconSize(QtCore.QSize(30, 30))
    #     # self.ui.PLcall_button.setAutoRepeatDelay(200)

    def toolbar(self):
        self.toolbar = self.addToolBar('Winner')
        BackHome = QAction(QIcon('Homebtnicon.png'), '返回主頁', self)
        BackHome.triggered.connect((self.BackHome))
        self.toolbar.addAction(BackHome)

        OpenMC = QAction(QIcon('multicharts_logo_big.png'), '開啟Multicahrts', self)
        OpenMC.triggered.connect((self.callMC))
        self.toolbar.addAction(OpenMC)

        OpenPL = QAction(QIcon('fx-sign.png'), '開啟PL Editor', self)
        OpenPL.triggered.connect((self.OpenPLEditor))
        self.toolbar.addAction(OpenPL)

        self.toolbar.addSeparator()
        exitAct = QAction(QIcon('exit.png'), '離開', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.close)
        self.toolbar.addAction(exitAct)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    # app.setStyleSheet(dark_stylesheet)
    ui = Mainwin()
    ui.link(link(), webcrawler(),article())
    ui.toolbar()
    ui.show()
    sys.exit(app.exec_())
