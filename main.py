import argparse
from rich import print
from services.library_manager import LibraryManager

manager = LibraryManager()

parser = argparse.ArgumentParser(
    description="Library Management System"
)

subparsers = parser.add_subparsers(
    dest="command"
)

add_book_parser = subparsers.add_parser(
    "add-book"
)
add_book_parser.add_argument(
    "title"
)
add_book_parser.add_argument(
    "author"
)

add_member_parser = subparsers.add_parser("add-member")
add_member_parser.add_argument("name")
add_member_parser.add_argument("email")

subparsers.add_parser("list-books")
subparsers.add_parser("list-members")

borrow_book_parser = subparsers.add_parser("borrow-book")
borrow_book_parser.add_argument("member_id", type=int)
borrow_book_parser.add_argument("book_id", type=int)

return_book_parser = subparsers.add_parser("return-book")
return_book_parser.add_argument("loan_id", type=int)

subparsers.add_parser("view-loans")

args = parser.parse_args()

if args.command == "add-book":
    manager.load_data()
    book = manager.add_book(
        args.title,
        args.author
    )
    manager.save_data()
    print(book)

elif args.command == "list-books":
    manager.load_data()
    for book in manager.books:
        print(book)

elif args.command == "add-member":
    manager.load_data()
    member = manager.add_member(
        args.name,
        args.email
    )
    manager.save_data()
    print(member)

elif args.command == "list-members":
    manager.load_data()
    for member in manager.members:
        print(member)

elif args.command == "borrow-book":
    manager.load_data()
    loan = manager.borrow_book(
        args.member_id,
        args.book_id
    )
    manager.save_data()
    print(loan)

elif args.command == "return-book":
    manager.load_data()
    loan = manager.return_book(
        args.loan_id
    )
    manager.save_data()
    print(loan)

elif args.command == "view-loans":
    manager.load_data()
    for loan in manager.loans:
        print(loan)
