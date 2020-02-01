# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 600)
        MainWindow.setStyleSheet(".QPushButton{\n"
"    cursor:pointer;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    max-height: 80px;\n"
"    background-color: black;\n"
"}\n"
"/*\n"
"#pushbutton{\n"
"    background-color: green;\n"
"    color:white;\n"
"}\n"
"\n"
"#pushButton_4{\n"
"    background-color: yellow;\n"
"    color:black;\n"
"}*/")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectBtn.setGeometry(QtCore.QRect(20, 380, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectBtn.sizePolicy().hasHeightForWidth())
        self.selectBtn.setSizePolicy(sizePolicy)
        self.selectBtn.setAutoFillBackground(False)
        self.selectBtn.setStyleSheet("QPushButton{\n"
"cursor:pointer;\n"
"    color:white;\n"
"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    max-height: 80px;\n"
"}\n"
"")
        self.selectBtn.setObjectName("selectBtn")
        self.statBtn = QtWidgets.QPushButton(self.centralwidget)
        self.statBtn.setGeometry(QtCore.QRect(20, 480, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statBtn.sizePolicy().hasHeightForWidth())
        self.statBtn.setSizePolicy(sizePolicy)
        self.statBtn.setAutoFillBackground(False)
        self.statBtn.setStyleSheet(".QPushButton{\n"
"    color:black;\n"
"    background-color: yellow;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    max-height: 80px;\n"
"}\n"
"")
        self.statBtn.setObjectName("statBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, -10, 251, 61))
        self.label.setStyleSheet("    font: bold 14px;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 330, 181, 21))
        self.label_2.setStyleSheet("    font: bold 14px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(56, 20, 71, 20))
        self.label_3.setStyleSheet("    font: bold 14px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 101, 20))
        self.label_4.setStyleSheet("    font: bold 14px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 20, 171, 20))
        self.label_5.setStyleSheet("    font: bold 14px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.selectLbl = QtWidgets.QLabel(self.centralwidget)
        self.selectLbl.setGeometry(QtCore.QRect(10, 50, 171, 171))
        self.selectLbl.setText("")
        self.selectLbl.setPixmap(QtGui.QPixmap("White.png"))
        self.selectLbl.setObjectName("selectLbl")
        self.staticLbl = QtWidgets.QLabel(self.centralwidget)
        self.staticLbl.setGeometry(QtCore.QRect(220, 50, 171, 171))
        self.staticLbl.setText("")
        self.staticLbl.setPixmap(QtGui.QPixmap("White.png"))
        self.staticLbl.setObjectName("staticLbl")
        self.rezultLbl = QtWidgets.QLabel(self.centralwidget)
        self.rezultLbl.setGeometry(QtCore.QRect(420, 60, 171, 171))
        self.rezultLbl.setText("")
        self.rezultLbl.setPixmap(QtGui.QPixmap("White.png"))
        self.rezultLbl.setObjectName("rezultLbl")
        self.scanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scanBtn.setGeometry(QtCore.QRect(20, 430, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanBtn.sizePolicy().hasHeightForWidth())
        self.scanBtn.setSizePolicy(sizePolicy)
        self.scanBtn.setAutoFillBackground(False)
        self.scanBtn.setStyleSheet("QPushButton{\n"
"cursor:pointer;\n"
"    color:white;\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    max-height: 80px;\n"
"}\n"
"")
        self.scanBtn.setObjectName("scanBtn")
        self.reztextLbl = QtWidgets.QLabel(self.centralwidget)
        self.reztextLbl.setGeometry(QtCore.QRect(630, 50, 221, 481))
        self.reztextLbl.setStyleSheet("background-color:white;\n"
"color:black;\n"
"")
        self.reztextLbl.setText("")
        self.reztextLbl.setObjectName("reztextLbl")
        self.statLbl = QtWidgets.QLabel(self.centralwidget)
        self.statLbl.setGeometry(QtCore.QRect(210, 360, 411, 171))
        self.statLbl.setStyleSheet("background-color:white;\n"
"color:black;")
        self.statLbl.setText("")
        self.statLbl.setObjectName("statLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectBtn.setText(_translate("MainWindow", "Виберіть фотографію"))
        self.statBtn.setText(_translate("MainWindow", "Дані для статистики"))
        self.label.setText(_translate("MainWindow", "Захворювання, до яких виявлена\n"
" схильність"))
        self.label_2.setText(_translate("MainWindow", "Статистика"))
        self.label_3.setText(_translate("MainWindow", "Ваше око"))
        self.label_4.setText(_translate("MainWindow", "Здорове око"))
        self.label_5.setText(_translate("MainWindow", "Результат сканування"))
        self.scanBtn.setText(_translate("MainWindow", "Сканувати"))
