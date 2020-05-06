#!/usr/bin/env python3.7
# lib packages used on this program
import argparse
import os
import sys
from file_print_func import print_lines

# Build parser
parser = argparse.ArgumentParser(description='Arg parse example program',prog='sys_exit_code_example.py')
parser.add_argument('filename', help='the file to be read')
parser.add_argument('--filename','-f','-file', help='the file to be read')
parser.add_argument('--limit','-l', type=int, help='to limit the number of lines to be read')
#parser.add_argument('--limit','-l', help='to limit the number of lines to be read')
parser.add_argument('--version','-v', action='version',version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename,'r')
    limit = int(args.limit or 0)
except FileNotFoundError as file_err:
    print(f"\n{file_err}")
    print(f"\nSorry the file : {args.filename} doesn't exist in the path { os.getenv('PWD') }\n")
    print(f'Exit code 255')
    sys.exit(255)
except ValueError as val_err:
    print(f"\n{val_err}")
    print(f'\nLimit should be numeric value. example "sys_exit_code_example.py data_dir/new_names.txt  --limit 2" \n')
    print(f'Exit code 254')
    sys.exit(254)
else:
    print("Input Parse completed.\n\nProgram Started...\n")

# Program to reverse the file
print("before reverse: ")
print("++++++++++++++++++++")
print_lines(args.filename)

# To reverse the lines in the file and store in list lines[]
with open(args.filename,'r') as f:
    lines = f.readlines()
    lines.reverse()

#if --limit argument is passed
# and
# to remove the "" empty lines from the lines[] list before doing the slicing
if args.limit:
    new_lines= []
    for line in lines:
        if not line.strip() != "":
            continue
        new_lines += [line]
    #After cleanup of empty lines, slicing based on the limit
    lines = new_lines[:int(args.limit)]

print("\n\n++++++++++++++++++++")
if limit:
    print("After reverse(with limit): ")
else:
    print("After reverse:")
print("++++++++++++++++++++")

#Print the new lines[] list with removed whitelines
for line in lines:
    # print(line.strip()[::-1]) # To print each line in reverse
    if not line.strip() != "":
        continue
    print(line.strip())
print("++++++++++++++++++++")
