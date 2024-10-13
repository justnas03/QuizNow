# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 371, 221))
        self.logo.setPixmap(QPixmap(u"logo.jpg"))
        self.logo.setScaledContents(True)
        self.signup_but = QPushButton(self.centralwidget)
        self.signup_but.setObjectName(u"signup_but")
        self.signup_but.setGeometry(QRect(150, 490, 101, 31))
        self.signup_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_but.setStyleSheet(u"font: 700 italic 14pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"color: rgb(85, 85, 255);\n"
"border: None;\n"
"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 251, 341, 241))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pwd_username = QLabel(self.widget)
        self.pwd_username.setObjectName(u"pwd_username")
        font = QFont()
        font.setPointSize(20)
        self.pwd_username.setFont(font)
        self.pwd_username.setScaledContents(True)

        self.verticalLayout.addWidget(self.pwd_username)

        self.username_textfield = QLineEdit(self.widget)
        self.username_textfield.setObjectName(u"username_textfield")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_textfield.sizePolicy().hasHeightForWidth())
        self.username_textfield.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.username_textfield)

        self.pwd_label = QLabel(self.widget)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setFont(font)
        self.pwd_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.pwd_label)

        self.pwd_textfield = QLineEdit(self.widget)
        self.pwd_textfield.setObjectName(u"pwd_textfield")
        self.pwd_textfield.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.pwd_textfield)

        self.warning_label = QLabel(self.widget)
        self.warning_label.setObjectName(u"warning_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.warning_label.sizePolicy().hasHeightForWidth())
        self.warning_label.setSizePolicy(sizePolicy1)
        self.warning_label.setMaximumSize(QSize(339, 16))
        self.warning_label.setStyleSheet(u"color: red")
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.warning_label)

        self.login_button = QPushButton(self.widget)
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

        self.verticalLayout.addWidget(self.login_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 388, 21))
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
        self.logo.setText("")
        self.signup_but.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.pwd_username.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.pwd_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.warning_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.menuLogin.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

