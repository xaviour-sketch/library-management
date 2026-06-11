from models.book import Book
from models.member import Member
from models.loan import Loan


class LibraryManager:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, title, author):
        book = Book(title, author)

        self.books.append(book)

        return book
    
    def add_member(self, name, email):
        member = Member(name, email)
    
        self.members.append(member)

        return member