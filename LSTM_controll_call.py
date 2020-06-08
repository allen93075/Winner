import os
import sys

from PyQt5 import QtWidgets
from LSTM_controll import Ui_Form
from LSTM2 import *


class LSTMcall(QtWidgets.QWidget):
    def __init__(self):
        super(LSTMcall, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.train_toolButton.clicked.connect(self.slot_btn_chooseDir_2)
        self.ui.test_toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.sentout_pushButton.clicked.connect(self.exec_lstm)
        self.resize(800, 600)

    def get_lookback(self):

        return int(self.ui.lookback_comboBox.currentText())

    def get_droprate(self):
        return float(self.ui.droprate_comboBox.currentText())

    def slot_btn_chooseDir_2(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取檔案",
                                                           self.cwd,
                                                           "All Files (*);;Excel (*.csv)")  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        self.ui.train_comboBox.addItem(dir_choose[0])
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)
        return dir_choose

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取檔案",
                                                           self.cwd,
                                                           "All Files (*);;Excel (*.csv)")  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        self.ui.test_comboBox.addItem(dir_choose[0])
        # print(type(dir_choose))
        # print("\n你選擇的文件夾為:")
        # print(dir_choose)
        return dir_choose

    def exec_lstm(self):
        print(self.ui.train_comboBox.currentText())
        print(self.ui.test_comboBox.currentText())
        print(self.get_droprate())
        print(type(self.get_droprate()))
        print(self.get_lookback())
        print(type(self.get_lookback()))
        build_model(self.get_droprate(),
                    self.get_lookback(),
                    train_data(self.ui.train_comboBox.currentText()),
                    test_data(self.ui.test_comboBox.currentText()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LSTMcall()
    ui.show()
    sys.exit(app.exec_())
