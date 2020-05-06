import Read_txt_UI, sys
from PyQt5 import QtWidgets

class ReadTXT(QtWidgets.QTableWidget):
    def __init__(self):
        f = open(r'/Users/tienyou/Desktop/test.txt')
        t = f.readline()
        text = t.split(",")
        text = list(map(str, text))
        text = [float(x) for x in text]
        # text = [round(x) for x in text]#round floats to integers
        # Earning odds
        t1 = (text[4]/text[5])
        EarningOdds = str(t1)#back to str
        #ProfitFactor
        t2 = (text[6]/text[7]-1)
        ProfitFactor = str(t2)
        #TotalTradesCost
        t3 = (1000*text[3])
        TotalTradesCost = str(t3)
        text = [str(x) for x in text]


        super(ReadTXT, self).__init__()
        self.ui = Read_txt_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.origin1.setText(text[0])
        self.ui.origin2.setText(text[1])
        self.ui.origin3.setText(EarningOdds)
        self.ui.origin4.setText(ProfitFactor)
        self.ui.origin5.setText(text[2])
        self.ui.origin6.setText(text[3])
        self.ui.origin7.setText(TotalTradesCost)

        # self.ui.toolButton.clicked.connect(self.slot_btn_chooseDir)
#       Form Title
        self.setWindowTitle('績效報告')

    # def ReadPerformance(self, text=[]):
    #     f = open(r'/Users/tienyou/Desktop/test.txt')
    #     t = f.readline()
    #     text = t.split(",")
    #     self.ui.origin1.setText(text[1])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = ReadTXT()
    ui.show()
    sys.exit(app.exec_())

# text = []
# f = open(r'/Users/tienyou/Desktop/test.txt')
# t = f.readline()
# text = t.split(",")
# print (text)




