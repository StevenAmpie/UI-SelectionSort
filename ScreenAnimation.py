# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ScreenAnimation.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenAnimation(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("InfoImages/LogoApp.ico"))
        MainWindow.resize(1228, 866)
        MainWindow.setMinimumSize(QtCore.QSize(1228, 866))
        MainWindow.setMaximumSize(QtCore.QSize(1228, 866))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parqueo = QtWidgets.QLabel(self.centralwidget)
        self.parqueo.setEnabled(False)
        self.parqueo.setGeometry(QtCore.QRect(0, 0, 1228, 866))
        self.parqueo.setMinimumSize(QtCore.QSize(1228, 866))
        self.parqueo.setMaximumSize(QtCore.QSize(1228, 866))
        self.parqueo.setMouseTracking(False)
        self.parqueo.setToolTipDuration(-1)
        self.parqueo.setStyleSheet("")
        self.parqueo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.parqueo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.parqueo.setText("")
        self.parqueo.setPixmap(QtGui.QPixmap("Parqueo/Parqueo.jpg"))
        self.parqueo.setObjectName("parqueo")
        self.car1 = QtWidgets.QLabel(self.centralwidget)
        self.car1.setGeometry(QtCore.QRect(50, 200, 101, 161))
        self.car1.setMinimumSize(QtCore.QSize(101, 161))
        self.car1.setMaximumSize(QtCore.QSize(101, 161))
        self.car1.setStyleSheet("")
        self.car1.setText("")
        self.car1.setPixmap(QtGui.QPixmap("Carros/car1.png"))
        self.car1.setScaledContents(True)
        self.car1.setObjectName("car1")
        self.labelSort = QtWidgets.QLabel(self.centralwidget)
        self.labelSort.setGeometry(QtCore.QRect(1030, 830, 191, 31))
        self.labelSort.setMinimumSize(QtCore.QSize(191, 31))
        self.labelSort.setMaximumSize(QtCore.QSize(191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSort.setFont(font)
        self.labelSort.setMouseTracking(True)
        self.labelSort.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.labelSort.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelSort.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelSort.setObjectName("labelSort")
        self.car4 = QtWidgets.QLabel(self.centralwidget)
        self.car4.setGeometry(QtCore.QRect(390, 200, 101, 161))
        self.car4.setMinimumSize(QtCore.QSize(101, 161))
        self.car4.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car4.setFont(font)
        self.car4.setStyleSheet("")
        self.car4.setText("")
        self.car4.setPixmap(QtGui.QPixmap("Carros/car4.png"))
        self.car4.setScaledContents(True)
        self.car4.setObjectName("car4")
        self.car2 = QtWidgets.QLabel(self.centralwidget)
        self.car2.setGeometry(QtCore.QRect(160, 200, 101, 161))
        self.car2.setMinimumSize(QtCore.QSize(101, 161))
        self.car2.setMaximumSize(QtCore.QSize(101, 161))
        self.car2.setStyleSheet("")
        self.car2.setText("")
        self.car2.setPixmap(QtGui.QPixmap("Carros/car2.png"))
        self.car2.setScaledContents(True)
        self.car2.setObjectName("car2")
        self.ButtonIniciarSortFin = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonIniciarSortFin.setGeometry(QtCore.QRect(1070, 700, 111, 131))
        self.ButtonIniciarSortFin.setMinimumSize(QtCore.QSize(111, 131))
        self.ButtonIniciarSortFin.setMaximumSize(QtCore.QSize(111, 131))
        self.ButtonIniciarSortFin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonIniciarSortFin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ButtonIniciarSortFin.setToolTipDuration(0)
        self.ButtonIniciarSortFin.setStyleSheet("border-image: url(InfoImages/palancaFin.png);")
        self.ButtonIniciarSortFin.setText("")
        self.ButtonIniciarSortFin.setObjectName("ButtonIniciarSortFin")
        self.car5 = QtWidgets.QLabel(self.centralwidget)
        self.car5.setGeometry(QtCore.QRect(510, 200, 101, 161))
        self.car5.setMinimumSize(QtCore.QSize(101, 161))
        self.car5.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car5.setFont(font)
        self.car5.setStyleSheet("")
        self.car5.setText("")
        self.car5.setPixmap(QtGui.QPixmap("Carros/car5.png"))
        self.car5.setScaledContents(True)
        self.car5.setObjectName("car5")
        self.car8 = QtWidgets.QLabel(self.centralwidget)
        self.car8.setGeometry(QtCore.QRect(850, 200, 101, 161))
        self.car8.setMinimumSize(QtCore.QSize(101, 161))
        self.car8.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car8.setFont(font)
        self.car8.setStyleSheet("")
        self.car8.setText("")
        self.car8.setPixmap(QtGui.QPixmap("Carros/car8.png"))
        self.car8.setScaledContents(True)
        self.car8.setObjectName("car8")
        self.car3 = QtWidgets.QLabel(self.centralwidget)
        self.car3.setGeometry(QtCore.QRect(280, 200, 101, 161))
        self.car3.setMinimumSize(QtCore.QSize(101, 161))
        self.car3.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car3.setFont(font)
        self.car3.setStyleSheet("")
        self.car3.setText("")
        self.car3.setPixmap(QtGui.QPixmap("Carros/car3.png"))
        self.car3.setScaledContents(True)
        self.car3.setObjectName("car3")
        self.car7 = QtWidgets.QLabel(self.centralwidget)
        self.car7.setGeometry(QtCore.QRect(730, 200, 101, 161))
        self.car7.setMinimumSize(QtCore.QSize(101, 161))
        self.car7.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car7.setFont(font)
        self.car7.setStyleSheet("")
        self.car7.setText("")
        self.car7.setTextFormat(QtCore.Qt.RichText)
        self.car7.setPixmap(QtGui.QPixmap("Carros/car7.png"))
        self.car7.setScaledContents(True)
        self.car7.setObjectName("car7")
        self.ButtonIniciarSort = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonIniciarSort.setGeometry(QtCore.QRect(1070, 700, 111, 131))
        self.ButtonIniciarSort.setMinimumSize(QtCore.QSize(111, 131))
        self.ButtonIniciarSort.setMaximumSize(QtCore.QSize(111, 131))
        self.ButtonIniciarSort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonIniciarSort.setStyleSheet("border-image: url(InfoImages/palanca.png);")
        self.ButtonIniciarSort.setText("")
        self.ButtonIniciarSort.setObjectName("ButtonIniciarSort")
        self.car6 = QtWidgets.QLabel(self.centralwidget)
        self.car6.setGeometry(QtCore.QRect(620, 200, 101, 161))
        self.car6.setMinimumSize(QtCore.QSize(101, 161))
        self.car6.setMaximumSize(QtCore.QSize(101, 161))
        self.car6.setStatusTip("")
        self.car6.setStyleSheet("")
        self.car6.setText("")
        self.car6.setPixmap(QtGui.QPixmap("Carros/car6.png"))
        self.car6.setScaledContents(True)
        self.car6.setObjectName("car6")
        self.car9 = QtWidgets.QLabel(self.centralwidget)
        self.car9.setGeometry(QtCore.QRect(960, 200, 101, 161))
        self.car9.setMinimumSize(QtCore.QSize(101, 161))
        self.car9.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car9.setFont(font)
        self.car9.setStyleSheet("")
        self.car9.setText("")
        self.car9.setPixmap(QtGui.QPixmap("Carros/car9.png"))
        self.car9.setScaledContents(True)
        self.car9.setObjectName("car9")
        self.car10 = QtWidgets.QLabel(self.centralwidget)
        self.car10.setGeometry(QtCore.QRect(1070, 200, 101, 161))
        self.car10.setMinimumSize(QtCore.QSize(101, 161))
        self.car10.setMaximumSize(QtCore.QSize(101, 161))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.car10.setFont(font)
        self.car10.setStyleSheet("")
        self.car10.setText("")
        self.car10.setPixmap(QtGui.QPixmap("Carros/car10.png"))
        self.car10.setScaledContents(True)
        self.car10.setObjectName("car10")
        self.posicion1 = QtWidgets.QLabel(self.centralwidget)
        self.posicion1.setGeometry(QtCore.QRect(50, 500, 101, 161))
        self.posicion1.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion1.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion1.setStyleSheet("")
        self.posicion1.setText("")
        self.posicion1.setScaledContents(True)
        self.posicion1.setObjectName("posicion1")
        self.posicion2 = QtWidgets.QLabel(self.centralwidget)
        self.posicion2.setGeometry(QtCore.QRect(160, 500, 101, 161))
        self.posicion2.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion2.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion2.setStyleSheet("")
        self.posicion2.setText("")
        self.posicion2.setScaledContents(True)
        self.posicion2.setObjectName("posicion2")
        self.posicion3 = QtWidgets.QLabel(self.centralwidget)
        self.posicion3.setGeometry(QtCore.QRect(280, 500, 101, 161))
        self.posicion3.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion3.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion3.setStyleSheet("")
        self.posicion3.setText("")
        self.posicion3.setScaledContents(True)
        self.posicion3.setObjectName("posicion3")
        self.posicion4 = QtWidgets.QLabel(self.centralwidget)
        self.posicion4.setGeometry(QtCore.QRect(390, 500, 101, 161))
        self.posicion4.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion4.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion4.setStyleSheet("")
        self.posicion4.setText("")
        self.posicion4.setScaledContents(True)
        self.posicion4.setObjectName("posicion4")
        self.posicion5 = QtWidgets.QLabel(self.centralwidget)
        self.posicion5.setGeometry(QtCore.QRect(510, 500, 101, 161))
        self.posicion5.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion5.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion5.setStyleSheet("")
        self.posicion5.setText("")
        self.posicion5.setScaledContents(True)
        self.posicion5.setObjectName("posicion5")
        self.posicion6 = QtWidgets.QLabel(self.centralwidget)
        self.posicion6.setGeometry(QtCore.QRect(620, 500, 101, 161))
        self.posicion6.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion6.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion6.setStyleSheet("")
        self.posicion6.setText("")
        self.posicion6.setScaledContents(True)
        self.posicion6.setObjectName("posicion6")
        self.posicion7 = QtWidgets.QLabel(self.centralwidget)
        self.posicion7.setGeometry(QtCore.QRect(730, 500, 101, 161))
        self.posicion7.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion7.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion7.setStyleSheet("")
        self.posicion7.setText("")
        self.posicion7.setScaledContents(True)
        self.posicion7.setObjectName("posicion7")
        self.posicion8 = QtWidgets.QLabel(self.centralwidget)
        self.posicion8.setGeometry(QtCore.QRect(850, 500, 101, 161))
        self.posicion8.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion8.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion8.setStyleSheet("")
        self.posicion8.setText("")
        self.posicion8.setScaledContents(True)
        self.posicion8.setObjectName("posicion8")
        self.posicion9 = QtWidgets.QLabel(self.centralwidget)
        self.posicion9.setGeometry(QtCore.QRect(960, 500, 101, 161))
        self.posicion9.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion9.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion9.setStyleSheet("")
        self.posicion9.setText("")
        self.posicion9.setScaledContents(True)
        self.posicion9.setObjectName("posicion9")
        self.posicion10 = QtWidgets.QLabel(self.centralwidget)
        self.posicion10.setGeometry(QtCore.QRect(1070, 500, 101, 161))
        self.posicion10.setMinimumSize(QtCore.QSize(101, 161))
        self.posicion10.setMaximumSize(QtCore.QSize(101, 161))
        self.posicion10.setStyleSheet("")
        self.posicion10.setText("")
        self.posicion10.setScaledContents(True)
        self.posicion10.setObjectName("posicion10")
        self.parqueo1 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo1.setGeometry(QtCore.QRect(50, 200, 101, 161))
        self.parqueo1.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo1.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo1.setStyleSheet("")
        self.parqueo1.setText("")
        self.parqueo1.setScaledContents(True)
        self.parqueo1.setObjectName("parqueo1")
        self.parqueo3 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo3.setGeometry(QtCore.QRect(280, 200, 101, 161))
        self.parqueo3.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo3.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo3.setStyleSheet("")
        self.parqueo3.setText("")
        self.parqueo3.setScaledContents(True)
        self.parqueo3.setObjectName("parqueo3")
        self.parqueo6 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo6.setGeometry(QtCore.QRect(620, 200, 101, 161))
        self.parqueo6.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo6.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo6.setStyleSheet("")
        self.parqueo6.setText("")
        self.parqueo6.setScaledContents(True)
        self.parqueo6.setObjectName("parqueo6")
        self.parqueo2 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo2.setGeometry(QtCore.QRect(160, 200, 101, 161))
        self.parqueo2.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo2.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo2.setStyleSheet("")
        self.parqueo2.setText("")
        self.parqueo2.setScaledContents(True)
        self.parqueo2.setObjectName("parqueo2")
        self.parqueo4 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo4.setGeometry(QtCore.QRect(390, 200, 101, 161))
        self.parqueo4.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo4.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo4.setStyleSheet("")
        self.parqueo4.setText("")
        self.parqueo4.setScaledContents(True)
        self.parqueo4.setObjectName("parqueo4")
        self.parqueo5 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo5.setGeometry(QtCore.QRect(510, 200, 101, 161))
        self.parqueo5.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo5.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo5.setStyleSheet("")
        self.parqueo5.setText("")
        self.parqueo5.setScaledContents(True)
        self.parqueo5.setObjectName("parqueo5")
        self.parqueo7 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo7.setGeometry(QtCore.QRect(730, 200, 101, 161))
        self.parqueo7.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo7.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo7.setStyleSheet("")
        self.parqueo7.setText("")
        self.parqueo7.setScaledContents(True)
        self.parqueo7.setObjectName("parqueo7")
        self.parqueo8 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo8.setGeometry(QtCore.QRect(850, 200, 101, 161))
        self.parqueo8.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo8.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo8.setStyleSheet("")
        self.parqueo8.setText("")
        self.parqueo8.setScaledContents(True)
        self.parqueo8.setObjectName("parqueo8")
        self.parqueo10 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo10.setGeometry(QtCore.QRect(1070, 200, 101, 161))
        self.parqueo10.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo10.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo10.setStyleSheet("")
        self.parqueo10.setText("")
        self.parqueo10.setScaledContents(True)
        self.parqueo10.setObjectName("parqueo10")
        self.parqueo9 = QtWidgets.QLabel(self.centralwidget)
        self.parqueo9.setGeometry(QtCore.QRect(960, 200, 101, 161))
        self.parqueo9.setMinimumSize(QtCore.QSize(101, 161))
        self.parqueo9.setMaximumSize(QtCore.QSize(101, 161))
        self.parqueo9.setStyleSheet("")
        self.parqueo9.setText("")
        self.parqueo9.setScaledContents(True)
        self.parqueo9.setObjectName("parqueo9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSort.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">SORT</span></p></body></html>"))
