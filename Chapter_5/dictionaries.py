# Dictionaries

# key-value pair
my_dict = {'name':'Alice','age':22,'color':'red'}
print(my_dict['name']) # prints 'Alice'

# Dict Methods: keys(), values(), items():
# returns list-like datatype which can be iterated on
# items() returns tuples of the items
for v in my_dict.values():
    print(v)

for k in my_dict.keys():
    print(k)

for i in my_dict.items():
    print(i)

# using the multiple assignment trick with the items() method:
for k, v in my_dict.items():
    print('keys: ' + str(k) + ', values: '+ str(v))

# checking for membership using the in\not in operators:
print('Alice' in my_dict) # False
print('Alice' in my_dict.values()) # True
print('name' in my_dict) # True
print('name' in my_dict.keys()) # True

# get() method:
my_dict.get('name','no name defined') # 'Alice'
my_dict.get('pet', 'no pet defined') # 'no pet defined'

# the setdefault() method:
# takes 2 arguments, the first is checked to be a key, if not
# the second is taken as the value of that key:
my_dict.setdefault('name','Bob') # 'Alice'
my_dict.setdefault('pet', 'dog') # 'dog', adds the key-value pair 'pet':'dog'

# nested dictionaries:
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought += v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(allGuests, 'apples')))
print(' - Cups           ' + str(total_brought(allGuests, 'cups')))
print(' - Cakes          ' + str(total_brought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(allGuests, 'apple pies')))
