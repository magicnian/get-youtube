#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        """调用父对象QWidget的构造器，使得Example对象可以访问父对象的属性"""
        super().__init__()
        """在Example对象的构造器中调用initUI方法，初始化qt界面"""
        self.initUI()

    def initUI(self):
        """以下三个方法都继承自QWidget类
            setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小
            参数分别代表屏幕坐标的x、y和窗口大小的宽、高
            也就是说这个方法是resize()和move()的合体
        """
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Example")
        """给窗口添加一个图标"""
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
