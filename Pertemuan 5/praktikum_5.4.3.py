class British:
    warna = 'Kuning'
    berat = True
    def sifat(self):
        return 'Lincah'

class Ragdoll:
    warna = 'Putih'
    tinggi = True
    def sifat(self):
        return 'Tenang'

class Campuran(British, Ragdoll):
    pass

Kiwi = Campuran()
print(Kiwi.warna)
print(Kiwi.berat)
print(Kiwi.tinggi)
print(Kiwi.sifat())