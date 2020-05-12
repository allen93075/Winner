import os
import sys

from PyQt5 import QtWidgets, QtGui
from RangeBreak_Performance import Ui_Form



class RB_Performance(QtWidgets.QWidget):
    def __init__(self):
        super(RB_Performance, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.performancedata_toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.sentout_button.clicked.connect(self.performance)

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取文件夾",
                                                           self.cwd,
                                                           "(*.txt)")  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        print(dir_choose[0])
        self.ui.performance_data_combobox.addItem(dir_choose[0])
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)
        print(self.ui.performance_data_combobox.currentText())
        print(type(self.ui.performance_data_combobox.currentText()))

    def performance(self):
        f = open(r'/Users/tienyou/PycharmProjects/Winner/Performance/RangeBreak.txt')
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
    ui = RB_Performance()
    ui.show()
    sys.exit(app.exec_())
