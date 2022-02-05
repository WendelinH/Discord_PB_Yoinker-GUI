# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

import pickle
import requests # pip install requests

from detailsDialog import Ui_detailsDialog
from newDialog import Ui_newDialog
from model import discordPerson


class Ui_MainWindow(object):
    
    def schliesenButtonPressed(self, MainWindow):
        MainWindow.close()
    
    def deleteButtonPressed(self):
        index = self.tblWidget_personen.currentRow()
        try:
            self.tblDataList.pop(index)
        except:
            print("Diese Row ist schohn gelöscht.")
        self.load_table()
        self.tablePressed()
    
    def newButtonPressed(self):
        self.newDialog = QtWidgets.QDialog()
        self.ui = Ui_newDialog()
        self.ui.setupUi(self.newDialog)
        self.newDialog.exec_() # Das ist das Zeichnen synchron und es warted.
        #self.newDialog.show() # Das ist das Zeichnen aber asynchron.
        if self.ui.save:
            self.tblDataList.append(self.ui.discordUser)
            self.load_table()
            self.tablePressed()
    
    def tablePressed(self):
        try:
            index = self.tblWidget_personen.currentRow()
            self.pbImage.loadFromData(requests.get(self.tblDataList[index].pbLink).content)
            self.pbPixmap = QtGui.QPixmap(self.pbImage)
            self.pbPixmap = self.pbPixmap.scaled(270, 270)
            self.label_2.setPixmap(self.pbPixmap)
        except:
            print("Items sind nicht vorhanden.")
            self.pbImage.loadFromData(requests.get(self.defaultImgLink).content)
            self.pbPixmap = QtGui.QPixmap(self.pbImage)
            self.pbPixmap = self.pbPixmap.scaled(270, 270)
            self.label_2.setPixmap(self.pbPixmap)
    
    def load_table(self):
        if len(self.tblDataList) > 5:
            self.tblWidget_personen.setRowCount(len(self.tblDataList))
            for n in range(5, len(self.tblDataList)):
                item = QtWidgets.QTableWidgetItem(f"{n+1}")
                self.tblWidget_personen.setVerticalHeaderItem(n, item)
        
        for n in range(self.tblWidget_personen.rowCount()):
            # Löschen und reseten.
            item = QtWidgets.QTableWidgetItem(" ")
            self.tblWidget_personen.setItem(n, 0, item)
            item = QtWidgets.QTableWidgetItem(" ")
            self.tblWidget_personen.setItem(n, 1, item)
        
        for n in range(len(self.tblDataList)):
            # Neue Werte eintragen.
            item = QtWidgets.QTableWidgetItem(self.tblDataList[n].username)
            self.tblWidget_personen.setItem(n, 0, item)
            item = QtWidgets.QTableWidgetItem(self.tblDataList[n].pbLink)
            self.tblWidget_personen.setItem(n, 1, item)
    
    def test_data(self):
        self.tblDataList.append(discordPerson.discordPerson("Test 1", 'https://i.pinimg.com/originals/65/86/5f/65865f32c8cc1e85a8e4168c8705300a.jpg', '248451798546172095'))
        self.tblDataList.append(discordPerson.discordPerson("Test 2", 'https://i.pinimg.com/originals/7b/45/cb/7b45cbd62c5a67adb3daf1ef5cbf0e2f.jpg', '495872267310571533'))
        self.load_table()
    
    def save_data(self):
        file = open('tblDataList.dat','wb')  #opened the file in write and binary mode 
        pickle.dump(self.tblDataList, file) #dumping the content in the list 'self.tblDataList' into the file
        file.close() #closing the file
    
    def load_data(self):
        try:
            file = open('tblDataList.dat','rb') #opening the file to read the data in the binary form
            self.tblDataList = pickle.load(file)
            file.close() #closing the file
        except:
            print("Die Datei ist leer oder nicht vorhanden.")
    
    def detailsButtonPressed(self):
        self.detailsDialog = QtWidgets.QDialog()
        self.ui = Ui_detailsDialog()
        self.ui.setupUi(self.detailsDialog)
        try:
            index = self.tblWidget_personen.currentRow()
            self.ui.setData(self.tblDataList[index])
        except:
            print("Items sind nicht vorhanden.")
        self.detailsDialog.exec_() # Das ist das Zeichnen synchron und es warted.
        #self.detailsDialog.show() # Das ist das Zeichnen aber asynchron.
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 392)
        
        # Liste mit allen DiscordUser Objekten darin.
        self.tblDataList = []
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tblWidget_personen = QtWidgets.QTableWidget(self.centralwidget)
        self.tblWidget_personen.setGeometry(QtCore.QRect(10, 40, 271, 217))
        self.tblWidget_personen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tblWidget_personen.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblWidget_personen.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblWidget_personen.setRowCount(5)
        self.tblWidget_personen.setColumnCount(2)
        self.tblWidget_personen.setObjectName("tblWidget_personen")
        
        
        self.tblWidget_personen.clicked.connect(self.tablePressed)
        self.tblWidget_personen.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tblWidget_personen.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        for n in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.tblWidget_personen.setVerticalHeaderItem(n, item)
        
        for n in range(2):
            item = QtWidgets.QTableWidgetItem()
            self.tblWidget_personen.setHorizontalHeaderItem(n, item)
        #self.test_data()
        self.load_data()
        self.load_table()
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Bild Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 1, 271, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # pbImage
        self.defaultImgLink = 'https://tse1.mm.bing.net/th?id=OIP.DAaJOe5dJ9oqeCeiYcNAKQHaFf&pid=Api'
        self.pbImage = QtGui.QImage()
        self.pbImage.loadFromData(requests.get(self.defaultImgLink).content)
        self.pbPixmap = QtGui.QPixmap(self.pbImage)
        self.pbPixmap = self.pbPixmap.scaled(270, 270)
        self.label_2.setPixmap(self.pbPixmap)
        
        # Button Details 
        self.btn_details = QtWidgets.QPushButton(self.centralwidget)
        self.btn_details.setGeometry(QtCore.QRect(490, 300, 93, 28))
        self.btn_details.setObjectName("btn_details")
        self.btn_details.clicked.connect(self.detailsButtonPressed)
        
        # Button Save 
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(390, 300, 93, 28))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(self.save_data)
        
        # Button Delete 
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(290, 300, 93, 28))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.deleteButtonPressed)
        
        # Button New 
        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(190, 300, 93, 28))
        self.btn_new.setObjectName("btn_new")
        self.btn_new.clicked.connect(self.newButtonPressed)
        
        
        # Menu
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Menu action Test-Data
        self.actionTestData = QtWidgets.QAction(MainWindow)
        self.actionTestData.setObjectName("actionTestData")
        self.actionTestData.triggered.connect(self.test_data)
        # Menu action speichen
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionSpeichern.triggered.connect(self.save_data)
        # Menu action schliesen
        self.actionSchliesen = QtWidgets.QAction(MainWindow)
        self.actionSchliesen.setObjectName("actionSchliesen")
        self.actionSchliesen.triggered.connect(lambda: self.schliesenButtonPressed(MainWindow))
        # Menu
        self.menuDatei.addAction(self.actionTestData)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionSchliesen)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tblWidget_personen.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tblWidget_personen.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tblWidget_personen.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tblWidget_personen.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tblWidget_personen.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tblWidget_personen.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tblWidget_personen.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PB-Link"))
        __sortingEnabled = self.tblWidget_personen.isSortingEnabled()
        self.tblWidget_personen.setSortingEnabled(False)
        self.tblWidget_personen.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Table Widget (Item-Based)"))
        self.btn_details.setText(_translate("MainWindow", "Details"))
        self.btn_save.setText(_translate("MainWindow", "Speichern"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_new.setText(_translate("MainWindow", "New"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionTestData.setText(_translate("MainWindow", "Create Test-Data"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))
        self.actionSchliesen.setText(_translate("MainWindow", "Schliesen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
