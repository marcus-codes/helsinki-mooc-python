"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: A line of hashes

Task:
Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

Sample output
Width: 3

###
Sample output
Width: 8

########
"""

# Write your solution here

# store the hash symbol as a variable
hash_var = '#'
# get the user to input how many hashes they want
user_num_input = int(input("Width: "))
# update the hash variable with the user input and store in a variable
hash_var = hash_var * user_num_input
# concatenate the hash variable by the number that the user input
print(hash_var)
