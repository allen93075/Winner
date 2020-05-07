import MLP_UI
from  PyQt5 import QtWidgets

class MLPUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(MLPUI, self).__init__()
        self.ui = MLP_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('多層感知器')