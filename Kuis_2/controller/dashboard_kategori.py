from PyQt5 import QtWidgets

from ui.dashboard_kategori import Ui_MainWindow as KategoriUI
from controller.dialog_kategori import Dialog_tambah_kategori as TambahKategoriUI
from controller.dialog_kategori import Dialog_ubah_kategori as UbahKategoriUI
from model.Kategori import Kategori

class HalamanKategori(QtWidgets.QMainWindow, KategoriUI):
    def __init__(self, username="Kasir", parent_controller=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.parent_controller = parent_controller

        self.kategori = Kategori()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID Kategori", "Nama Kategori"])

        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        header = self.tableWidget.horizontalHeader()
        header.setMinimumSectionSize(110)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)
        if hasattr(self, 'pushButton_5'):
            self.pushButton_5.clicked.connect(self.ke_dashboard_barang)

    def tampil_tabel(self):
        data = self.kategori.get_Data()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, val in enumerate(row_data):
                self.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(val))
                )
        self.tableWidget.resizeRowsToContents()

    def buka_form_tambah(self):
        dialog = TambahKategoriUI(username=self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def buka_form_ubah(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data kategori yang ingin diubah terlebih dahulu!")
            return

        id_kategori = self.tableWidget.item(row, 0).text()
        nama_kategori = self.tableWidget.item(row, 1).text()

        dialog = UbahKategoriUI(id_kategori, nama_kategori, username=self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def konfirmasi_hapus(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih data kategori yang ingin dihapus terlebih dahulu!")
            return

        id_kategori = self.tableWidget.item(row, 0).text()
        nama_kategori = self.tableWidget.item(row, 1).text()

        reply = QtWidgets.QMessageBox.question(
            self, "Konfirmasi", f"Yakin akan menghapus kategori '{nama_kategori}' (ID: {id_kategori})?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            success = self.kategori.delete(id_kategori)
            if success:
                self.kategori.insert_log(self.username, f"Menghapus kategori: {nama_kategori} (ID: {id_kategori})")
                self.tampil_tabel()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Gagal menghapus data kategori!")

    def ke_dashboard_barang(self):
        """Beralih langsung ke Dashboard Barang"""
        self.close()
        if self.parent_controller:
            self.parent_controller.buka_dashboard_barang()

    def kembali(self):
        """Kembali ke Menu Kasir"""
        reply = QtWidgets.QMessageBox.question(
            self, "Konfirmasi", "Yakin ingin kembali ke menu utama kasir?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
            if self.parent_controller:
                self.parent_controller.tampilkan_menu_kasir()
