from connectiondbkampus import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE kampus1")
    print("Database kampus berhasil dibuat.")

except Exception as e:
    print(e)
