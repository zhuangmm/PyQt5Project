"""
QTextEdit控件
"""

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout=QFormLayout(self)
        self.textEdit=QTextEdit()
        self.setWindowTitle('QTextLineEdit')

        textButton=QPushButton("显示文本")
        textButton.clicked.connect(self.onClickedTextButton)
        htmlButton=QPushButton("显示HTML")
        htmlButton.clicked.connect(self.onClickedHtmlButton)
        printTextButton=QPushButton("输出文本")
        printTextButton.clicked.connect(self.onClickedPrintTextButton)
        printHtmlButton=QPushButton("输出HTML")
        printHtmlButton.clicked.connect(self.onClickedPrintHtmlButton)

        layout.addRow(self.textEdit)
        layout.addRow(textButton)
        layout.addRow(htmlButton)
        layout.addRow(printTextButton)
        layout.addRow(printHtmlButton)

    def onClickedTextButton(self):
        self.textEdit.setPlainText("Hello World！")
    
    def onClickedHtmlButton(self):
        self.textEdit.setHtml('<font color="#00FFAA" size="5">Hello World！<font>')

    def onClickedPrintHtmlButton(self):
        print(self.textEdit.toHtml())
    
    def onClickedPrintTextButton(self):
        print(self.textEdit.toPlainText())

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QTextEditDemo()
    mainWindow.show()
    sys.exit(app.exec_())