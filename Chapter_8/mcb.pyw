#! /usr/bin/python3.6
# remember to allow execution of the file with 'chmod +x <filename>.py'
# Multi Clip-Board - clipboard for saving multiple strings.
# these strings are accessible by dictionary-type keywords.
# Usage: mcb.pyw save <keyword>     - saves the clipboard contents to keyword
#        mcb.pyw delete <keyword>   - deletes the keyword-value pair.
#        mcb.pyw <keyword>          - loads the keyword-value to the clipboard
#        mcb.pyw list               - lists all the keywords to the terminal.

import os, sys
import pyperclip
import shelve
import pprint

num_arguments = len(sys.argv)
path = '/home/alon/PycharmProjects/AtBS/Chapter_8/mcb_data'
help_string = '''
Multi Clip-Board - clipboard for saving multiple strings.
these strings are accessible by dictionary-type keywords.
    
Usage: mcb.pyw save <keyword>     - saves the clipboard contents to keyword
mcb.pyw delete <keyword>          - deletes the keyword-value pair.
mcb.pyw <keyword>                 - loads the keyword-value to the clipboard
mcb.pyw list                      - lists all the keywords to the terminal.
'''

def save_contents(keyword):
    clipboard_file = shelve.open(path)
    value = str(pyperclip.paste())
    clipboard_file[keyword] = value
    clipboard_file.close()
    print('clipboard contents saved successfully as: ' + str(keyword) + '.')


def delete_contents(keyword):
    clipboard_file = shelve.open(path)
    del clipboard_file[keyword]
    clipboard_file.close()
    print(str(keyword) + ' and his value have been deleted successfully.')


def get_list():
    clipboard_file = shelve.open(path)

    if list(clipboard_file.keys()) == []:  # if the list is empty print a nice comment.
        print('The Multi Clipboard is currently empty!')
    else:
        pprint.pprint(list(clipboard_file.keys()))

    clipboard_file.close()


if num_arguments == 3:
    first_arg , second_arg = str(sys.argv[1]).lower(), str(sys.argv[2]).lower()
    if first_arg == 'save':
        save_contents(second_arg)

    elif first_arg == 'delete':
        delete_contents(second_arg)

    else:
        print('first argument is invald, save\delete only.')

elif num_arguments == 2:
    first_arg = str(sys.argv[1]).lower()

    if first_arg == 'list':
        get_list()

    elif first_arg == 'help':
        print(help_string)

    else:
        try:
            value = shelve.open(path)[first_arg]
            pyperclip.copy(value)
            print(str(first_arg) + 's value has been copied to the clipboard.')

        except KeyError:
            print('keyword does not exist.')
            sys.exit()

elif num_arguments == 1:
    print(help_string)

else:
    print('number of arguments too large, ')

