# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(471, 547)
        self.logo = QLabel(Form)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(70, 20, 331, 201))
        self.logo.setPixmap(QPixmap(u"logo.jpg"))
        self.logo.setScaledContents(True)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 270, 421, 214))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.fullNameLabel = QLabel(self.formLayoutWidget)
        self.fullNameLabel.setObjectName(u"fullNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.fullNameLabel)

        self.fullNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.fullNameLineEdit.setObjectName(u"fullNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.fullNameLineEdit)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.emailLineEdit)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.passwordLineEdit)

        self.confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.confirmPasswordLabel)

        self.confirmPasswordLineEdit = QLineEdit(self.formLayoutWidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.confirmPasswordLineEdit)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 300 18pt \"Segoe UI Light\";\n"
"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_7)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 500, 83, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.fullNameLabel.setText(QCoreApplication.translate("Form", u"Full Name:", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.confirmPasswordLabel.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Register New Account", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Register", None))
    # retranslateUi

