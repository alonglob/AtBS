# What does it take to be a Python Expert?
# James Powel


# Data Model:
# some behavior that i want to implement -> write some __ function __  AKA (dunder methods)/(data-model methods)
# top level function or top-level function -> corresponding data-model methods.
# x + y   -> __add__
# init x  -> __init__
# repr x  -> __repr__
# x()     -> __call__

class Polynomial:
    # the __init__ method allows inputing arguments into the object creator
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    # the __repr__ method calls the return when calling the object
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    pass

    # defines the + operator between 2 of these classes. self is the first, other is the second. 'self + other'
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    # the size of a polynomial is the degree (amount of coeffs)
    def __len__(self):
        return len(self.coeffs)

    # calling the function
    def __call__(self, *args, **kwargs):
        print('Polynomial(*{!r})'.format(self.coeffs))

p1 = Polynomial(1, 2, 3)  # x^2 + 2x + 3  # using __init__
p2 = Polynomial(3, 4, 3)  # 3x^2 + 4x + 3  # using __init__
print(p2)  # using __repr__
p3 = p1 + p2  # using __add__
print(len(p3))  # using __len__
p3()  # using __call__



