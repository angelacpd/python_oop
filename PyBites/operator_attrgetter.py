# Using Python module operator
# Use attrgetter to fetch one or more attributes of a class

from operator import attrgetter


class Person:
    name = 'John Doe'
    age = 44
    sex = 'M'


p = Person()
f = attrgetter('name', 'age', 'sex')
print(f(p))

g = attrgetter('age')
print(g(p))

# Output:

# ('John Doe', 44, 'M')

# 44
