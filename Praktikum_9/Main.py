from PyQt5 import QtWidgets
import sys

from ui.form_login import Ui_MainWindow as LoginUI
from controller.dashboard_admin import HalamanAdmin
from controller.dashboard_kasir import HalamanKasir
from model.User import User

class HalamanLogin(QtWidgets.QMainWindow, LoginUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.keluar)

    def keluar(self):
        QtWidgets.QApplication.quit()

class AppController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.current_user = ""

    def logout(self):
        if self.current_user:
            user = User()
            user.insert_log(self.current_user,"Logout dari sistem")
        self.window.close()
        self.show_login()

    def run(self):
        self.show_login()
        sys.exit(self.app.exec_())

    def show_login(self):
        self.login = HalamanLogin()
        self.login.show()
        self.login.pushButton.clicked.connect(self.proses_login)

    def proses_login(self):
        username = self.login.lineEdit.text()
        password = self.login.lineEdit_2.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(None, "Error", "Isi semua field!")
            return

        user = User()
        level = user.login(username, password)

        if level:
            self.current_user = username
            user.insert_log(self.current_user, "Login ke sistem")
            
            self.login.close()
            if level == "Admin":
                self.window = HalamanAdmin(self.current_user)
                self.window.show()
                self.window.pushButton_4.clicked.connect(self.logout)
            elif level == "Kasir":
                self.window = HalamanKasir(self.current_user)
                self.window.show()
                self.window.pushButton_4.clicked.connect(self.logout)
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Login gagal!")

if __name__ == "__main__":
    controller = AppController()
    controller.run()
