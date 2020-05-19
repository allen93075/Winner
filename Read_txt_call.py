import Read_txt_UI, sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog

class ReadTXT(QtWidgets.QTableWidget):
    def __init__(self):
        # #Turtle30k
        # f = open(r'Performance/turtle.txt')
        # t = f.readline()
        # text = t.split(",")
        # text = list(map(str, text))
        # text = [float(x) for x in text]
        # # text = [round(x) for x in text]#round floats to integers
        # # Earning odds
        # t1 = (text[4]/text[5])
        # EarningOdds = str(t1)#back to str
        # #ProfitFactor
        # t2 = (text[6]/text[7]-1)
        # ProfitFactor = str(t2)
        # #TotalTradesCost
        # t3 = (1000*text[3])
        # TotalTradesCost = str(t3)
        # text = [str(x) for x in text]

        #Turtle30k+Kelly
        f1 = open(r'Performance/turtle_kelly.txt')
        tk = f1.readline()
        text_tk = tk.split(",")
        text_tk = list(map(str, text_tk))
        text_tk = [float(x) for x in text_tk]
        # Earning odds
        tk1 = (text_tk[4] / text_tk[5])
        EarningOdds_tk = str(tk1)  # back to str
        # ProfitFactor
        tk2 = (text_tk[6] / text_tk[7] - 1)
        ProfitFactor_tk = str(tk2)
        # TotalTradesCost
        tk3 = (1000 * text_tk[3])
        TotalTradesCost_tk = str(tk3)
        text_tk = [str(x) for x in text_tk]

        #Turtle30k+FixedRatio
        f2 = open(r'Performance/turtle_FR.txt')
        t_fr = f2.readline()
        text_fr = t_fr.split(",")
        text_fr = list(map(str, text_fr))
        text_fr = [float(x) for x in text_fr]
        # Earning odds
        t_fr1 = (text_fr[4] / text_fr[5])
        EarningOdds_fr = str(t_fr1)  # back to str
        # ProfitFactor
        t_fr2 = (text_fr[6] / text_fr[7] - 1)
        ProfitFactor_fr = str(t_fr2)
        # TotalTradesCost
        t_fr3 = (1000 * text_fr[3])
        TotalTradesCost_fr = str(t_fr3)
        text_fr = [str(x) for x in text_fr]

        # Turtle30k+OptimalF
        f3 = open(r'Performance/turtle_optimalF.txt')
        t_OF = f3.readline()
        text_OF = t_OF.split(",")
        text_OF = list(map(str, text_fr))
        text_OF = [float(x) for x in text_OF]
        # Earning odds
        t_OF1 = (text_OF[4] / text_OF[5])
        EarningOdds_OF = str(t_OF1)  # back to str
        # ProfitFactor
        t_OF2 = (text_OF[6] / text_OF[7] - 1)
        ProfitFactor_OF = str(t_OF2)
        # TotalTradesCost
        t_OF3 = (1000 * text_OF[3])
        TotalTradesCost_OF = str(t_OF3)
        text_OF = [str(x) for x in text_OF]

        # Turtle30k+LarryWilliams
        f4 = open(r'Performance/turtle_william.txt')
        t_lw = f4.readline()
        text_lw = t_lw.split(",")
        text_lw = list(map(str, text_lw))
        text_lw = [float(x) for x in text_lw]
        # Earning odds
        t_lw1 = (text_lw[4] / text_lw[5])
        EarningOdds_lw = str(t_lw1)  # back to str
        # ProfitFactor
        t_lw2 = (text_lw[6] / text_lw[7] - 1)
        ProfitFactor_lw = str(t_lw2)
        # TotalTradesCost
        t_lw3 = (1000 * text_lw[3])
        TotalTradesCost_lw = str(t_lw3)
        text_lw = [str(x) for x in text_lw]

        # Turtle30k+FixedFractional
        f5 = open(r'Performance/turtle_FF.txt')
        t_ff = f5.readline()
        text_ff = t_ff.split(",")
        text_ff = list(map(str, text_ff))
        text_ff = [float(x) for x in text_ff]
        # Earning odds
        t_ff1 = (text_ff[4] / text_ff[5])
        EarningOdds_ff = str(t_ff1)  # back to str
        # ProfitFactor
        t_ff2 = (text_ff[6] / text_ff[7] - 1)
        ProfitFactor_ff = str(t_ff2)
        # TotalTradesCost
        t_ff3 = (1000 * text_ff[3])
        TotalTradesCost_ff = str(t_ff3)
        text_ff = [str(x) for x in text_ff]

        super(ReadTXT, self).__init__()
        self.ui = Read_txt_UI.Ui_Form()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.toolButton_2.clicked.connect(self.slot_btn_chooseDir2)
        self.ui.toolButton_3.clicked.connect(self.slot_btn_chooseDir3)
        self.ui.toolButton_4.clicked.connect(self.slot_btn_chooseDir4)
        self.ui.toolButton_5.clicked.connect(self.slot_btn_chooseDir5)
        self.ui.toolButton_6.clicked.connect(self.slot_btn_chooseDir6)

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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.origin1.setText(text[0])
            self.ui.origin2.setText(text[1])
            self.ui.origin3.setText(EarningOdds)
            self.ui.origin4.setText(ProfitFactor)
            self.ui.origin5.setText(text[2])
            self.ui.origin6.setText(text[3])
            self.ui.origin7.setText(TotalTradesCost)
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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.kelly1.setText(text[0])
            self.ui.kelly2.setText(text[1])
            self.ui.kelly3.setText(EarningOdds)
            self.ui.kelly4.setText(ProfitFactor)
            self.ui.kelly5.setText(text[2])
            self.ui.kelly6.setText(text[3])
            self.ui.kelly7.setText(TotalTradesCost)

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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.fixratio1.setText(text[0])
            self.ui.fixratio2.setText(text[1])
            self.ui.fixratio3.setText(EarningOdds)
            self.ui.fixratio4.setText(ProfitFactor)
            self.ui.fixratio5.setText(text[2])
            self.ui.fixratio6.setText(text[3])
            self.ui.fixratio7.setText(TotalTradesCost)

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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.optimal1.setText(text[0])
            self.ui.optimal2.setText(text[1])
            self.ui.optimal3.setText(EarningOdds)
            self.ui.optimal4.setText(ProfitFactor)
            self.ui.optimal5.setText(text[2])
            self.ui.optimal6.setText(text[3])
            self.ui.optimal7.setText(TotalTradesCost)

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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.william1.setText(text[0])
            self.ui.william2.setText(text[1])
            self.ui.william3.setText(EarningOdds)
            self.ui.william4.setText(ProfitFactor)
            self.ui.william5.setText(text[2])
            self.ui.william6.setText(text[3])
            self.ui.william7.setText(TotalTradesCost)

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
            EarningOdds = str(t1)  # back to str
            # ProfitFactor
            t2 = (text[6] / text[7] - 1)
            ProfitFactor = str(t2)
            # TotalTradesCost
            t3 = (1000 * text[3])
            TotalTradesCost = str(t3)
            text = [str(x) for x in text]

            self.ui.fixfraction1.setText(text[0])
            self.ui.fixfraction2.setText(text[1])
            self.ui.fixfraction3.setText(EarningOdds)
            self.ui.fixfraction4.setText(ProfitFactor)
            self.ui.fixfraction5.setText(text[2])
            self.ui.fixfraction6.setText(text[3])
            self.ui.fixfraction7.setText(TotalTradesCost)


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




