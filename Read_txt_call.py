import Read_txt_UI, sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from Performance.Rename_txt import renamefile

class ReadTXT(QtWidgets.QTableWidget):
    def __init__(self):

        super(ReadTXT, self).__init__()
        self.ui = Read_txt_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.toolButton_2.clicked.connect(self.slot_btn_chooseDir2)
        self.ui.toolButton_3.clicked.connect(self.slot_btn_chooseDir3)
        self.ui.toolButton_4.clicked.connect(self.slot_btn_chooseDir4)
        self.ui.toolButton_5.clicked.connect(self.slot_btn_chooseDir5)
        self.ui.toolButton_6.clicked.connect(self.slot_btn_chooseDir6)
        # rename text file to chinese
        renamefile()

#       Form Title
        self.setWindowTitle('績效報告')

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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st1_1.setText(text[0])
            self.ui.st1_2.setText(text[1])
            self.ui.st1_3.setText(EarningOdds)
            self.ui.st1_4.setText(ProfitFactor)
            self.ui.st1_5.setText(text[2])
            self.ui.st1_6.setText(text[3])
            self.ui.st1_7.setText(TotalTradesCost)
            self.ui.strategy_1.setText(Filename2[0])

    def slot_btn_chooseDir2(self):
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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st2_1.setText(text[0])
            self.ui.st2_2.setText(text[1])
            self.ui.st2_3.setText(EarningOdds)
            self.ui.st2_4.setText(ProfitFactor)
            self.ui.st2_5.setText(text[2])
            self.ui.st2_6.setText(text[3])
            self.ui.st2_7.setText(TotalTradesCost)
            self.ui.strategy_2.setText(Filename2[0])

    def slot_btn_chooseDir3(self):
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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st3_1.setText(text[0])
            self.ui.st3_2.setText(text[1])
            self.ui.st3_3.setText(EarningOdds)
            self.ui.st3_4.setText(ProfitFactor)
            self.ui.st3_5.setText(text[2])
            self.ui.st3_6.setText(text[3])
            self.ui.st3_7.setText(TotalTradesCost)
            self.ui.strategy_3.setText(Filename2[0])

    def slot_btn_chooseDir4(self):
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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st4_1.setText(text[0])
            self.ui.st4_2.setText(text[1])
            self.ui.st4_3.setText(EarningOdds)
            self.ui.st4_4.setText(ProfitFactor)
            self.ui.st4_5.setText(text[2])
            self.ui.st4_6.setText(text[3])
            self.ui.st4_7.setText(TotalTradesCost)
            self.ui.strategy_4.setText(Filename2[0])

    def slot_btn_chooseDir5(self):
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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st5_1.setText(text[0])
            self.ui.st5_2.setText(text[1])
            self.ui.st5_3.setText(EarningOdds)
            self.ui.st5_4.setText(ProfitFactor)
            self.ui.st5_5.setText(text[2])
            self.ui.st5_6.setText(text[3])
            self.ui.st5_7.setText(TotalTradesCost)
            self.ui.strategy_5.setText(Filename2[0])

    def slot_btn_chooseDir6(self):
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

            # print file name
            Filename = str(file)
            Filetext = Filename.split("/")
            Filetext1 = Filetext
            Filename1 = Filetext1[-1]
            Filename2 = Filename1.split(".txt")

            # read into performance and calculate
            f = open(file, "r")
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

            self.ui.st6_1.setText(text[0])
            self.ui.st6_2.setText(text[1])
            self.ui.st6_3.setText(EarningOdds)
            self.ui.st6_4.setText(ProfitFactor)
            self.ui.st6_5.setText(text[2])
            self.ui.st6_6.setText(text[3])
            self.ui.st6_7.setText(TotalTradesCost)
            self.ui.strategy_6.setText(Filename2[0])


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




