"""DrawPointsDemo
    绘制一个正弦曲线
    y=A sin(wx+p)+k
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import math


class DrawPointsDemo(QWidget):
    def __init__(self):
        super(DrawPointsDemo, self).__init__()
        self.setWindowTitle("DrawPointsDemo")

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            x = 100 * (-1 + 2 * i / 1000) + size.width() / 2.0
            y = 50* math.sin((x - size.width() / 2)*math.pi/50) + size.height() / 2.0
            painter.drawPoint(int(x), int(y))
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = DrawPointsDemo()
    mainWindow.show()
    sys.exit(app.exec_())
