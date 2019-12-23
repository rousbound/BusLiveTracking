# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BusLinesTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusLinesTextBrowser.setGeometry(QtCore.QRect(20, 10, 761, 521))
        self.BusLinesTextBrowser.setObjectName("BusLinesTextBrowser")
        self.BusLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BusLineEdit.setGeometry(QtCore.QRect(130, 560, 111, 21))
        self.BusLineEdit.setObjectName("BusLineEdit")
        self.BusLineLabel = QtWidgets.QLabel(self.centralwidget)
        self.BusLineLabel.setGeometry(QtCore.QRect(30, 550, 111, 31))
        self.BusLineLabel.setObjectName("BusLineLabel")
        self.BusSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.BusSearchButton.setGeometry(QtCore.QRect(260, 550, 101, 61))
        self.BusSearchButton.setObjectName("BusSearchButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BusLineLabel.setText(_translate("MainWindow", "Enter bus line:"))
        self.BusSearchButton.setText(_translate("MainWindow", "Search"))

