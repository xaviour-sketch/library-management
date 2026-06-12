import argparse

from rich.console import Console
from rich.table import Table

from services.library_manager import LibraryManager

console = Console()
manager = LibraryManager()

# ==========================
# CLI SETUP
# ==========================

parser = argparse.ArgumentParser(
    description="Library Management System"
)

subparsers = parser.add_subparsers(dest="command")

# Add Book
add_book_parser = subparsers.add_parser(
    "add-book",
    help="Add a new book"
)
add_book_parser.add_argument("title")
add_book_parser.add_argument("author")

# List Books
subparsers.add_parser(
    "list-books",
    help="View all books"
)

# Add Member
add_member_parser = subparsers.add_parser(
    "add-member",
    help="Add a new member"
)
add_member_parser.add_argument("name")
add_member_parser.add_argument("email")

# List Members
subparsers.add_parser(
    "list-members",
    help="View all members"
)

# Borrow Book
borrow_book_parser = subparsers.add_parser(
    "borrow-book",
    help="Borrow a book"
)
borrow_book_parser.add_argument("member_id", type=int)
borrow_book_parser.add_argument("book_id", type=int)

# Return Book
return_book_parser = subparsers.add_parser(
    "return-book",
    help="Return a borrowed book"
)
return_book_parser.add_argument("loan_id", type=int)

# View Loans
subparsers.add_parser(
    "view-loans",
    help="View all loan records"
)

args = parser.parse_args()

# ==========================
# COMMANDS
# ==========================

if args.command == "add-book":

    manager.load_data()

    book = manager.add_book(
        args.title,
        args.author
    )

    manager.save_data()

    console.print(
        "\n[bold green]✓ Book Added Successfully[/bold green]"
    )

    console.print(book)


elif args.command == "list-books":

    manager.load_data()

    table = Table(title=" Library Books")

    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Status")

    for book in manager.books:

        status = (
            "Available"
            if book.is_available
            else "Borrowed"
        )

        table.add_row(
            str(book.book_id),
            book.title,
            book.author,
            status
        )

    console.print(table)


elif args.command == "add-member":

    manager.load_data()

    member = manager.add_member(
        args.name,
        args.email
    )

    manager.save_data()

    console.print(
        "\n[bold green]✓ Member Added Successfully[/bold green]"
    )

    console.print(member)


elif args.command == "list-members":

    manager.load_data()

    table = Table(title="👤 Library Members")

    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("Email")

    for member in manager.members:

        table.add_row(
            str(member.member_id),
            member.name,
            member.email
        )

    console.print(table)


elif args.command == "borrow-book":

    manager.load_data()

    loan = manager.borrow_book(
        args.member_id,
        args.book_id
    )

    manager.save_data()

    console.print(
        "\n[bold green]✓ Book Borrowed Successfully[/bold green]"
    )

    console.print(loan)


elif args.command == "return-book":

    manager.load_data()

    loan = manager.return_book(
        args.loan_id
    )

    manager.save_data()

    console.print(
        "\n[bold green]✓ Book Returned Successfully[/bold green]"
    )

    console.print(loan)


elif args.command == "view-loans":

    manager.load_data()

    table = Table(title=" Loan Records")

    table.add_column("Loan ID", style="cyan")
    table.add_column("Member ID")
    table.add_column("Book ID")
    table.add_column("Status")

    for loan in manager.loans:

        status = (
            "Returned"
            if loan.returned
            else "Borrowed"
        )

        table.add_row(
            str(loan.loan_id),
            str(loan.member_id),
            str(loan.book_id),
            status
        )

    console.print(table)


# ==========================
# WELCOME SCREEN
# ==========================

else:

    console.print("""
[bold blue]
=========================================
      LIBRARY MANAGEMENT SYSTEM
=========================================
[/bold blue]

[yellow]Available Commands[/yellow]

 BOOKS

add-book <title> <author>
list-books

 MEMBERS

add-member <name> <email>
list-members

 LOANS

borrow-book <member_id> <book_id>
return-book <loan_id>
view-loans

=========================================
EXAMPLES
=========================================

Add a Book:
python3 main.py add-book "Atomic Habits" "James Clear"

View Books:
python3 main.py list-books

Add a Member:
python3 main.py add-member "John" "john@gmail.com"

View Members:
python3 main.py list-members

Borrow a Book:
python3 main.py borrow-book 1 2

Return a Book:
python3 main.py return-book 1

View Loans:
python3 main.py view-loans

=========================================
""")