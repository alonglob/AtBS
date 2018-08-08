# What does it take to be a Python Expert?
# James Powel

# Generators
# top-level syntax, function -> underscore method
# x()        __call__
from time import sleep
# the main idea of a generator with bad syntax:
'''
class Compute:
    def __init__(self):
        pass

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

for value in Compute():
    print(value)
'''

# the better syntax, an actual Generator:


def compute():
    for i in range(10):
        yield i  # yield instead of return is the difference between a normal function and a generator


for value in compute():
    print(value)

'''bad api call:
this api needs us to input usercode between the api calls, that is why the functions are divided.
so the api allows us to interleave our usercode into the api, but we must do it in a specific order.

class Api:
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        third

nothing stops us from calling the second method from Api.run_this_second()
thus we can use generators which wont allow such a code breaking option
this generator wont allow us to call the functions in any other order, but the one set.
'''


def first():
    print('first')


def second():
    print('second')


def last():
    print('last')


def api():
    first()
    yield
    second()
    yield
    last()


api()
