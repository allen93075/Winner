import strategic_management
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Str_tree(QtWidgets.QMainWindow):
    def __init__(self):
        super(Str_tree, self).__init__()
        self.ui = strategic_management.Ui_Strategic_management()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Str_tree()
    ui.show()
    sys.exit(app.exec_())