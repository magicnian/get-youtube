#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QProgressBar)
import youtube_dl
from youtube_dl import YoutubeDL


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.video_url_title = QLabel('视频链接地址')
        self.video_url = QTextEdit()
        self.save_path_title = QLabel('保存路径')
        self.save_path = QLineEdit()
        self.btn = QPushButton('提交', self)
        self.progress = QProgressBar(self)
        self.info = QLabel('loading...', self)

        self.btn.clicked.connect(self.listen)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.info, 1, 0)
        grid.addWidget(self.progress, 2, 0)
        grid.addWidget(self.video_url_title, 3, 0)
        grid.addWidget(self.video_url, 3, 1)
        grid.addWidget(self.save_path_title, 4, 0)
        grid.addWidget(self.save_path, 4, 1)

        grid.addWidget(self.btn, 5, 0)

        self.setLayout(grid)

        self.setGeometry(200, 200, 600, 500)
        self.show()

    def listen(self):
        video_url = self.video_url.toPlainText()
        print('video_url:', video_url)
        save_path = self.save_path.text()
        print('save_path:', save_path)

        """下载"""
        params = {
            "format": "bestvideo+bestaudio",
            "outtmpl": save_path + os.sep + '%(title)s.%(ext)s',
            "progress_hooks": [self.my_hook]
        }

        urls = []
        for url in video_url.split('\n'):
            urls.append(url)

        yd = YoutubeDL(params)
        yd.download(urls)

    def my_hook(self, d):
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Done downloading {}".format(file_tuple[1]))
        if d['status'] == 'downloading':
            print(d['filename'], d['_percent_str'], d['_eta_str'])
            self.info.setText(d['_eta_str'])
            self.progress.setValue(float(d['_percent_str'].replace('%', '')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
