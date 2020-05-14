import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from RangeBreak_Performance import Ui_Form



class RB_Performance(QtWidgets.QWidget):
    def __init__(self):
        super(RB_Performance, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.performancedata_toolButton.clicked.connect(self.slot_btn_chooseDir)
        # self.ui.sentout_button.clicked.connect(self.performance)

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                           "選取多文件",
                                                           self.cwd,
                                                           "Text Files (*.txt)")  # 起始路径
        if len(files) == 0:
            print("\n取消選擇")

        if len(files) >0:
            print("\n你選擇的文件為:")
            for file in files:
                print(file)
            print("\n你選擇的文件類型為:", filetype)
        # print(self.ui.performance_data_combobox.currentText())
        # print(type(self.ui.performance_data_combobox.currentText()))

            f = open(file, "r")
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

    # def performance(self):
    #     f = open(r'/Users/tienyou/PycharmProjects/Winner/Performance/RangeBreak.txt')
    #     t = f.readline()
    #     text = t.split(",")
    #     text = list(map(str, text))
    #     text = [float(x) for x in text]
    #     # Earning odds
    #     t1 = (text[4] / text[5])
    #     EarningOdds = str(t1)  # back to str
    #     # ProfitFactor
    #     t2 = (text[6] / text[7] - 1)
    #     ProfitFactor = str(t2)
    #     # TotalTradesCost
    #     t3 = (1000 * text[3])
    #     TotalTradesCost = str(t3)
    #     text = [str(x) for x in text]
    #
    #     self.ui.netprofit_label.setText(text[0])
    #     self.ui.winrate_label.setText(text[1])
    #     self.ui.winloserate_label.setText(EarningOdds)
    #     self.ui.profit_factor_label.setText(ProfitFactor)
    #     self.ui.mdd_label.setText(text[2])
    #     self.ui.trade_count_label.setText(text[3])
    #     self.ui.trade_cost_labeL.setText(TotalTradesCost)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = RB_Performance()
    ui.show()
    sys.exit(app.exec_())
