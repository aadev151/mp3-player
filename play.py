from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtMultimedia, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import eyed3
from mutagen.mp3 import MP3, HeaderNotFoundError

from static import play_ui


class PlayMusic(QWidget, play_ui.Ui_Form):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.setupUi(self)
        self.initUI(filename)
        self.play(filename)

    def initUI(self, filename):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.background.setPixmap(QPixmap('static/bg.jpg').scaled(
            self.background.width(), self.background.height()))
        try:
            file = eyed3.load(filename)
            self.name.setText(file.tag.title)
            self.artist.setText(file.tag.artist)
        except AttributeError:
            self.name.setText(filename.split('/')[-1][:-5])
        self.action_button.clicked.connect(self.pause_play)
        try:
            afile = MP3(filename)
            try:
                with open('static/cover.png', 'wb') as fff:
                    fff.write(afile.tags.getall('APIC')[0].data)
                self.cover.setPixmap(QPixmap('static/cover.png').scaled(
                    self.cover.width(), self.cover.height()))
            except IndexError:
                self.cover.setPixmap(QPixmap('static/music.png'))
        except HeaderNotFoundError:
            self.cover.setPixmap(QPixmap('static/music.png'))

    def play(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def pause_play(self):
        if self.action_button.text() == '| |':
            self.action_button.setText('►')
            self.player.pause()
        else:
            self.action_button.setText('| |')
            self.player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.pause_play()

    def closeEvent(self, event):
        self.player.pause()
        event.accept()
