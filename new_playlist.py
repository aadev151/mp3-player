from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import sqlite3

from static import new_playlists_ui


class NewPlaylist(QMainWindow, new_playlists_ui.Ui_Form):

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
        self.pushButton.clicked.connect(self.create_playlist)
        self.update_data()

    def update_data(self):
        self.listWidget.clear()
        connection = sqlite3.connect('static/db.db')
        all_music = connection.cursor().execute('SELECT * FROM music')\
            .fetchall()
        connection.close()
        all_music = [el[1] + f' \t[({el[2]}])' for el in all_music]
        self.listWidget.addItems(all_music)
        self.listWidget.itemClicked.connect(self.add_song)

    def add_song(self, item):
        connection = sqlite3.connect('static/db.db')
        track_id = connection.cursor().execute(
            f"SELECT id FROM music WHERE dir = "
            f"'{item.text().split('[(')[-1][:-2]}'").fetchone()[0]
        connection.commit()
        connection.close()
        self.tracks += str(track_id) + ';'
        QMessageBox.information(self,
                                'Успешно', 'Трек успешно добавлен в плейлист')

    def create_playlist(self):
        if not self.tracks:
            QMessageBox.information(self,
                                    'Добавьте музыку',
                                    'Сначала добавьте музыку')
            return

        name = self.lineEdit.text()
        if not name:
            QMessageBox.information(self,
                                    'Дайте название плейлисту',
                                    'Дайте название плейлисту')
            return

        try:
            connection = sqlite3.connect('static/db.db')
            connection.cursor().execute(
                f"INSERT INTO playlists(name, content) VALUES("
                f"'{name}', '{self.tracks}')").fetchall()
            connection.commit()
            connection.close()
            QMessageBox.information(self,
                                    'Плейлист создан',
                                    f'Плейлист "{name}" успешно создан!')
            self.destroy()
        except sqlite3.IntegrityError:
            QMessageBox.critical(self,
                                 f'Плейлист с названием "{name}" '
                                 f'уже существует',
                                 f'Плейлист с названием "{name}" '
                                 f'уже существует')

    def closeEvent(self, event):
        if self.tracks:
            if QMessageBox.question(self,
                                    'Изменения не сохранены',
                                    'Если Вы закроете окно, '
                                    'плейлист не сохранится. '
                                    'Вы уверены, что хотите закрыть окно?',
                                    QMessageBox.Yes | QMessageBox.No) \
                    == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
