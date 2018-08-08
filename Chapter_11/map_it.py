#! /usr/bin/python3.7

# Map It
# this program searches for the address given as a bash argument.
# if no arguments given, it will copy from the clipboard.
# this is an example for the "webbrowser" module.

import webbrowser
import pyperclip
import sys

address = 'https://www.google.com/maps/place/'
if len(sys.argv) == 1:
    address += pyperclip.paste()
else:
    address = address + '+'.join(sys.argv[1:])

webbrowser.open(address)

