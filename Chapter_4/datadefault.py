# Implementing default values in data classes

from dataclasses import dataclass, field
import random


# Generate a random price
def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # You can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # price: float = 0.0
    # price: float  # It will raise errors
    # Attributes without default value has to come before attributes with default values.
    # price: float = field(default=10.0)
    # default_factory
    price: float = field(default_factory=price_func)


# b1 = Book()   # To test default values
# print(b1)
b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)
