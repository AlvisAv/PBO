from HitungBangun.luas import lingkaran
from HitungBangun.luas import persegi
from HitungBangun.volume import kubus
from HitungBangun.volume import tabung

while(True):
    print("Menu : ")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Luas Lingkaran")
    print("3. Hitung Volume Kubus")
    print("4. Hitung Volume Tabung")
    print("5. Exit")

    pilihan = int(input("Pilih : "))

    if pilihan == 1:
        sisi = int(input("Masukkan sisi: "))
        persegi.LuasPersegi(sisi)

    elif pilihan == 2:
        jarijari = int(input("Masukkan jari-jari: "))
        lingkaran.LuasLingkaran(jarijari)

    elif pilihan == 3:
        sisi = int(input("Masukkan sisi: "))
        kubus.VolumeKubus(sisi)

    elif pilihan == 4:
        jarijari = int(input("Masukkan jari-jari: "))
        tinggi = int(input("Masukkan tinggi: "))
        tabung.VolumeTabung(jarijari, tinggi)

    elif pilihan == 5:
        exit()

    else:
        print("Pilihan tidak ada")