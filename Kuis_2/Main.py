from PyQt5 import QtWidgets
import sys

from ui.form_login import Ui_MainWindow as LoginUI
from controller.dashboard_admin import HalamanAdmin
from controller.dashboard_kasir import HalamanKasir
from controller.dashboard_kategori import HalamanKategori
from controller.menu_kasir import HalamanMenuKasir
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
        self.window = None

    def logout(self):
        if self.current_user:
            user = User()
            user.insert_log(self.current_user, "Logout dari sistem")
        if self.window:
            self.window.close()
        self.current_user = ""
        self.show_login()

    def run(self):
        self.show_login()
        sys.exit(self.app.exec_())

    def show_login(self):
        self.login = HalamanLogin()
        self.login.show()
        self.login.pushButton.clicked.connect(self.proses_login)

    def proses_login(self):
        username = self.login.lineEdit.text().strip()
        password = self.login.lineEdit_2.text().strip()

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
                self.buka_dashboard_admin()
            elif level == "Kasir":
                self.tampilkan_menu_kasir()
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Login gagal! Username atau password salah.")

    def buka_dashboard_admin(self):
        """Membuka Dashboard Admin"""
        if self.window:
            self.window.close()
        self.window = HalamanAdmin(username=self.current_user, parent_controller=self)
        self.window.show()

    def tampilkan_menu_kasir(self):
        """Menampilkan menu pilihan untuk Kasir: Dashboard Barang atau Dashboard Kategori"""
        if self.window:
            self.window.close()
        self.window = HalamanMenuKasir(username=self.current_user, parent_controller=self)
        self.window.show()

    def buka_dashboard_barang(self):
        """Membuka Dashboard Barang (dapat diakses oleh Admin maupun Kasir sesuai Use Case)"""
        if self.window:
            self.window.close()
        self.window = HalamanKasir(username=self.current_user, parent_controller=self)
        self.window.show()

    def buka_dashboard_kategori(self):
        """Membuka Dashboard Kategori untuk Kasir"""
        if self.window:
            self.window.close()
        self.window = HalamanKategori(username=self.current_user, parent_controller=self)
        self.window.show()

if __name__ == "__main__":
    controller = AppController()
    controller.run()
