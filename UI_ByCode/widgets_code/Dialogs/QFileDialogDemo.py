"""QFileDialogDemo
文件对话框
打开一个图形和文本文件并显示
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QFileDialogDemo(QWidget):

    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.__layout = QVBoxLayout(self)
        self.__imageLabel = QLabel()
        self.__textEdit = QTextEdit()
        self.__imageButton = QPushButton("打开图像文件")
        self.__imageButton.clicked.connect(self.onClickedImageButton)
        self.__textButton = QPushButton("打开文本文件")
        self.__textButton.clicked.connect(self.onClickedTextButton)
        self.__layout.addWidget(self.__imageButton)
        self.__layout.addWidget(self.__imageLabel)
        self.__layout.addWidget(self.__textButton)
        self.__layout.addWidget(self.__textEdit)
        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("QFileDialogDemo")

    def onClickedImageButton(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "打开图像", '.', "图像文件(*.jpg *.png)")
        self.__imageLabel.setPixmap(QPixmap(filename))

    def onClickedTextButton(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()

            with open(filenames[0], 'r',)as f:
                self.__textEdit.setText(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QFileDialogDemo()
    mainWindow.show()
    sys.exit(app.exec_())
