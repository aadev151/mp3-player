import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import sqlite3

from static import main_ui
from play import PlayMusic
from share import ShareScreen


class MainScreen(QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        with open('static/name.txt') as name_file:
            name = name_file.read()
        self.greeting_label.setText(f'Здравствуйте, {name}!')
        self.new_mp3_button.clicked.connect(self.choose_file)
        self.to_friends.clicked.connect(self.share_screen)
        self.already.hide()
        self.update_data()

    def update_data(self):
        self.listWidget.clear()
        connection = sqlite3.connect('static/db.db')
        all_music = connection.cursor().execute('SELECT * FROM music').fetchall()
        connection.close()
        all_music = [el[1] + f' \t[({el[2]}])' for el in all_music]
        self.listWidget.addItems(all_music)
        self.listWidget.itemClicked.connect(self.open_player)

    def open_player(self, item):
        if os.path.isfile(item.text().split('[(')[-1][:-2]):
            self.player = PlayMusic(item.text().split('[(')[-1][:-2], item.text().split('[(')[0])
            self.player.show()
        else:
            QMessageBox.critical(self, 'Файл был удален', 'Файл был удален')
            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor().execute(
                f"DELETE from music WHERE dir = '{item.text().split('[(')[-1][:-2]}'").fetchall()
            connection.commit()
            connection.close()
            self.update_data()

    def choose_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Выбрать песню', 'MP3 файл (*.mp3)')[0]
        if filename:
            connection = sqlite3.connect('static/db.db')
            cursor = connection.cursor()
            name = filename.split('/')[-1].split('.')[0]
            try:
                cursor.execute(f"INSERT INTO music(name, dir) VALUES('{name}', '{filename}')").fetchall()
                self.player = PlayMusic(filename, name)
                self.player.show()
                connection.commit()
                self.listWidget.addItem(name + f' \t[({filename}])')
                self.already.hide()
            except sqlite3.IntegrityError:
                self.already.show()
            connection.close()

    def share_screen(self):
        self.share = ShareScreen()
        self.share.show()
