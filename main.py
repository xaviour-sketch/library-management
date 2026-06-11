from services.library_manager import LibraryManager

manager = LibraryManager()

manager.load_data()

print("BOOKS")
for book in manager.books:
    print(book)

print("\nMEMBERS")
for member in manager.members:
    print(member)

print("\nLOANS")
for loan in manager.loans:
    print(loan)