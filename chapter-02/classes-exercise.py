class Book:

    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False

    def __str__(self):
        status = "read" if self.read else "not read"
        return f"Name: {self.name}\nAuthor: {self.author}\nRelease date:{self.release_date} Status: {status}"


class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []

        elif all(isinstance(book, Book) for book in books):
            self.books = books
        else:
            raise TypeError("books must be a list of Book instances or None")

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("book must be an instance of Book (class)")
        # print(f"Added book: {book.name}")

    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                book.read = True
                return
        print(f"Book names {book_name} not found in the collection")

    def list_books(self):
        if not self.books:
            print("The book collection is empty")
        for book in self.books:
            print("")
            print(book)
            print("")


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)


# Create a book collection
my_collection = BookCollection()

# # Add books to the collection
my_collection.add_book(book1)
my_collection.add_book(book2)
my_collection.add_book(book3)

# # List all books
my_collection.list_books()
# my_collection.mark_as_read("default book")

# # Mark a book as read
# my_collection.mark_as_read("1984")

# # List books again to see updated status
# my_collection.list_books()

# # Try to mark a non-existing book as read
# my_collection.mark_as_read("Unknown Book")
