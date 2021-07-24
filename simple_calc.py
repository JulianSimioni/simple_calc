import sys
from calc import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from math import pi, e, log10, log, sin, cos, tan, sqrt, log2, acos, asin, atan, acosh, asinh, atanh, cosh, sinh, tanh

class Calc(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.setFixedSize(312, 312)

        self.btnone.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnone.text())
        )
        self.btntwo.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btntwo.text())
        )
        self.btnthree.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnthree.text())
        )
        self.btnfour.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnfour.text())
        )
        self.btnfive.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnfive.text())
        )
        self.btnsix.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnsix.text())
        )
        self.btnseven.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnseven.text())
        )
        self.btneight.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btneight.text())
        )
        self.btnnine.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnnine.text())
        )
        self.btnzero.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnzero.text())
        )
        self.btndot.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btndot.text())
        )
        self.btnparentd.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnparentd.text())
        )
        self.btnparente.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.btnparente.text())
        )
        self.plus.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.plus.text())
        )
        self.minus.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.minus.text())
        )
        self.divide.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.divide.text())
        )
        self.multiply.clicked.connect(
            lambda: self.display.setText(self.display.text() + self.multiply.text())
        )
        self.btnclear.clicked.connect(
            lambda: self.display.setText('')
        )
        self.btnerase.clicked.connect(
            lambda: self.display.setText(self.display.text()[:-1])
        )
        self.btnequal.clicked.connect(self.igual)

    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Erro: entendi nada')

if __name__ == '__main__':

    qt = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    qt.exec_()
