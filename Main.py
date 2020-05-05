import sys, os, webbrowser
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from webcrawler import webcrawler, link
from Menu import About_US, Turtle60k_Strategies, Turtle30k_Strategies, MoveAverage_Strategies, RangeBreak_Strategies, AdaboostUI, MLPUI, RFUI
from MainUI import Ui_MainWindow
from LSTM_call import LSTM
# from RF_call import RF


class Mainwin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack1 = QtWidgets.QWidget()
        self.ui.stack1 = LSTM()
        self.ui.stack1.__int__()
        self.ui.stack1.setObjectName("LSTM_UI")
        self.ui.stackedWidget.addWidget(self.ui.stack1)
        self.ui.stack2 = RFUI()
        self.ui.stack2.__int__()
        self.ui.stack2.setObjectName("Randomforest")
        self.ui.stackedWidget.addWidget(self.ui.stack2)
        self.resize(600, 600)
        self.ui.actionMLP_2.triggered.connect(self.callMLP)
        self.ui.actionAdaboost.triggered.connect(self.callAdaboost)
        self.ui.actionLSTM_2.triggered.connect(self.callLSTM)
        self.ui.actionAbout.triggered.connect(self.AboutusUI)
        self.ui.actionAboutMC.triggered.connect(self.AboutMC)
        self.ui.actionMulticharts.triggered.connect(self.callMC)
        self.ui.actionPowerLanguage_Editor.triggered.connect(self.OpenPLEditor)
        self.ui.actionTurtle30k.triggered.connect(self.Turtle30kUI)
        self.ui.actionTurtle60k.triggered.connect(self.Turtle60kUI)
        self.ui.actionMA_Original.triggered.connect(self.MAUI)
        self.ui.actionRangeBreak_Original.triggered.connect(self.RangeBreakUI)
        self.ui.actionRF_2.triggered.connect(self.callRF)
        self.ui.title1.setOpenExternalLinks(True)
        self.ui.title2.setOpenExternalLinks(True)
        self.ui.title3.setOpenExternalLinks(True)
        self.ui.title4.setOpenExternalLinks(True)
        self.ui.title5.setOpenExternalLinks(True)
        #   MainWindow Title
        self.setWindowTitle('期貨贏家機器人')

    def web(self, a=[]):
        self.ui.title1.setText(a[0])
        self.ui.title2.setText(a[1])
        self.ui.title3.setText(a[2])
        self.ui.title4.setText(a[3])
        self.ui.title5.setText(a[4])

    def link(self, b=[], a=[]):
        self.ui.title1.setText(("<a href=\"" + b[0] + "\">\n" + a[0]))
        self.ui.title2.setText(("<a href=\"" + b[1] + "\">\n" + a[1]))
        self.ui.title3.setText(("<a href=\"" + b[2] + "\">\n" + a[2]))
        self.ui.title4.setText(("<a href=\"" + b[3] + "\">\n" + a[3]))
        self.ui.title5.setText(("<a href=\"" + b[4] + "\">\n" + a[4]))

    def callLSTM(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        print(self.ui.stackedWidget.count())
        print(self.ui.stackedWidget.currentIndex())
        print(self.ui.stackedWidget.currentWidget().objectName())
        print(self.ui.stackedWidget.currentWidget())
        print(self.ui.stackedWidget.indexOf(self.ui.stack1))

    def callRF(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def callMC(self):
        self.call = os.system(
            'open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [2].app"')

    def OpenPLEditor(self):
        self.call = os.system(
            'open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')

    def AboutMC(self):
        webbrowser.open("https://www.multicharts.com.tw/characteristic.aspx")

    def AboutusUI(self):
        self.aboutus = About_US()
        self.aboutus.show()

    def Turtle30kUI(self):
        self.turtle30kui = Turtle30k_Strategies()
        self.turtle30kui.show()

    def Turtle60kUI(self):
        self.turtle60kui = Turtle60k_Strategies()
        self.turtle60kui.show()

    def MAUI(self):
        self.maui = MoveAverage_Strategies()
        self.maui.show()

    def RangeBreakUI(self):
        self.rangebreakui = RangeBreak_Strategies()
        self.rangebreakui.show()

    def callAdaboost(self):
        self.calladaboost = AdaboostUI()
        self.calladaboost.show()

    def callMLP(self):
        self.callmlp = MLPUI()
        self.callmlp.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Mainwin()
    ui.link(link(), webcrawler())
    ui.show()
    sys.exit(app.exec_())