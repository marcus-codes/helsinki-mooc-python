"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: A rectangle of hashes

Task:
Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########
"""

# Write your solution here

# get the width from the user
width = int(input("Width: "))
# get the height from the user
height = int(input("Height: "))
# create a for loop that creates rows based on the height input
for _ in range(0, height, 1):
    print('#'*width)


