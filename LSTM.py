# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LSTM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 580)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.look_back_count = QtWidgets.QComboBox(Form)
        self.look_back_count.setObjectName("look_back_count")
        self.look_back_count.addItem("")
        self.look_back_count.addItem("")
        self.look_back_count.addItem("")
        self.horizontalLayout_4.addWidget(self.look_back_count)
        self.K_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.K_label.setFont(font)
        self.K_label.setObjectName("K_label")
        self.horizontalLayout_4.addWidget(self.K_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dropout_rate = QtWidgets.QComboBox(Form)
        self.dropout_rate.setObjectName("dropout_rate")
        self.dropout_rate.addItem("")
        self.dropout_rate.addItem("")
        self.dropout_rate.addItem("")
        self.dropout_rate.addItem("")
        self.dropout_rate.addItem("")
        self.dropout_rate.addItem("")
        self.horizontalLayout_3.addWidget(self.dropout_rate)
        self.K_label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.K_label_2.setFont(font)
        self.K_label_2.setObjectName("K_label_2")
        self.horizontalLayout_3.addWidget(self.K_label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.train_data_combobox = QtWidgets.QComboBox(Form)
        self.train_data_combobox.setObjectName("train_data_combobox")
        self.horizontalLayout_2.addWidget(self.train_data_combobox)
        self.traindata_toolButton = QtWidgets.QToolButton(Form)
        self.traindata_toolButton.setObjectName("traindata_toolButton")
        self.horizontalLayout_2.addWidget(self.traindata_toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.test_data_combobox = QtWidgets.QComboBox(Form)
        self.test_data_combobox.setObjectName("test_data_combobox")
        self.horizontalLayout.addWidget(self.test_data_combobox)
        self.testdata_toolButton = QtWidgets.QToolButton(Form)
        self.testdata_toolButton.setObjectName("testdata_toolButton")
        self.horizontalLayout.addWidget(self.testdata_toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.sentout_button = QtWidgets.QPushButton(Form)
        self.sentout_button.setObjectName("sentout_button")
        self.horizontalLayout_12.addWidget(self.sentout_button)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.netprofit_label = QtWidgets.QLabel(Form)
        self.netprofit_label.setObjectName("netprofit_label")
        self.horizontalLayout_5.addWidget(self.netprofit_label, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.winrate_label = QtWidgets.QLabel(Form)
        self.winrate_label.setObjectName("winrate_label")
        self.horizontalLayout_6.addWidget(self.winrate_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.winloserate_label = QtWidgets.QLabel(Form)
        self.winloserate_label.setObjectName("winloserate_label")
        self.horizontalLayout_7.addWidget(self.winloserate_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.profit_factor_label = QtWidgets.QLabel(Form)
        self.profit_factor_label.setObjectName("profit_factor_label")
        self.horizontalLayout_8.addWidget(self.profit_factor_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.mdd_label = QtWidgets.QLabel(Form)
        self.mdd_label.setObjectName("mdd_label")
        self.horizontalLayout_9.addWidget(self.mdd_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.trade_count_label = QtWidgets.QLabel(Form)
        self.trade_count_label.setObjectName("trade_count_label")
        self.horizontalLayout_10.addWidget(self.trade_count_label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.trade_cost_labeL = QtWidgets.QLabel(Form)
        self.trade_cost_labeL.setObjectName("trade_cost_labeL")
        self.horizontalLayout_11.addWidget(self.trade_cost_labeL)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.result_graphicsView = QtWidgets.QGraphicsView(Form)
        self.result_graphicsView.setObjectName("result_graphicsView")
        self.verticalLayout_2.addWidget(self.result_graphicsView)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "長短期記憶模型"))
        self.look_back_count.setItemText(0, _translate("Form", "30"))
        self.look_back_count.setItemText(1, _translate("Form", "60"))
        self.look_back_count.setItemText(2, _translate("Form", "90"))
        self.K_label.setText(_translate("Form", "訓練週期單位"))
        self.dropout_rate.setItemText(0, _translate("Form", "0.1"))
        self.dropout_rate.setItemText(1, _translate("Form", "0.15"))
        self.dropout_rate.setItemText(2, _translate("Form", "0.2"))
        self.dropout_rate.setItemText(3, _translate("Form", "0.3"))
        self.dropout_rate.setItemText(4, _translate("Form", "0.35"))
        self.dropout_rate.setItemText(5, _translate("Form", "0.4"))
        self.K_label_2.setText(_translate("Form", "Droprate"))
        self.label_9.setText(_translate("Form", "選擇訓練資料"))
        self.traindata_toolButton.setText(_translate("Form", "..."))
        self.label_10.setText(_translate("Form", "選擇測試資料"))
        self.testdata_toolButton.setText(_translate("Form", "..."))
        self.sentout_button.setText(_translate("Form", "確認送出"))
        self.label_8.setText(_translate("Form", "勝率"))
        self.label.setText(_translate("Form", "淨利:"))
        self.netprofit_label.setText(_translate("Form", "n/a"))
        self.label_2.setText(_translate("Form", "勝率:"))
        self.winrate_label.setText(_translate("Form", "n/a"))
        self.label_3.setText(_translate("Form", "賺賠比:"))
        self.winloserate_label.setText(_translate("Form", "n/a"))
        self.label_4.setText(_translate("Form", "獲利因子:"))
        self.profit_factor_label.setText(_translate("Form", "n/a"))
        self.label_5.setText(_translate("Form", "最大策略虧損:"))
        self.mdd_label.setText(_translate("Form", "n/a"))
        self.label_6.setText(_translate("Form", "交易次數:"))
        self.trade_count_label.setText(_translate("Form", "n/a"))
        self.label_7.setText(_translate("Form", "交易成本:"))
        self.trade_cost_labeL.setText(_translate("Form", "n/a"))

