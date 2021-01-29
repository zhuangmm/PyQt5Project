'''
    使用Validator来限制QLineEdit的输入
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout=QFormLayout(self)
        intLineEdit=QLineEdit(self)
        doubleLineEdit=QLineEdit(self)
        regExpLineEdit=QLineEdit(self)

        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)
        regExp=QRegExp('[a-zA-Z0-9]+$')
        regExpValidator=QRegExpValidator(self)
        regExpValidator.setRegExp(regExp)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regExpLineEdit.setValidator(regExpValidator)

        layout.addRow('int',intLineEdit)
        layout.addRow('double',doubleLineEdit)
        layout.addRow('RegExp',regExpLineEdit)

        self.setWindowTitle('QLineEditValidator')

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QLineEditValitor()
    mainWindow.show()
    sys.exit(app.exec_())