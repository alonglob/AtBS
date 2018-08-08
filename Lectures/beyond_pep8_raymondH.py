import collections

# Named Tuples
color = collections.namedtuple('Color', ['hue', 'saturation', 'luminosity'])

p = color(170, 0.1, 0.6)
if p.saturation >= 0.5:
    print('Whew, that is bright!')
if p.luminosity >= 0.5:
    print('Wow, that is light!')
