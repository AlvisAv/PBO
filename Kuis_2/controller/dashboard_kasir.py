from PyQt5 import QtWidgets

from ui.dashboard_kasir import Ui_MainWindow as KasirUI
from controller.dialog_kasir import Dialog_tambah_barang as TambahBarangUI
from controller.dialog_kasir import Dialog_ubah_barang as UbahBarangUI
from model.Barang import Barang

class HalamanKasir(QtWidgets.QMainWindow, KasirUI):
    def __init__(self, username="Kasir", parent_controller=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.parent_controller = parent_controller

        self.barang = Barang()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Kode", "Nama", "Stok", "Harga", "Kategori"]
        )

        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        header = self.tableWidget.horizontalHeader()
        header.setMinimumSectionSize(90)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)

        if hasattr(self, 'pushButton_5'):
            self.pushButton_5.clicked.connect(self.ke_dashboard_kategori)

    def tampil_tabel(self):
        data = self.barang.select_all()
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
        dialog = TambahBarangUI(self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def buka_form_ubah(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Warning", "Pilih data barang terlebih dahulu!")
            return

        kode_barang = self.tableWidget.item(row, 0).text()
        nama = self.tableWidget.item(row, 1).text()
        stok = self.tableWidget.item(row, 2).text()
        harga = self.tableWidget.item(row, 3).text()
        kategori = self.tableWidget.item(row, 4).text()

        dialog = UbahBarangUI(kode_barang, nama, stok, harga, kategori, self.username)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def konfirmasi_hapus(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Warning", "Pilih data barang terlebih dahulu!")
            return

        kode_barang = self.tableWidget.item(row, 0).text()

        reply = QtWidgets.QMessageBox.question(
            self, "Konfirmasi", f"Yakin akan menghapus barang dengan Kode '{kode_barang}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            success = self.barang.delete(kode_barang)
            if success:
                self.barang.insert_log(self.username, f"Menghapus barang Kode: {kode_barang}")
                self.tampil_tabel()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Gagal menghapus data barang!")

    def ke_dashboard_kategori(self):
        """Beralih ke Dashboard Kategori jika tombol tersedia"""
        self.close()
        if self.parent_controller:
            self.parent_controller.buka_dashboard_kategori()

    def kembali(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin kembali ke menu utama kasir?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
            if self.parent_controller:
                self.parent_controller.tampilkan_menu_kasir()
