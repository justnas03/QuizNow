# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 250, 351, 236))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pwd_username = QLabel(self.verticalLayoutWidget)
        self.pwd_username.setObjectName(u"pwd_username")
        font = QFont()
        font.setPointSize(20)
        self.pwd_username.setFont(font)
        self.pwd_username.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.pwd_username)

        self.usernam_textfield = QLineEdit(self.verticalLayoutWidget)
        self.usernam_textfield.setObjectName(u"usernam_textfield")

        self.verticalLayout_2.addWidget(self.usernam_textfield)

        self.pwd_label = QLabel(self.verticalLayoutWidget)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setFont(font)
        self.pwd_label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.pwd_label)

        self.pwd_textfield = QLineEdit(self.verticalLayoutWidget)
        self.pwd_textfield.setObjectName(u"pwd_textfield")

        self.verticalLayout_2.addWidget(self.pwd_textfield)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.login_button.setFont(font1)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_button.setAutoFillBackground(False)
        self.login_button.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.login_button.setCheckable(False)

        self.verticalLayout_2.addWidget(self.login_button)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 371, 221))
        self.logo.setPixmap(QPixmap(u"logo.jpg"))
        self.logo.setScaledContents(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 490, 101, 31))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"font: 700 italic 14pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"color: rgb(85, 85, 255);\n"
"border: None;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 388, 25))
        self.menuLogin = QMenu(self.menubar)
        self.menuLogin.setObjectName(u"menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pwd_username.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.pwd_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.logo.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.menuLogin.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

