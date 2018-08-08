 # Transforming Code into Beautiful Idiomatic Python
 # by Raymond Hettinger


# For loop idioms:


colors = ['red', 'blue', 'green']

# bad:
for i in range(len(colors)):
    print(colors[i])

# good:
for color in colors:
    print(color)

# in reverse:
for color in reversed(colors):
    print(color)

# for the collection and indices:
for i,color in enumerate(colors):
    print(i, color)

# for two collections:
names = ['alon','lior','ohad']
for name,color in zip(names,colors):
    print(name, color)

# looping in sorted order
for color in sorted(colors):
    print(color)

# call a function until a sentinel value:
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# for-else usage:
# this loop tries to find factors for numbers between 2-10
# some numbers are prime, which means they dont have factors and the break wont happen.
# when the break doesnt happen, the else is called:
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break  # found the factor.
    else:
        # the loop failed to find a factor, break wasent called.
        print(n, 'is a prime number')


# Dictionary Skills:

# looping over dictionary keys:
d = {'matthew': 'blue','rachel': 'green', 'raymond': 'red'}

# the for loop on dictionaries returns the keys:
for k in d:
    print(k)
# when mutating a dictionary we loop over a NEW list of keys:
for k in d.keys():
    if k.startswith('r'):
        del d[k]
# or
d = {k: d[k] for k in d if not k.startswith('r')}

# looping over keys and values:
# does not return a list, items[] = iteritems()
for k, b in d.items():
    print(k,b)

# Construct Dictionaries from pairs:
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names,colors))

# Counting with dictionaries:
colors = ['red', 'green', 'red', 'green', 'blue', 'red']
d = {}
for color in colors:
    d[color]  = d.get(color, 0) + 1

# Grouping with dictionaries
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

import collections
d= collections.defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# Clarify multiple return values with named tuples
TestResults = collections.namedtuple('TestResults', ['failed', 'attempted'])

# How to open and close files:

with open('data.txt') as f:
    data = f.read()


