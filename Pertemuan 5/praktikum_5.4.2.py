class Mamalia():
    ekor = 'Ada / Tidak ada'
    def bergerak(self):
        return 'Berjalan/ Berenang'

class Kucing(Mamalia):
    ekor = 'Ada'
    def bergerak(self):
        return 'Berjalan'

class British(Kucing):
    pass

Kiwi = British()
print(Kiwi.ekor)
print(Kiwi.bergerak())