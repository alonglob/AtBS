#! /usr/bin/python3.7
# Image Mosiac Creator
# using a folder of many images called tiles, and a source image, we recreate the source image from the smaller images.
# Usage:
# $ ./mosiac source_filename tiles_directory
# this outputs the recreated image to the source folder.

import logging
import sys
from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt


def create_source_arr(source_image_path):
    # working with the source file
    with Image.open(source_image_path) as source_img:
        source_arr = np.array(source_img)  # create a 3d array of (height, width, RGb_depth=3)

    source_height, source_width = source_arr.shape[:-1]
    logging.debug('size of source image as an array: ' + str(source_arr.shape))

    return source_arr


def create_tiles_arr(tiles_path):
    for dir_name, subfolders, filenames in os.walk(tiles_path):
        tiles_list = []
        tile_rgb_mean_list = []

        for i, filename in enumerate(filenames):
            try:
                with Image.open(dir_name + '/' + filename) as tile_img:  # create an array from a tile image
                    tile_img = tile_img.convert('RGB')
                    temp_tile_arr = np.array(tile_img)
                    tile_height, tile_width = temp_tile_arr.shape[:-1]

                if i > 0:
                    if tile_height != old_h or tile_width != old_w:  # checking if the tiles are of the same size
                        raise Exception('tiles are not of the same size')

                old_h, old_w = tile_height, tile_width  # saving these values to check if the next tile is also of the same size

                tiles_list.append(temp_tile_arr)  # add the new image array to the list.

                rgb_mean = temp_tile_arr.mean(axis=(0, 1))  # list of 3 RGB values which are the average of the image.
                tile_rgb_mean_list.append(rgb_mean)

            except OSError as err:
                print('could not open: ' + filename + ' probably broken image.')

    return tiles_list, tile_rgb_mean_list


def iter_source(source_arr, tiles_arr, tile_rgb_mean_list):
    """
    :param source_arr: ndarray of the source image
    :param tile_list: a list of ndarrays of tile images
    :param tile_rgb_mean_list: a list of the rgb mean in a tile
    :return: final_arr: recreated source_arr from tiles
    """

    tile_height, tile_width = tiles_arr[0].shape[0:2]
    source_height, source_width = source_arr.shape[:-1]

    for i in range(int(source_height / tile_height)):
        print('current row: ' + str(i*tile_height) + '/' + str(source_height), end='')
        print('\r', end='')

        for j in range(int(source_width / tile_width)):
            point = [i*tile_height, j*tile_width]

            if point[0] >= source_height:
                break

            # get the source tile, and then its mean value.
            source_tile = source_arr[point[0]:point[0]+tile_height, point[1]:point[1]+tile_width]
            source_tile_mean = source_tile.mean(axis=(0, 1))  # get the mean value of the current source tile

            # Find the best match for the source tile mean in the tile_rgb_list
            for index, mean in enumerate(tile_rgb_mean_list):
                temp_delta = abs(mean - source_tile_mean)

                if index == 0 or temp_delta.max() < best_delta.max():
                    if index == 100:
                        print(len(tile_rgb_mean_list))
                        print(source_tile_mean)
                        print(temp_delta)
                        print(best_delta)
                        exit()
                    best_delta = temp_delta
                    best_index = index

            # Using the source array as the new reconstructed array switch the source tile with the best match.
            source_arr[point[0]:point[0] + tile_height, point[1]:point[1] + tile_width] = tiles_arr[best_index]

    return source_arr


def main(argv):
    # Create the Info Debugging level
    logging.disable(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Start of program')

    # obtain the arguments passed to the script and make sure only 2 were passed.
    if len(sys.argv) != 3:  # make sure 2 arguments were passed to the commandline
        raise Exception(
            str(len(sys.argv) - 1) + ' arguments passed (2 needed). please pass a source image and a tile directory')

    source_image_path, tiles_path = argv[1:]

    # create a source image array
    source_arr = create_source_arr(source_image_path)
    print('SOURCE IMAGE PATH: ' + os.path.abspath(source_image_path), ', (HEIGHT, WIDTH): ' + str(source_arr.shape[0:2]))

    # create a tiles array and a mean rgb value array from the tiles array
    tiles_arr, rgb_arr = create_tiles_arr(tiles_path)
    print('TILES DIRECTORY: ' + os.path.abspath(tiles_path), ', (HEIGHT, WIDTH): ' + str(tiles_arr[0].shape[0:2]))

    # Iterate over the source array, switching its tiles with new tiles based on the rgb difference.
    reconstructed_arr = iter_source(source_arr, tiles_arr, rgb_arr)

    # After reconstructing the Soure Image, display it.
    plt.imshow(reconstructed_arr)
    plt.show()

    # Save the reconstructed Image.
    result = Image.fromarray(reconstructed_arr, 'RGB')
    result.save('reconstructed.png')
    print('reconstructed image saved to: ' + os.path.dirname(os.path.abspath(source_image_path)) + '/reconstructed.png')


if __name__ == "__main__":
    main(sys.argv)


