import AboutUS_UI, Turtle60k_Strategies_UI,Turtle30k_Strategies_UI, MoveAverage_Strategies_UI, RangeBreak_Strategies_UI , os, Adaboost_UI, MLP_UI, RF
from PyQt5 import QtWidgets

class About_US(QtWidgets.QTableWidget):
    def __init__(self):
        super(About_US, self).__init__()
        self.ui = AboutUS_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('關於我們')

class Turtle60k_Strategies(QtWidgets.QTableWidget):
    def __init__(self):
        super(Turtle60k_Strategies, self).__init__()
        self.ui = Turtle60k_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
#       Form Title
        self.setWindowTitle('海龜60k策略集')

    def OpenEditor(self):
        self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')

class Turtle30k_Strategies(QtWidgets.QTableWidget):
    def __init__(self):
        super(Turtle30k_Strategies, self).__init__()
        self.ui = Turtle30k_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
#       Form Title
        self.setWindowTitle('海龜30k策略集')

    def OpenEditor(self):
        self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')

class MoveAverage_Strategies(QtWidgets.QTableWidget):
    def __init__(self):
        super(MoveAverage_Strategies, self).__init__()
        self.ui = MoveAverage_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
#       Form Title
        self.setWindowTitle('移動均線策略集')

    def OpenEditor(self):
        self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')

class RangeBreak_Strategies(QtWidgets.QTableWidget):
    def __init__(self):
        super(RangeBreak_Strategies, self).__init__()
        self.ui = RangeBreak_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
#       Form Title
        self.setWindowTitle('區間突破策略集')

    def OpenEditor(self):
        self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')

class AdaboostUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(AdaboostUI, self).__init__()
        self.ui = Adaboost_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('自適應增強')

class MLPUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(MLPUI, self).__init__()
        self.ui = MLP_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('多層感知器')

class RFUI(QtWidgets.QWidget):
    def __int__(self):
        super(RFUI,self).__init__()
        self.ui = RF.Ui_Form()
        self.ui.setupUi(self)
        # Form Title
        self.setWindowTitle("隨機森林")