# praktikum7.py (Praktikum 4.7: Membatasi Akses Modifier)

class Mahasiswa:
    def __init__(self, val1='', val2=0, val3=''):
        self.__nama = val1      # Private
        self.nim = val2         # Public
        self.__prodi = val3     # Private
        
    # Getter methods untuk mengakses atribut private
    def get_nama(self):
        return self.__nama
        
    def get_nim(self):
        return self.nim
        
    def get_prodi(self):
        return self.__prodi

mhs1 = Mahasiswa('Alya', 1234, 'Ilmu Hukum')

# Mengakses atribut public secara langsung
print("NIM \t:", mhs1.nim)

# Mengakses atribut private harus menggunakan getter
print("Nama \t:", mhs1.get_nama())
print("Prodi\t:", mhs1.get_prodi())