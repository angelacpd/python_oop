class Dog:
    species = "Canis familiaris"

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."


# Children classes
class JackRussellTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
print(miles)
buddy = Dachshund("Buddy", 9)
print(buddy)
jack = Bulldog("Jack", 3)
print(jack)
