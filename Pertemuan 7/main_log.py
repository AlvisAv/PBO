# Latihan Bab 7: Pengembangan Mini Project Kasir dengan Fitur Log Activity
from user import User
from barang import Barang
from log import Log

usr = User()
brg = Barang()
lg = Log()

def greeting():
    print("="*40)
    print("SELAMAT DATANG DI APLIKASI KASIR APOTEK")
    print("="*40)

def menu_admin():
    print(">> Menu Admin")
    print("1) Lihat data user \n2) Tambah data user \n3) Edit data user \n4) Delete data user \n5) Tampil data log \n6) Logout")

def menu_kasir():
    print(">> Menu Kasir")
    print("1) Lihat data barang \n2) Tambah data barang \n3) Edit data barang \n4) Delete data barang \n5) Logout")

def login():
    print("\nSilahkan masukkan username dan password ")
    usernamelogin = input("Username : ")
    passwordlogin = input("Password : ")
    level_login = usr.login(usernamelogin, passwordlogin)
    if level_login:
        lg.insert_data(usernamelogin, "Login berhasil sebagai " + str(level_login))
    return usernamelogin, level_login

greeting()

try:
    user_aktif, level_login = login()

    menu_berlanjut = True
    while(menu_berlanjut):
        if(level_login == "Admin"):
            menu_admin()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            if(menu == 1):
                usr.select_data()
                lg.insert_data(user_aktif, "Melihat data user")
            elif(menu == 2):
                nama_baru = input("Masukkan nama :")
                username_baru = input("Masukkan username :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level :")
                usr.insert_data(nama_baru, username_baru, password_baru, level_baru)
                usr.select_data()
                lg.insert_data(user_aktif, "Menambah data user: " + username_baru)
            elif(menu == 3):
                username = input("Masukkan username data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level :")
                usr.update_data(nama_baru, password_baru, level_baru, username)
                usr.select_data()
                lg.insert_data(user_aktif, "Mengedit data user: " + username)
            elif(menu == 4):
                username = input("Masukkan username data yang akan dihapus :")
                usr.delete_data(username)
                usr.select_data()
                lg.insert_data(user_aktif, "Menghapus data user: " + username)
            elif(menu == 5):
                print("\n>> Data Log Aktivitas:")
                lg.select_data()
                lg.insert_data(user_aktif, "Melihat data log aktivitas")
            elif(menu == 6):
                lg.insert_data(user_aktif, "Logout")
                user_aktif, level_login = login()
            else:
                menu_berlanjut = False

        elif(level_login == "Kasir"):
            menu_kasir()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            if(menu == 1):
                brg.select_data()
                lg.insert_data(user_aktif, "Melihat data barang")
            elif(menu == 2):
                id_baru = input("Masukkan id : ")
                nama_baru = input("Masukkan nama : ")
                stok_baru = input("Masukkan stok : ")
                harga_baru = input("Masukkan harga : ")
                kategori_baru = input("Masukkan kategori : ")
                brg.insert_data(id_baru, nama_baru, stok_baru, harga_baru, kategori_baru)
                brg.select_data()
                lg.insert_data(user_aktif, "Menambah data barang: " + id_baru)
            elif(menu == 3):
                id = input("Masukkan id data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                stok_baru = input("Masukkan stok :")
                harga_baru = input("Masukkan harga :")
                kategori_baru = input("Masukkan kategori :")
                brg.update_data(nama_baru, stok_baru, harga_baru, kategori_baru, id)
                brg.select_data()
                lg.insert_data(user_aktif, "Mengedit data barang: " + id)
            elif(menu == 4):
                id = input("Masukkan id data yang akan dihapus :")
                brg.delete_data(id)
                brg.select_data()
                lg.insert_data(user_aktif, "Menghapus data barang: " + id)
            elif(menu == 5):
                lg.insert_data(user_aktif, "Logout")
                user_aktif, level_login = login()
            else:
                menu_berlanjut = False

except Exception as e:
    print(e)

