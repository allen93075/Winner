import os
import sys

from  PyQt5 import QtWidgets
import MLP_UI 
from mlp import *

class MLPUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(MLPUI, self).__init__()
        self.ui = MLP_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('多層感知器')
        self.ui.choseDataBtn.clicked.connect(self.slot_btn_chooseDir)
        self.ui.startTrainBtn.clicked.connect(self.exec_mlp)
        self.ui.startTrainBtn.clicked.connect(self.performance)
        
    def exec_mlp(self):
        print("_______",self.ui.comboBox.currentText())
        mlp_main(loadFile(self.ui.comboBox.currentText()))

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取文件夾",
                                                           self.cwd,
                                                           "excel(*.csv)")  # 起始路徑

        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.comboBox.addItem(dir_choose[0])
        print(self.ui.comboBox.currentText())
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)

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

        self.ui.profitOut.setText(text[0])
        self.ui.winRateOut.setText(text[1])
        self.ui.winLossOut.setText(EarningOdds)
        self.ui.profitFactorOut.setText(ProfitFactor)
        self.ui.mddOut.setText(text[2])
        self.ui.tradeCuntOut.setText(text[3])
        self.ui.costOut.setText(TotalTradesCost)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MLPUI()
    ui.__init__()
    ui.show()
    sys.exit(app.exec_())

