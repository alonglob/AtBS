#! /usr/bin/python3.7
# phone_email_extractor.py - finds phone numbers and emails in long text
# that are coppied to the pc clipboard.

import pyperclip
import re

phone_regex = re.compile(r'''(
                        (\d{2,3})         # area code \ company 
                        (\s|-|\.)?      # seperator
                        (\d{3})         # first 3 digits
                        (\s|-|\.)?       # seperator
                        (\d{4})         # last 4 digits
                        )''', re.VERBOSE)

email_regex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+              # account name
                        (@\w+)             # @domain
                        (\.[a-zA-Z]+)+           # .something
                        )''',re.VERBOSE)

input_text = str(pyperclip.paste())

email_list = email_regex.findall(input_text)
phone_number_tuple = phone_regex.findall(input_text)

matches = []
print('Phone Numbers:')
for group in phone_number_tuple:
    value = ('-'.join([group[1], group[3], group[5]]))
    matches.append(value)
    print(value)

print('\nEmails:')
for group in email_list:
    matches.append(group[0])
    print(group[0])

if len(matches[0]) > 0:
    pyperclip.copy('/n'.join(matches))
    print('values copied to clipboard:')
    print('/n'.join(matches))
else:
    print('No phone numbers or email addresses found in the clipboard.')
