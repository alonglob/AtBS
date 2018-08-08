#! /usr/bin/python3.6
# Pattern Matching with Regular Expressions (regex)
import re

# Creating a regex object:
# /d means digit
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search('my number is 054-238-4422')
print(mo.group())  # returns 054-238-4422

# Grouping regex with paranthesis
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('my number is 054-238-4422')
print(mo.group())   # returns 054-238-4422
print(mo.group(0))  # returns 054-238-4422
print(mo.group(1))  # returns 054
print(mo.group(2))  # returns 238-4422
print(mo.groups())  # returns a tuple: ('054', '238-4422')
# using the multiple assignment trick:
company_code, private_code = mo.groups()

# Matching multiple groups with the Pipe ( | ):
hero_regex = re.compile(r'batman|superman|aquaman')
mo = hero_regex.search('i love batman')
print(mo.group())  # returns 'batman'
mo = hero_regex.search('i love superman')
print(mo.group())  # returns 'superman'
mo = hero_regex.search('i love aquaman')
print(mo.group())  # returns 'aquaman'

# Optional MAtching with the Question Mark ( ? ):
bat_regex = re.compile(r'bat(wo)?man')
mo = bat_regex.search('i love batman')
print(mo.group())  # prints 'batman'
mo = bat_regex.search('i love batwoman')
print(mo.group())  # prints 'batwoman'

# Matching zero or more with the asterisk\star ( * ):
bat_regex = re.compile(r'bat(wo)*man')
mo = bat_regex.search('i love batwowowoman')
print(mo.group())  # prints 'batwowowoman'

# Matching one or more with the Plus ( + ):
bat_regex = re.compile(r'bat(wo)+man')
mo = bat_regex.search('i love batman')
print(mo.group())  # prints None

# Matching specific repetition with the curly brackets {}:
ha_regex = re.compile(r'(ha){3,5}')
mo= ha_regex.search('hahahaha')
print(mo.group())  # prints 'hahahaha'
mo= ha_regex.search('haha')
print(mo.group())  # prints None

# Greedy and NonGreedy Matching:
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
mo1.group()  # returns 'HaHaHaHaHa'

nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
mo2.group()  # returns 'HaHaHa'

# The findall() Method:
# if the regex isn't grouped, returns a list of all the matches,
# if the regex IS grouped, returns a tuple of lists. ea list contains a matched group.
phone_num_regex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')  # returns ['415-555-9999', '212-555-0000']
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')  # [('415', '555', '9999'), ('212', '555', '0000')]

# Creating Character Classes:
# using square brackets [] we can define character classes
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('Robocop eats baby food. BABY FOOD.')  # returns all the vowels in a list.
# using the caret character (^) we can define a negetive regex.
# negetive regex matches characters that are NOT in the character class
negetive_regex = re.compile(r'[^aeiouAEIOU]')
vowel_regex.findall('Robocop eats baby food. BABY FOOD.') # returns everything that ISN'T a vowel.

# The Caret and Dollar Sign Characters:
begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello world!')

# The Wildcard Character ( . ):
at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.')  # returns ['cat', 'hat', 'sat', 'lat', 'mat']

# Match anything with dot-str ( .* ):
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Alon Last Name: Globerman')
mo.group(1)  # returns Alon
mo.group(2)  # returns Globerman

# Case-Insensitive Matching
insens_regex = re.compile('RoBoCoP',re.I)
insens_regex.search('robocop is part man, part machine, all robot.').group()  # returns robocop

# Substituting Strings with the sub() Method:
names_regex = re.compile(r'Agent \w+')
names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')
# returns 'CENSORED gave the secret documents to CENSORED.'
# using the matched string as the substitution:
agent_names_regex = re.compile(r'Agent (\w)\w*')
agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent'  
                                 'Eve knew Agent Bob was a double agent.')
# returns A**** told C**** that E**** knew B**** was a double agent.'

# Managing Complex Regexes
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')  # bad...

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, re.VERBOSE:
combined_regex = re.compile('foo', re.IGNORECASE|re.DOTALL|re.VERBOSE)