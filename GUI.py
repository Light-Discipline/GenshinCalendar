# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils import getnamelist,downloadpic,search_items,filenamelist,folderexist,readcsv,writecsv,weekday,showdeveloplist
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt,QStringListModel
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 1059)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(96, 50))
        self.label_4.setObjectName("label_4")
        
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.piclabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.piclabel_4.setMinimumSize(QtCore.QSize(180, 140))
        self.piclabel_4.setText("")
        self.piclabel_4.setObjectName("piclabel_4")
        self.piclabel_4.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.piclabel_4, 0, 3, 1, 1)
        
        self.textlabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel_3.setMinimumSize(QtCore.QSize(180, 50))
        self.textlabel_3.setObjectName("textlabel_3")
        self.textlabel_3.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.textlabel_3, 1, 2, 1, 1)
        
        self.textlabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel_4.setMinimumSize(QtCore.QSize(180, 50))
        self.textlabel_4.setObjectName("textlabel_4")
        self.textlabel_4.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.textlabel_4, 1, 3, 1, 1)
        
        self.piclabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.piclabel_5.setMinimumSize(QtCore.QSize(180, 140))
        self.piclabel_5.setText("")
        self.piclabel_5.setObjectName("piclabel_5")
        self.piclabel_5.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.piclabel_5, 0, 4, 1, 1)
        
        self.textlabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel_1.setMinimumSize(QtCore.QSize(180, 50))
        self.textlabel_1.setObjectName("textlabel_1")
        self.textlabel_1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.textlabel_1, 1, 0, 1, 1)
        
        self.textlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel_2.setMinimumSize(QtCore.QSize(180, 100))
        self.textlabel_2.setObjectName("textlabel_2")
        self.textlabel_2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.textlabel_2, 1, 1, 1, 1)
        
        self.textlabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel_5.setMinimumSize(QtCore.QSize(180, 50))
        self.textlabel_5.setObjectName("textlabel_5")
        self.textlabel_5.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.textlabel_5, 1, 4, 1, 1)
        
        self.piclabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.piclabel_1.setMinimumSize(QtCore.QSize(180, 140))
        self.piclabel_1.setText("")
        self.piclabel_1.setObjectName("piclabel_1")
        self.piclabel_1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.piclabel_1, 0, 0, 1, 1)
        
        self.piclabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.piclabel_3.setMinimumSize(QtCore.QSize(180, 140))
        self.piclabel_3.setText("")
        self.piclabel_3.setObjectName("piclabel_3")
        self.piclabel_3.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.piclabel_3, 0, 2, 1, 1)
        
        self.piclabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.piclabel_2.setMinimumSize(QtCore.QSize(180, 140))
        self.piclabel_2.setText("")
        self.piclabel_2.setObjectName("piclabel_2")
        self.piclabel_2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.piclabel_2, 0, 1, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        
        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(595, 542))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setFirstDayOfWeek(Qt.Sunday)
        self.getdatetype()
        self.gridLayout_6.addWidget(self.calendarWidget, 0, 1, 1, 2)
        
        self.developlist=readcsv('D:\\GenshinCalendar\\data.csv')
        self.develop_name_list=[]
        self.develop_material_list=[]
        self.develop_day_list=[]
        self.develop_show=[]
        for listrow in self.developlist:
            a=listrow.replace("\n","")
            s=a.split(",")
            self.develop_name_list.append(s[0])
            self.develop_material_list.append(s[1])
            self.develop_day_list.append(s[2])
        for l in range(0,len(self.developlist)):
            self.developlist[l]=[self.develop_name_list[l],self.develop_material_list[l],self.develop_day_list[l]]
        print(self.developlist)
        
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setEditTriggers(QtWidgets.QListView.NoEditTriggers)
        self.listView.setMinimumSize(QtCore.QSize(281, 381))
        self.listView.setObjectName("listView")
        self.showtodaylist()
        self.gridLayout_4.addWidget(self.listView, 1, 0, 2, 1)
        
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setMinimumSize(QtCore.QSize(180, 50))
        self.remove_button.setObjectName("remove_button")
        self.gridLayout_4.addWidget(self.remove_button, 2, 1, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(20, 238, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(180, 50))
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        
        spacerItem1 = QtWidgets.QSpacerItem(580, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 2, 2, 1, 1)
        
        spacerItem2 = QtWidgets.QSpacerItem(580, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 1, 2, 1, 1)
        
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(108, 50))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(108, 50))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        
        self.starchoose = QtWidgets.QComboBox(self.centralwidget)
        self.starchoose.setMinimumSize(QtCore.QSize(100, 50))
        self.starchoose.setMaximumSize(QtCore.QSize(128, 50))
        self.starchoose.setObjectName("starchoose")
        self.starchoose.addItem("")
        self.starchoose.addItem("")
        self.gridLayout_3.addWidget(self.starchoose, 1, 0, 1, 1)
        
        self.list1=getnamelist()
        self.namelist = QtWidgets.QComboBox(self.centralwidget)
        self.namelist.setMinimumSize(QtCore.QSize(200, 50))
        self.namelist.setMaximumSize(QtCore.QSize(200, 50))
        self.namelist.setObjectName("namelist")
        self.namelist.addItems(self.list1[0])
        self.gridLayout_3.addWidget(self.namelist, 1, 1, 1, 1)
        
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 2, 1)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setMinimumSize(QtCore.QSize(180, 50))
        self.add_button.setMaximumSize(QtCore.QSize(180, 50))
        self.add_button.setObjectName("add_button")
        self.gridLayout_5.addWidget(self.add_button, 1, 2, 1, 1)
        
        self.searchitems_button = QtWidgets.QPushButton(self.centralwidget)
        self.searchitems_button.setMinimumSize(QtCore.QSize(180, 50))
        self.searchitems_button.setMaximumSize(QtCore.QSize(180, 50))
        self.searchitems_button.setObjectName("searchitems_button")
        self.gridLayout_5.addWidget(self.searchitems_button, 1, 1, 1, 1)
        
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 2, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.starchoose.currentIndexChanged.connect(self.namelistchange)
        self.searchitems_button.clicked.connect(self.search)
        self.add_button.clicked.connect(self.add)
        self.calendarWidget.clicked[QtCore.QDate].connect(self.switchdate)
        self.remove_button.clicked.connect(self.remove)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GenshinCalendar"))
        self.label_4.setText(_translate("MainWindow", "培养材料"))
        self.textlabel_3.setText(_translate("MainWindow", ""))
        self.textlabel_4.setText(_translate("MainWindow", ""))
        self.textlabel_1.setText(_translate("MainWindow", ""))
        self.textlabel_2.setText(_translate("MainWindow", ""))
        self.textlabel_5.setText(_translate("MainWindow", ""))
        self.remove_button.setText(_translate("MainWindow", "移出培养列表"))
        self.label_3.setText(_translate("MainWindow", "当天需要培养"))
        self.label_2.setText(_translate("MainWindow", "角色"))
        self.label.setText(_translate("MainWindow", "星级"))
        self.starchoose.setItemText(0, _translate("MainWindow", "五星"))
        self.starchoose.setItemText(1, _translate("MainWindow", "四星"))
        self.add_button.setText(_translate("MainWindow", "加入培养列表"))
        self.searchitems_button.setText(_translate("MainWindow", "查询"))
    
    def namelistchange(self):
        self.namelist.clear()
        if(self.starchoose.currentIndex()==0):
            self.namelist.addItems(self.list1[0])
        else:
            self.namelist.addItems(self.list1[1])
            
    def showpictures(self,name):
        list1=filenamelist('D:\\GenshinCalendar\\pictures\\'+name)
        itemname=list1[1]
        filename=list1[0]
        self.textlabel_1.setText(itemname[0])
        before=itemname[1]
        after=before.split(";")
        self.textlabel_2.setText(after[0]+'\n'+after[1])
        self.textlabel_3.setText(itemname[2])
        self.textlabel_4.setText(itemname[3])
        self.textlabel_5.setText(itemname[4])
        self.piclabel_1.setPixmap(QPixmap('D:\\GenshinCalendar\\pictures\\'+name+'./'+filename[0]))
        self.piclabel_2.setPixmap(QPixmap('D:\\GenshinCalendar\\pictures\\'+name+'./'+filename[1]))
        self.piclabel_3.setPixmap(QPixmap('D:\\GenshinCalendar\\pictures\\'+name+'./'+filename[2]))
        self.piclabel_4.setPixmap(QPixmap('D:\\GenshinCalendar\\pictures\\'+name+'./'+filename[3]))
        self.piclabel_5.setPixmap(QPixmap('D:\\GenshinCalendar\\pictures\\'+name+'./'+filename[4]))
        
    def search(self):
        material_list=search_items(self.namelist.currentText())
        downloadpic(material_list)
        name=material_list[3]
        self.showpictures(name)
        
    def add(self):
        name=self.namelist.currentText()
        if(folderexist('D:\\GenshinCalendar\\pictures\\'+name)==0):
            self.search()
        else:
            self.showpictures(name)
        if name in self.develop_name_list:
            print("already in the list")
        else:
            item_name=filenamelist('D:\\GenshinCalendar\\pictures\\'+name)[1]
            material=item_name[1].split(";")
            self.develop_name_list.append(name)
            self.develop_material_list.append(material[0])
            self.develop_day_list.append(material[1])
            self.developlist.append([name,material[0],material[1]])
            writecsv('D:\\GenshinCalendar\\data.csv',self.developlist)
            self.showtodaylist()
    
    def getdatetype(self):
        today=self.calendarWidget.selectedDate()
        weekday_today=(weekday(today))
        if(weekday_today==1 or weekday_today==4):
            self.weekdaytype=1
        elif(weekday_today==2 or weekday_today==5):
            self.weekdaytype=2
        elif(weekday_today==3 or weekday_today==6):
            self.weekdaytype=3
        else:
            self.weekdaytype=4
            
    def showtodaylist(self):
        self.develop_show=showdeveloplist(self.developlist,self.weekdaytype)
        slm=QStringListModel()
        slm.setStringList(self.develop_show)
        self.listView.setModel(slm)
            
    def switchdate(self):
        self.getdatetype()
        self.showtodaylist()
        
    def remove(self):
        try:
            name=str(self.listView.selectedIndexes()[0].data())
            name=name.split("----")[0]
            for i in range(0,len(self.developlist)):
                if(self.developlist[i][0]==name):
                    break
            self.developlist.pop(i)
            self.develop_name_list.pop(i)
            self.develop_material_list.pop(i)
            self.develop_day_list.pop(i)
            writecsv('D:\\GenshinCalendar\\data.csv',self.developlist)
            self.showtodaylist()
        except:
            print("You haven't selected anything")