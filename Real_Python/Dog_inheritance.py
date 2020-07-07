class Dog:
    species = "Canis familiaris"

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} barks: {sound}."


# Children classes
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}."
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
print(miles)
buddy = Dachshund("Buddy", 9)
print(buddy)
jack = Bulldog("Jack", 3)
print(jack)

# determine which class a given object belongs to
print(type(miles))

# determine if miles is also an instance of the Dog class
print(isinstance(miles, Dog))
print(isinstance(miles, JackRussellTerrier))

print(miles.speak())
print(miles.speak("Grrr"))
print(jack.speak("Woof"))

dobby = GoldenRetriever(name="Dobby", age=6)
print(dobby)
print(dobby.speak())
