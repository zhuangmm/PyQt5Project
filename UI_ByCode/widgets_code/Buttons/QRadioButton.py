from PyQt5.QtWidgets import *
import sys

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButtonDemo')
        layout=QHBoxLayout(self)

        radioButton1=QRadioButton('RadioButton1')
        radioButton1.setChecked(True)
        radioButton1.toggled.connect(self.onRadioButtonChecked)
        radioButton2=QRadioButton('RadioButton2')
        radioButton2.toggled.connect(self.onRadioButtonChecked)
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)

    def onRadioButtonChecked(self):
        radioButton=self.sender() 
        if radioButton.isChecked()==True:
            print('<'+radioButton.text()+'> 被选中')
        else:
            print('<'+radioButton.text()+'> 未被选中')

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QRadioButtonDemo()
    mainWindow.show()
    sys.exit(app.exec_())
        