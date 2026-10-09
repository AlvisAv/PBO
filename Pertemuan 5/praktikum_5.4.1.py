class Kucing():
    warna = 'Kuning'
    def bersuara(self):
        return 'meow'

class Sapi():
    warna = 'Putih'
    def bersuara(self):
        return 'Moo'

Kiwi = Kucing()
print(Kiwi.warna)
print(Kiwi.bersuara())

api = Sapi()
print(api.warna)
print(api.bersuara())