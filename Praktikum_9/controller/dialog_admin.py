from dataclasses import field
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.log import Ui_Dialog as LogUI
from ui.tambah_user import Ui_Dialog as TambahUserUI
from ui.ubah_user import Ui_Dialog as UbahUserUI
from model.User import User

class Dialog_tambah_user(QtWidgets.QDialog, TambahUserUI):
    def __init__(self, admin_user="Admin"):
        super().__init__()
        self.setupUi(self)
        self.admin_user = admin_user
        self.user = User()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        nama = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if self.radioButton.isChecked():
            level = "Admin"
        elif self.radioButton_2.isChecked():
            level = "Kasir"
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Pilih level!")
            return

        if not nama or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "Data tidak boleh kosong!")
            return

        self.user.insert_data(nama, username, password, level)
        self.user.insert_log(self.admin_user, f"Menambahkan user baru: {username} ({level})")
        self.accept()

class Dialog_ubah_user(QtWidgets.QDialog, UbahUserUI):
    def __init__(self, nama, username, password, level, admin_user="Admin"):
        super().__init__()
        self.setupUi(self)
        self.admin_user = admin_user

        # isi data lama
        self.lineEdit.setText(nama)
        self.lineEdit_2.setText(username)
        self.lineEdit_3.setText(password)
        if level == "Admin":
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)

        self.user = User()
        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        nama = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if self.radioButton.isChecked():
            level = "Admin"
        elif self.radioButton_2.isChecked():
            level = "Kasir"
        self.user.update_data(nama, password, level, username)
        self.user.insert_log(self.admin_user, f"Mengubah user: {username} ({level})")
        self.accept()

class Dialog_log(QtWidgets.QDialog, LogUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user = User()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Tanggal & Jam","User","Keterangan"])
        
        data = self.user.select_log()
        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)  
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)   
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)