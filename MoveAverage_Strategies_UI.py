# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MoveAverage_Strategies_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1195, 729)
        Form.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 958, 513))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 958, 515))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab_3.setFont(font)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 958, 515))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.scrollArea_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab_4.setFont(font)
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 958, 515))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.addWidget(self.scrollArea_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab_5.setFont(font)
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 958, 515))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.addWidget(self.scrollArea_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tab_6.setFont(font)
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 958, 515))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.gridLayout_13.addWidget(self.label_14, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_8.addWidget(self.scrollArea_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "前往PowerLanguage Editor"))
        self.label_2.setText(_translate("Form", "移動均線策略"))
        self.label.setText(_translate("Form", "名稱：\n"
"移動均線基本策略\n"
"\n"
"解釋如下："))
        self.label_9.setText(_translate("Form", "移動均線策略是以5日均線以及20日均線的交叉作為買賣交易點，\n"
"當5日均線由下向上穿越20日均線（黃金交叉），則在下一根K棒買進，\n"
"當5日均線由上向下穿越20日均線（死亡交叉），則在下一根K棒作空。\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "原始策略"))
        self.label_3.setText(_translate("Form", "名稱：\n"
"移動均線＋凱利公式\n"
"\n"
"解釋如下："))
        self.label_10.setText(_translate("Form", "凱利公式是一種資金管理的方法，\n"
"最初為貝爾實驗室物理學家John Larry Kelly於1956年在《貝爾系統技術期刊》中發表，\n"
"用以計算每次賭局中，決定下一次賭注所投入的資金比例，重在長期累積的獲利，只在乎最終輸贏的結果不在乎順序，\n"
"用最佳化的下注比例，以最大化長期的收益累計。\n"
"\n"
"f=下注比例（f = p - q/b）, b=賠率, p=獲利機率, q=虧損機率\n"
"並且設定pTS(交易口數)=f\n"
"\n"
"並且將凱利公式加上移動均線策略：\n"
"當5日均線由下向上穿越20日均線（黃金交叉），則在下一根K棒買進pTS，\n"
"當5日均線由上向下穿越20日均線（死亡交叉），則在下一根K棒作空pTS。\n"
"備註：凱利公式並未計算到MDD(最大策略虧損)，因此一般使用上大多都是只用於比較資金管理後的差異，不會實際放在是市場上使用。\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "凱利公式"))
        self.label_4.setText(_translate("Form", "名稱：\n"
"移動均線＋固定比率\n"
"\n"
"解釋如下："))
        self.label_11.setText(_translate("Form", "固定比率（Fixed Ratio）的資金管理模式，是由Ryan Jones在1999寫的「The Trading Game」書中所提出的。\n"
"基本上的計算方式是這樣的：\n"
"\n"
"假設我們的初始資金有NTD $100萬，delta 設為 NTD $20000。假設我們現在用$100萬交易一口合約。\n"
"\n"
"交易第二口合約所需資金 = 交易第一口合約所需資金 + delta($2萬元) * 1\n"
"\n"
"交易第三口合約所需資金 = 交易第二口合約所需資金 + delta($2萬元) * 2\n"
"\n"
"依此類推……\n"
"\n"
"並設定\n"
"Equity = Round((InitialCapital + Netprofit + OpenPositionProfit), 0)\n"
"contractamount = 0.5*(1 + SquareRoot(1 + 8*Equity/Delta));\n"
"if contractamount < 1 then ContractAmt = 1;\n"
"if contractamount > MaxSize then ContractAmt = Maxsize;\n"
"而pTS（交易口數）＝ contractamount\n"
"最後將此套入移動暈線策略中使用：\n"
"當5日均線由下向上穿越20日均線（黃金交叉），則在下一根K棒買進pTS，\n"
"當5日均線由上向下穿越20日均線（死亡交叉），則在下一根K棒作空pTS。\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "固定比率"))
        self.label_5.setText(_translate("Form", "名稱：\n"
"移動均線＋固定分數\n"
"\n"
"解釋如下："))
        self.label_12.setText(_translate("Form", "固定分數（Fixed Fraction）和固定比率都是常用的資金管理模式，\n"
"而固定分數的基本邏輯是，限制住每一交易所冒的風險佔我們整體資金的比例。\n"
"假設今天我們有NTD $100萬的資金，而每次交易的損失不超過手中資金的2%，而這2%就數我們的交易風險比例。\n"
"\n"
"我們將此資金管理方法加入移動均線策略中使用：\n"
"當5日均線由下向上穿越20日均線（黃金交叉），則在下一根K棒買進pTS，\n"
"當5日均線由上向下穿越20日均線（死亡交叉），則在下一根K棒作空pTS。\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "固定分數"))
        self.label_13.setText(_translate("Form", "最佳F值法是由Ralph Vince在1992年\n"
"《The Mathematics of Money Management: Risk Analysis Techniques for Traders》一\n"
"書中認為凱利公式只適用於理論上輸贏機率各半的傳統賭局，不適合變化多端的實際賭局因此提出。\n"
"最佳F值法（Optimal f），巧妙的運用Kelly的概念，\n"
"由於實際賭局中輸贏機率為動態的，故透過下注後去計算每次的持有收益率，\n"
"進而避開傳統賭局的固定機率與賠率的限制，\n"
"期望在資金配置的同時可以在投資與損失之中達到平衡。\n"
"\n"
"我們將此資金管理方法加入移動均線策略中使用：\n"
"當5日均線由下向上穿越20日均線（黃金交叉），則在下一根K棒買進pTS，\n"
"當5日均線由上向下穿越20日均線（死亡交叉），則在下一根K棒作空pTS。\n"
""))
        self.label_6.setText(_translate("Form", "名稱：\n"
"移動均線＋最佳F值\n"
"\n"
"解釋如下："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "最佳F值"))
        self.label_14.setText(_translate("Form", "Larry Williams資金方法，\n"
"係指第一口合約所需資金 = 初始保證金＋歷史回測中的MDD(最大策略虧損)*150%\n"
"每賺到一個MDD*150%的資金，就加碼一口\n"
"\n"
"並且將此資金管理方法加入移動均線策略中使用。\n"
""))
        self.label_7.setText(_translate("Form", "名稱：\n"
"移動均線＋LarryWilliams\n"
"\n"
"解釋如下："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "LarryWilliams"))
        self.pushButton_2.setText(_translate("Form", "前往Multicharts主程式"))
