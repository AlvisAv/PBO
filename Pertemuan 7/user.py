from connectiondb import mydb

mycursor = mydb.cursor()

class User:
    def __init__(self):
        pass

    def login(self, vall, val2):
        try:
            sql = "SELECT level FROM user WHERE username = %s AND password = %s"
            val = (vall, val2)
            mycursor.execute(sql, val)
            level = mycursor.fetchone()
            return str(level[0])
        except Exception as e:
            print(e)


    def select_data(self, current_user):
        try:
            sql = "SELECT * FROM user"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
            self.insert_log(current_user, "Melihat data user")
        except Exception as e:
            print(e)

    def insert_data(self, vall, val2, val3, val4, current_user):
        try:
            sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
            val = (vall, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
            self.insert_log(current_user, f"Menambahkan user: {val2}")
        except Exception as e:
            print(e)

    def update_data(self, vall, val2, val3, val4, current_user):
        try:
            sql = "UPDATE user SET nama = %s, password = %s, level = %s WHERE username = %s"
            val = (vall, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
            self.insert_log(current_user, f"Mengubah user: {val4}")
        except Exception as e:
            print(e)

    def delete_data(self, vall, current_user):
        try:
            sql = "DELETE FROM user WHERE username = %s"
            value = (vall,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
            self.insert_log(current_user, f"Menghapus user: {vall}")
        except Exception as e:
            print(e)
    
    def insert_log(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggaljam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def select_log(self):
        try:
            sql = "SELECT * FROM log"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print("\n=== DATA LOG AKTIVITAS ===")
            for x in myresult:
                waktu_format = x[0].strftime("%d-%m-%Y %H:%M:%S")
                print(f"{waktu_format} | {x[1]} |{x[2]}")
            print("==========================\n")
        except Exception as e:
            print(e)