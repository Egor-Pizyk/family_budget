import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

from check_db import *
from v5.design import login_user_ui
from v5.logic import main_window


class LoginUser(QtWidgets.QMainWindow, login_user_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # strat my func
        self.user_login_btn.clicked.connect(self.login)
        self.user_register_btn.clicked.connect(self.reg)
        self.base_line_edit = [self.user_login_input, self.user_password_input]

        self.msg = QtWidgets.QMessageBox()

        # func for login\reg
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    # decorator vor input field validation
    def check_input(func):
        def wraper(self):
            self.msg.setWindowTitle("Ошибка")
            for input_param in self.base_line_edit:
                if len(input_param.text()) == 0:
                    self.msg.setText("Поле логина или пароля не заполнено!")
                    self.msg.exec_()
                    self.user_login_input.clear()
                    self.user_password_input.clear()
                    return

            func(self)

        return wraper

    # get signal result
    def signal_handler(self, value):
        if value:
            self.window = main_window.MainMenyUser()
            self.window.set_hello(value)
            self.window.show()
            self.close()

        self.user_login_input.clear()
        self.user_password_input.clear()

    # get input data from input field
    @check_input
    def login(self):
        user_login = self.user_login_input.text()
        user_password = self.user_password_input.text()
        self.check_db.thr_login(user_login, user_password)

    @check_input
    def reg(self):
        user_login = self.user_login_input.text()
        user_password = self.user_password_input.text()
        self.check_db.thr_reg(user_login, user_password)


# def main():
#     app = QApplication(sys.argv)
#     window = LoginUser()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
