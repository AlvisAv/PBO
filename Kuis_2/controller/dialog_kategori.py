from PyQt5 import QtWidgets

from ui.tambah_kategori import Ui_Dialog as TambahKategoriUI
from ui.ubah_kategori import Ui_Dialog as UbahKategoriUI
from model.Kategori import Kategori

class Dialog_tambah_kategori(QtWidgets.QDialog, TambahKategoriUI):
    def __init__(self, username="Kasir"):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.kategori = Kategori()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        id_kategori = self.lineEdit.text().strip()
        nama_kategori = self.lineEdit_2.text().strip()

        if not id_kategori or not nama_kategori:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        success = self.kategori.insert(id_kategori, nama_kategori)
        if success:
            self.kategori.insert_log(self.username, f"Menambahkan kategori baru: {nama_kategori} (ID: {id_kategori})")
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Gagal menambahkan data! Pastikan ID tidak duplikat.")

class Dialog_ubah_kategori(QtWidgets.QDialog, UbahKategoriUI):
    def __init__(self, id_kategori, nama_kategori, username="Kasir"):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.id_kategori = id_kategori
        self.kategori = Kategori()

        self.lineEdit.setText(id_kategori)
        self.lineEdit_2.setText(nama_kategori)

        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        nama_kategori = self.lineEdit_2.text().strip()

        if not nama_kategori:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Nama kategori tidak boleh kosong!")
            return

        success = self.kategori.update(nama_kategori, self.id_kategori)
        if success:
            self.kategori.insert_log(self.username, f"Mengubah kategori ID: {self.id_kategori} menjadi {nama_kategori}")
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Gagal memperbarui data kategori!")
