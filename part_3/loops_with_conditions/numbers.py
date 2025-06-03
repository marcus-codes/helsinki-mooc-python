"""
Helsinki MOOC - Part 3: Loops With Conditions
Exercise: Numbers

Task:
Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

Sample output
Upper limit: 5
1
2
3
4
"""

# Write your solution here
num = int(input("Upper limit: "))
start = 1

while start < num:
    print(start)
    start += 1

