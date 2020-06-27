# Basic class
class Book:
    def __init__(self, title):  # initialize the new object with new information
        self.title = title


# Instance of class Book
b1 = Book("Brave New World")
b2 = Book("War and Peace")


# Print class and property
print(b1)
print(b1.title)
