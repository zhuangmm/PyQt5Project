"""DrawAllDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class DrawAllDemo(QWidget):
    def __init__(self):
        super(DrawAllDemo, self).__init__()
        self.setWindowTitle("DrawAllDemo")
        self.resize(600,800)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        #一个alen=1/16角度
        #绘制弧
        painter.drawArc(0,0,100,100,0,45*16)
        #绘制圆
        painter.drawArc(200,0,100,100,0,360*16)
        #绘制带弦的弧
        painter.drawChord(400,0,100,100,0,120*16)
        #绘制椭圆
        painter.drawEllipse(0,200,100,50)
        #绘制圆
        painter.drawEllipse(200,200,100,100)
        #绘制扇形
        painter.drawPie(400,200,100,100,90*16,120*16)
        #绘制多边形
        point1=QPoint(20,420)
        point2=QPoint(30,470)
        point3=QPoint(80,500)
        point4=QPoint(179,570)
        point5=QPoint(100,500)
        polygon=QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polygon)

        #绘制图像
        image=QImage("../../../icon/test.ico")
        rect=QRect(200,400,image.width()*8,image.height()*8)
        painter.drawImage(rect,image)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = DrawAllDemo()
    mainWindow.show()
    sys.exit(app.exec_())
