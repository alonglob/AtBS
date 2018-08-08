import os

my_files = ['accounts.txt','details.csv','invite.docx']

# using os.path.join to make OS specific path's.
for filenames in my_files:
    print(os.path.join('/home/alon/',filenames))

# The Current Working Directory
os.getcwd()  # returns a string of the cwd
os.chdir('/home/alon')  # changes the cwd to the passed string.

# Absolute Vs. Relative Paths
os.path.abspath('/Documents')  # returns the absolute path of the relative path passed to the method.
os.path.isabs(os.getcwd())  # returns True because getcwd() returns the abs path of the cwd.
os.path.relpath('/home/alon/Documents', '/home/alon/')  # returns 'Documents' as the relative path

path = '/home/alon/pycharm.sh'
os.path.dirname(path)  # returns '/home/alon'
os.path.basename(path)  # returns 'pycharm.sh'
os.path.split(path)  # returns a tuple: ('/home/alon','pycharm.sh')
path.split(os.path.sep)  # returns a tuple: ('','home','alon','pycharm.sh')

# Finding File Sizes and Folder Content:
os.path.getsize('/home/alon/pycharm.sh')  # returns the filesize of the file passed to the method (in bytes).
os.listdir('/home/alon/Documents')  # returns the folders in the path passed to the method.

# together:
total_size = 0
path = '/home/alon/Documents/tf_records/'
for filename in os.listdir(path):
    total_size += os.path.getsize(path + filename)

# Checking Path Validity:
os.path.exists(path)  # returns True for a valid path
os.path.isfile(path)  # returns False because this is a directory
os.path.isdir(path)   # returns True because this is a directory

# Opening Files with the open() Function:
# the open() functions returns a File Object.
hello_file = open('./hello.txt')  # relative path
hello_file = open('/home/alon/PycharmProjects/AtBS/Chapter_8/hello.txt')  # absolute path

# Reading the Contents of Files:
# if you think of the contents of a file as a string, thats what this method returns:
string_from_file = hello_file.read()  # returns the string 'Hello World' stored in the file.
list_of_strings = hello_file.readlines()  # returns a list of all the lines that are breaked with a \n

# Writing to Files:
bacon_file = open('./bacon.txt','w')  # creating a new .txt file and opening it in 'write' mode
bacon_file.write('Hello World!\n')  # adds a string to the new .txt file. this method returns the number of total chars.
#=> 13
bacon_file.close()  # closing the file. "saving".
bacon_file = open('./bacon.txt','a')  # opening the file, this time in 'append' mode
bacon_file.write('Bacon is not a vegetable.')  # adding this string to the next line in the txt file (because \n)
#=> 25
bacon_file.close()
bacon_file = open('bacon.txt')
content = bacon_file.read()  # reads the file an returns a single string
bacon_file.close()
print(content)
#=> Hello World!
#=> Bacon is not a vegetable.

# Saving Variables with the Shelve Module
import shelve
shelve_file = shelve.open('my_data')  # create a file to store variables in
cats = ['Zhopie', 'Pooka', 'Simon']  # a list to store in the file.
shelve_file['cats'] = cats  # the key 'cats' will return the list cats
print(shelve_file['cats'])  # should return the list, just to make sure.
#=> ['Zhopie', 'Pooka', 'Simon']
shelve_file.close()  # close the file object.