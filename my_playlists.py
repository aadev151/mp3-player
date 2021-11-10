"""
The widget that shows a collection of
a user's playlists in a QListWidget
"""


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
import sqlite3

from playlist import Playlist
from static import my_playlists_ui


class MyPlaylists(QMainWindow, my_playlists_ui.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tracks = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.statusBar().hide()
        self.background.setPixmap(QPixmap('static/bg.jpg').scaled(
            self.background.width(), self.background.height()))
        self.update_data()

    def update_data(self):
        """The function updates the QListWidget,
                 which stores all uploaded tracks"""

        self.listWidget.clear()
        connection = sqlite3.connect('static/db.db')
        all_music = connection.cursor().execute('SELECT name FROM playlists')\
            .fetchall()
        connection.close()
        all_music = [el[0] for el in all_music]
        self.listWidget.addItems(all_music)
        self.listWidget.itemClicked.connect(self.show_playlist)

    def show_playlist(self, item):
        self.playlist = Playlist(item.text())
        self.playlist.show()
