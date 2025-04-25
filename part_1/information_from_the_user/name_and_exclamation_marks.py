"""
Helsinki MOOC - Part 1: Information from the user
Exercise: Name and exclamation marks

Problem Statement:
Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the
beginning of the line, another between the two names and a third one at the end of the line.

The program should function as follows:

Sample output
What is your name? Paul
!Paul!Paul!
"""

# Your solution here
name = input("Enter your name")
print("!" + name + "!" + name + "!")