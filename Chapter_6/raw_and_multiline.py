
# Escape Characters:
print('that\'s Alice\'s cat')  # prints: that's Alice's cat without issues.
print('hello!\nhow are you?\tare you having a good day?')

# Raw Strings
# allows the use of many backslashes, python will ignore the escape operations
print(r'that\s Alice\s cat')  # prints: that\s Alice\s cat

# Multiline Strings with Triple Quotes:
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Multiline Comments:
"""This
is
a
valid
comment
"""

# Indexing and Slicing Strings:
my_string = 'Hello World'
print(my_string[-1])  # prints: 'd'
print(my_string[6:])  # prints: 'Hello'

# In and Not In operators
print('Hello' in my_string)  # returns False


