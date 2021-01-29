"""QSpinBoxDemo
"""

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QSpinBox
from PyQt5.QtCore import Qt
import sys

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSpinBoxDemo")
        layout=QVBoxLayout(self)
        self.spinBox=QSpinBox()
        self.spinBox.setValue(1)
        self.spinBox.setRange(1,12)
        self.spinBox.valueChanged.connect(self.onValueChanged)
        self.label=QLabel('当前月份：'+self.spinBox.text()+'月')
        layout.addWidget(self.label)
        layout.addWidget(self.spinBox)
    
    def onValueChanged(self):
        self.label.setText('当前月份：'+self.spinBox.text()+'月')

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QSpinBoxDemo()
    mainWindow.show()
    sys.exit(app.exec_())