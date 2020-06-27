# Using Abstract Base Classes to enforce class constraints


class GraphicShape:
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side


g = GraphicShape()

c = Circle(10)
print(c.calculate_area())
s = Square(12)
print(c.calculate_area())
