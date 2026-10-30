import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="av123",
    database="kampus"
)

try:
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE mahasiswa ADD COLUMN jurusan VARCHAR(50)")
    mycursor.execute("ALTER TABLE mahasiswa ADD COLUMN umur INT")
    print("Kolom jurusan dan umur berhasil ditambahkan.")

except Exception as e:
    print(e)
