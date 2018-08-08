# upper() and lower() methods:
"""useful when comparing strings because they are case sensitive
and these methods eliminate the sensitivity:
"""
my_string = 'Hello World'
print('hello' in my_string)  # returns False
print('hello' in my_string.lower())  # returns True

# isupper() and islower() methods:
print(my_string.isupper())  # returns True
print(my_string.islower())  # returns True
print('1234'.isupper())  #returns False
print('1234'.islower())  #returns False

# the isX methods:
# helpful when trying to validate user input.
print(my_string.isalpha())  # returns True
print(my_string.isalnum())  # returns False (no numbers)
print('aa12'.isalnum())  # returns True
print('aa12'.isdecimal())  # returns False
print('1122'.isdecimal())  # returns True
print('         '.isspace())  # returns True
print(my_string.istitle())  # returns True

# startswith() and endswith() methods:
print(my_string.startswith('Hello'))  # returns True
print(my_string.endswith('World'))  # returns True
print(my_string.startswith('He'))  # returns True
print(my_string.startswith('World'))  # returns False

# join() and split() methods:
', '.join(['cats','rats','bats'])  # returns 'cats, rats, bats'
joined_string = 'ABC'.join(['my','name','is','Alice'])  # returns 'myABCnameABCisABCAlice'
# by default the split() method splits the string at whitespaces, not including them at the new list.
'my name is Alice'.split()  # returns ['my','name','is','Alice']
joined_string.split('ABC')  # returns ['my','name','is','Alice']
# A common use of split is with multiline strings:
multiline_string = '''Dear Alice,
how have you been? my life is a wreak.
i need help, fast!

please call me.
sincerely,
Bob.'''

print(multiline_string.split('\n')) # returns: ['Dear Alice,', 'how have you been? my life is a wreak.',
                                    # 'i need help, fast!', '', 'please call me.', 'sincerely,', 'Bob.']

# Justifying Text with rjust(), ljust(), and center().
hello = 'Hello'
hello.rjust(10)  # returns: '          Hello'
hello.ljust(3,'*')  # returns: 'Hello***'
hello.center(3,'*')  # returns: '***Hello***'

# Removing whitespaces with rstrip(), lstrip() and strip()
# the order of the characters in the string passed to the strip methods doesnt matter.
# by default the character is a whitespace.
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('pamS'))  # prints: 'BaconSpamEggs'


# PyperClip Module
# Allows the copying and printing of strings from the computer clipboard:
import pyperclip
pyperclip.copy('this string is copied to the clipboard')
print(pyperclip.paste())  # returns the copied string