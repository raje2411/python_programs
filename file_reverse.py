#!/usr/bin/env python3.7
import argparse
from file_print_func import print_lines
# Build parser
parser = argparse.ArgumentParser(description='Arg parse example program',prog='argparse_example.py')
parser.add_argument('filename', help='the file to be read')
parser.add_argument('--limit','-l', type=int, help='to limit the number of lines to be read')
parser.add_argument('--version','-v', action='version',version='%(prog)s 1.0')

args = parser.parse_args()

# Program to reverse the file
print("before reverse: ")
print("++++++++++++++++++++")
print_lines(args.filename)

print("++++++++++++++++++++")
print("After reverse: ")
print("++++++++++++++++++++")
with open(args.filename,'r') as f:
    lines = f.readlines()
    lines.reverse()

#if --limit argument is passed
if args.limit:
    lines = lines[:args.limit]

for line in lines:
    # print(line.strip()[::-1]) # To print each line in reverse
    print(line.strip()[::])
print("++++++++++++++++++++")
