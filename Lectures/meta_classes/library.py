# What does it take to be a Python Expert?
# James Powel

# Meta Classes:

# library.py

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError('bad user class')

        return super().__new__(cls, name, bases, body)

class Base:
    def foo(self):
        return self.bar()