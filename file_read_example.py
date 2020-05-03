#!/usr/bin/env python3.7
import os

#opening a file with read mode
file_obj = open("data_dir/names.txt",'r')

#iterate through each line of file to remove blank lines and print the non-empty lines
for line in file_obj:
    if not line.strip() != "":
        continue
    print(line.strip())

#close the file
file_obj.close()
