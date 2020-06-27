# Check class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Shining")
b2 = Book("Huckleberry Finn")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# Use type() to inspect the object type
print(type(b1))
print(type(n1))

# Compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n2))

# Use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))   # All classes in python derive from object

