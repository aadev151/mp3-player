from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from static import play_ui
import sqlite3


class PlayMusic(QWidget, play_ui.Ui_Form):

    def __init__(self, filename, name):
        super().__init__()
        self.filename = filename
        self.setupUi(self)
        self.initUI(name)
        self.play(filename)

    def initUI(self, name):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.cover.setPixmap(QPixmap('static/music.png'))
        self.name.setText(name)
        self.action_button.clicked.connect(self.pause_play)

    def play(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def pause_play(self):
        if self.action_button.text() == '||':
            self.action_button.setText('►')
            self.player.pause()
        else:
            self.action_button.setText('||')
            self.player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.pause_play()

    def closeEvent(self, event):
        self.player.pause()
        event.accept()
