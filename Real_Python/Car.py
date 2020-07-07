class Car:
    kind = "vehicle"
    wheels = 4

    def __init__(self, manufacturer, model, year, doors):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.doors = doors

    def __str__(self):
        return f"{self.manufacturer} {self.model} of year {self.year} has {self.doors} doors."


mustang = Car(manufacturer="Ford", model="Mustang", year=74, doors=2)
print(mustang)
