"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: The longer string

Task:
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is,
whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long
"""

# Write your solution here
str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

if len(str1) > len(str2):
    print(str1, "is longer")
elif len(str2) > len(str1):
    print(str2, "is longer")
else:
    print("The strings are equally long")
