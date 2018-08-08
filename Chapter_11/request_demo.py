#! /usr/bin/python3.7

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()  # raise an exception if an error occurred

with open('play.txt', 'wb') as play_file:
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
