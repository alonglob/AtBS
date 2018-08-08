def my_division(x, divide_by):
    try:
        return x/divide_by
    except ZeroDivisionError:
        print('cannot divide by zero, invalid argument.')
        return None


for i in range(0, 10, 1):
    print(my_division(3, i))
