#! /usr/bin/python3.7

import subprocess
import os

file_obj = open('hello.txt', 'w')
file_obj.write('Hello World')
file_obj.close()

subprocess.Popen(['kate', 'sudoedit', 'hello.txt'])  # runs a command-line (bash) command