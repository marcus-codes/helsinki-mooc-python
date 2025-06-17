"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: Substrings, part 1

Task:
Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character,
from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test
"""

# Write your solution here

word = input("Please type in a string: ")

for i in range(1, len(word) + 1, 1):
    print(word[0:i])


