from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QCheckBoxDemo')
        layout=QHBoxLayout(self)
        self.checkbox1=QCheckBox('复选框1')
        self.checkbox2=QCheckBox('复选框2')
        self.checkbox3=QCheckBox('复选框3')
        self.checkbox1.setChecked(True)
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox1.stateChanged.connect(self.onStateChanged)
        self.checkbox2.stateChanged.connect(self.onStateChanged)
        self.checkbox3.stateChanged.connect(self.onStateChanged)
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)

    def onStateChanged(self):
        print('名称:'+self.checkbox1.text()+' 是否被选中:'+str(self.checkbox1.isChecked())+' 状态:'+str(self.checkbox1.checkState()))
        print('名称:'+self.checkbox2.text()+' 是否被选中:'+str(self.checkbox2.isChecked())+' 状态:'+str(self.checkbox2.checkState()))
        print('名称:'+self.checkbox3.text()+' 是否被选中:'+str(self.checkbox3.isChecked())+' 状态:'+str(self.checkbox3.checkState()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QCheckBoxDemo()
    mainWindow.show()
    sys.exit(app.exec_())