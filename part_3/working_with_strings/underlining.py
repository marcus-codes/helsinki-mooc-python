"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: Underlining

Task:
Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below.
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string:
"""

# Write your solution here

# create a while loop that runs until an empty string is input

# the starting variable for the loop takes the users input string
user_str = input("")
# based on the length of the str, create a series of dashes the same length as the str
while len(user_str) > 0:
    print(user_str)
    print('-' * len(user_str))
    user_str = input("")
# print a blank space in order to line break?
# once it is printed - ask for a new user input

