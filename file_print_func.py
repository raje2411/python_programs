#!/usr/bin/env python3.7
import os
def print_lines(file_obj,default=None):
    with open(file_obj, 'r') as f:
        for line in f :
            if not line.strip() != "":
                continue
            print(line.strip())
    return None
