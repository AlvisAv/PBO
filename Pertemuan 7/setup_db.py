# Praktikum 7.1: Menyiapkan Tabel Barang dan Tabel Log
from connectiondb import mydb

try:
    mycursor = mydb.cursor()

    # 1. Buat tabel barang (Praktikum 7.1)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS barang (
            id VARCHAR(10) PRIMARY KEY,
            nama VARCHAR(55),
            stok INT(11),
            harga INT(11),
            kategori VARCHAR(50)
        )
    """)
    print("Tabel barang berhasil dibuat/disiapkan.")

    # 2. Buat tabel log (Latihan Bab 7)
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS log (
            tanggal_jam DATETIME,
            user VARCHAR(55),
            keterangan VARCHAR(255)
        )
    """)
    print("Tabel log berhasil dibuat/disiapkan.")

    # Data awal barang sesuai modul halaman 17
    mycursor.execute("SELECT COUNT(*) FROM barang")
    if mycursor.fetchone()[0] == 0:
        sql = "INSERT INTO barang (id, nama, stok, harga, kategori) VALUES (%s, %s, %s, %s, %s)"
        val = ("01", "paracetamol", 12, 10000, "obat ringan")
        mycursor.execute(sql, val)
        mydb.commit()
        print("Data awal barang ('01', 'paracetamol') berhasil ditambahkan.")

except Exception as e:
    print(e)

