"""QColorDialogDemo
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QColorDialogDemo")
        self.textColorButton=QPushButton("选择文本颜色")
        self.textColorButton.clicked.connect(self.onTextColorButtonClicked)
        self.backgroundColorButton=QPushButton("选择背景颜色")
        self.backgroundColorButton.clicked.connect(self.onBackgroundColorButtonClicked)
        self.colorLabel=QLabel("测试文字")
        self.colorLabel.setAutoFillBackground(True)
        layout=QVBoxLayout(self)
        layout.addWidget(self.colorLabel)
        layout.addWidget(self.textColorButton)
        layout.addWidget(self.backgroundColorButton)

    def onTextColorButtonClicked(self):
        color=QColorDialog.getColor()
        palette=QPalette()
        palette.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(palette)

    def onBackgroundColorButtonClicked(self):
        color=QColorDialog.getColor()
        palette=QPalette()
        palette.setColor(QPalette.Window,color)
        self.colorLabel.setPalette(palette)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QColorDialogDemo()
    mainWindow.show()
    sys.exit(app.exec_())
