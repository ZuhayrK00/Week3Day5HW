from models.book import *

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Psychological Fiction", True)
book2 = Book("To Kill a Mockingbird", "J. R. R. Tolkien", "Domestic Fiction", False)
book3 = Book("The Catcher in the Rye", "J. D. Salinger", "Young Adult Fiction", True)
books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)


def delete_book_by_index(index):
    books.pop(index)
