"""
    Qlabel与伙伴控件
"""
from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #addWidget
        nameLabel=QLabel("&Name",self)
        nameLineEdit=QLineEdit(self)
        passwordLabel=QLabel("&Password",self)
        passwordLineEdit=QLineEdit(self)
        okButton=QPushButton("ok",self)
        cancelButton=QPushButton("cancel",self)
        #setBuddy
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel.setBuddy(passwordLineEdit)
        #setLayout
        windowLayout=QGridLayout()
        windowLayout.addWidget(nameLabel,0,0,1,1)
        windowLayout.addWidget(nameLineEdit,0,1,1,2)
        windowLayout.addWidget(passwordLabel,1,0,1,1)
        windowLayout.addWidget(passwordLineEdit,1,1,1,2)
        windowLayout.addWidget(okButton,2,1,1,1)
        windowLayout.addWidget(cancelButton,2,2,1,1)
        
        self.setWindowTitle("QLabelBuddy")
        self.setLayout(windowLayout)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QLabelBuddy()
    mainWindow.show()
    sys.exit(app.exec_())
