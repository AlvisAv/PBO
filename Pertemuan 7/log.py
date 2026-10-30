from connectiondb import mydb
from datetime import datetime

mycursor = mydb.cursor()

class Log:
    def __init__(self):
        self

    def insert_data(self, user, keterangan):
        try:
            sql = "INSERT INTO log (tanggal_jam, user, keterangan) VALUES (%s, %s, %s)"
            sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            val = (sekarang, user, keterangan)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)

    def select_data(self):
        try:
            sql = "SELECT * FROM log"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        except Exception as e:
            print(e)

