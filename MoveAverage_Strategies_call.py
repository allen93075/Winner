import MoveAverage_Strategies_UI, os, sys
from  PyQt5 import QtWidgets

class MoveAverage_Strategies(QtWidgets.QWidget):
    def __init__(self):
        super(MoveAverage_Strategies, self).__init__()
        self.ui = MoveAverage_Strategies_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenEditor)
        self.ui.pushButton_2.clicked.connect(self.OpenMC)
#       Form Title
        self.setWindowTitle('移動均線策略集')
        self.resize(600, 600)

    def OpenEditor(self):
        self.call = os.system('open -a "C:\Program Files\TS Support\MultiCharts64\PLEditor.exe"')
    def OpenMC(self):
        self.call = os.system('open -a "C:\Program Files\TS Support\MultiCharts64\MultiCharts64.exe"')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MoveAverage_Strategies()
    ui.show()
    sys.exit(app.exec_())