#! /usr/bin/python3.7

from PIL import Image
import os

# Create an Image object from a image file
IMAGE_PATH = '/home/alon/Documents/automate_online-materials/zophie.png'
cat_im = Image.open(IMAGE_PATH)

os.chdir(os.getcwd() + '/manipulated_images')


width, height = cat_im.size  # returns the width and height of the image
file_name = cat_im.filename  # returns the filename string
file_format = cat_im.format  # returns a string of the file format such as png

cat_im.save('zophie.jpg')

# Creating an empty Image Object
img = Image.new('RGBA', (100, 200), 'purple')
img.save('purple_image.png')
img = Image.new('RGBA', (20, 20))
img.save('transparent_image.png')

# Cropping images with tuple boxes
cropped_img = cat_im.crop((335, 345, 565, 560))
cropped_img.save('cropped_img.png')

# Pasting images onto images
cat_im.paste(cropped_img, (0, 0))
cat_im.paste(cropped_img, (335, 345))
cat_im.save('pasted_image.png')

# Example:

cat_im_width,cat_im_height = cat_im.size
face_width, face_height = cropped_img.size
cat_copy = cat_im.copy()

for left in range(0,cat_im_width,face_width):
    for top in range(0,cat_im_height,face_height):
        cat_copy.paste(cropped_img, (left, top))

cat_copy.save('faced_cat.png')

# Resizing images
quarter_img = cat_im.resize((int(width/2), int(height/2)))
quarter_img.save('quarterized.png')

# Rotating and Flipping an image
cat_im.rotate(180).save('flipped_cat.png')
cat_im.rotate(10, expand=True).save('rotated_cat.png')
cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
cat_im.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Changing individual pixels
img = Image.new('RGBA', (100, 100))
print(img.getpixel((0, 0)))  # returns (0,0,0,0)
for width in range(100):
    for height in range(50):
        img.putpixel((width, height), (3*height, 3*height, 3*height))

from PIL import ImageColor
for width in range(100):
    for height in range(50, 100):
        img.putpixel((width, height), ImageColor.getcolor('darkgray', 'RGBA'))

img.save('put_pixel.png')

