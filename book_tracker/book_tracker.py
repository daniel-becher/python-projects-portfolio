class Book():
    def __init__(self, title, author, pages):
        self.is_borrowed = False
        self.title = title
        self.pages = pages
        self.author = author

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"You borrowed {self.title}!")
        else:
            print(f"Book {self.title} is not available!")

    def return_book(self):
        self.is_borrowed = False
        print ("Book returned!")

    def info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} | {self.author} | {self.pages} pages | {status}\n"


class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        [book.borrow() for book in self.books if book.title == title]

    def return_book(self, title):
        [book.return_book() for book in self.books if book.title == title]

    def show_available(self):
        [print (book.info()) for book in self.books if book.is_borrowed == False]   

    def save_catalog(self, filename):
        try:
            with open (filename, "w", encoding="utf-8") as file:
                for book in self.books:
                    file.write(book.info())
        except Exception as e:
            print(f"Error saving a file {e}")

library = Library("Prague City Library")
library.add_book(Book("The Pragmatic Programmer", "David Thomas", 352))
library.add_book(Book("Clean Code", "Robert Martin", 431))
library.add_book(Book("Python Crash Course", "Eric Matthes", 544))
library.add_book(Book("Deep Learning", "Ian Goodfellow", 775))

library.borrow_book("Clean Code")
library.borrow_book("Deep Learning")
library.borrow_book("Clean Code")

library.show_available()
library.save_catalog("library.txt")