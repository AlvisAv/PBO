from PyQt5 import QtWidgets

from ui.menu_kasir import Ui_MainWindow as MenuKasirUI

class HalamanMenuKasir(QtWidgets.QMainWindow, MenuKasirUI):
    def __init__(self, username="Kasir", parent_controller=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.parent_controller = parent_controller

        self.pushButton.clicked.connect(self.buka_barang)
        self.pushButton_2.clicked.connect(self.buka_kategori)
        self.pushButton_3.clicked.connect(self.logout)

    def buka_barang(self):
        if self.parent_controller:
            self.parent_controller.buka_dashboard_barang()

    def buka_kategori(self):
        if self.parent_controller:
            self.parent_controller.buka_dashboard_kategori()

    def logout(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin logout?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            if self.parent_controller:
                self.parent_controller.logout()
            else:
                self.close()
