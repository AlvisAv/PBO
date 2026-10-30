import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="av123"
)

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE kampus")
    print("Database kampus berhasil dibuat.")

except Exception as e:
    print(e)
