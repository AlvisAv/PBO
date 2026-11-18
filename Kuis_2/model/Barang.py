from model.connectiondb import mydb
from model.Kategori import Kategori

mycursor = mydb.cursor()

class Barang:
    def __init__(self, kode="", nama="", harga=0, stok=0, kategori=""):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.kategori_obj = Kategori(kategori=kategori) if kategori else None

    def insert_log(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggaljam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print("Error insert_log:", e)

    def select_all(self):
        try:
            sql = "SELECT kode, nama, stok, harga, kategori FROM barang"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print("Error select_all barang:", e)
            return []

    def select_by_id(self, kode_barang):
        try:
            sql = "SELECT kode, nama, stok, harga, kategori FROM barang WHERE kode = %s"
            mycursor.execute(sql, (kode_barang,))
            return mycursor.fetchone()
        except Exception as e:
            print("Error select_by_id barang:", e)
            return None

    def insert(self, kode, nama, stok, harga, kategori):
        try:
            sql = "INSERT INTO barang (kode, nama, stok, harga, kategori) VALUES (%s, %s, %s, %s, %s)"
            val = (kode, nama, stok, harga, kategori)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data barang berhasil ditambahkan.")
            return True
        except Exception as e:
            print("Error insert barang:", e)
            return False

    def update(self, nama, stok, harga, kategori, kode):
        try:
            sql = "UPDATE barang SET nama = %s, stok = %s, harga = %s, kategori = %s WHERE kode = %s"
            val = (nama, stok, harga, kategori, kode)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data barang berhasil diupdate.")
            return True
        except Exception as e:
            print("Error update barang:", e)
            return False

    def delete(self, kode):
        try:
            sql = "DELETE FROM barang WHERE kode = %s"
            mycursor.execute(sql, (kode,))
            mydb.commit()
            print(mycursor.rowcount, "Data barang berhasil dihapus.")
            return True
        except Exception as e:
            print("Error delete barang:", e)
            return False
