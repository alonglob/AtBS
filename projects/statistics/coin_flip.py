import random
import pprint

options = ['heads', 'tails']
wins = {'heads': 0, 'tails':0}
for i in range(10000):
    wins[options[random.randrange(0, 2)]] += 1
    pprint.pprint(wins)