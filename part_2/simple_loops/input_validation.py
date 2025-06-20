"""
Helsinki MOOC - Part 2: Simple Loops
Exercise: Input validation

Task:
Please write a program which asks the user for integer numbers.

If the number is below zero, the program should print out the message "Invalid number".

If the number is above zero, the program should print out the square root of the number using the Python sqrt function.

In either case, the program should then ask for another number.

If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

Below you'll find a reminder of how the sqrt function is used. Remember to import it in the beginning of the program.

# sqrt function will not work without this line in the beginning of the program
from math import sqrt

print(sqrt(9))
Sample output
3.0

An example of expected behaviour of your program:

Sample output
Please type in a number: 16
4.0
Please type in a number: 4
2.0
Please type in a number: -3
Invalid number
Please type in a number: 1
1.0
Please type in a number: 0
Exiting...
"""

from math import sqrt
# Write your solution here

while True:
    number = int(input("Please type in a number: "))

    if number > 0:
        print(sqrt(number))

    if number < 0:
        print("Invalid number")
    elif number == 0:
        break


print("Exiting...")

