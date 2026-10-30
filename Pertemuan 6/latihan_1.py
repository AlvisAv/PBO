# Latihan 1: Analisis kelemahan menyimpan data hanya menggunakan variabel biasa tanpa database

"""
Kelemahan jika aplikasi hanya menyimpan data di variabel:
1. Data tidak permanen (volatile) - Data akan hilang saat aplikasi ditutup atau komputer restart karena tersimpan di RAM.
2. Keterbatasan memori - RAM memiliki kapasitas terbatas, data yang terlalu banyak bisa menyebabkan memori penuh (out of memory).
3. Tidak mendukung multi-user / konkurensi - Sulit mengelola banyak pengguna yang mengakses data bersamaan tanpa terjadi crash atau konflik data.
4. Pencarian data tidak efisien - Tidak memiliki sistem query seperti SQL, jadi pencarian data harus dibuat manual dengan looping.
5. Keamanan dan integritas data rendah - Tidak ada validasi bawaan seperti primary key, unique, maupun hak akses user.
"""

print("--- Kelemahan Menyimpan Data Hanya Menggunakan Variabel ---")
print("1. Data bersifat sementara (volatile) dan akan hilang ketika program berhenti.")
print("2. Kapasitas terbatas oleh ukuran RAM komputer.")
print("3. Tidak mendukung akses bersamaan (multi-user) dan rentan konflik data.")
print("4. Proses pencarian dan pengolahan data rumit karena tidak ada fitur query SQL.")
print("5. Tidak ada jaminan integritas data (seperti primary key) dan keamanan.")
