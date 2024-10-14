# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(240, 10, 601, 481))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: rgb(0, 255, 255);\n"
"	color: black;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 105, 58))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 9pt \"Times New Roman\";\n"
"font: 600 14pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(240, 490, 611, 61))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 255, 255); \n"
"    color: black;\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton_3.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 255, 255); \n"
"    color: black;\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.pushButton_4.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Times New Roman\";\n"
"font: 600 14pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 70, 120, 92))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Times New Roman\";\n"
"font: 600 14pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 9pt \"Times New Roman\";\n"
"font: 600 14pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Times New Roman\";\n"
"font: 600 14pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_4)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 490, 98, 56))
        self.verticalLayout_3 = QVBoxLayout(self.widget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 255, 255); \n"
"    color: black;\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"	font-weight:bold;\n"
"	font-size: 12px;\n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.widget3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 255, 255); \n"
"    color: black;\n"
"    border:none;\n"
"	border-radius: 3px;\n"
"	font-weight:bold;\n"
"	font-size: 12px;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 928, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 \u0110\u1ec1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u1ec1n \u0111\u1ec1 thi", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee7 \u0111\u1ec1", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T\u00e1c gi\u1ea3", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 c\u00e2u h\u1ecfi", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Thi", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, {user}", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1o \u0111\u1ec1 thi", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ec1 thi c\u1ee7a t\u00f4i", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111\u1ec1 \u0111\u00e3 thi:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111\u1ec1 \u0111\u00e3 t\u1ea1o: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed5i M\u1eadt Kh\u1ea9u", None))
    # retranslateUi

