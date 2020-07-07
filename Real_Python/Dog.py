class Dog:
    # Class attribute
    species = "Canis familiaris"

    # dunder methods: begin and end with double underscores.

    # Instance attributes
    def __init__(self, name='Rex', age='1'):
        self.name = name
        self.age = age

    # Instance methods
    # def description(self):
    #     return f"{self.name} is {self.age} years old."

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."


# Instantiate object
a = Dog()
print(f"Dog a: name = {a.name}, age = {a.age}")
b = Dog()
print(f"Dog b: name = {b.name}, age = {b.age}")

print(f"Is a equal to b? {a == b}")
# The output is False because each instance represents different objects

print(f"Species: {a.species}")

a = Dog('Tinkerbell', 4)
print(f"Dog a: name = {a.name}, age = {a.age}")

# Change attributes dynamically
a.age = 9
print(f"Dog a: name = {a.name}, age = {a.age}")

# print(a.description())
print(a.speak("Woof Woof"))
print(a)


