# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from database import QuizNowDB
from UI.ui_login import Ui_MainWindow 
from UI.ui_register import Ui_Form
from UI.ui_homepage import Ui_MainWindow as homepage
from Connect.Login_connect import Login_Connect 

class Login(QMainWindow):
    def __init__(self, stwidget, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.warning_label.hide()
        #connect database 
        self.db = db

        #set Stacked Widget
        self.stwidget = stwidget
        self.stwidget.addWidget(self)
        #Connect
        self.confun = Login_Connect(self)
        self.ui.signup_but.clicked.connect(self.confun.openRegisterForm)
        self.ui.login_button.clicked.connect(self.confun.LoginConfirmation)

class Register(QWidget):
    def __init__(self, stwidget, db,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #connect database 
        self.db = db
        
        #set Stacked Widget
        self.stwidget = stwidget
        self.stwidget.addWidget(self)
class Homepage(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = homepage()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stwidget = QStackedWidget()
    db = QuizNowDB()
    login = Login(stwidget,db)
    register = Register(stwidget,db)
    db.connect()

    stwidget.addWidget(login)
    stwidget.addWidget(register)

    stwidget.setCurrentWidget(login)
    stwidget.resize(login.width(),login.height())
    
    stwidget.setWindowTitle('QuizNow')
    stwidget.show()



    homepage_window = Homepage()
    homepage_window.show()
    
    sys.exit(app.exec())
