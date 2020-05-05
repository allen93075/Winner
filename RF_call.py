import sys

from PyQt5 import QtWidgets
from RF import Ui_Form


class RF(QtWidgets.QWidget):
    def __int__(self):
        super(RF,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("隨機森林")


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ui = RF()
#     ui.__int__()
#     ui.show()
#     sys.exit(app.exec_())
