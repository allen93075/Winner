import os
import sys

from PyQt5 import QtWidgets
from RF import Ui_Form
from rf_example_new import *

class RF(QtWidgets.QWidget):
    def __init__(self):
        super(RF,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("隨機森林")
        self.ui.toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.startTrainBtn.clicked.connect(self.exec_rf)        
            
    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "選取文件夾",
                                                           self.cwd,
                                                           "excel(*.csv)")  # 起始路徑
        
        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.comboBox.addItem(dir_choose[0])
        print(self.ui.comboBox.currentText())
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)

    def exec_rf(self):
        a, b = rf_main(loadFile(self.ui.comboBox.currentText()))      
        self.ui.trainAcc.setText(str(round(a.item(), 3)))
        self.ui.testAcc.setText(str(round(b.item(), 3)))
        #print(type(a))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = RF()
    # ui.__init__()
    ui.show()
    sys.exit(app.exec_())