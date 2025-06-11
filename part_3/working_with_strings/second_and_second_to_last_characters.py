"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: Second and second to last characters

Task:
Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the
second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""

# Write your solution here

# ask the user to input a string
user_string = input("Please type in a string: ")
# store the last char in the str in a variable
second_last_char = user_string[-2]
# store the 2nd last char in the str as a variable
second_char = user_string[1]
# check if both variables are equal, use an if statement
if second_last_char == second_char:
    print(f"The second and the second to last characters are {second_last_char}")
else:
    print("The second and the second to last characters are different")
# print 1 of 2 messages, either they're different, or print the letter that they are

