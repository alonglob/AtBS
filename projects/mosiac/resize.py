#! /usr/bin/python3.7

'''
after downloading images with this command line script:
googleimagesdownload --keywords "Polar bears, baloons, Beaches" --limit 20 --chromedriver /home/alon/PycharmProjects/AtBS/Chapter_11/chromedriver
we can resize the images.
images are resized but the scaling will be off.

'''

from PIL import Image
import os, sys


def resize(path, output_dir, new_height, new_width):
    for folder_name, subfolders, filenames in os.walk(path):
        for f in filenames:
            try:
                im = Image.open(path + f)
                imResize = im.resize((new_height, new_width), Image.ANTIALIAS)
                imResize.save(output_dir + f + '_resized.png', 'PNG', quality=100)
            except Exception as err:
                print(str(err))

if __name__ == "__main__":
    source_path = "/home/alon/downloads/Parrot/"
    output_path = "/home/alon/downloads/resized_images/"
    new_height, new_width = 40, 40

    resize(source_path, output_path, new_height, new_width)
