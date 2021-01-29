"""QSliderDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class QSliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSliderDemo")
        layout=QVBoxLayout(self)
        self.lable=QLabel("Hello World!")
        self.slider=QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(12,38)
        self.slider.setSingleStep(6)
        self.slider.setValue(18)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(6)
        self.slider.valueChanged.connect(self.onSliderValueChanged)
        layout.addWidget(self.lable)
        layout.addWidget(self.slider)

    def onSliderValueChanged(self):
        self.adjustSize()
        self.lable.setFont(QFont('Arial',self.slider.value()))
        print('Slider的当前值为：{}。'.format(self.slider.value()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QSliderDemo()
    mainWindow.show()
    sys.exit(app.exec_())