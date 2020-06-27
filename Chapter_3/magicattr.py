# Attribute access
# Using __getattribute__, __setattr__ and __getattr__


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string representation of the
    # object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # __getattribute__ called when an attr is retrieved. Don't directly access the attr name
    # otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return  p - (p * d)
        return super().__getattribute__(name)

    # __setattr__ called when attribute value is set. Don't set the attr directly here
    # otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float.")
        return super().__setattr__(name, value)

    # __getattr__ called when __getattribute__ lookup fails
    # You can pretty much generate attributes on the fly with this methods
    # It will be called if the attribute doesn't exist.
    def __getattr__(self, name):
        return name + " is not here!"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

b1.price = 38.95
print(b1)

# b2.price = 40     # To raise a ValueError
b2.price = float(40)
print(b2)

# Comment def __getattribute__ to access __getattr__
print(b1.randomprop)
