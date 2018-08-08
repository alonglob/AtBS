#! /usr/bin/python3.7

import threading
import time

print('start of program 1')

def take_a_nap():
    time.sleep(5)
    print('wake up!')


thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()
print('end of program 1')


print('start of program 2')

thread_obj = threading.Thread(
    target=print,
    args=['Cats', 'Dogs', 'Frogs'],
    kwargs={'sep': ' & '})
thread_obj.start()

print('end of program 2')