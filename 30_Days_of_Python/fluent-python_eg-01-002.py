"""
Vector 2D
Mathematical operations using special methods

Extended from book:
Fluent Python
Example 1-2
"""


import math


class Vector:

    def __init__(self, x1=0, x2=0):
        self.x1 = x1
        self.x2 = x2
        
    def __repr__(self):
        return f"Vector({self.x1!r}, {self.x2!r})"
    
    def __bool__(self):
        return bool(abs(self))
    
    def __abs__(self):
        return math.sqrt((self.x1)**2 + (self.x2)**2)
        # return math.hypot(self.x1, self.x2)
        
    def __add__(self, other):
        x1 = self.x1 + other.x1
        x2 = self.x2 + other.x2
        return Vector(x1, x2)
    
    def __mul__(self, scalar):
        return Vector(self.x1 * scalar, self.x2 * scalar)


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"string representation: {v1}")
    print(f"absolute: {abs(v1)}")
    print(f"boolean: {bool(v1)}")
    print(f"addition: {v1 + v2}")
    print(f"scalar multiplication: {v1 * 3}")
    

# Output

# string representation: Vector(3, 4)
# absolute: 5.0
# boolean: True
# addition: Vector(4, 6)
# scalar multiplication: Vector(9, 12)
