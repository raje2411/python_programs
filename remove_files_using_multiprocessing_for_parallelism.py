#!/usr/bin/env python3.7
import multiprocessing
import sys
import glob
import os
import subprocess
import datetime

def process_line(line_command):
    #subprocess.check_call(line_command, shell=True)
    os.unlink(line_command)
    # print(f"Executing this cmd : {line_command}")

num_cpu = multiprocessing.cpu_count()
job_pool = multiprocessing.Pool(200)

files_to_remove = glob.glob('/Users/rraman/python_programs/books/new/*.json')
#prefix_str = 'rm -r '
# suffix_str = '")'
#data = [prefix_str + sub for sub in files_to_remove ]
#rm_command_list = [x.strip("'") for x in data[:]]
#print(str(rm_command_list[:5]))
j = 0;
print(f'Remove process started at : { datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")}')
for i in range(int(len(files_to_remove)/1000)):
    print(f"iteration {i}")
    job_pool.map(process_line, files_to_remove[j:j+1000])
    j += 1000

print(f'Remove process ended at : { datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")}')
