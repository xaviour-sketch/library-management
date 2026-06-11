from models.book import Book
from models.member import Member
from models.loan import Loan


class LibraryManager:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)

        self.books.append(book)

        return book