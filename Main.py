import sys, os, webbrowser
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from webcrawler import webcrawler, link
from str_tree import Str_tree
from About_US import About_US
from Strategies import Turtle60k_Strategies, Turtle30k_Strategies, MoveAverage_Strategies, RangeBreak_Strategies
from MainUI import Ui_MainWindow
class Mainwin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Mainwin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionDT_Original.triggered.connect(self.des)
        self.ui.actionAbout.triggered.connect(self.AboutUs)
        self.ui.actionAboutMC.triggered.connect(self.AboutMC)
        self.ui.actionMulticharts.triggered.connect(self.callMC)
        self.ui.actionTurtle30k.triggered.connect(self.Turtle30kUI)
        self.ui.actionTurtle60k.triggered.connect(self.Turtle60kUI)
        self.ui.actionMA_Original.triggered.connect(self.MAUI)
        self.ui.actionRangeBreak_Original.triggered.connect(self.RangeBreakUI)
        self.ui.link1.setOpenExternalLinks(True)
        self.ui.link2.setOpenExternalLinks(True)
        self.ui.link3.setOpenExternalLinks(True)
        self.ui.link4.setOpenExternalLinks(True)
        self.ui.link5.setOpenExternalLinks(True)
    #   MainWindow Title
        self.setWindowTitle('期貨贏家機器人')

    def web(self, a=[]):
        self.ui.title1.setText(a[0])
        self.ui.title2.setText(a[1])
        self.ui.title3.setText(a[2])
        self.ui.title4.setText(a[3])
        self.ui.title5.setText(a[4])

    def link(self, b=[]):
        self.ui.link1.setText(("<a href=\"" + b[0] + "\">" + b[0]))
        self.ui.link2.setText(("<a href=\"" + b[1] + "\">" + b[1]))
        self.ui.link3.setText(("<a href=\"" + b[2] + "\">" + b[2]))
        self.ui.link4.setText(("<a href=\"" + b[3] + "\">" + b[3]))
        self.ui.link5.setText(("<a href=\"" + b[4] + "\">" + b[4]))

    def des(self):
        self.a = Str_tree()
        self.a.show()

    def callMC(self):
        self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [2].app"')

    def AboutMC(self):
        webbrowser.open("https://www.multicharts.com.tw/characteristic.aspx")

    def AboutUs(self):
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Mainwin()
    ui.web(webcrawler())
    ui.link(link())
    ui.show()
    sys.exit(app.exec_())
