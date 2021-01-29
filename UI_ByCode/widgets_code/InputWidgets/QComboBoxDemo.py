"""QComboBoxDemo
"""
from PyQt5.QtWidgets import QApplication,QWidget,QComboBox,QVBoxLayout,QLabel
import sys

class QComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QComboBoxDemo")
        layout=QVBoxLayout(self)

        self.lable=QLabel("请选择语言")
        self.comboBox=QComboBox()
        self.comboBox.addItem("C++")
        self.comboBox.addItem("Python")
        self.comboBox.addItems(["Java","C#","Go"])
        self.comboBox.currentIndexChanged.connect(self.onCurrentIndexChanged)

        layout.addWidget(self.lable)
        layout.addWidget(self.comboBox)
    
    def onCurrentIndexChanged(self,index):
        self.lable.setText(self.comboBox.currentText())
        self.lable.adjustSize()
        for i in range(self.comboBox.count()):
            print('item'+str(i)+'='+self.comboBox.itemText(i))
        print('current index'+str(index)+'selected changed'+self.comboBox.currentText())

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QComboBoxDemo()
    mainWindow.show()
    sys.exit(app.exec_())