#!/usr/bin/env python3.7
import os
#Remember 'w' mode truncate that file and write from the beginning.
file_obj_wrt = open("data_dir/new_names.txt",'w')
file_obj_read = open("data_dir/names.txt",'r')

#just an example to tell  start position of reading a file.
# After a first read() , the pointer will move the end of the file.
file_obj_read.seek(0)
for line in file_obj_read:
    if not line.strip() != "":
        continue
    #to strip the whitespace characters at begining and ending of the line
    file_obj_wrt.write(line.strip() + "\n")
    # print(line.strip())

file_obj_wrt.close()
file_obj_read.close()
