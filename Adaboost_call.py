import os
import sys

import Adaboost_UI
from  PyQt5 import QtWidgets, QtGui
from ada_model import *
from autoscript import callQM,callMC3


class AdaboostUI(QtWidgets.QWidget):
    def __init__(self):
        super(AdaboostUI, self).__init__()
        self.ui = Adaboost_UI.Ui_Form()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('自適應增強')
        self.ui.choseDataBtn.clicked.connect(self.slot_btn_chooseDir)
        self.ui.startTrainBtn.clicked.connect(self.exec_ada)
        # self.ui.startTrainBtn.clicked.connect(self.performance)
        self.resize(800, 600)


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

    def exec_ada(self):
        print("_______", self.ui.comboBox.currentText())
        ada_main(loadFile(self.ui.comboBox.currentText()))
    # def performance(self):
        callQM()
        callMC3()
        f = open(r'Performance/adaresult.txt')
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

        self.ui.profitOut.setText(text[0])
        self.ui.winRateOut.setText(text[1])
        self.ui.winLossOut.setText(EarningOdds)
        self.ui.profitFactorOut.setText(ProfitFactor)
        self.ui.mddOut.setText(text[2])
        self.ui.tradeCuntOut.setText(text[3])
        self.ui.costOut.setText(TotalTradesCost)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = AdaboostUI()
    ui.show()
    sys.exit(app.exec_())

