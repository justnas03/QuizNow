#All Screen Index 
screen = {'Login':0,'Register':1}
class Login_Connect:
    def __init__(self,cur_win):
        self.cur_win = cur_win
    
    def openRegisterForm(self):     
        w = self.cur_win.stwidget.widget(screen['Register']).width()
        h = self.cur_win.stwidget.widget(screen['Register']).height()
        self.cur_win.stwidget.setCurrentIndex(screen['Register'])
        self.cur_win.stwidget.resize(w,h)

    def LoginConfirmation(self):
        cur = self.cur_win.db.connection.cursor()
        username = self.cur_win.ui.username_textfield.text()
        password = self.cur_win.ui.pwd_textfield.text()
        sql = "select password from user where username='{0}'".format(username)
        result = cur.execute(sql).fetchone()
        if result!=None:
            if len(result)!=0:
                if result[0] == password:
                    self.cur_win.stwidget.setCurrentIndex(screen['Register'])
                else:
                    self.cur_win.ui.warning_label.setText('Wrong password!')
                    self.cur_win.ui.warning_label.show()
        else: 
            self.cur_win.ui.warning_label.setText('Wrong username!')
            self.cur_win.ui.warning_label.show()
            
    