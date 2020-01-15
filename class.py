# There's is not much more to show about classes
# They work the same way as most other languages
# When making a new object, there's no need for 'new'
# Python is interpreted and comes with a garbage collector
# Python has inheritance and multiple inheritance but I won't touch on it during this workshop

class Square:
    # the first argument is always a reference to itself, it's a convention to use 'self'
    def __init__(self, size, coordinate):
        self.size = size
        self.coordinate = coordinate
        # to make a private variavle
        self.__private = 'yeet'

    # Here's how you would implement string representation
    def __repr__(self):
        return f'Square(size={self.size}, coordinate={self.coordinate})'

    def __str__(self):
        return f'Square is {self.size} units big and at {self.coordinate}'
    # What's the difference? In short,
    # __repr__ is to be unambiguos, great for debugging
    # __str__ is more for nice printing
    # To learn more, you can simply type in the question into google

    # Here's how you would implement equality checking
    def __eq__(self, other):
        return self.size == other.size
        # same as
        return self.size == other

s = Square(10, (2, 3))
print(s)
print(repr(s))
print(s == Square(20, (0, 0)))
print(s == Square(10, (0, 0)))
