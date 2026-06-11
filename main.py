from services.library_manager import LibraryManager

manager = LibraryManager()

manager.add_book(
    1,
    "Harry Potter",
    "J.K. Rowling"
)

for book in manager.books:
    print(book)