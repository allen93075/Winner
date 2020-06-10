import os
import sys
from PyQt5 import QtWidgets, QtGui
from LSTM import Ui_Form
from LSTM2 import *
from autoscript import callMC2,callQM


class LSTM(QtWidgets.QWidget):
    def __init__(self):
        super(LSTM, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.testdata_toolButton.clicked.connect(self.slot_btn_chooseDir_2)
        # self.ui.sentout_button.clicked.connect(self.performance)
        self.ui.sentout_button.clicked.connect(self.exec_lstm)
        self.resize(800, 600)

    def slot_btn_chooseDir_2(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取檔案",
                                                           self.cwd,"excel(*.csv)")  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
        self.ui.test_data_combobox.addItem(dir_choose[0])
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)
        return dir_choose

    def exec_lstm(self):
        model = keras.models.load_model('LSTM_model')
        print(self.ui.test_data_combobox.currentText())
        predict(model,60,test_data(self.ui.test_data_combobox.currentText()))
        callQM()
        callMC2()

    # def performance(self):
        f = open(r'test.txt')
        t = f.readline()
        text = t.split(",")
        text = list(map(str, text))
        text = [float(x) for x in text]
        # Earning odds
        t1 = (text[4] / text[5])
        EarningOdds = str(round(t1,3))  # back to str
        # ProfitFactor
        t2 = (text[6] / text[7]*-1)
        ProfitFactor = str(round(t2,3))
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
        self.ui.trade_cost_label.setText(TotalTradesCost)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LSTM()
    ui.show()
    sys.exit(app.exec_())
