# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RangeBreak_Strategies_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1195, 857)
        Form.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 948, 680))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.scrollArea_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.addWidget(self.scrollArea_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.addWidget(self.scrollArea_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_13.addWidget(self.label_14, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_8.addWidget(self.scrollArea_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "前往PowerLanguage Editor"))
        self.label_2.setText(_translate("Form", "區間突破策略"))
        self.label.setText(_translate("Form", "策略基本介紹：\n"
"區間突破基本策略\n"
"\n"
"程式碼如下："))
        self.label_9.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"//RangeBreak\n"
"Buy(\"buy\") next bar closed(1) + Tr stop;\n"
"sellshort(\"sell\") next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\") next bar market;\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\") next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell next bar market;\n"
"buytocover next bar market;\n"
"end;\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "原始策略"))
        self.label_3.setText(_translate("Form", "策略基本介紹：\n"
"區間突破＋凱利公式\n"
"\n"
"程式碼如下："))
        self.label_10.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"//-----Kelly-----(1)\n"
"input:InitialCapital(1000000), MaxSize(10)\n"
";\n"
"var:pTs(1),b(0),p(0),q(0),f(0),pCapitalperContract(200000),ExitAmount(0),MP(0);\n"
"//K%=W-(1-W)/R\n"
"if Grossprofit<>0 and Totaltrades<>0 and grossloss<>0 and   Numlostrades <>0 then\n"
" b = (Grossprofit/ numwintrades)/(grossloss/ Numlostrades);\n"
"if Numwintrades<>0 and Totaltrades<>0 then\n"
"     p = Numwintrades/ Totaltrades;\n"
"     q = 1-p;\n"
"if b<>0 and p<>0 then\n"
"     f = p-(q/b);\n"
"if f<>0 and f*(InitialCapital+netprofit)>0 then\n"
" pTS =IntPortion((f*(InitialCapital+netprofit))/pCapitalperContract);\n"
" if pTS < 1 then pTS = 1 ;\n"
" if pTS > MaxSize then pTS = MaxSize ;\n"
"\n"
"//RangeBreak\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"Buy(\"buy\") pTS shares next bar closed(1) + Tr stop;\n"
"sellshort(\"sell\") pTS shares next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\") pTS shares next bar market;\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\") pTS shares next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell pTS shares next bar market;\n"
"buytocover pTS shares next bar market;\n"
"end;\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "凱利公式"))
        self.label_4.setText(_translate("Form", "策略基本介紹：\n"
"區間突破＋固定比率\n"
"\n"
"程式碼如下："))
        self.label_11.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"Inputs: InitialCapital(10000000), Delta(20000);//Fixed Ratio\n"
"Inputs: InCloudOpenPL(false), Maxsize(10);\n"
"Vars: contractAmt(0), ExitAmount(0), Equity(0), MP(0), pTS(0);\n"
"\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"\n"
"//Fixed Ratio\n"
"if InCloudOpenPL then Equity = Round((InitialCapital + Netprofit + OpenPositionProfit), 0)\n"
"    else Equity = Round((InitialCapital + NetProfit), 0);\n"
"\n"
"//Position Sizing - Fixed Ratio\n"
"if Delta > 0 and Equity/Delta > 0 then\n"
"    contractAmt = 0.5*(1 + SquareRoot(1 + 8*Equity/Delta));\n"
"    contractAmt = MaxList(1, IntPortion(ContractAmt));\n"
"\n"
"if contractAmt < 1 then ContractAmt = 1;\n"
"if contractAmt > MaxSize then ContractAmt = Maxsize;\n"
"pTS = contractAmt;\n"
"\n"
"//RangeBreak\n"
"if Marketposition = 0 then\n"
"    Buy(\"buy\") pTS shares next bar closed(1) + Tr stop;\n"
"if ExitAmount = ContractAmt then\n"
"    sellshort(\"sell\")pTS shares next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\") pTS shares next bar market;\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\") pTS shares next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell pTS shares next bar market;\n"
"buytocover pTS shares next bar market;\n"
"end;\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "固定比率"))
        self.label_5.setText(_translate("Form", "策略基本介紹：\n"
"區間突破＋固定分數\n"
"\n"
"程式碼如下："))
        self.label_12.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"Inputs: earning(5), out(2), pIC(1000000), Delta(9999), IncludeOpenPL(false), Maxsize(10);//Money Management(Fixed Fraction)\n"
"Vars: Equity(0), contractamt(0), pTS(0);\n"
"\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"//Money Management (Fixed Fraction)\n"
"if InCludeOpenPL then\n"
"   Equity = Round((pIC + NetProfit + OpenPositionProfit),0)\n"
"   else Equity = Round((pIC + NetProfit),0);\n"
"If Delta > 0 and Equity/Delta > 0 then\n"
"   contractamt = 0.5 * (1 + squareroot(1 + 8 * Equity/Delta));\n"
"contractamt = MaxList(1, IntPortion(contractamt));\n"
"if contractamt < 1 then contractamt = 1 ;\n"
"if contractamt > MaxSize then contractamt = MaxSize ;\n"
"pTS = contractamt;\n"
"\n"
"//RangeBreak\n"
"Buy(\"buy\") pTS shares next bar closed(1) + Tr stop;\n"
"sellshort(\"sell\")pTS shares next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\")pTS shares next bar market;\n"
"\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\")pTS shares next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell pTS shares next bar market;\n"
"buytocover pTS shares next bar market;\n"
"end;\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "固定分數"))
        self.label_6.setText(_translate("Form", "策略基本介紹：\n"
"區間突破＋最佳F值\n"
"\n"
"程式碼如下："))
        self.label_13.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"\n"
"//-----Optimal F Rule-----(4)\n"
"\n"
"var: pTS(1), OptimalF_Num(10),_OptimalF(0),Equity(0),ExitAmount(0),InCludeOpenPL(false),mp(0), len(0);\n"
"\n"
"if InCludeOpenPL then\n"
" Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else\n"
" Equity = Round((InitialCapital + NetProfit),0);\n"
" _OptimalF=Mf_OptimalF(close,OptimalF_Num,false)/100;\n"
"if _OptimalF<>0 and maxiddrawdown<>0 then\n"
" pTS = (Equity * _OptimalF)/absvalue(maxiddrawdown);\n"
" pTS = MaxList(1, IntPortion(pTS));\n"
"\n"
"\n"
"//RangeBreak\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"Buy(\"buy\") pTS shares next bar closed(1) + Tr stop;\n"
"sellshort(\"sell\") pTS shares next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\") pTS shares next bar market;\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\") pTS shares next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell pTS shares next bar market;\n"
"buytocover pTS shares next bar market;\n"
"end;"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "最佳F值"))
        self.label_7.setText(_translate("Form", "策略基本介紹：\n"
"區間突破＋LarryWilliams\n"
"\n"
"程式碼如下："))
        self.label_14.setText(_translate("Form", "Inputs: LookBack(10), Rang(0.4), When(4);\n"
"Vars: HighValue(0), LowValue(1000000),Tr(0);\n"
"\n"
"//-----LarryWilliams Rule-----\n"
"Input:  InitialCapital(1000000), InCludeOpenPL(false), MaxSize(10);\n"
"var: pCapitalperContract(200000), Equity(0), mp(0), ExitAmount(0), pTS(1);\n"
"\n"
"if InCludeOpenPL then Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else Equity = Round((InitialCapital + NetProfit),0);\n"
"\n"
"if InCludeOpenPL then\n"
" Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else\n"
" Equity = Round((InitialCapital + NetProfit),0);\n"
"if maxiddrawdown <> 0 and entryprice <> 0 then begin\n"
" if netprofit<>0 and maxiddrawdown<>0 then\n"
"     pTS=IntPortion(netprofit/(absvalue(maxiddrawdown)*1.3))+1;\n"
" if pTS > IntPortion(Equity  / entryprice) then\n"
"     pTS = IntPortion(Equity  / entryprice);\n"
"end;\n"
"\n"
"//RangeBreak\n"
"LowValue = Lowest(L, LookBack);\n"
"HighValue = Highest(H, LookBack);\n"
"Tr = (HighValue - LowValue)*Range;\n"
"\n"
"Buy(\"buy\") pTS shares next bar closed(1) + Tr stop;\n"
"sellshort(\"sell\") pTS shares next bar closed(1) - Tr stop;\n"
"\n"
"If Close < LowValue[1] Then\n"
"sell(\"EXIT_buy\") pTS shares next bar market;\n"
"If Close > HighValue[1] Then\n"
"buytocover(\"EXIT_sell\") pTS shares next bar market;\n"
"\n"
"If barssinceentry = When and openpositionprofit < 0 then begin\n"
"sell pTS shares next bar market;\n"
"buytocover pTS shares next bar market;\n"
"end;\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "LarryWilliams"))
