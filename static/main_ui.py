# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, 0, 951, 801))
        self.background.setObjectName("background")
        self.greeting_label = QtWidgets.QLabel(self.centralwidget)
        self.greeting_label.setGeometry(QtCore.QRect(10, 50, 791, 51))
        font = QtGui.QFont()
        font.setFamily("helvetica")
        font.setPointSize(29)
        font.setItalic(True)
        self.greeting_label.setFont(font)
        self.greeting_label.setStyleSheet("font-family: helvetica; padding: .4em; color: white")
        self.greeting_label.setAlignment(QtCore.Qt.AlignCenter)
        self.greeting_label.setObjectName("greeting_label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 310, 771, 401))
        self.listWidget.setStyleSheet("font-size: 19px; background-color: grey; border: 2px solid black")
        self.listWidget.setObjectName("listWidget")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(290, 730, 231, 26))
        self.export_button.setStyleSheet("background-color: green; color: white")
        self.export_button.setObjectName("export_button")
        self.new_mp3_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_mp3_button.setGeometry(QtCore.QRect(30, 160, 231, 41))
        self.new_mp3_button.setStyleSheet("background-color: green; color: white; border-radius: 10")
        self.new_mp3_button.setObjectName("new_mp3_button")
        self.my_playlists = QtWidgets.QPushButton(self.centralwidget)
        self.my_playlists.setGeometry(QtCore.QRect(30, 230, 231, 41))
        self.my_playlists.setStyleSheet("background-color: green; color: white; border-radius: 10")
        self.my_playlists.setObjectName("my_playlists")
        self.new_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.new_playlist.setGeometry(QtCore.QRect(280, 230, 231, 41))
        self.new_playlist.setStyleSheet("background-color: green; color: white; border-radius: 10")
        self.new_playlist.setObjectName("new_playlist")
        self.to_friends = QtWidgets.QPushButton(self.centralwidget)
        self.to_friends.setGeometry(QtCore.QRect(560, 730, 231, 26))
        self.to_friends.setStyleSheet("background-color: green; color: white")
        self.to_friends.setObjectName("to_friends")
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(20, 730, 231, 26))
        self.load_button.setStyleSheet("background-color: green; color: white")
        self.load_button.setObjectName("load_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 341, 16))
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.background.setText(_translate("MainWindow", "TextLabel"))
        self.greeting_label.setText(_translate("MainWindow", "TextLabel"))
        self.export_button.setText(_translate("MainWindow", "Экспортировать медиатеку"))
        self.new_mp3_button.setText(_translate("MainWindow", "Загрузить новый трек"))
        self.my_playlists.setText(_translate("MainWindow", "Посмотреть плейлисты"))
        self.new_playlist.setText(_translate("MainWindow", "Создать новый плейлист"))
        self.to_friends.setText(_translate("MainWindow", "Расскажите о нас друзьям"))
        self.load_button.setText(_translate("MainWindow", "Загрузить медиатеку"))
        self.label_2.setText(_translate("MainWindow", "Кликните на трек, чтобы воспроизвести"))
