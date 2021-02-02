"""QFontDialogDemo
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QFontDialogDemo")
        layout=QVBoxLayout(self)
        self.fontDialogButton=QPushButton("选择字体")
        self.fontLabel=QLabel("你好，世界!")

        self.fontDialogButton.clicked.connect(self.onFontDialogButtonClicked)
        layout.addWidget(self.fontLabel)
        layout.addWidget(self.fontDialogButton)

    def onFontDialogButtonClicked(self):
        font,ok=QFontDialog().getFont()
        if ok:
            self.fontLabel.setFont(font)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QFontDialogDemo()
    mainWindow.show()
    sys.exit(app.exec_())
