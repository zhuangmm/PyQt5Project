"""BrushDrawDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class BrushDrawDemo(QWidget):
    def __init__(self):
        super(BrushDrawDemo, self).__init__()
        self.setWindowTitle("BrushDrawDemo")

    def paintEvent(self, a0:QPaintEvent):
        painter=QPainter(self)
        painter.begin(self)
        brush=QBrush(Qt.SolidPattern)
        brush.setColor(Qt.red)
        painter.setBrush(brush)
        painter.drawRect(10,10,90,90)

        brush.setStyle(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(110, 10, 90, 90)

        brush.setStyle(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(210, 10, 90, 90)

        brush.setStyle(Qt.CrossPattern)
        painter.setBrush(brush)
        painter.drawRect(310, 10, 90, 90)

        brush.setStyle(Qt.TexturePattern)
        brush.setTexture(QPixmap('../../../icon/test.ico'))
        painter.setBrush(brush)
        painter.drawRect(410, 10, 90, 90)

        brush.setStyle(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(510, 10, 90, 90)

        brush.setStyle(Qt.ConicalGradientPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 110, 90, 90)

        brush.setStyle(Qt.RadialGradientPattern)
        painter.setBrush(brush)
        painter.drawRect(110, 110, 90, 90)

        painter.end()

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=BrushDrawDemo()
    mainWindow.show()
    sys.exit(app.exec_())
