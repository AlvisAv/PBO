from model.connectiondb import mydb

mycursor = mydb.cursor()

class User:
    def __init__(self, username="", password="", nama="", level=""):
        self.username = username
        self.password = password
        self.nama = nama
        self.level = level

    def login(self, username, password):
        try:
            sql = "SELECT level FROM user WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            level = mycursor.fetchone()
            if level:
                return str(level[0]).capitalize()
            return None
        except Exception as e:
            print("Error login:", e)
            return None

    def insert_log(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggaljam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print("Error insert_log:", e)

    def select_log(self):
        try:
            sql = "SELECT tanggaljam, user, keterangan FROM log ORDER BY tanggaljam DESC"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print("Error select_log:", e)
            return []

    def select_all(self):
        try:
            sql = "SELECT nama, username, password, level FROM user"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print("Error select_all user:", e)
            return []

    def select_by_id(self, username):
        try:
            sql = "SELECT nama, username, password, level FROM user WHERE username = %s"
            mycursor.execute(sql, (username,))
            return mycursor.fetchone()
        except Exception as e:
            print("Error select_by_id user:", e)
            return None

    def insert(self, nama, username, password, level):
        try:
            sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
            val = (nama, username, password, level)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data user berhasil ditambahkan.")
            return True
        except Exception as e:
            print("Error insert user:", e)
            return False

    def update(self, nama, password, level, username):
        try:
            sql = "UPDATE user SET nama = %s, password = %s, level = %s WHERE username = %s"
            val = (nama, password, level, username)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data user berhasil diupdate.")
            return True
        except Exception as e:
            print("Error update user:", e)
            return False

    def delete(self, username):
        try:
            sql = "DELETE FROM user WHERE username = %s"
            mycursor.execute(sql, (username,))
            mydb.commit()
            print(mycursor.rowcount, "Data user berhasil dihapus.")
            return True
        except Exception as e:
            print("Error delete user:", e)
            return False
