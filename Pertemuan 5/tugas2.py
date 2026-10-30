from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title='', authorship='', publicationYear=0):
        self.title = title
        self.authorship = authorship
        self.publicationYear = publicationYear
    
    @abstractmethod
    def displayDetails(self):
        pass

class Book(LibraryItem):
    def __init__(self, title='', authorship='', publicationYear=0, genre='', pageNumber=0):
        super().__init__(title, authorship, publicationYear)
        self.genre = genre
        self.pageNumber = pageNumber

class DigitalAsset(LibraryItem):
    def __init__(self, title='', authorship='', publicationYear=0, fileFormat='', fileSize=0.0):
        super().__init__(title, authorship, publicationYear)
        self.fileFormat = fileFormat
        self.fileSize = fileSize

class Movie(LibraryItem):
    def __init__(self, title='', authorship='', publicationYear=0, duration=0, genre=''):
        super().__init__(title, authorship, publicationYear)
        self.duration = duration
        self.genre = genre

class PrintedBook(Book):
    def __init__(self, title='', authorship='', publicationYear=0, genre='', pageNumber=0, coverType='', weight=0.0):
        super().__init__(title, authorship, publicationYear, genre, pageNumber)
        self.coverType = coverType
        self.weight = weight

    def displayDetails(self):
        pass

class EBook(Book, DigitalAsset):
    def __init__(self, title='', authorship='', publicationYear=0, genre='', pageNumber=0, fileFormat='', fileSize=0.0):
        Book.__init__(self, title, authorship, publicationYear, genre, pageNumber)
        DigitalAsset.__init__(self, title, authorship, publicationYear, fileFormat, fileSize)

    def displayDetails(self):
        pass

class DigitalMovie(DigitalAsset, Movie):
    def __init__(self, title='', authorship='', publicationYear=0, fileFormat='', fileSize=0.0, duration=0, genre=''):
        DigitalAsset.__init__(self, title, authorship, publicationYear, fileFormat, fileSize)
        Movie.__init__(self, title, authorship, publicationYear, duration, genre)

    def displayDetails(self):
        pass

class BluRay(Movie):
    def __init__(self, title='', authorship='', publicationYear=0, duration=0, genre='', resolution=''):
        super().__init__(title, authorship, publicationYear, duration, genre)
        self.resolution = resolution

    def displayDetails(self):
        pass

class DVD(Movie):
    def __init__(self, title='', authorship='', publicationYear=0, duration=0, genre='', regionCode=0):
        super().__init__(title, authorship, publicationYear, duration, genre)
        self.regionCode = regionCode

    def displayDetails(self):
        pass