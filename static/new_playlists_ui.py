# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newPlaylist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 375)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-3, -5, 401, 381))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 12; padding: .5em")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 160, 371, 151))
        self.listWidget.setStyleSheet("font-size: 19px; background-color: grey; border: 2px solid black")
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 341, 16))
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: green; color: white; border-radius: 10")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.background.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "Создать новый плейлист"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Название плейлиста"))
        self.label_2.setText(_translate("Form", "Кликните на трек, чтобы добавить в плейлист"))
        self.pushButton.setText(_translate("Form", "Сохранить"))
