#! /usr/bin/python3.7

# this is a example for using beautiful soup 4

import requests
import bs4

'''
# for example, using requests to feed bs4 method:
res = requests.get('https://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
'''

# because we have the file in this directory, we will use it instead.

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file)
