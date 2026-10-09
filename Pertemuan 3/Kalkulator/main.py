from kalkulator import *

def hitung_lagi():
    hitung_lagi = input("Apakah ingin menghitung lagi? (y/n): ")
    if hitung_lagi == "n":
        exit()
            
print("=== KALKULATOR ===")
while True:
    try:
        bil1 = float(input("Angka pertama : "))
        bil2 = float(input("Angka kedua : "))
    except ValueError:
        print("Error: Input harus berupa angka\n")
        hitung_lagi()
        continue

    print("\n1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    try:
        pilihan = int(input("Pilih operasi: "))

        if pilihan == 1:
            print(tambah(bil1, bil2))
        
        elif pilihan == 2:
            print(kurang(bil1, bil2))
        
        elif pilihan == 3:
            print(kali(bil1, bil2))
            
        elif pilihan == 4:
            try:
                print(bagi(bil1, bil2))
            except ZeroDivisionError:
                print("Error: Tidak boleh membagi dengan nol\n") 
        else:
            print("Error: Pilihan operasi tidak tersedia\n")
        hitung_lagi()
    except ValueError:
        print("Error: Pilihan operasi tidak tersedia\n")
        hitung_lagi()