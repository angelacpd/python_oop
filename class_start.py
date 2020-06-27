# Using class-level and static methods


class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # Double-underscore properties are hidden from other classes
    __book_list = None

    # Create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # Create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list is None:
            Book.__book_list = []
        return Book.__book_list

    # Instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title, book_type):
        self.title = title
        if (not book_type in Book.BOOK_TYPES):
            raise ValueError(f"{book_type} ins not a valid book type")
        else:
            self.book_type = book_type


# Access the class attribute
print("Book types: ", Book.get_book_types())

# Create some book instances
b1 = Book("Title 1", "HARDCOVER")
# b2 = Book("Title 2", "COMIC")   # Show an error
b2 = Book("Title 2", "PAPERBACK")

# Use the static method to access a singleton object
the_books = Book.get_book_list()
the_books.append(b1)
the_books.append(b2)
print(the_books)
