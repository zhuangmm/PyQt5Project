"""
    QLineEdit综合实践
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout=QFormLayout(self)
        self.setWindowTitle("QLineEditDemo")

        intValidatorEdit=QLineEdit()
        intValidatorEdit.setValidator(QIntValidator())
        intValidatorEdit.setMaxLength(4)
        intValidatorEdit.setFont(QFont('Arial',20))

        doubleValidatorEdit=QLineEdit()
        doubleValidatorEdit.setValidator(QDoubleValidator(0.99,99.99,2))
        
        maskEdit=QLineEdit()
        maskEdit.setInputMask('9999-99-99;0')

        echoModeEdit=QLineEdit()
        echoModeEdit.setEchoMode(QLineEdit.Password)
        echoModeEdit.editingFinished.connect(self.onEditFinished)
        textChangedEdit=QLineEdit()
        textChangedEdit.textChanged.connect(self.onTextChanged)
        readOnlyEdit=QLineEdit()
        readOnlyEdit.setText("只读")
        readOnlyEdit.setReadOnly(True)

        layout.addRow('intValidatorEdit',intValidatorEdit)
        layout.addRow('doubleValidatorEdit',doubleValidatorEdit)
        layout.addRow('maskEdit',maskEdit)
        layout.addRow('textChangedEdit',textChangedEdit)
        layout.addRow('echoModeEdit',echoModeEdit)
        layout.addRow('readOnlyEdit',readOnlyEdit)

    def onTextChanged(self,text):
        print('输入的内容：',text)

    def onEditFinished(self):
        print('已输入值')


if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QLineEditDemo()
    mainWindow.show()
    sys.exit(app.exec_())