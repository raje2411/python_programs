#!/usr/bin/env python3.7
import os
#Using my own python script to print_lines for better looking code
from file_print_func import print_lines
file_name = "data_dir/new_names.txt"

#Before Append the content:-

print("++++++++++++++")
print("Before Append:")
print("++++++++++++++")
# file_obj_append.seek(0)
print_lines(file_name)
print("++++++++++++++")


#to append some custom new lines to the existing file:
print("\nTrying to append...\n")
#Remember 'a+' mode will append the new data from the end of that file.  + will allow us to read the file as well.
file_obj_append = open(file_name,'a+')
file_obj_append.write("This is the new line added using file_append_example.py" + "\n")
file_obj_append.close()
print("\nAppend finished and file is closed\n")

#After Append the content:-
print("++++++++++++++")
print("After Append:")
print("++++++++++++++")
# file_obj_append.seek(0)
print_lines(file_name)
print("++++++++++++++")

# #close the file
# file_obj_append.close()

