class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, Book):
        self.books.append(Book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f'the no. of books in library is {self.noBooks} The books are')
        for book in self.books:
            print(book)



L1 = Library()
L1.addBook('Ramayana')
L1.showInfo()