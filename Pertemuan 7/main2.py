from user import User
from barang import Barang

def greeting():
    print("="*40)
    print("SELAMAT DATANG DI APLIKASI KASIR APOTEK")
    print("="*40)

def menu_admin():
    print(">> Menu Admin")
    print("1) Lihat data user \n2) Tambah data user \n3) Edit data user \n4) Delete data user \n5) Lihat log aktivitas \n6) Logout")

def menu_kasir():
    print(">> Menu Kasir")
    print("1) Lihat data barang \n2) Tambah data barang \n3) Edit data barang \n4) Delete data barang \n5) Logout")

def login():
    print("\nSilahkan masukkan username dan password ")
    usernamelogin = input("Username: ")
    passwordlogin = input("Password : ")
    level_login = usr.login(usernamelogin, passwordlogin)
    return usernamelogin, level_login

usr = User()
brg = Barang()

greeting()

try:
    usernamelogin, level_login = login()
    usr.insert_log(usernamelogin, "Login ke sistem")
    menu_berlanjut = True
    
    while (menu_berlanjut):
        if (level_login.lower() == "admin"):
            menu_admin()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            
            if (menu == 1):
                usr.select_data()
                usr.insert_log(usernamelogin, "Lihat data user")
            elif (menu == 2):
                nama_baru = input("Masukkan nama :")
                username_baru = input("Masukkan username :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level (Admin/Kasir): ")
                usr.insert_data(nama_baru, username_baru, password_baru, level_baru)
                usr.select_data()
                usr.insert_log(usernamelogin, "Tambah data user")
            elif (menu == 3):
                username = input("Masukkan username data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level (Admin/Kasir):")
                usr.update_data(nama_baru, password_baru, level_baru, username)
                usr.select_data()
                usr.insert_log(usernamelogin, "Edit data user")
            elif (menu == 4):
                username = input("Masukkan username data yang akan dihapus:")
                usr.delete_data(username)
                usr.select_data()
                usr.insert_log(usernamelogin, "Delete data user")
            elif (menu == 5):
                usr.select_log()
                usr.insert_log(usernamelogin, "Lihat log aktivitas")
            elif (menu == 6):
                usr.insert_log(usernamelogin, "Logout")
                usernamelogin, level_login = login()
            else:
                menu_berlanjut = False
                
        elif (level_login.lower() == "kasir"):
            menu_kasir()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            
            if (menu == 1):
                brg.select_data()
                brg.insert_log(usernamelogin, "Lihat data barang")
            elif (menu == 2):
                id_baru = input("Masukkan id: ")
                nama_baru = input("Masukkan nama : ")
                stok_baru = input("Masukkan stok: ")
                harga_baru = input("Masukkan harga: ")
                kategori_baru = input("Masukkan kategori : ")
                brg.insert_data(id_baru, nama_baru, stok_baru, harga_baru, kategori_baru)
                brg.select_data()
                brg.insert_log(usernamelogin, "Tambah data barang")
            elif (menu == 3):
                id = input("Masukkan id data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                stok_baru = input("Masukkan stok:")
                harga_baru = input("Masukkan harga :")
                kategori_baru = input("Masukkan kategori : ")
                brg.update_data(nama_baru, stok_baru, harga_baru, kategori_baru, id)
                brg.select_data()
                brg.insert_log(usernamelogin, "Edit data barang")
            elif (menu == 4):
                id = input("Masukkan id data yang akan dihapus:")
                brg.delete_data(id)
                brg.select_data()
                brg.insert_log(usernamelogin, "Delete data barang")
            elif (menu == 5):
                brg.insert_log(usernamelogin, "Logout")
                usernamelogin, level_login = login()
            else:
                menu_berlanjut = False
        else:
            print("Login Gagal")
            break

except Exception as e:
    print(e)