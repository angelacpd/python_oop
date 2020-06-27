# Using instance methods and attributes


class Book:
    # The init function is called when the instance is created and ready to be initialized
    def __init__(self, title, author, pages, price):
        # instance attributes => values are unique to each instance of the object that is declared
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        # Attribute with one underscore: tell other developers that  this attribute
        # is internal to the class and should not be accessed outside the class
        self._discount = amount


# Book instances
b1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1300, 49.99)
b2 = Book("A Song of Ice and Fire", "George R.R. Martin", 9547, 78.35)

# Call method get_price to print price
print(b1.get_price())

# Set the discount
print(b2.get_price())
b2.set_discount(0.25)
print(f'Price of the book after the discount: {b2.get_price()}')

# Properties with double underscores are hidden by the interpreter
# print(b2.__secret)  # shows an error
print(b2._Book__secret)     # Name mangling.
