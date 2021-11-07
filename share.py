from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QUrl, QDesktopServices
from PyQt5 import uic

from static import share_ui
import sqlite3
import datetime


class ShareScreen(QWidget, share_ui.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Расскажите о Moob\'е друзьям')
        self.pushButton.clicked.connect(self.open_vk)
        self.pushButton_2.clicked.connect(self.open_reddit)
        self.pushButton_3.clicked.connect(self.open_twitter)

    def open_vk(self):
        QDesktopServices.openUrl(QUrl(
            'https://vk.com/share.php?comment='
            f'Скачайте%20MP3-плеер%20MOOB%0A%0A{self.textEdit.toPlainText()}'
            f'&url=https://aadev151.github.io/moob'))
        connection = sqlite3.connect('static/db.db')
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO share_log(type, date) "
                       f"VALUES((SELECT id FROM share_types WHERE type = 'vk'), "
                       f"'{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}')").fetchall()
        connection.commit()
        connection.close()

    def open_reddit(self):
        QDesktopServices.openUrl(QUrl(
            'https://www.reddit.com/submit?title='
            f'Скачайте%20MP3-плеер%20MOOB%0A%0A{self.textEdit.toPlainText()}'
            f'&url=https://aadev151.github.io/moob'))

    def open_twitter(self):
        QDesktopServices.openUrl(QUrl(
            'https://twitter.com/intent/tweet?text='
            f'Скачайте%20MP3-плеер%20MOOB%0A%0A{self.textEdit.toPlainText()}'
            f'%0A%0A%0Ahttps://aadev151.github.io/moob'))
