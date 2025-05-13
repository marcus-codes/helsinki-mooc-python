"""
Helsinki MOOC - Part 2: More Conditionals
Exercise: Greater than or equal to

Task:
Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

Some examples of expected behaviour:

Sample output
Please type in the first number: 5
Please type in another number: 3
The greater number was: 5

Sample output
Please type in the first number: 5
Please type in another number: 8
The greater number was: 8

Sample output
Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
"""

# Write your solution here
num_one = int(input("Please type in the first number: "))
num_two = int(input("Please type in the second number: "))

if num_one == num_two:
    print("The numbers are equal!")

elif num_one > num_two:
    print(f"The greater number was: {num_one}")

else:
    print(f"The greater number was: {num_two}")

