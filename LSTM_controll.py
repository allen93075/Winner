# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LSTM_controll.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 533)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lookback_comboBox = QtWidgets.QComboBox(Form)
        self.lookback_comboBox.setObjectName("lookback_comboBox")
        self.lookback_comboBox.addItem("")
        self.lookback_comboBox.addItem("")
        self.lookback_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.lookback_comboBox)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.droprate_comboBox = QtWidgets.QComboBox(Form)
        self.droprate_comboBox.setObjectName("droprate_comboBox")
        self.droprate_comboBox.addItem("")
        self.droprate_comboBox.addItem("")
        self.droprate_comboBox.addItem("")
        self.droprate_comboBox.addItem("")
        self.droprate_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.droprate_comboBox)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.train_comboBox = QtWidgets.QComboBox(Form)
        self.train_comboBox.setObjectName("train_comboBox")
        self.horizontalLayout_3.addWidget(self.train_comboBox)
        self.train_toolButton = QtWidgets.QToolButton(Form)
        self.train_toolButton.setObjectName("train_toolButton")
        self.horizontalLayout_3.addWidget(self.train_toolButton)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.test_comboBox = QtWidgets.QComboBox(Form)
        self.test_comboBox.setObjectName("test_comboBox")
        self.horizontalLayout_2.addWidget(self.test_comboBox)
        self.test_toolButton = QtWidgets.QToolButton(Form)
        self.test_toolButton.setObjectName("test_toolButton")
        self.horizontalLayout_2.addWidget(self.test_toolButton)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.accurency_label = QtWidgets.QLabel(Form)
        self.accurency_label.setObjectName("accurency_label")
        self.horizontalLayout.addWidget(self.accurency_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sentout_pushButton = QtWidgets.QPushButton(Form)
        self.sentout_pushButton.setObjectName("sentout_pushButton")
        self.verticalLayout.addWidget(self.sentout_pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LSTM 管理區域"))
        self.lookback_comboBox.setItemText(0, _translate("Form", "30"))
        self.lookback_comboBox.setItemText(1, _translate("Form", "60"))
        self.lookback_comboBox.setItemText(2, _translate("Form", "90"))
        self.label_2.setText(_translate("Form", "週期"))
        self.droprate_comboBox.setItemText(0, _translate("Form", "0.1"))
        self.droprate_comboBox.setItemText(1, _translate("Form", "0.15"))
        self.droprate_comboBox.setItemText(2, _translate("Form", "0.2"))
        self.droprate_comboBox.setItemText(3, _translate("Form", "0.25"))
        self.droprate_comboBox.setItemText(4, _translate("Form", "0.3"))
        self.label_3.setText(_translate("Form", "Droprate"))
        self.train_toolButton.setText(_translate("Form", "..."))
        self.label_4.setText(_translate("Form", "選擇訓練資料"))
        self.test_toolButton.setText(_translate("Form", "..."))
        self.label_5.setText(_translate("Form", "選擇測試資料"))
        self.label_6.setText(_translate("Form", "準確率:"))
        self.accurency_label.setText(_translate("Form", "n/a"))
        self.sentout_pushButton.setText(_translate("Form", "確定送出"))