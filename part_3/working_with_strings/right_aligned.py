"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: Right-aligned

Task:
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed.
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python

**************python
Sample output
Please type in a string: alongerstring

*******alongerstring
Sample output
Please type in a string: averyverylongstring

*averyverylongstring
"""

# Write your solution here

# get a user input for the string
user_str = input("Please type in a string: ")
stars_str = ''
# get the length of the str - if it's less than 20, create a loop
for i in range((20 - len(user_str)), 0, -1):
    stars_str += '*'
    # print(stars_str)
print(stars_str + user_str)
# the loop should start at 20 - the str length and count down to 0
# each iteration of the loop should add a new * to the str
