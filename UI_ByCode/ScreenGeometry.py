import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication

class screenGeometry(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        self.move(200,300)
        self.button1=QPushButton(parent=self)
        self.button1.setText('按钮')
        self.button1.clicked.connect(self.onClickButton)

    def onClickButton(self):
        print(1)
        print('self.x()=%d'%(self.x()))#窗口横坐标
        print('self.y()=%d'%(self.y()))#窗口纵坐标
        print('self.width()=%d'%(self.width()))#工作区宽度
        print('self.height()=%d'%(self.height()))#工作区高度

        print(2)
        print('self.geometry().x()=%d'%(self.geometry().x()))#工作区横坐标
        print('self.geometry().y()=%d'%(self.geometry().y()))#工作区纵坐标
        print('self.geometry().width()=%d'%(self.geometry().width()))#工作区宽度
        print('self.geometry().height()=%d'%(self.geometry().height()))#工作区高度

        print(3)
        print('self.frameGeometry().x()=%d'%(self.frameGeometry().x()))#窗口横坐标
        print('self.frameGeometry().y()=%d'%(self.frameGeometry().y()))#窗口纵坐标
        print('self.frameGeometry().width()=%d'%(self.frameGeometry().width()))#窗口宽度
        print('self.frameGeometry().height()=%d'%(self.frameGeometry().height()))#窗口高度

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=screenGeometry()
    mainWindow.show()
    sys.exit(app.exec_())
