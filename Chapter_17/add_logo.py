#! /usr/bin/python3.7

from PIL import Image
import os

SQUARE_SIZE = 300
LOGO_PATH = '/home/alon/Documents/automate_online-materials/catlogo.png'
PICTURES_PATH = '/home/alon/PycharmProjects/AtBS/Chapter_17/manipulated_images/'
FINAL_PATH = "/home/alon/PycharmProjects/AtBS/Chapter_17/LOGO_images/"

logo = Image.open(LOGO_PATH)
logo = logo.resize((100, 100))
width, height = logo.size

os.makedirs(FINAL_PATH, exist_ok=True)
os.chdir(PICTURES_PATH)
for filename in os.listdir():
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename == 'catlogo.png':
        continue

    img = Image.open(filename)
    img_width, img_height = img.size
    if img_width > 300 or img_height > 300:
        if img_width > img_height:
            img_height = int(img_height*(300/img_width))
            img_width = 300
        else:
            img_width = int(img_width * (300 / img_height))
            img_height = 300

        img=img.resize((img_width, img_height))

    img.paste(logo, (img_width-width, img_height-height), logo)
    img.save(FINAL_PATH + filename)