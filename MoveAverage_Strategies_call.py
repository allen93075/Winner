import MoveAverage_Strategies_UI, os
from  PyQt5 import QtWidgets

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
