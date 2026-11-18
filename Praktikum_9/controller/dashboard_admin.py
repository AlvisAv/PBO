from PyQt5 import QtWidgets
import sys

from ui.dashboard_admin import Ui_MainWindow as AdminUI
from controller.dialog_admin import Dialog_tambah_user as TambahUserUI
from controller.dialog_admin import Dialog_ubah_user as UbahUserUI
from controller.dialog_admin import Dialog_log as LogUI
from model.User import User

class HalamanAdmin(QtWidgets.QMainWindow, AdminUI):
    def __init__(self, username="Admin"):
        super().__init__()
        self.setupUi(self)
        self.username = username

        # menampilkan database ke tabel
        self.user = User()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Nama", "Username", "Password", "Level"])

        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)
        self.pushButton_5.clicked.connect(self.buka_log)

    def tampil_tabel(self):
        data = self.user.select_data_tabel()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, val in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))

    def buka_form_tambah(self):
        dialog = TambahUserUI(self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def buka_form_ubah(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        nama = self.tableWidget.item(row, 0).text()
        username = self.tableWidget.item(row, 1).text()
        password = self.tableWidget.item(row, 2).text()
        level = self.tableWidget.item(row, 3).text()

        dialog = UbahUserUI(nama, username, password, level, self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def konfirmasi_hapus(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        username = self.tableWidget.item(row, 1).text()

        reply = QtWidgets.QMessageBox.question(
            None, "Konfirmasi", "Yakin akan menghapus data?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            self.user.delete_data(username)
            self.user.insert_log(self.username, f"Menghapus user: {username}")
            self.tampil_tabel()

    def kembali(self):
        reply = QtWidgets.QMessageBox.question(
            None,
            "Konfirmasi",
            "Yakin ingin logout?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            self.close()

    def buka_log(self):
        dialog = LogUI()
        dialog.exec_()
