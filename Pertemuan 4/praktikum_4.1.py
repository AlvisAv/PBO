class Mahasiswa:
    nim = 0
    def __init__(self):
        self.nama = ''
        self.prodi = ''
        
    # Method dengan Overloading (Praktikum 4.6)
    def set_atribut(self, val1='', val2=0, val3=''):
        self.nama = val1
        self.nim = val2
        self.prodi = val3
        
    def get_atribut(self):
        print("Nama \t:", self.nama, 
              "\nNIM \t:", self.nim, 
              "\nProdi\t:", self.prodi)

class MataKuliah:
    prodi = ''
    def __init__(self):
        self.nama = ''
        self.sks = 0
        
    def set_atribut(self, val1='', val2=0):
        self.nama = val1
        self.sks = val2
        
    def get_atribut(self):
        print("Nama \t:", self.nama, 
              "\nSKS \t:", self.sks)


# --- Pengujian Objek ---
print("--- Set Atribut Standar ---")
mhs1 = Mahasiswa()
mhs1.set_atribut('Alya', 111, 'Informatika')
mhs1.get_atribut()

print("\n--- Method Overloading ---")
mhs5 = Mahasiswa()
mhs5.set_atribut(val1='Furqan', val2=8080123)
mhs5.get_atribut()

mhs6 = Mahasiswa()
mhs6.set_atribut(val1='Farrah', val3='Farmasi')
mhs6.get_atribut()

print("\n--- Fungsi hasattr() ---")
print("Cek atribut 'nim' pada mhs1:", hasattr(mhs1, 'nim'))
print("Cek atribut 'alamat' pada mhs1:", hasattr(mhs1, 'alamat'))