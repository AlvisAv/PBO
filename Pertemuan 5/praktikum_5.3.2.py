class Mamalia:
    def __init__(self):
        self.paruparu = True

class Kucing(Mamalia):
    def __init__(self, val1, val2, val3):
        super().__init__()
        self.nama = val1
        self.kaki = val2
        self.warna = val3

obj1 = Kucing('Kiwi', 4, 'Golden')
print(obj1.nama)
print(obj1.kaki)
print(obj1.paruparu)

obj2 = Kucing('Berry', 4, 'Abu')
print(obj2.nama)
print(obj2.kaki)
print(obj2.paruparu)