import os
import sys

from PyQt5 import QtWidgets, QtGui
from LSTM import Ui_Form
from LSTM2 import *


class LSTM(QtWidgets.QWidget):
    def __init__(self):
        super(LSTM, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.traindata_toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.testdata_toolButton.clicked.connect(self.slot_btn_chooseDir_2)
        self.ui.sentout_button.clicked.connect(self.exec_lstm)
        self.ui.sentout_button.clicked.connect(self.performance)

    def get_look_back_count(self):
        print("我有沒有執行一次呢?")
        print("lookback_type:", type(self.ui.look_back_count.currentText()))
        return self.ui.look_back_count.currentText()  # string型態傳回

    def get_droprate(self):
        return self.ui.dropout_rate.currentText()

    def exec_lstm(self):

        build_model(float(self.get_droprate()), int(self.get_look_back_count()),
                    train_data(self.ui.train_data_combobox.currentText()),
                    test_data(self.ui.test_data_combobox.currentText()))

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取文件夾",
                                                           self.cwd,
                                                           "excel(*.csv)")  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        print(dir_choose[0])
        self.ui.train_data_combobox.addItem(dir_choose[0])
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)
        print(self.ui.train_data_combobox.currentText())
        print(type(self.ui.train_data_combobox.currentText()))

    def slot_btn_chooseDir_2(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取文件夾",
                                                           self.cwd)  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        self.ui.test_data_combobox.addItem(dir_choose[0])
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)
        return dir_choose

    def performance(self):
        f = open(r'C:/Users/Allen/PycharmProjects/Winner/test.txt')
        t = f.readline()
        text = t.split(",")
        text = list(map(str, text))
        text = [float(x) for x in text]
        # Earning odds
        t1 = (text[4] / text[5])
        EarningOdds = str(t1)  # back to str
        # ProfitFactor
        t2 = (text[6] / text[7] - 1)
        ProfitFactor = str(t2)
        # TotalTradesCost
        t3 = (1000 * text[3])
        TotalTradesCost = str(t3)
        text = [str(x) for x in text]

        self.ui.netprofit_label.setText(text[0])
        self.ui.winrate_label.setText(text[1])
        self.ui.winloserate_label.setText(EarningOdds)
        self.ui.profit_factor_label.setText(ProfitFactor)
        self.ui.mdd_label.setText(text[2])
        self.ui.trade_count_label.setText(text[3])
        self.ui.trade_cost_labeL.setText(TotalTradesCost)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LSTM()
    ui.show()
    sys.exit(app.exec_())