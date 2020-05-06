#!/usr/bin/env python3.7
import argparse

parser = argparse.ArgumentParser(description='Arg parse example program',prog='argparse_example.py')
parser.add_argument('filename', help='the file to be read')
parser.add_argument('--limit','-l', type=int, help='to limit the number of lines to be read')
parser.add_argument('--version','-v', action='version',version='%(prog)s 1.0')

args = parser.parse_args()

print(args)
