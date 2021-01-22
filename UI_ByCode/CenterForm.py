import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super(CenterForm,self).__init__(parent)
        self.setWindowTitle("居中窗口")
        self.resize(400,300)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(newLeft,newTop)


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/test.ico'))
    mainWindow=CenterForm()
    mainWindow.show()
    sys.exit(app.exec_())