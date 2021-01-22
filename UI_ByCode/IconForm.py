import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置窗口图标")
        self.setGeometry(200,200,400,400)
        self.setWindowIcon(QIcon('icon/test.ico'))


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/test.ico'))
    mainWindow=IconForm()
    mainWindow.show()
    sys.exit(app.exec_())