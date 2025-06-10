"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: End to beginning

Task:
Please write a program which asks the user for a string. The program then prints out the input string in reversed order,
from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h
"""

# Write your solution here
input_string = input("Please type in a string: ")
index = -1
while index >= -len(input_string):
    print(input_string[index])
    index -= 1
