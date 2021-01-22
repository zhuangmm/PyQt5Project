import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWindow,self).__init__(parent)

        self.setWindowTitle("第一个主窗口应用")

        self.resize(400,300)

        self.status=self.statusBar()

        self.status.showMessage("只存在5秒的消息",5000)

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/test.ico'))
    mainWindow=FirstMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())