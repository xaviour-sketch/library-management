from services.library_manager import LibraryManager

manager = LibraryManager()

manager.add_book(
    "Harry Potter",
    "J.K. Rowling"
)

manager.add_book(
    "Narnia",
    "C.S. Lewis"
)

manager.save_books()