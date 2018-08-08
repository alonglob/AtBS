import shutil
import os

abs_path = '/home/alon/PycharmProjects/AtBS/Chapter_9/'

# Copying Files and Folders:
# files: shutil.copy('source', 'destination')
shutil.copy('/home/alon/PycharmProjects/AtBS/Chapter_8/hello',abs_path)  # copies the source file to destination.

# folders: shutil.copytree('source', 'destination')
shutil.copytree(abs_path,'/home/alon/Chapter_9')  # creates the new folder and copies all the files from source to it.

# Moving and Renaming Files and Folders:
# shutil.move('source', 'destination')
shutil.move(abs_path + 'hello', '/home/alon/Chapter_9')  # moving to that folder
shutil.move(abs_path + 'hello', '/home/alon/chapter_9/hello_copy')  # moving the source file and renaming it

# Permanently Deleting Files and Folders:
# os.unlink(path)     - deletes file at path
# os.rmdir(path)      - deletes the folder at path, only if empty.
# shutil.rmtree(path) - deletes the folder and its contents permanently

# Safely Delete with the send2trash Module
import send2trash
my_file = open('new_file', 'a')  # creates a file
my_file.write('This new file will soon be sent to pc_hell')  # writes text to the file.
my_file.close()
send2trash.send2trash('new_file')  # sends the file to the trash

# Walking a Directory Tree
# the os.walk(path) returns 3 values back when iterated on with a for loop:
# * a string of the current folder
# * a list of strings of the subfolders in the current folder
# * a list of strings of the filenames in the current folder
import os
for folder_name, subfolders, filenames in os.walk('/home/alon/PycharmProjects/AtBS/'):
    print('the current folder is ' + folder_name)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': ' + filename)
    print('\n')

# Reading Zip Files
import zipfile
os.chdir('/home/alon/PycharmProjects/AtBS/Chapter_9/')
zipfile_object = zipfile.ZipFile('example.zip')
print(zipfile_object.namelist())
#=> ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
zipfile_info = zipfile_object.getinfo('spam.txt')
zipfile_info.file_size
#=> 13908
zipfile_info.compress_size
#=> 3828
'Compressed file is %sx smaller!' %(round(zipfile_info.file_size/zipfile_info.compress_size,2))
zipfile_object.close()

# Extracing from Zip Files
zipfile_object = zipfile.ZipFile('example.zip')
zipfile_object.extractall()  # extracts all the content to the cwd
zipfile_object.extract('spam.txt','/home/alon/PycharmProjects/AtBS/Chapter_9/')
zipfile_object.close()
# extracts a member to the cwd, or to the destination if specified

# Creating and Adding to Zip Files:
new_zip = zipfile.ZipFile('new.zip', 'w')  # opening\creating a new zip file in "write" mode
new_zip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

