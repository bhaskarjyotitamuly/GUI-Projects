 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookstore.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

#Creating the database called 'bookstore.db'
# You'll need to have 'sqlite3' installed in your system.If not,go to CMD,& type 'pip install sqlite3'.

conn=sqlite3.connect('bookstore.db')
MyCursor=conn.cursor()
MyCursor.execute('''CREATE TABLE Books (
    Book_ID INTEGER       PRIMARY KEY AUTOINCREMENT,
    Title   TEXT (60)     NOT NULL,
    Author  TEXT (50),
    Sell    [PRICE FLOAT],
    Rent    PRICE,
    Copies  INTEGER
);''')
MyCursor.execute('''INSERT INTO TABLE VALUES(1,'The Kite Runner','Khaled Hosseini',
                350,150,6),(2,'The Mystic Eye','Jaggi Vasudev',250.75,100,8),(3,'Meditations',
                'Marcus Aurelius',750,350,9);''')
conn.commit()
conn.close()



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 553)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 113, 20)) 
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 170, 31, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 31, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 113, 20)) 
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 170, 113, 20)) 
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 70, 41, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 51, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 200, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 270, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 270, 51, 20))
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(110, 100, 82, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 100, 82, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 350, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 350, 141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.radioButton_3=QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(100,300,82,21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.lineEdit_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_3.raise_()
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.pushButton_4.raise_()
        self.lineEdit_6.raise_()
        title=self.lineEdit.text()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.statuschk)
        self.radioButton.toggled.connect(lambda:self.choice('Sell'))
        self.radioButton_2.toggled.connect(lambda:self.choice('Rent'))
        self.pushButton_3.clicked.connect(self.disp_price)
        self.pushButton_2.clicked.connect(self.total_price)
        self.radioButton_3.toggled.connect(self.Sold)
        self.pushButton_4.clicked.connect(self.disp_copies)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Price"))
        self.label_2.setText(_translate("Form", "Title"))
        self.pushButton.setText(_translate("Form", "Status"))
        self.label_3.setText(_translate("Form", "Status"))
        self.label_4.setText(_translate("Form", "Quantity"))
        self.pushButton_2.setText(_translate("Form", "Total Price"))
        self.pushButton_3.setText(_translate("Form", "Price"))
        self.label_5.setText(_translate("Form", "Total Price"))
        self.radioButton.setText(_translate("Form", "Sell"))
        self.radioButton_2.setText(_translate("Form", "Rent"))
        self.pushButton_4.setText(_translate("Form", "Copies Left"))
        self.radioButton_3.setText(_translate("Form","Sold"))
        
    def statuschk(self,Form):
        title=self.lineEdit.text()
        MyObject=sqlite3.connect('bookstore.db')
        myCurs=MyObject.cursor()
         
        myCurs.execute("SELECT * FROM Books_2 WHERE Title== '"+title+"';")
        try:
            record=myCurs.fetchone()
            if record!=None:
                self.lineEdit_2.setText('Available')
            else:
                self.lineEdit_2.setText('Not Available')
            MyObject.commit()
        except:
            print('There was an error.')
            MyObject.rollback()
        MyObject.close()
            
    def choice(self,text):
        title=self.lineEdit.text()
        MyObject=sqlite3.connect('bookstore.db')
        myCurs=MyObject.cursor()
        myCurs.execute("SELECT * FROM Books_2 WHERE Title== '"+title+"';")
        record=myCurs.fetchone()
        if text=='Sell':
            self.price=record[3]
        elif text=='Rent':
            self.price=record[4]
        MyObject.close()

    def disp_price(self):
        self.lineEdit_3.setText('Rs.'+str(self.price))

    def total_price(self):
        quant=int(self.lineEdit_4.text())
        total=quant*self.price
        self.lineEdit_5.setText('Rs.'+str(total))
        print(total)


    def Sold(self):
        title=self.lineEdit.text()
        quant=str(self.lineEdit_4.text())
        MyObject=sqlite3.connect('bookstore.db')
        MyCurs=MyObject.cursor()
        if self.radioButton_3.isChecked()==True:
            MyCurs.execute("UPDATE Books_2 SET Copies=Copies-(?) WHERE Title=='"+title+"';",(quant))
            MyObject.commit()
        MyObject.close()


    def disp_copies(self):
        title=self.lineEdit.text()
        MyObject=sqlite3.connect('bookstore.db')
        MyCurs=MyObject.cursor()
        MyCurs.execute("SELECT * FROM Books_2 WHERE Title== '"+title+"';")
        record=MyCurs.fetchone()
        copies=record[5]
        MyObject.commit()
        self.lineEdit_6.setText(str(copies))
        MyObject.close()
            
            
if __name__ == "__main__" :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

