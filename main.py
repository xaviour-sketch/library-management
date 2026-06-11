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

manager.borrow_book(
    member.member_id,
    book.book_id
)

manager.save_data()

print("Data saved successfully!")