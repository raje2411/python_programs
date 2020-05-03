#!/usr/bin/env python3.7
import os
#Remember 'a+' mode will append the new data from the end of that file.  + will allow us to read the file as well.
file_obj_append = open("data_dir/new_names.txt",'a+')

#Before Append the content:-

print("++++++++++++++")
print("Before Append:")
print("++++++++++++++")
file_obj_append.seek(0)
for line in file_obj_append:
    if not line.strip() != "":
        continue
    #to strip the whitespace characters at begining and ending of the line
    #file_obj_append.write(line.strip() + "\n")
    print(line.strip())
print("++++++++++++++")


#to append some custom new lines to the existing file:
file_obj_append.write("This is the new line added using file_append_example.py" + "\n")

#After Append the content:-
print("++++++++++++++")
print("After  Append:")
print("++++++++++++++")
file_obj_append.seek(0)
for line in file_obj_append:
    if not line.strip() != "":
        continue
    #to strip the whitespace characters at begining and ending of the line
    #file_obj_append.write(line.strip() + "\n")
    print(line.strip())
print("++++++++++++++")

#close the file
file_obj_append.close()

