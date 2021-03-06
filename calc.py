# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 312)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(16)
        self.display.setFont(font)
        self.display.setText("")
        self.display.setObjectName("display")
        self.btnseven = QtWidgets.QPushButton(self.centralwidget)
        self.btnseven.setGeometry(QtCore.QRect(10, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnseven.setFont(font)
        self.btnseven.setObjectName("btnseven")
        self.btneight = QtWidgets.QPushButton(self.centralwidget)
        self.btneight.setGeometry(QtCore.QRect(70, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btneight.setFont(font)
        self.btneight.setObjectName("btneight")
        self.btnnine = QtWidgets.QPushButton(self.centralwidget)
        self.btnnine.setGeometry(QtCore.QRect(130, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnnine.setFont(font)
        self.btnnine.setMouseTracking(False)
        self.btnnine.setTabletTracking(False)
        self.btnnine.setObjectName("btnnine")
        self.btnclear = QtWidgets.QPushButton(self.centralwidget)
        self.btnclear.setGeometry(QtCore.QRect(250, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnclear.setFont(font)
        self.btnclear.setObjectName("btnclear")
        self.btnfour = QtWidgets.QPushButton(self.centralwidget)
        self.btnfour.setGeometry(QtCore.QRect(10, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnfour.setFont(font)
        self.btnfour.setObjectName("btnfour")
        self.btnfive = QtWidgets.QPushButton(self.centralwidget)
        self.btnfive.setGeometry(QtCore.QRect(70, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnfive.setFont(font)
        self.btnfive.setObjectName("btnfive")
        self.btnsix = QtWidgets.QPushButton(self.centralwidget)
        self.btnsix.setGeometry(QtCore.QRect(130, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnsix.setFont(font)
        self.btnsix.setObjectName("btnsix")
        self.btntwo = QtWidgets.QPushButton(self.centralwidget)
        self.btntwo.setGeometry(QtCore.QRect(70, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btntwo.setFont(font)
        self.btntwo.setObjectName("btntwo")
        self.btnone = QtWidgets.QPushButton(self.centralwidget)
        self.btnone.setGeometry(QtCore.QRect(10, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnone.setFont(font)
        self.btnone.setObjectName("btnone")
        self.btnthree = QtWidgets.QPushButton(self.centralwidget)
        self.btnthree.setGeometry(QtCore.QRect(130, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnthree.setFont(font)
        self.btnthree.setObjectName("btnthree")
        self.btnerase = QtWidgets.QPushButton(self.centralwidget)
        self.btnerase.setGeometry(QtCore.QRect(250, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnerase.setFont(font)
        self.btnerase.setObjectName("btnerase")
        self.btndot = QtWidgets.QPushButton(self.centralwidget)
        self.btndot.setGeometry(QtCore.QRect(250, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btndot.setFont(font)
        self.btndot.setObjectName("btndot")
        self.btnparente = QtWidgets.QPushButton(self.centralwidget)
        self.btnparente.setGeometry(QtCore.QRect(10, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnparente.setFont(font)
        self.btnparente.setObjectName("btnparente")
        self.btnzero = QtWidgets.QPushButton(self.centralwidget)
        self.btnzero.setGeometry(QtCore.QRect(70, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnzero.setFont(font)
        self.btnzero.setObjectName("btnzero")
        self.btnparentd = QtWidgets.QPushButton(self.centralwidget)
        self.btnparentd.setGeometry(QtCore.QRect(130, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnparentd.setFont(font)
        self.btnparentd.setObjectName("btnparentd")
        self.btnequal = QtWidgets.QPushButton(self.centralwidget)
        self.btnequal.setGeometry(QtCore.QRect(250, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.btnequal.setFont(font)
        self.btnequal.setObjectName("btnequal")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(190, 70, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(190, 130, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(190, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(190, 250, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora fria"))
        self.btnseven.setText(_translate("MainWindow", "7"))
        self.btneight.setText(_translate("MainWindow", "8"))
        self.btnnine.setText(_translate("MainWindow", "9"))
        self.btnclear.setText(_translate("MainWindow", "C"))
        self.btnfour.setText(_translate("MainWindow", "4"))
        self.btnfive.setText(_translate("MainWindow", "5"))
        self.btnsix.setText(_translate("MainWindow", "6"))
        self.btntwo.setText(_translate("MainWindow", "2"))
        self.btnone.setText(_translate("MainWindow", "1"))
        self.btnthree.setText(_translate("MainWindow", "3"))
        self.btnerase.setText(_translate("MainWindow", "<-"))
        self.btndot.setText(_translate("MainWindow", "."))
        self.btnparente.setText(_translate("MainWindow", "("))
        self.btnzero.setText(_translate("MainWindow", "0"))
        self.btnparentd.setText(_translate("MainWindow", ")"))
        self.btnequal.setText(_translate("MainWindow", "="))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
