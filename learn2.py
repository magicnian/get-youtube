#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
