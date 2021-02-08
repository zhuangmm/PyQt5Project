"""DrawMultiLineDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class DrawMultiLineDemo(QWidget):
    def __init__(self):
        super(DrawMultiLineDemo, self).__init__()
        self.setWindowTitle("DrawMultiLineDemo")

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.begin(self)
        pen=QPen(Qt.red,3,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(150,40,450,40)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(150, 80, 450, 80)
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(150, 120, 450, 120)
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(150, 160, 450, 160)
        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(150, 200, 450, 200)
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,2,4,2])
        painter.setPen(pen)
        painter.drawLine(150, 240, 450, 240)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = DrawMultiLineDemo()
    mainWindow.show()
    sys.exit(app.exec_())
