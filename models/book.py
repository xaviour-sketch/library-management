class Book:
    id_counter = 1

    def __init__(self, title, author, is_available=True):
        self.book_id = Book.id_counter
        Book.id_counter += 1

        self.title = title
        self.author = author
        self.is_available = is_available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["title"],
            data["author"],
            data["is_available"]
        )

        book.book_id = data["book_id"]

        return book

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"

        return (
            f"Book ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Status: {status}"
        )