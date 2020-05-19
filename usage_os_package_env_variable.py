#!/usr/bin/env python3.7

'''
Script usage:

DIGITS=5 python3 usage_os_package_env_variable.py
 or
DIGITS=5 usage_os_package_env_variable.py
or
python3 usage_os_package_env_variable.py
'''

import os
from os import getenv
from math import pi

# Input and it's validation
while True:
    try:
        #my_float = int(input("Enter the number of floating digits for pi output(1-10): ") or 10)
        my_float = int(getenv("DIGITS") or getenv("DIGITS".lower()) or 10)
        if isinstance(my_float,int):
            float_precision = '.'+str(my_float)+'f'
            break
        else:
            print("Else : Oops the entered value is not a number, please retry..")
    except ValueError:
        print("Oops the entered value is not a number, please retry..")
        continue

# print(format(math.pi,'.10f'))  - To print pi number.
print(f"Pi is : { format(pi,float_precision) }")
print(f"The user who ran this program : {getenv('USER') }")
print(f"This program is executed from the path : {getenv('PWD') }")
print(f"Dump of all OS env variables:\n\n {os.environ}")

