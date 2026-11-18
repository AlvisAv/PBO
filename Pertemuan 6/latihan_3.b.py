from connectiondbkampus import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE mahasiswa (nim VARCHAR(15) PRIMARY KEY, nama VARCHAR(50))")
    print("Tabel mahasiswa berhasil dibuat.")

except Exception as e:
    print(e)
