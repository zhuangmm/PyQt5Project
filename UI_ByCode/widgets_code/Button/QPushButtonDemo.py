from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButtonDemo")
        layout=QFormLayout(self)
        
        
        self.button1=QPushButton("第一个按钮")
        self.button1.setText("First Button")
        self.button1.setCheckable(True)
        self.button1.clicked.connect(lambda:self.onButtonClicked(self.button1))
        self.button1.toggled.connect(self.onButton1Toggled)

        self.button2=QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap('icon/test.ico')))
        self.button2.clicked.connect(lambda:self.onButtonClicked(self.button2))

        self.button3=QPushButton("不可用按钮")
        self.button3.setEnabled(False)

        self.button4=QPushButton("&Default")
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.onButtonClicked(self.button4))

        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.button3)
        layout.addRow(self.button4)

    def onButtonClicked(self,button:QAbstractButton):
        print('被单击的按钮是',button.text())
    
    def onButton1Toggled(self):
        if self.button1.isChecked():
            print("按钮已被选中")
        else:
            print("按钮未被选中")

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QPushButtonDemo()
    mainWindow.show()
    sys.exit(app.exec_())