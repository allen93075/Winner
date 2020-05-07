import os
import sys

from PyQt5 import QtWidgets
from RF import Ui_Form


class RF(QtWidgets.QWidget):
    def __int__(self):
        super(RF,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("隨機森林")
        self.ui.choseDataBtn.clicked.connect(self.slot_btn_chooseDir)

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                "選取文件夾",
                                                                self.cwd)  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.comboBox.addItem(dir_choose)
        print(self.ui.comboBox.currentText())
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = RF()
    ui.__int__()
    ui.show()
    sys.exit(app.exec_())
