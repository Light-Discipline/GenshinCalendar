import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import os
from utils import folderexist

#create folder
if(folderexist('D:\\GenshinCalendar')==0):
    os.makedirs('D:\\GenshinCalendar')

import GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())