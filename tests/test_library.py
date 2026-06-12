from models.book import Book
from models.member import Member


def test_book_creation():
    book = Book(
        "Harry Potter",
        "J.K. Rowling"
    )

    assert book.title == "Harry Potter"


def test_book_available():
    book = Book(
        "Harry Potter",
        "J.K. Rowling"
    )

    assert book.is_available is True


def test_member_creation():
    member = Member(
        "John",
        "john@gmail.com"
    )

    assert member.name == "John"