from model.connectiondb import mydb

mycursor = mydb.cursor()

class Kategori:
    def __init__(self, id="", kategori=""):
        self.id = id
        self.kategori = kategori

    def insert_log(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggaljam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print("Error log:", e)

    def get_Data(self):
        try:
            sql = "SELECT id, kategori FROM kategori"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print("Error get_Data kategori:", e)
            return []

    def insert(self, id_kategori, nama_kategori):
        try:
            sql = "INSERT INTO kategori (id, kategori) VALUES (%s, %s)"
            val = (id_kategori, nama_kategori)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Kategori berhasil ditambahkan.")
            return True
        except Exception as e:
            print("Error insert kategori:", e)
            return False

    def update(self, nama_kategori, id_kategori):
        try:
            sql_get = "SELECT kategori FROM kategori WHERE id = %s"
            mycursor.execute(sql_get, (id_kategori,))
            row = mycursor.fetchone()
            nama_lama = row[0] if row else None

            sql = "UPDATE kategori SET kategori = %s WHERE id = %s"
            val = (nama_kategori, id_kategori)
            mycursor.execute(sql, val)
            mydb.commit()

            if nama_lama and nama_lama != nama_kategori:
                sql_update_barang = "UPDATE barang SET kategori = %s WHERE kategori = %s"
                mycursor.execute(sql_update_barang, (nama_kategori, nama_lama))
                mydb.commit()

            print(mycursor.rowcount, "Kategori berhasil diupdate.")
            return True
        except Exception as e:
            print("Error update kategori:", e)
            return False

    def delete(self, id_kategori):
        try:
            sql_get = "SELECT kategori FROM kategori WHERE id = %s"
            mycursor.execute(sql_get, (id_kategori,))
            row = mycursor.fetchone()
            nama_lama = row[0] if row else None

            sql = "DELETE FROM kategori WHERE id = %s"
            val = (id_kategori,)
            mycursor.execute(sql, val)
            mydb.commit()

            if nama_lama:
                sql_update_barang = "UPDATE barang SET kategori = '' WHERE kategori = %s"
                mycursor.execute(sql_update_barang, (nama_lama,))
                mydb.commit()

            print(mycursor.rowcount, "Kategori berhasil dihapus.")
            return True
        except Exception as e:
            print("Error delete kategori:", e)
            return False
