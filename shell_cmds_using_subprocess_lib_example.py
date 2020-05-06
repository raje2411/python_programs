#!/usr/bin/env python3.7
import subprocess

# Function code to execute shell commands
def subprocess_run(cmd,default=['pwd']):
    '''
    Create a proc variable and call run method from subprocess to execute.
    All output is stored in proc variable
    '''
    proc = subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print (f"Command executed: {proc.args[:]}")     #To access the commands that it executed
    print (f"Command returncode: {proc.returncode}")    #To check the return code of the commands run
    print(f"\nStdout stored in proc: \n{(proc.stdout).decode()}")   #To get the stdout output in prettier format.   stdout is by default binary stream, which is not formatted.

#Prepare the input commands to be executed in a separate list for each cmd
ls_cmd = ['ls','-lrt']
df_cmd = ['df','-h']

#First iteration on ls_cmd
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
subprocess_run(ls_cmd)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#Second iteration on df_cmd
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
subprocess_run(df_cmd)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
