# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adaboostt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(964, 698)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(513, 10, 441, 676))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.profitCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.profitCol.setFont(font)
        self.profitCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profitCol.setObjectName("profitCol")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.profitCol)
        self.profitOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.profitOut.setFont(font)
        self.profitOut.setAlignment(QtCore.Qt.AlignCenter)
        self.profitOut.setObjectName("profitOut")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.profitOut)
        self.winrateCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.winrateCol.setFont(font)
        self.winrateCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.winrateCol.setObjectName("winrateCol")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.winrateCol)
        self.winRateOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.winRateOut.setFont(font)
        self.winRateOut.setAlignment(QtCore.Qt.AlignCenter)
        self.winRateOut.setObjectName("winRateOut")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.winRateOut)
        self.winLossCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.winLossCol.setFont(font)
        self.winLossCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.winLossCol.setObjectName("winLossCol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.winLossCol)
        self.winLossOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.winLossOut.setFont(font)
        self.winLossOut.setAlignment(QtCore.Qt.AlignCenter)
        self.winLossOut.setObjectName("winLossOut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.winLossOut)
        self.profitFactorCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.profitFactorCol.setFont(font)
        self.profitFactorCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profitFactorCol.setObjectName("profitFactorCol")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.profitFactorCol)
        self.profitFactorOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.profitFactorOut.setFont(font)
        self.profitFactorOut.setAlignment(QtCore.Qt.AlignCenter)
        self.profitFactorOut.setObjectName("profitFactorOut")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.profitFactorOut)
        self.mddCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.mddCol.setFont(font)
        self.mddCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mddCol.setObjectName("mddCol")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.mddCol)
        self.mddOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.mddOut.setFont(font)
        self.mddOut.setAlignment(QtCore.Qt.AlignCenter)
        self.mddOut.setObjectName("mddOut")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mddOut)
        self.sharpeCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.sharpeCol.setFont(font)
        self.sharpeCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sharpeCol.setObjectName("sharpeCol")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sharpeCol)
        self.sharpeOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.sharpeOut.setFont(font)
        self.sharpeOut.setAlignment(QtCore.Qt.AlignCenter)
        self.sharpeOut.setObjectName("sharpeOut")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sharpeOut)
        self.costCol = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.costCol.setFont(font)
        self.costCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.costCol.setObjectName("costCol")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.costCol)
        self.costOut = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.costOut.setFont(font)
        self.costOut.setAlignment(QtCore.Qt.AlignCenter)
        self.costOut.setObjectName("costOut")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.costOut)
        self.verticalLayout_4.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(24, 10, 441, 676))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headingLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.headingLabel_2.setFont(font)
        self.headingLabel_2.setObjectName("headingLabel_2")
        self.verticalLayout_3.addWidget(self.headingLabel_2)
        spacerItem1 = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.dataPath_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.dataPath_2.setFont(font)
        self.dataPath_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dataPath_2.setObjectName("dataPath_2")
        self.horizontalLayout_3.addWidget(self.dataPath_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.train_data_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.train_data_combobox.setObjectName("train_data_combobox")
        self.horizontalLayout_2.addWidget(self.train_data_combobox)
        self.traindata_toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.traindata_toolButton.setObjectName("traindata_toolButton")
        self.horizontalLayout_2.addWidget(self.traindata_toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        spacerItem3 = QtWidgets.QSpacerItem(17, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.startTrainBtn_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.startTrainBtn_2.setObjectName("startTrainBtn_2")
        self.verticalLayout_3.addWidget(self.startTrainBtn_2)
        spacerItem4 = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        spacerItem5 = QtWidgets.QSpacerItem(515, 485, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(470, 20, 20, 661))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "績效"))
        self.profitCol.setText(_translate("Form", "淨利:"))
        self.profitOut.setText(_translate("Form", "─"))
        self.winrateCol.setText(_translate("Form", "勝率:"))
        self.winRateOut.setText(_translate("Form", "─"))
        self.winLossCol.setText(_translate("Form", "賺賠比:"))
        self.winLossOut.setText(_translate("Form", "─"))
        self.profitFactorCol.setText(_translate("Form", "獲利因子:"))
        self.profitFactorOut.setText(_translate("Form", "─"))
        self.mddCol.setText(_translate("Form", "最大策略虧損:"))
        self.mddOut.setText(_translate("Form", "─"))
        self.sharpeCol.setText(_translate("Form", "夏普比率:"))
        self.sharpeOut.setText(_translate("Form", "─"))
        self.costCol.setText(_translate("Form", "交易成本:"))
        self.costOut.setText(_translate("Form", "─"))
        self.headingLabel_2.setText(_translate("Form", "ADABOOST"))
        self.label_15.setText(_translate("Form", "檔案:"))
        self.dataPath_2.setText(_translate("Form", "--"))
        self.traindata_toolButton.setText(_translate("Form", "..."))
        self.startTrainBtn_2.setText(_translate("Form", "開始訓練"))
