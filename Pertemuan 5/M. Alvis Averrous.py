class Item:
    def __init__(self, code, title, description, category, picture, quantityInStock, price):
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantityInStock = quantityInStock
        self.price = price

    def viewFullDescription(self):
        pass

    def addToCart(self):
        pass

    def updateStockLevel(self):
        pass


class DVD(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, director, certificate, listOfActors):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.director = director
        self.certificate = certificate
        self.listOfActors = listOfActors


class MP3(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, duration, artist):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.duration = duration
        self.artist = artist

    def playExtract(self):
        pass

    def download(self):
        pass


class Book(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, isbn, author, synopsis):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.isbn = isbn
        self.author = author
        self.synopsis = synopsis

    def preview(self):
        pass

item1 = Item("I01", "Keyboard", "Keyboard mekanikal RGB", "Elektronik", "keyboard.png", 20, 250000)
dvd1 = DVD("D01", "Interstellar", "Film sci-fi luar angkasa", "DVD", "interstellar.png", 10, 80000, "Christopher Nolan", "PG-13", ["Matthew McConaughey", "Anne Hathaway"])
mp3_1 = MP3("M01", "Fix You", "Lagu alternatif rock", "Audio", "coldplay.png", 50, 15000, "4:55", "Coldplay")
buku1 = Book("B01", "Bumi Manusia", "Novel sejarah", "Buku", "bumi_manusia.png", 15, 90000, "978-979-973-123-4", "Pramoedya Ananta Toer", "Minke pemuda pribumi yang bersekolah di HBS.")