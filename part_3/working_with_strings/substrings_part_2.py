"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: Substrings, part 2

Task:
Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character,
from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test
"""

# Write your solution here

# variable as user input
# start a for loop that starts at -1 and moves down to the final index of the str
# print the word with the index starting at the i var and moving to the first index
s = input("Please type in a string: ")
for i in range(1, len(s), +1):
    print(s[-i:])



