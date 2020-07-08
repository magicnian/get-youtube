#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication)
import youtube_dl
from youtube_dl import YoutubeDL


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.video_url_title = QLabel('视频链接地址')
        self.video_url = QLineEdit()
        self.save_path_title = QLabel('保存路径')
        self.save_path = QLineEdit()
        self.btn = QPushButton('提交', self)

        self.btn.clicked.connect(self.listen)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.video_url_title, 1, 0)
        grid.addWidget(self.video_url, 1, 1)
        grid.addWidget(self.save_path_title, 2, 0)
        grid.addWidget(self.save_path, 2, 1)

        grid.addWidget(self.btn, 3, 0)

        self.setLayout(grid)

        self.setGeometry(200, 200, 600, 500)
        self.show()

    def listen(self):
        video_url = self.video_url.text()
        print('video_url:', video_url)
        save_path = self.save_path.text()
        print('save_path:', save_path)

        """下载"""
        params = {
            "format": "bestvideo+bestaudio"
        }
        yd = YoutubeDL(params)
        yd.download(['https://www.youtube.com/watch?v=ABkINFNlq8Y'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
