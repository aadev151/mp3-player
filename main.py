"""
This is the main screen of the app.
Here:
- the library of the music is stored;
- the opportunity to upload a new track is given;
- the opportunity to upload/download the library is given;
- the playlists can be created and viewed.
"""


import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import sqlite3

from play import PlayMusic
from share import ShareScreen
from new_playlist import NewPlaylist
from my_playlists import MyPlaylists

from static import main_ui


class MainScreen(QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.statusBar().hide()
        self.background.setPixmap(QPixmap('static/bg.jpg').scaled(
            self.background.width(), self.background.height()))
        with open('static/name.txt') as name_file:
            name = name_file.read()
        self.greeting_label.setText(f'Здравствуйте, {name}!')
        self.new_mp3_button.clicked.connect(self.choose_file)
        self.to_friends.clicked.connect(self.share_screen)
        self.export_button.clicked.connect(self.export_data)
        self.load_button.clicked.connect(self.load_data)
        self.my_playlists.clicked.connect(self.show_playlists)
        self.new_playlist.clicked.connect(self.create_playlist)
        self.update_data()

    def update_data(self):
        """The function updates the QListWidget,
         which stores all uploaded tracks"""

        self.listWidget.clear()
        connection = sqlite3.connect('static/db.db')
        all_music = connection.cursor().execute(
            'SELECT * FROM music').fetchall()
        connection.close()
        all_music = [el[1] + f' \t[({el[2]}])' for el in all_music]
        self.listWidget.addItems(all_music)
        self.listWidget.itemClicked.connect(self.open_player)

    def open_player(self, item):
        """The function opens player"""

        # Check whether a file still exists
        if os.path.isfile(item.text().split('[(')[-1][:-2]):
            self.player = PlayMusic(item.text().split('[(')[-1][:-2])
            self.player.show()
        else:
            QMessageBox.critical(self, 'Файл был удален', 'Файл был удален')
            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE from music WHERE dir = "
                f"'{item.text().split('[(')[-1][:-2]}'").fetchall()
            connection.commit()
            connection.close()
            self.update_data()

    def choose_file(self):
        """The function chooses a new MP3 track"""

        filename = QFileDialog.getOpenFileName(self, 'Выбрать песню',
                                               'MP3 файл (*.mp3)')[0]
        if filename:
            if not filename.endswith('.mp3'):
                QMessageBox.critical(self, 'Выберите песню!',
                                     'Только mp3-файлы допускаются!')
                return

            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor()
            name = filename.split('/')[-1].split('.')[0]
            try:
                cursor.execute(f"INSERT INTO music(name, dir) "
                               f"VALUES('{name}', '{filename}')").fetchall()
                self.player = PlayMusic(filename)
                self.player.show()
                connection.commit()
                self.listWidget.addItem(name + f' \t[({filename}])')
            except sqlite3.IntegrityError:
                QMessageBox.information(self,
                                        'Файл уже присутствует в медиатеке',
                                        'Файл уже присутствует в медиатеке')
            connection.close()

    def share_screen(self):
        """The function opens a share screen"""

        self.share = ShareScreen()
        self.share.show()

    def export_data(self):
        """The function exports data about the stored music
        to os.getcwd() + /data.moob

        Example of content of data.moob:
        Mask Off 	[(/Users/user/Downloads/Mask Off.mp3])
        Life is Good    [(/Users/user/Downloads/LG.mp3])
        """
        
        with open('data.moob', 'w') as export_file:
            export_file.write(
                '\n'.join([self.listWidget.item(x).text()
                           for x in range(self.listWidget.count())])
            )
        QMessageBox.information(self,
                                'Экспорт данных завершен',
                                'Файл с данными Вашей медиатеки '
                                'присутсвует по адресу: '
                                f'{os.getcwd() + "/data.moob"}')

    def load_data(self):
        """The function loads data about music in the format
        of data.moob, which is described in
        export_data()"""
        
        filename = QFileDialog.getOpenFileName(self,
                                               'Загрузить медиатеку',
                                               'Медиатека (*.moob)')[0]
        if filename:
            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE from music").fetchall()
            cursor.execute(
                f"DELETE from playlists").fetchall()
            connection.commit()
            with open(filename) as input_file:
                for line in input_file:
                    file_info = line.split('\t')
                    cursor.execute(
                        f"INSERT INTO music(name, dir) "
                        f"VALUES('{file_info[0]}', "
                        f"'{file_info[1].strip()[2:-2]}')").fetchall()
                    connection.commit()
            connection.close()

            self.update_data()
            QMessageBox.information(self, 'Успешно!', 'Успешно!')

    def create_playlist(self):
        """The function creates a new playlist"""
        
        self.create_playlist_screen = NewPlaylist()
        self.create_playlist_screen.show()

    def show_playlists(self):
        """The function shows existing playlists"""
        
        self.show_playlists_screen = MyPlaylists()
        self.show_playlists_screen.show()
