"""
This is a start screen of the app.
If the user is authenticated, it will redirect her to the main screen.
Otherwise, it will ask her to input her name.
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtGui import QPixmap

from main import MainScreen
from static import start_ui


class StartScreen(QMainWindow, start_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moob - качай музыку из телеги (нет)')
        self.background.setPixmap(QPixmap('static/bg.jpg').scaled(
            self.background.width(), self.background.height()))
        self.pushButton.clicked.connect(self.enter_name)

    def enter_name(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Как Вас зовут?")
        if ok_pressed:
            with open('static/name.txt', 'w') as name_file:
                name_file.write(name)
            self.open_main_screen()

    def open_main_screen(self):
        self.main_window = MainScreen()
        self.main_window.show()
        self.destroy()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open('static/name.txt') as name_file:
        if name_file.read():
            main_screen = MainScreen()
            main_screen.show()
        else:
            start_screen = StartScreen()
            start_screen.show()

    sys.exit(app.exec())
