class Mamalia:
    paruparu = True
    def __init__(self, val):
        self.nama = val

class Kucing(Mamalia):
    kaki = 4
    def __init__(self, val):
        self.nama = val

obj1 = Kucing('Kiwi')
print(obj1.nama)
print(obj1.kaki)
print(obj1.paruparu)

obj2 = Kucing('Berry')
print(obj2.nama)
print(obj2.kaki)
print(obj2.paruparu)