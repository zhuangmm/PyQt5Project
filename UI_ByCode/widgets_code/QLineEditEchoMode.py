"""
QLineEdit

回显模式(EchoMode):
Normal
NoEcho
Password
PasswordEchoOnEdit

"""

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout=QFormLayout(self)

        normalLineEdit=QLineEdit(self)
        noEchoLineEdit=QLineEdit(self)
        passwordLineEdit=QLineEdit(self)
        passwordEchoOnEditLineEdit=QLineEdit(self)

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        layout.addRow(normalLineEdit)
        layout.addRow(noEchoLineEdit)
        layout.addRow(passwordLineEdit)
        layout.addRow(passwordEchoOnEditLineEdit)

        self.setWindowTitle("QLineEditDemo")

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QLineEditEchoMode()
    mainWindow.show()
    sys.exit(app.exec_())
        