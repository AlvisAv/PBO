import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="av123",
    database="kampus"
)

try:
    mycursor = mydb.cursor()

    sql = "INSERT INTO mahasiswa (nim, nama, jurusan, umur) VALUES (%s, %s, %s, %s)"
    val = [
        ("E3122001", "Alvis Averrous", "Manajemen Informatika", 20),
        ("E3122002", "Budi Santoso", "Teknik Informatika", 21),
        ("E3122003", "Chandra Wijaya", "Teknik Komputer", 19)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan...")

    sql = "UPDATE mahasiswa SET nama = %s WHERE nim = %s"
    val = ("Budi Pratama", "E3122002")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil diupdate.")

    sql = "DELETE FROM mahasiswa WHERE nim = %s"
    val = ("E3122003", )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil dihapus.")

    mycursor.execute("SELECT * FROM mahasiswa")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

except Exception as e:
    print(e)