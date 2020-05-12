# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Turtle30k_Strategies_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1195, 889)
        Form.setStyleSheet("background-color: rgb(53, 69, 89);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setStyleSheet("background-color: rgb(53, 69, 89);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "前往PowerLanguage Editor"))
        self.label_2.setText(_translate("Form", "海龜30k策略"))
        self.label_9.setText(_translate("Form", "Input:len(20);\n"
"var: pts(1),MP(0),ExitAmount(0);\n"
"MP=marketposition*currentcontracts;\n"
"\n"
"if Close cross over Highest(high,len)[1] then buy(\"buy\")pts contract the next bar at market;\n"
"if Close cross over Lowest(low,len)[1] then sellshort(\"sell\")pts contract the next bar at market;\n"
"ExitAmount=pts;\n"
"\n"
"\n"
"if MP=1 then buy pts contract next bar at entryprice*\n"
"(1+0.01)stop;\n"
"\n"
"if MP=-1 then sellshort pts contract next bar at entryprice*\n"
"(1-0.01)stop;\n"
"\n"
"\n"
"\n"
"if MP>=1 then sell pts contract next bar at entryprice*\n"
"(1- 0.02)stop;\n"
"\n"
"if MP<=1 then buytocover pts contract next bar at entryprice*\n"
"(1+0.02)stop;\n"
""))
        self.label.setText(_translate("Form", "策略基本介紹：\n"
"海龜30k基本策略\n"
"\n"
"程式碼如下："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "原始策略"))
        self.label_3.setText(_translate("Form", "策略基本介紹：\n"
"海龜30k＋凱利公式\n"
"\n"
"程式碼如下："))
        self.label_10.setText(_translate("Form", "//-----Kelly-----(1)\n"
"input:InitialCapital(1000000), MaxSize(10),len(20);\n"
"var:pTs(1),b(0),p(0),q(0),f(0),pCapitalperContract(200000),ExitAmount(0),MP(0);\n"
"\n"
"\n"
"//K%=W-(1-W)/R\n"
"if Grossprofit<>0 and Totaltrades<>0 and grossloss<>0 and   Numlostrades <>0 then\n"
"    b = (Grossprofit/ numwintrades)/(grossloss/ Numlostrades);\n"
"if Numwintrades<>0 and Totaltrades<>0 then\n"
"        p = Numwintrades/ Totaltrades;\n"
"        q = 1-p;\n"
"if b<>0 and p<>0 then\n"
"        f = p-(q/b);\n"
"if f<>0 and f*(InitialCapital+netprofit)>0 then\n"
"    pTS =IntPortion((f*(InitialCapital+netprofit))/pCapitalperContract);\n"
"    if pTS < 1 then pTS = 1 ;\n"
"    if pTS > MaxSize then pTS = MaxSize ;\n"
"\n"
"\n"
"\n"
"//------turtle30(len)\n"
"\n"
"MP=marketposition*currentcontracts;\n"
"\n"
"if Close cross over Highest(high,len)[1] then buy(\"buy\")pTS contract the next bar at market;\n"
"if Close cross over Lowest(low,len)[1] then sellshort(\"sell\")pTS contract the next bar at market;\n"
"ExitAmount=pts;\n"
"\n"
"\n"
"if MP=1 then buy pTS contract next bar at entryprice*\n"
"(1+0.01)stop;\n"
"\n"
"if MP=-1 then sellshort pTS contract next bar at entryprice*\n"
"(1-0.01)stop;\n"
"\n"
"\n"
"\n"
"if MP>=1 then sell pTS contract next bar at entryprice*\n"
"(1- 0.02)stop;\n"
"\n"
"if MP<=1 then buytocover pTS contract next bar at entryprice*\n"
"(1+0.02)stop;\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "凱利公式"))
        self.label_11.setText(_translate("Form", "//-----Fixed_Ratio-----(2)\n"
"Inputs: InitialCapital(1000000), Delta(20000),len(20);\n"
"Inputs: InCludeOpenPL(false), MaxSize(10);\n"
"Var: ContractAmt(0),ExitAmount(0),Equity(0),MP(0),pts(0);\n"
"\n"
"if InCludeOpenPL then Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"     else Equity = Round((InitialCapital + NetProfit),0);\n"
"\n"
"{Position Sizing - Fixed Ratio }\n"
"If Delta > 0 and Equity/Delta > 0 then\n"
"    ContractAmt = 0.5 * (1 + squareroot(1 + 8 * Equity/Delta));\n"
"    ContractAmt = MaxList(1, IntPortion(ContractAmt));  //IntPortion->int\n"
"\n"
"if ContractAmt < 1 then ContractAmt = 1 ;\n"
"if ContractAmt > MaxSize then ContractAmt = MaxSize ;\n"
"pts = ContractAmt;\n"
"\n"
"\n"
"//------turtle(len)\n"
"\n"
"\n"
"MP=marketposition*currentcontracts;\n"
"\n"
"if Close cross over Highest(high,len)[1] then buy(\"buy\")pts contract the next bar at market;\n"
"if Close cross over Lowest(low,len)[1] then sellshort(\"sell\")pts contract the next bar at market;\n"
"ExitAmount=pts;\n"
"\n"
"\n"
"if MP=1 then buy pts contract next bar at entryprice*\n"
"(1+0.01)stop;\n"
"\n"
"if MP=-1 then sellshort pts contract next bar at entryprice*\n"
"(1-0.01)stop;\n"
"\n"
"\n"
"\n"
"if MP>=1 then sell pts contract next bar at entryprice*\n"
"(1- 0.02)stop;\n"
"\n"
"if MP<=1 then buytocover pts contract next bar at entryprice*\n"
"(1+0.02)stop;\n"
""))
        self.label_4.setText(_translate("Form", "策略基本介紹：\n"
"海龜30k＋固定比率\n"
"\n"
"程式碼如下："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "固定比率"))
        self.label_13.setText(_translate("Form", "//-----Optimal F Rule-----(4)\n"
"\n"
"Input:len(20);\n"
"var: pTS(1), OptimalF_Num(10),_OptimalF(0),Equity(0),ExitAmount(0),InCludeOpenPL(false),mp(0);\n"
"\n"
"if InCludeOpenPL then\n"
"    Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else\n"
"    Equity = Round((InitialCapital + NetProfit),0);\n"
"    _OptimalF=Mf_OptimalF(close,OptimalF_Num,false)/100;\n"
"if _OptimalF<>0 and maxiddrawdown<>0 then\n"
"    pTS = (Equity * _OptimalF)/absvalue(maxiddrawdown);\n"
"    pTS = MaxList(1, IntPortion(pTS));\n"
"\n"
"\n"
"//------turtle(len)\n"
"\n"
"\n"
"mp=marketposition*currentcontracts;\n"
"\n"
"if Close cross over Highest(high,len)[1] then buy(\"buy\")pTS contract the next bar at market;\n"
"if Close cross over Lowest(low,len)[1] then sellshort(\"sell\")pTS contract the next bar at market;\n"
"ExitAmount=pts;\n"
"\n"
"\n"
"if mp=1 then buy pTS contract next bar at entryprice*\n"
"(1+0.01)stop;\n"
"\n"
"if mp=-1 then sellshort pTS contract next bar at entryprice*\n"
"(1-0.01)stop;\n"
"\n"
"\n"
"\n"
"if mp>=1 then sell pTS contract next bar at entryprice*\n"
"(1- 0.02)stop;\n"
"\n"
"if mp<=1 then buytocover pTS contract next bar at entryprice*\n"
"(1+0.02)stop;\n"
""))
        self.label_6.setText(_translate("Form", "策略基本介紹：\n"
"海龜30k＋最佳F值\n"
"\n"
"程式碼如下："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "最佳F值"))
        self.label_7.setText(_translate("Form", "策略基本介紹：\n"
"海龜30k＋LarryWilliams\n"
"\n"
"程式碼如下："))
        self.label_14.setText(_translate("Form", "//-----LarryWilliams-----(3)\n"
"Input:  InitialCapital(1000000), InCludeOpenPL(false),MaxSize(10),len(20);\n"
"var: pCapitalperContract(200000),Equity(0),mp(0),ExitAmount(0),pts(1);\n"
"\n"
"if InCludeOpenPL then Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else Equity = Round((InitialCapital + NetProfit),0);\n"
"//-----LarryWilliams Rule-----\n"
"if InCludeOpenPL then\n"
"    Equity = Round((InitialCapital + NetProfit + OpenPositionProfit),0)\n"
"else\n"
"    Equity = Round((InitialCapital + NetProfit),0);\n"
"if maxiddrawdown <> 0 and entryprice <> 0 then begin\n"
"    if netprofit<>0 and maxiddrawdown<>0 then\n"
"              pts=IntPortion(netprofit/(absvalue(maxiddrawdown)*1.3))+1;\n"
"    if pts > IntPortion(Equity  / entryprice) then\n"
"        pts = IntPortion(Equity  / entryprice);\n"
"end;\n"
"\n"
"\n"
"\n"
"//------turtle30(len)\n"
"\n"
"mp=marketposition*currentcontracts;\n"
"\n"
"if Close cross over Highest(high,len)[1] then buy(\"buy\")pts contract the next bar at market;\n"
"if Close cross over Lowest(low,len)[1] then sellshort(\"sell\")pts contract the next bar at market;\n"
"ExitAmount=pts;\n"
"\n"
"\n"
"if mp=1 then buy pts contract next bar at entryprice*\n"
"(1+0.01)stop;\n"
"\n"
"if mp=-1 then sellshort pts contract next bar at entryprice*\n"
"(1-0.01)stop;\n"
"\n"
"\n"
"\n"
"if mp>=1 then sell pts contract next bar at entryprice*\n"
"(1- 0.02)stop;\n"
"\n"
"if mp<=1 then buytocover pts contract next bar at entryprice*\n"
"(1+0.02)stop;\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "LarryWilliams"))
