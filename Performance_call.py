import Performance_UI
from PyQt5 import QtWidgets

class PerformanceUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(PerformanceUI, self).__init__()
        self.ui = Performance_UI.Ui_widget()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('績效報告')