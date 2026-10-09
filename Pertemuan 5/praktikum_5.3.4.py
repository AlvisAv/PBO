class Mamalia():
    paruparu = True
    def __init__(self):
        self.gigi = True
    
    def bergerak(self):
        return 'Berjalan/Berenang'

class Kucing(Mamalia):
    ekor = True
    def __init__(self, val1, val2, val3):
        super().__init__() # memanggil konstruktor superclass
        self.nama = val1
        self.kaki = val2
        self.suara = val3

    def bersuara(self):
        return self.suara

obj = Kucing('Kiwi', 4, 'Meow')
print('Suara : ', obj.bersuara())
print('Kaki : ', obj.kaki)
print('Ekor : ', obj.ekor)
print('Bergerak : ', obj.bergerak())
print('Paru-paru : ', obj.paruparu)
print('Gigi : ', obj.gigi) 