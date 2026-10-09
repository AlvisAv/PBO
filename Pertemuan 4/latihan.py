# --- Latihan 1 & 2: Rancangan Kelas Kendaraan dengan Modifier ---
class Kendaraan:
    def __init__(self, merk, jumlah_roda, nomor_mesin):
        # Public attribute (dapat diakses dari luar kelas)
        self.merk = merk 
        self.jumlah_roda = jumlah_roda 
        # Private attribute (terenkapsulasi, ditandai dengan double underscore)
        self.__nomor_mesin = nomor_mesin 
        
    def get_nomor_mesin(self):
        return self.__nomor_mesin

print("--- Latihan 1 & 2: Kelas Kendaraan ---")
motor = Kendaraan("Honda", 2, "MH1JM21")
print("Merk \t\t:", motor.merk)
print("Nomor Mesin \t:", motor.get_nomor_mesin())

# --- Latihan 3: Penggunaan hasattr() ---
class Siswa:
    nama = "Andi"

print("\n--- Latihan 3: hasattr() ---")
# a. Memeriksa apakah atribut nama tersedia
print("Cek atribut 'nama':", hasattr(Siswa, 'nama')) 

# b. Memeriksa apakah atribut kelas tersedia
print("Cek atribut 'kelas':", hasattr(Siswa, 'kelas')) 


# --- Latihan 4: Kelas AkunBank (Public & Private Modifier) ---
class AkunBank:
    def __init__(self, nama, saldo_awal):
        self.nama = nama           # Public
        self.__saldo = saldo_awal  # Private

    def lihat_saldo(self):
        print("Saldo Anda saat ini: Rp", self.__saldo)

    def setor_uang(self, jumlah):
        self.__saldo += jumlah
        print(f"Setoran Rp {jumlah} berhasil dilakukan.")

print("\n--- Latihan 4: Kelas AkunBank ---")
akun = AkunBank("Budi", 100000)
print("Nama Pemilik \t:", akun.nama)
akun.lihat_saldo()
akun.setor_uang(50000)
akun.lihat_saldo()
# Jika akun.__saldo dipanggil di sini, akan menghasilkan AttributeError

# --- Latihan 5: Implementasi Overloading ---
class Hitung:
    # Menggunakan default parameter (None) untuk meniru overloading
    def jumlah(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

print("\n--- Latihan 5: Method Overloading ---")
kalkulator = Hitung()
print("Penjumlahan 2 angka (10 + 20) \t\t:", kalkulator.jumlah(10, 20))
print("Penjumlahan 3 angka (10 + 20 + 30) \t:", kalkulator.jumlah(10, 20, 30))