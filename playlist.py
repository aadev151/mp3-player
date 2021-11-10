"""
The window shows a playlist.
The music is stored on a QListWidget, similarly to
one on the Main screen
"""


import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import sqlite3

from play import PlayMusic
from static import playlist_ui


class Playlist(QMainWindow, playlist_ui.Ui_Form):

    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.statusBar().hide()
        self.background.setPixmap(QPixmap('static/bg.jpg').scaled(
            self.background.width(), self.background.height()))
        self.name_label.setText(self.name)
        self.update_data()

    def update_data(self):
        """The function updates the QListWidget,
                 which stores all uploaded tracks"""
        
        self.listWidget.clear()
        connection = sqlite3.connect('static/db.db')
        all_ids = connection.cursor().execute('SELECT content FROM playlists '
                                              'WHERE '
                                              f'name = \'{self.name}\'') \
            .fetchone()[0].split(';')[:-1]

        all_music = []
        for el in all_ids:
            track = connection.cursor() \
                .execute('SELECT name, dir FROM music '
                         'WHERE '
                         f'id = \'{el}\'').fetchone()
            if track:
                all_music.append(track[:2])

        connection.close()
        all_music = [el[0] + f' \t[({el[1]}])' for el in all_music]

        self.listWidget.addItems(all_music)
        self.listWidget.itemClicked.connect(self.open_player)

    def open_player(self, item):
        # Check whether a file still exists
        # and deleting it from the database if not
        if os.path.isfile(item.text().split('[(')[-1][:-2]):
            self.player = PlayMusic(item.text().split('[(')[-1][:-2])
            self.player.show()
        else:
            QMessageBox.critical(self, 'Файл был удален', 'Файл был удален')
            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM music "
                f"WHERE dir = '{item.text().split('[(')[-1][:-2]}'")\
                .fetchall()
            connection.commit()
            connection.close()
            self.update_data()
