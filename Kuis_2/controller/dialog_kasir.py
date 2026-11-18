from PyQt5 import QtWidgets

from ui.tambah_barang import Ui_Dialog as TambahBarangUI
from ui.ubah_barang import Ui_Dialog as UbahBarangUI
from model.Barang import Barang
from model.Kategori import Kategori

class Dialog_tambah_barang(QtWidgets.QDialog, TambahBarangUI):
    def __init__(self, username="Kasir"):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.label_2.setText("Kode         :")

        self.comboBox.clear()
        self.comboBox.addItem("")
        kategori_data = Kategori().get_Data()
        if kategori_data:
            for item in kategori_data:
                self.comboBox.addItem(str(item[1]))
        self.comboBox.setCurrentIndex(0)

        self.barang = Barang()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        kode_barang = self.lineEdit.text().strip()
        nama = self.lineEdit_2.text().strip()
        stok = self.spinBox.value()
        harga = self.lineEdit_4.text().strip()
        kategori = self.comboBox.currentText().strip()

        if not kode_barang or not nama or not harga:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        success = self.barang.insert(kode_barang, nama, stok, harga, kategori)
        if success:
            self.barang.insert_log(self.username, f"Menambahkan barang baru: {nama} (Kode: {kode_barang})")
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Gagal menambahkan data barang! Pastikan Kode tidak duplikat.")

class Dialog_ubah_barang(QtWidgets.QDialog, UbahBarangUI):
    def __init__(self, kode_barang, nama, stok, harga, kategori, username="Kasir"):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.kode_barang = kode_barang
        self.label_2.setText("Kode         :")

        self.comboBox.clear()
        self.comboBox.addItem("")
        kategori_data = Kategori().get_Data()
        daftar_kategori = [str(item[1]) for item in kategori_data] if kategori_data else []

        if daftar_kategori:
            for item in daftar_kategori:
                self.comboBox.addItem(item)
            kategori_str = str(kategori).strip()
            if kategori_str and kategori_str in daftar_kategori:
                self.comboBox.setCurrentText(kategori_str)
            else:
                self.comboBox.setCurrentIndex(0)
        else:
            self.comboBox.setCurrentIndex(0)

        self.lineEdit.setText(kode_barang)
        self.lineEdit_2.setText(nama)
        self.spinBox.setValue(int(stok))
        self.lineEdit_4.setText(harga)

        self.barang = Barang()
        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        kode_barang = self.lineEdit.text().strip()
        nama = self.lineEdit_2.text().strip()
        stok = self.spinBox.value()
        harga = self.lineEdit_4.text().strip()
        kategori = self.comboBox.currentText().strip()

        if not nama or not harga:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Nama dan harga tidak boleh kosong!")
            return

        success = self.barang.update(nama, stok, harga, kategori, kode_barang)
        if success:
            self.barang.insert_log(self.username, f"Mengubah barang: {nama} (Kode: {kode_barang})")
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Gagal memperbarui data barang!")
