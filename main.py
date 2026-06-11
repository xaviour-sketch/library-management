from services.library_manager import LibraryManager

manager = LibraryManager()

book = manager.add_book(
    "Harry Potter",
    "J.K. Rowling"
)

member = manager.add_member(
    "John",
    "john@gmail.com"
)

loan = manager.borrow_book(
    member.member_id,
    book.book_id
)

print(loan)
print(book)
manager = LibraryManager()

book = manager.add_book(
    "Harry Potter",
    "J.K. Rowling"
)

member = manager.add_member(
    "John",
    "john@gmail.com"
)

loan = manager.borrow_book(
    member.member_id,
    book.book_id
)

manager.return_book(
    loan.loan_id
)

print(loan)
print(book)