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
    
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None
    
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:
            raise ValueError("Member not found")

        if book is None:
            raise ValueError("Book not found")

        if not book.is_available:
            raise ValueError("Book is already borrowed")

        loan = Loan(member_id, book_id)

        self.loans.append(loan)

        book.is_available = False

        return loan