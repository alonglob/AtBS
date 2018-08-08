#! /usr/bin/python3.7

# The Time Module
import time
print(time.time())  # This is the time that has passed since the Unix Epoch time reference.

## Showing off some Decorators
def timer(func):  # a timer that calculates the time it takes from execution to evaluation of the arg
    def f(*args, **kwargs):
        time_0 = time.time()  # time before evaluation
        r_value = func(*args, **kwargs)  # evaluation
        time_1 = time.time()  # the time after the evaluation
        print(str(time_1-time_0) + ' seconds to evaluate the function ' + str(func.__name__))

        return r_value
    return f


@timer
def calcProd():  # A random Function doing a long calculation
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 1000):
           product = product * i
       return product


calcProd()

# the Sleep method
sleep_seconds = 2
time.sleep(sleep_seconds)  # tells the interpeter to sleep for 2 seconds

# because Ctrl + C only interupts after the sleep is over, we can sleep for 30 seconds like this:
for i in range(30):
    time.sleep((1))

# Round Function:
print(round(time.time()))  # rounds untill the dot
print(round(time.time(), 4))  # rounds untill the specified number of numbers after the dot, here 4

