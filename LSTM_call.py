import os
import sys

from PyQt5 import QtWidgets,QtGui
from LSTM import Ui_Form


class LSTM(QtWidgets.QWidget):
    def __int__(self):
        super(LSTM, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.sentout_button.clicked.connect(self.get_look_back_count)
        # self.ui.sentout_button.clicked.connect(self.set_pic)
        self.ui.traindata_toolButton.clicked.connect(self.slot_btn_chooseDir)
        self.ui.testdata_toolButton.clicked.connect(self.slot_btn_chooseDir_2)

    def get_look_back_count(self):
        return self.ui.look_back_count.currentText()  # string型態傳回

    def get_droprate(self):
        return self.ui.dropout_rate.currentText()

    # def set_pic(self):
    #     self.pic = QtWidgets.QGraphicsScene
    #     self.pic.addPixmap(QtGui.QPixmap("Users\Allen\PycharmProjects\Winner\mpl_finace_TXF.png"))
    #     self.ui.result_graphicsView.setScene(self.pic)

    def slot_btn_chooseDir(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                "選取文件夾",
                                                                self.cwd)  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.train_data_combobox.addItem(dir_choose)
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)

    def slot_btn_chooseDir_2(self):
        self.cwd = os.getcwd()
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                "選取文件夾",
                                                                self.cwd)  # 起始路径

        if dir_choose == "":
            print("\n取消選擇")
            return
        self.ui.test_data_combobox.addItem(dir_choose)
        print(type(dir_choose))
        print("\n你選擇的文件夾為:")
        print(dir_choose)


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ui = LSTM()
#     ui.__int__()
#     ui.show()
#     sys.exit(app.exec_())
