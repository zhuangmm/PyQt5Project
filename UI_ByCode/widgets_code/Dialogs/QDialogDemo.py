"""QDialogDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dialogButton=QPushButton("点击一下，会弹出一个对话框，不信你试试")
        self.setWindowTitle("QDialogDemo")
        layout=QVBoxLayout(self)
        layout.addWidget(self.dialogButton)
        self.dialogButton.clicked.connect(self.onDialogButtonClicked)

    def onDialogButtonClicked(self):
        dialog=QDialog()
        dialog.setWindowTitle("一个对话框")
        layout=QVBoxLayout(dialog)
        dialog.button=QPushButton("点击即可关闭对话框")
        dialog.button.clicked.connect(dialog.close)
        layout.addWidget(dialog.button)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QDialogDemo()
    mainWindow.show()
    sys.exit(app.exec_())