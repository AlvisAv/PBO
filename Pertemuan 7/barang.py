from connectiondb import mydb

mycursor = mydb.cursor()

class Barang:
    def __init__(self):
        pass

    def insert_log(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggaljam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def select_data(self, current_user):
        try:
            sql = "SELECT * FROM barang"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
            self.insert_log(current_user, "Melihat data barang")
        except Exception as e:
            print(e)

    def insert_data(self, vall, val2, val3, val4, val5, current_user):
        try:
            sql = "INSERT INTO barang (id, nama, stok, harga, kategori) VALUES (%s, %s, %s, %s, %s)"
            val = (vall, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
            self.insert_log(current_user, f"Menambahkan barang ID: {vall}")
        except Exception as e:
            print(e)

    def update_data(self, vall, val2, val3, val4, val5, current_user):
        try:
            sql = "UPDATE barang SET nama = %s, stok = %s, harga = %s, kategori = %s WHERE id = %s"
            val = (vall, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
            self.insert_log(current_user, f"Mengubah barang ID: {val5}")
        except Exception as e:
            print(e)

    def delete_data(self, vall, current_user):
        try:
            sql = "DELETE FROM barang WHERE id = %s"
            value = (vall,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
            self.insert_log(current_user, f"Menghapus barang ID: {vall}")
        except Exception as e:
            print(e)