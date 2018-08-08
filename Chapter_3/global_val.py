global_var = 0


def my_function():
    print('changing the global variable in a local scope from 0 to 1')
    global global_var
    global_var = 1

my_function()
print(global_var)
