# Form implementation generated from reading ui file 'mentor_meeting_page2.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 799)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 850))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-90, -80, 1381, 1000))
        self.frame.setStyleSheet("background-color:rgb(255, 230, 169)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.labelbaslikmentormeeting = QtWidgets.QLabel(parent=self.frame)
        self.labelbaslikmentormeeting.setGeometry(QtCore.QRect(510, 80, 331, 61))
        self.labelbaslikmentormeeting.setStyleSheet("font-size: 26px; /* Başlık boyutu */\n"
"    font-weight: bold; /* Kalın yazı tipi */\n"
"    font-family: \'Comic Sans MS\'; /* Özgün yazı tipi (örnek) */\n"
"    color: #2c3e50;")
        self.labelbaslikmentormeeting.setObjectName("labelbaslikmentormeeting")
        self.pushButtonsearch = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonsearch.setGeometry(QtCore.QRect(500, 180, 131, 51))
        self.pushButtonsearch.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: Arial;\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background-color: #dcdcdc; /* Açık gri arka plan rengi */\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"    /* Gölgelendirme eklemek için: */\n"
"    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); /* Gölgenin boyutu ve rengi */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; /* Hover durumunda biraz daha koyu gri */\n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* Hover sırasında daha belirgin gölge */\n"
"}")
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.pushButton_2exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2exit.setGeometry(QtCore.QRect(500, 270, 131, 51))
        self.pushButton_2exit.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: Arial;\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background-color: #dcdcdc; /* Açık gri arka plan rengi */\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"    /* Gölgelendirme eklemek için: */\n"
"    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); /* Gölgenin boyutu ve rengi */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; /* Hover durumunda biraz daha koyu gri */\n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* Hover sırasında daha belirgin gölge */\n"
"}")
        self.pushButton_2exit.setObjectName("pushButton_2exit")
        self.pushButton_3allmeetings = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3allmeetings.setGeometry(QtCore.QRect(160, 180, 251, 51))
        self.pushButton_3allmeetings.setStyleSheet("   QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: Arial;\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background-color: #dcdcdc; /* Açık gri arka plan rengi */\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"    /* Gölgelendirme eklemek için: */\n"
"    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); /* Gölgenin boyutu ve rengi */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; /* Hover durumunda biraz daha koyu gri */\n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* Hover sırasında daha belirgin gölge */\n"
"}")
        self.pushButton_3allmeetings.setObjectName("pushButton_3allmeetings")
        self.pushButton_4returnmenu = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4returnmenu.setGeometry(QtCore.QRect(160, 270, 251, 51))
        self.pushButton_4returnmenu.setStyleSheet(" QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    font-family: Arial;\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background-color: #dcdcdc; /* Açık gri arka plan rengi */\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"    /* Gölgelendirme eklemek için: */\n"
"    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); /* Gölgenin boyutu ve rengi */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; /* Hover durumunda biraz daha koyu gri */\n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* Hover sırasında daha belirgin gölge */\n"
"}")
        self.pushButton_4returnmenu.setObjectName("pushButton_4returnmenu")
        self.lineEditaramabosluk = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEditaramabosluk.setGeometry(QtCore.QRect(700, 180, 441, 51))
        self.lineEditaramabosluk.setStyleSheet("QLineEdit {\n"
"    font-size: 18px;\n"
"    font-family: Arial;\n"
"    color: #333;\n"
"    background-color: #fff;\n"
"    border: 4px solid #2c3e50;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);\n"
"}\n"
"QLineEdit:placeholder {\n"
"    color: rgba(150, 150, 150, 0.8);\n"
"    font-style: italic;\n"
"}\n"
"")
        self.lineEditaramabosluk.setText("")
        self.lineEditaramabosluk.setReadOnly(False)
        self.lineEditaramabosluk.setClearButtonEnabled(False)
        self.lineEditaramabosluk.setObjectName("lineEditaramabosluk")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(700, 280, 451, 31))
        self.comboBox.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: Arial;\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background-color: #dcdcdc; /* Açık gri arka plan rengi */\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: none;\n"
"    \n"
"    /* Gölgelendirme eklemek için: */\n"
"    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3); /* Gölgenin boyutu ve rengi */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; /* Hover durumunda biraz daha koyu gri */\n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* Hover sırasında daha belirgin gölge */\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(290, 360, 731, 321))
        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(54)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelbaslikmentormeeting.setText(_translate("MainWindow", "MENTOR MEETING PAGE"))
        self.pushButtonsearch.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_2exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_3allmeetings.setText(_translate("MainWindow", "ALL MEETINGS"))
        self.pushButton_4returnmenu.setText(_translate("MainWindow", "RETURN TO PREFERENCE MENU"))
        self.lineEditaramabosluk.setPlaceholderText(_translate("MainWindow", "Enter the text you want to search for here"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Participation in the entire VIT project is appropriate"))
        self.comboBox.setItemText(1, _translate("MainWindow", "It would be appropriate to direct the VIT project to the first IT training area"))
        self.comboBox.setItemText(2, _translate("MainWindow", "It would be appropriate to direct the VIT project to the English training area"))
        self.comboBox.setItemText(3, _translate("MainWindow", "It can be directly directed within the scope of the VIT project"))
        self.comboBox.setItemText(4, _translate("MainWindow", "It would be appropriate to direct it to individual coaching directly"))
        self.comboBox.setItemText(5, _translate("MainWindow", "It would be more appropriate to participate in the next VIT project."))
        self.comboBox.setItemText(6, _translate("MainWindow", "It would be appropriate to redirect to another sector."))
        self.comboBox.setItemText(7, _translate("MainWindow", "Other"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Meeting Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mentor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IT Knowledge"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Current Intensit"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Feedback"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
