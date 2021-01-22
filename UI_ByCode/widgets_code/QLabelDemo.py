"""
    @Widget
        QLable
    @Function
        setAlignment() --设置文本对齐模式
        setIndent() --设置文本缩进
        text()  --获取文本内容
        setBuddy() --设置伙伴关系
        setText() --设置文本内容
        selectedText() --返回所选择地字符
        setWordWrop() --设置是否允许换行
    @Signal
        linkHovered() --鼠标滑过时触发
        linkClicked() --鼠标单击中时触发
"""
import sys
from PyQt5.QtWidgets import QVBoxLayout,QApplication,QLabel,QWidget,QToolTip
from PyQt5.QtGui import QPalette,QFont,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    """
        QLabel Demo Class
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
            initUI
        """
        self.setWindowTitle("QlabelDemo")
        self.setGeometry(200,200,400,400)
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        label1.setText("<font color=yellow>It is a lable.</font>")
        label1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)#设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        QToolTip.setFont(QFont("SansSerif",12))
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("icon/test.ico"))
        label4.setText("<a href='www.baidu.com'>百度</a>")
        #如果设为True，访问外部网页，设为False，调用槽
        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")

        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        self.setLayout(layout)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

    def linkHovered(self):
        """
            当鼠标滑过时，触发事件
        """
        print("当鼠标滑过Label2时，触发事件")

    def linkClicked(self):
        """
            当鼠标单击时，触发事件
        """
        print("当鼠标单击label4时，触发事件")

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWindow=QLabelDemo()
    mainWindow.show()
    sys.exit(app.exec_())
