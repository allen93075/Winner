import Turtle30k_Strategies_UI, os, sys
from  PyQt5 import QtWidgets

class Turtle30k_Strategies(QtWidgets.QTableWidget):
    def __init__(self):
        super(Turtle30k_Strategies, self).__init__()
        self.ui = Turtle30k_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
#       Form Title
        self.setWindowTitle('海龜30k策略集')
        self.resize(600, 600)
    def OpenEditor(self):
        # self.call = os.system('open -a "/Users/tienyou/Applications (Parallels)/{a385b35d-69a7-4fa5-9d2b-3a0d2c95954e} Applications.localized/MultiCharts64 [4].app"')
        self.call = os.system('"C:\Program Files\TS Support\MultiCharts64\PLEditor.exe"')
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Turtle30k_Strategies()
    ui.show()
    sys.exit(app.exec_())