#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.qle = QLineEdit(self)
        self.btn = QPushButton('Button', self)

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

        self.qle.move(60, 100)

        self.btn.clicked.connect(self.submit)

        self.setGeometry(200, 200, 500, 400)
        self.setWindowTitle('QLineEdit')
        self.show()

    def submit(self):
        print(self.qle.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
