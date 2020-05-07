import Adaboost_UI
from  PyQt5 import QtWidgets

class AdaboostUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(AdaboostUI, self).__init__()
        self.ui = Adaboost_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('自適應增強')

