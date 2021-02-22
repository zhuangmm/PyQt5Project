"""QInputDialogDemo
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QInputDialogDemo")
        layout=QFormLayout()
        self.button1=QPushButton("获取列表中的选项")
        self.button2=QPushButton("获取字符串")
        self.button3=QPushButton("获取整数")
        self.lineEdit1=QLineEdit()
        self.lineEdit2=QLineEdit()
        self.lineEdit3=QLineEdit()
        self.button1.clicked.connect(self.getItem)
        self.button2.clicked.connect(self.getText)
        self.button3.clicked.connect(self.getInt)

        layout.addRow(self.button1,self.lineEdit1)
        layout.addRow(self.button2,self.lineEdit2)
        layout.addRow(self.button3,self.lineEdit3)
        self.setLayout(layout)
        self.adjustSize()

    def getItem(self):
        items=("C","C++","Python","Java","C#","Golang")
        item,ok=QInputDialog.getItem(self,"","请选择编程语言",items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        text,ok=QInputDialog.getText(self,'',"请输入文本")
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        num,ok=QInputDialog.getInt(self,'',"请选择数字")
        if ok and num:
            self.lineEdit3.setText(str(num))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=QInputDialogDemo()
    mainWindow.show()
    sys.exit(app.exec_())


