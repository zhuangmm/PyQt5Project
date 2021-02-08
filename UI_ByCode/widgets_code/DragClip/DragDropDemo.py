"""
DragDropDemo

首先应让A控件能被拖动，B控件能接收被拖入的控件
A.setDragEnable(True)
B.setAcceptDrops(True)

B需要处理的两个事件
1.dragEnterEvent()
2.dropEvent()
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MyCombobox(QComboBox):
    def __init__(self):
        super(MyCombobox, self).__init__()

    def dragEnterEvent(self, e:QDragEnterEvent):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e:QDropEvent):
        self.addItem(e.mimeData().text())

class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        self.setWindowTitle("DragDropDemo")
        self.layout=QFormLayout(self)
        self.label=QLabel("将左侧文本编辑器的内容拖到右侧下拉列表即可添加")
        self.edit=QLineEdit()
        self.edit.setDragEnabled(True)
        self.combobox=MyCombobox()
        self.combobox.setAcceptDrops(True)
        self.layout.addRow(self.label)
        self.layout.addRow(self.edit,self.combobox)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=DragDropDemo()
    mainWindow.show()
    sys.exit(app.exec_())