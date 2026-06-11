import json
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
    
    def find_loan(self, loan_id):
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan

        return None
    
    def return_book(self, loan_id):
        loan = self.find_loan(loan_id)

        if loan is None:
            raise ValueError("Loan not found")

        if loan.returned:
            raise ValueError("Book already returned")

        book = self.find_book(loan.book_id)

        loan.returned = True
        book.is_available = True

        return loan
    
    def save_books(self):
        books_data = [
            book.to_dict()
            for book in self.books
        ]

        with open(
            "data/books.json",
            "w"
        ) as file:
            json.dump(
                books_data,
                file,
                indent=4
            )

    def save_members(self):
        members_data = [
            member.to_dict()
            for member in self.members
        ]

        with open("data/members.json", "w") as file:
            json.dump(
                members_data,
                file,
                indent=4
            )

    def save_loans(self):
        loans_data = [
            loan.to_dict()
            for loan in self.loans
        ]

        with open("data/loans.json", "w") as file:
            json.dump(
                loans_data,
                file,
                indent=4
            )

    def save_data(self):
        self.save_books()
        self.save_members()
        self.save_loans()