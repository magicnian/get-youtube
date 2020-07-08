#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication

"""通过按钮关闭窗口
    QPushButton(string text, QWidget parent = None)
    text参数是想要显示的按钮名称，parent参数是放在按钮上的组件，在我们的例子里，这个参数是QWidget
    应用中的组件都是一层一层（继承而来的？）的，在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口
"""


class OtherExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """创建一个提示框，使用SansSerif字体，字号10px"""
        QToolTip.setFont(QFont('SansSerif', 10))

        """设置提示内容，可以使用富文本格式"""
        self.setToolTip('This is a <b>QWidget</b> widget')

        """创建一个按钮，并且为按钮添加一个提示框"""
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        """调整按钮大小，并让按钮在屏幕上显示出来
            sizeHint()方法提供了一个默认的按钮大小
        """
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


class Example(QWidget):

    def __init__(self, otherExample):
        super().__init__()
        self.otherExample = otherExample
        self.initUI(self.otherExample)

    def initUI(self, otherExample: OtherExample):
        """
        创建一个继承自QPushButton的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自Qwidget的Example类
        """
        qbtn = QPushButton('Quit', self)

        otherExample.setWindowIcon(QIcon('web.png'))

        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ot = OtherExample()
    ex = Example(ot)
    sys.exit(app.exec_())
