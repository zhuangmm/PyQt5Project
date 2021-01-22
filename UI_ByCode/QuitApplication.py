import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QMainWindow,QApplication,QWidget
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(400,300)
        self.setWindowTitle("退出应用程序")
        #添加Button
        self.button1=QPushButton("退出应用程序")
        #将信号与槽关联
        self.button1.clicked.connect(self.onClickButton)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainForm=QWidget()
        mainForm.setLayout(layout)
        self.setCentralWidget(mainForm)

    def onClickButton(self):
        sender=self.sender()
        print(sender.text()+" 按钮被按下")
        app=QApplication.instance()
        #退出应用程序
        app.quit()

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/test.ico'))
    mainWindow=QuitApplication()
    mainWindow.show()
    sys.exit(app.exec_())