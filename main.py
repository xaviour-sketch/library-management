from services.library_manager import LibraryManager

manager = LibraryManager()

manager.add_book(
    "Harry Potter",
    "J.K. Rowling"
)

manager.add_member(
    "Mary",
    "banana"
)

print("BOOKS")
for book in manager.books:
    print(book)

print("\nMEMBERS")
for member in manager.members:
    print(member)