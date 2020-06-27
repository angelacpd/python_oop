# Using multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


# Inherit from multiple base classes
# python looks at the super classes by the order they are defined from left to right
# Exchange A and B as arguments of C below.
class C(B, A):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.show_props()

# Method resolution order
print(C.__mro__)
