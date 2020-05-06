import Performance_UI, os
from PyQt5 import QtWidgets

class PerformanceUI(QtWidgets.QTableWidget):
    def __init__(self):
        super(PerformanceUI, self).__init__()
        self.ui = Performance_UI.Ui_widget()
        self.ui.setupUi(self)
#       Form Title
        self.setWindowTitle('績效報告')

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                "選取文件夾",
                                                                self.cwd)  # 起始路径
        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.comboBox.addItem(dir_choose)
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)