#!/usr/bin/env python3.7

# Function to print the message
def print_message(message,count) :
    temp_count = 1
    while count > 0 :
        print(f"{temp_count} : {message}")
        count -= 1
        temp_count += 1

# Program starts here
# GET Input message, count
message = input("Enter your message to be echoed : ")
while True :
    try :
        count = int(input("Enter the number of time to echo this msg : ") or 1)  # If no number given, count will be default to 1
        break
    except ValueError :
        print("Oops! That was not a valid number.  Try again...")
a = "rajesh"
if a:
    print(a)
else:
    print("a is False")
# Call function to print message
print_message(message, count)
