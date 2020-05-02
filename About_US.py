import AboutUS
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class About_US(QtWidgets.QTableWidget):
    def __init__(self):
        super(About_US, self).__init__()
        self.ui = AboutUS.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('關於我們')


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = About_US()
    ui.show()