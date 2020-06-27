# Using Abstract Base Class to implement interfaces


from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def to_json(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return f"{{\" Circle\" : {str(self.calculate_area())} }}"


c = Circle(10)
print(c.calculate_area())
print(c.to_json())
