#! /usr/bin/python3.7

# example of how to place exceptions and handling them.
# exceptions are called inside the function, the try and except are used when the function is called.


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater then 2.')
    if height <= 2:
        raise Exception('Height must be larger then 2.')

    print(symbol * width)
    for _ in range(height):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 10, 10), ('O', 4, 4), ('XX', 4, 4)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An Exception happend: ' + str(err))
