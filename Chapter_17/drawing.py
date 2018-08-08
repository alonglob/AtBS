#! /usr/bin/python3.7

from PIL import Image
from PIL import ImageDraw

# Shapes:
img = Image.new('RGBA', (300, 300), 'white')
draw = ImageDraw.Draw(img)

draw.point((0, 0), fill='black')
draw.line([(0, 0), (300, 300)], fill='black', width=3)
draw.rectangle((100,100,150,200), outline='black')
draw.ellipse((100,100,150,200), outline='black')
draw.polygon([(0,0),(20,200), (200,30), (300,300)], outline='blue')

for i in range(0,300,10):
    draw.line([(300-i,0),(300,300-i)], fill='green')

img.save('/home/alon/PycharmProjects/AtBS/Chapter_17/manipulated_images/drawing.png')

# Text:
