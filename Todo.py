# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Todo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect('mylist.db')
c = conn.cursor()
c.execute(""" CREATE TABLE if not exists todo_list(list_item text) """)

conn.commit()
conn.close()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(20, 50, 131, 32))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(160, 50, 111, 32))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(280, 50, 111, 32))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(20, 10, 511, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.list_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.list_listWidget.setGeometry(QtCore.QRect(20, 90, 511, 341))
        self.list_listWidget.setObjectName("list_listWidget")
        self.savedb_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save_it())
        self.savedb_pushButton.setGeometry(QtCore.QRect(399, 50, 131, 32))
        self.savedb_pushButton.setObjectName("savedb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 24))
        self.menubar.setObjectName("menubar")
        self.menuTo_Do_List = QtWidgets.QMenu(self.menubar)
        self.menuTo_Do_List.setObjectName("menuTo_Do_List")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTo_Do_List.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.grab_all()
        
    def grab_all(self):
        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        
    
        conn.commit()
        conn.close()
        for record in records:
            self.list_listWidget.addItem(str(record[0]))

        
    def add_it(self):
        item = self.additem_lineEdit.text()
        self.list_listWidget.addItem(item)
        self.additem_lineEdit.setText("")    
        
    def delete_it(self):
        clicked = self.list_listWidget.currentRow()
        self.list_listWidget.takeItem(clicked)    
    
    def clear_it(self):
        self.list_listWidget.clear() 
        
    def save_it(self):
        conn = sqlite3.connect('mylist.db')
        c = conn.cursor()
        
        c.execute('DELETE FROM todo_list;',)
        
        
        
        
        items = []
        for index in range(self.list_listWidget.count()):
            items.append(self.list_listWidget.item(index))
            
        for item in items:
            print(item.text())
            c.execute("INSERT INTO todo_list VALUES (:items)",
                      
                      {
                         'items' : item.text(),  
                          
                      })
        
        conn.commit()
        conn.close()
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item To List"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear List"))
        self.savedb_pushButton.setText(_translate("MainWindow", "Save To Database"))
        self.menuTo_Do_List.setTitle(_translate("MainWindow", "To Do List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

