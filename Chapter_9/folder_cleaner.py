#! /usr/bin/python3.6
# remember to allow execution of the file with 'chmod +x <filename>.py'
# folder_cleaner - cleans folders from many different extension files (.txt,.csv.zip... etc)
# Usage: folder_cleaner <source> <destination>

import zipfile
import os
import sys


def cleaner(source, destination=True):
    if destination:
        destination = source + '../'  # the destination is the dir before the source dir

    main_zip = zipfile.ZipFile(os.path.join(destination, 'cleaner.zip'), 'w')  # creates the new .zip

    for folder_name, subfolders, file_names in os.walk(source):  # walk through the dir 'touching' every file
        for file in file_names:
            _, extension = str(file).split('.')  # find the extension of the file to specify its new folder.
            main_zip.write(source + file, extension + '/' + file, zipfile.ZIP_DEFLATED)

    main_zip.close()


num_arguments = len(sys.argv)
destination = ''

if num_arguments == 3:
    file_name, source, destination = sys.argv

    if not str(source).endswith('/'):  # make sure the paths contain '/' at the end.
        source = str(source) + '/'
    if not str(destination).endswith('/'):
        destination = str(destination) + '/'

    cleaner(source, destination)

elif num_arguments == 2:
    file_name, source = sys.argv
    cleaner(source)

else:
    if num_arguments > 3:
        print('too many arguments passed to script')
    else:
        print('no arguments passed.')


