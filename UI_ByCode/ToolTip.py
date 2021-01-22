import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QToolTip,QPushButton
from PyQt5.QtGui import QFont

class ToolTip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",12))
        self.setToolTip("今天是<b>星期五</b>")
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("设置提示信息")

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=ToolTip()
    mainWindow.show()
    sys.exit(app.exec_())