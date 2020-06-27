# Creating immutable data classes

from dataclasses import dataclass


# The "frozen" parameter makes the class immutable
@dataclass(frozen = True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval1):
        self.value2 = newval1


obj = ImmutableClass()
print(obj.value1)

# Attempting to change the value of an immutable class throws and exception
# obj.value1 = "Another value"
# print(obj.value1)

# Even functions within the class can't change anything
obj.some_func(20)
