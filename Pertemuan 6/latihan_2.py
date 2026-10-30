# Latihan 2: Langkah-langkah dasar menghubungkan Python dengan database MySQL

"""
Langkah-langkah menghubungkan Python ke MySQL:
1. Install library connector: pip install mysql-connector-python
2. Import library: import mysql.connector
3. Buka koneksi dengan memanggil mysql.connector.connect()
4. Buat cursor dengan mydb.cursor()
5. Jalankan query SQL dengan mycursor.execute() atau executemany()
6. Lakukan commit untuk query DML dengan mydb.commit()
7. Ambil hasil query DQL (SELECT) dengan mycursor.fetchall()
8. Tutup koneksi jika sudah selesai
"""

print("--- Langkah-Langkah Menghubungkan Python ke MySQL ---")
print("1. Install library konektor: pip install mysql-connector-python")
print("2. Import library: import mysql.connector")
print("3. Buka koneksi: mydb = mysql.connector.connect(host, user, password, database)")
print("4. Buat cursor: mycursor = mydb.cursor()")
print("5. Jalankan query: mycursor.execute(sql) atau executemany(sql, val)")
print("6. Commit data: mydb.commit() (khusus insert, update, delete)")
print("7. Ambil hasil: mycursor.fetchall() (khusus select)")
print("8. Tutup koneksi: mydb.close()")
