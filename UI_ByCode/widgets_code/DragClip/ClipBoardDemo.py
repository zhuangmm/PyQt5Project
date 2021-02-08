"""ClipBoardDemo
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ClipBoardDemo(QWidget):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.setWindowTitle("ClipBoardDemo")
        layout = QGridLayout(self)
        textCopyButton = QPushButton("拷贝文本")
        textPasteButton = QPushButton("粘贴文本")
        htmlCopyButton = QPushButton("拷贝HTML")
        htmlPasteButton = QPushButton("粘贴HTML")
        imageCopyButton = QPushButton("拷贝图像")
        imagePasteButton = QPushButton("粘贴图像")
        self.textLabel = QLabel("测试文本")
        self.imageLabel = QLabel()
        textCopyButton.clicked.connect(self.onTextCopyButtonClicked)
        textPasteButton.clicked.connect(self.onTextPasteButtonClicked)
        htmlCopyButton.clicked.connect(self.onHtmlCopyButtonClicked)
        htmlPasteButton.clicked.connect(self.onHtmlPasteButtonClicked)
        imageCopyButton.clicked.connect(self.onImageCopyButtonClicked)
        imagePasteButton.clicked.connect(self.onImagePasteButtonClicked)

        self.imageLabel.setPixmap(QPixmap('../../../icon/test.ico'))
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imagePasteButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

    def onTextCopyButtonClicked(self):
        clipBoard = QApplication.clipboard()
        clipBoard.setText("Hello,world!")

    def onTextPasteButtonClicked(self):
        clipBoard = QApplication.clipboard()
        self.textLabel.setText(clipBoard.text())

    def onHtmlCopyButtonClicked(self):
        clipBoard = QApplication.clipboard()
        mimeDate = QMimeData()
        mimeDate.setHtml('<b>It is <font color=red>red</font></b>')
        clipBoard.setMimeData(mimeDate)

    def onHtmlPasteButtonClicked(self):
        clipBoard = QApplication.clipboard()
        mimeDate = clipBoard.mimeData()
        if mimeDate.hasHtml():
            self.textLabel.setText(mimeDate.html())

    def onImageCopyButtonClicked(self):
        clipBoard = QApplication.clipboard()
        pixMap = QPixmap("../../../icon/test.ico")
        clipBoard.setPixmap(pixMap)

    def onImagePasteButtonClicked(self):
        clipBoard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipBoard.pixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ClipBoardDemo()
    mainWindow.show()
    sys.exit(app.exec_())
