"""DrawTextDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.setWindowTitle("DrawTextDemo")
        self.text = "测试文本：001"

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(25, 100, 230))
        painter.setFont(QFont('SimSun', 25))
        painter.drawText(a0.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = DrawTextDemo()
    mainWindow.show()
    sys.exit(app.exec_())
