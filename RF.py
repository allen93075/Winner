# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RF.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1090, 889)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headingLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")
        self.verticalLayout.addWidget(self.headingLabel)
        spacerItem = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.dataPath = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.dataPath.setFont(font)
        self.dataPath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dataPath.setObjectName("dataPath")
        self.horizontalLayout_2.addWidget(self.dataPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.choseDataBtn = QtWidgets.QToolButton(Form)
        self.choseDataBtn.setObjectName("choseDataBtn")
        self.horizontalLayout.addWidget(self.choseDataBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem2 = QtWidgets.QSpacerItem(17, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.startTrainBtn = QtWidgets.QPushButton(Form)
        self.startTrainBtn.setObjectName("startTrainBtn")
        self.verticalLayout.addWidget(self.startTrainBtn)
        spacerItem3 = QtWidgets.QSpacerItem(17, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        spacerItem4 = QtWidgets.QSpacerItem(515, 485, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.profitCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.profitCol.setFont(font)
        self.profitCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profitCol.setObjectName("profitCol")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.profitCol)
        self.profitOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.profitOut.setFont(font)
        self.profitOut.setAlignment(QtCore.Qt.AlignCenter)
        self.profitOut.setObjectName("profitOut")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.profitOut)
        self.winrateCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.winrateCol.setFont(font)
        self.winrateCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.winrateCol.setObjectName("winrateCol")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.winrateCol)
        self.winRateOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.winRateOut.setFont(font)
        self.winRateOut.setAlignment(QtCore.Qt.AlignCenter)
        self.winRateOut.setObjectName("winRateOut")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.winRateOut)
        self.winLossCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.winLossCol.setFont(font)
        self.winLossCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.winLossCol.setObjectName("winLossCol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.winLossCol)
        self.winLossOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.winLossOut.setFont(font)
        self.winLossOut.setAlignment(QtCore.Qt.AlignCenter)
        self.winLossOut.setObjectName("winLossOut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.winLossOut)
        self.profitFactorCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.profitFactorCol.setFont(font)
        self.profitFactorCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profitFactorCol.setObjectName("profitFactorCol")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.profitFactorCol)
        self.profitFactorOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.profitFactorOut.setFont(font)
        self.profitFactorOut.setAlignment(QtCore.Qt.AlignCenter)
        self.profitFactorOut.setObjectName("profitFactorOut")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.profitFactorOut)
        self.mddCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.mddCol.setFont(font)
        self.mddCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mddCol.setObjectName("mddCol")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.mddCol)
        self.mddOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.mddOut.setFont(font)
        self.mddOut.setAlignment(QtCore.Qt.AlignCenter)
        self.mddOut.setObjectName("mddOut")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mddOut)
        self.sharpeCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.sharpeCol.setFont(font)
        self.sharpeCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sharpeCol.setObjectName("sharpeCol")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sharpeCol)
        self.sharpeOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.sharpeOut.setFont(font)
        self.sharpeOut.setAlignment(QtCore.Qt.AlignCenter)
        self.sharpeOut.setObjectName("sharpeOut")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sharpeOut)
        self.costCol = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.costCol.setFont(font)
        self.costCol.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.costCol.setObjectName("costCol")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.costCol)
        self.costOut = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.costOut.setFont(font)
        self.costOut.setAlignment(QtCore.Qt.AlignCenter)
        self.costOut.setObjectName("costOut")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.costOut)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.headingLabel.setText(_translate("Form", "隨機森林"))
        self.label_14.setText(_translate("Form", "選擇商品資料:"))
        self.dataPath.setText(_translate("Form", "--"))
        self.choseDataBtn.setText(_translate("Form", "..."))
        self.startTrainBtn.setText(_translate("Form", "開始訓練"))
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

