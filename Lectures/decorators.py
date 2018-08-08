# What does it take to be a Python Expert?
# James Powel

# Decorators
# allows the user to wrap functions with other operations easily, instead of function = wrapper(function)
# building a decorator syntax:
'''


def dec(function):                                # the input of a decorator is a function, but is not used like normal arguments.
    def wrapper(*args, **kwargs)                  # allows multiple arguments to the function
        do_something_with_wrappers()              # use the wrappers in some way
        return_value = function(*args, **kwargs)  # use the function that is wrapped
        return return_value                       # return the value the function generated
    return wrapper                                # return the function that wraps the first function


@dec
def function(*args, **kwargs):
    return do_something_with_args(*args, **kwargs)

'''
#  for example:
from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f


def ntimes(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                rv = func(*args, **kwargs)
                return rv
        return wrapper
    return inner


def add(x, y=10):
    return x + y


def sub(x, y=10):
    return x - y


print('add(10)', add(10))
print('add(20,30)', add(20, 30))
print('add("a", "b")', add("a", "b"))

print('sub(10)', sub(10))
print('sub(20,30)', sub(20, 30))

