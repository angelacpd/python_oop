# Using Abstract Base Classes to enforce class constraints

# ABC = Abstract Base Class
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod     # Each subclass has to override this method
    def calculate_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


# g = GraphicShape()

c = Circle(10)
print(c.calculate_area())
s = Square(12)
print(s.calculate_area())
