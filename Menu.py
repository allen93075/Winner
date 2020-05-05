import AboutUS_UI
from PyQt5 import QtWidgets

class About_US(QtWidgets.QTableWidget):
    def __init__(self):
        super(About_US, self).__init__()
        self.ui = AboutUS_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('關於我們')