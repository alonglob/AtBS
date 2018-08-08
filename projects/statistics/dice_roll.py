import random
import pprint

options = ['1', '2', '3', '4', '5', '6']
wins = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
for i in range(600000):
    wins[options[random.randrange(0, 6)]] += 1
    pprint.pprint(wins)