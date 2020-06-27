# Using __call__


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # Use the __str__ method to return a string -> user
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # The __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
print(b1)

# Call the object as if it were a function
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
