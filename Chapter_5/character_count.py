import pprint

my_string = 'its such a sunny day outside, why am i indoors?'
counter = {}

for character in my_string:
    counter.setdefault(character,0)
    counter[character] += 1

pprint.pprint(counter)
# which is the same as print(pprint.pformat(counter))
