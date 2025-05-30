"""
Helsinki MOOC - Part 2: Simple Loops
Exercise: Working with numbers

Task:
Pre-task
Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

Sample output
Please type in integer numbers. Type in 0 to finish.
Number: 5
Number: 22
Number: 9
Number: -2
Number: 0

Part 1: Count
After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

Sample output
... the program asks for numbers
Numbers typed in 4

Part 2: Sum
The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

The program should now print out the following:

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34

Part 3: Mean
The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation.
You may assume the user will always type in at least one valid non-zero number.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5

Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers were positive and how many were negative.
The zero at the end should not be included in the calculation.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3
Negative numbers 1
"""

# Write your solution here

increment = 0
num_add = 0
pos = 0
neg = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number "))

    if num == 0:
        break

    increment += 1
    num_add += num

    if num < 0:
        neg += 1
    else:
        pos += 1

print(f"Numbers typed in {increment}")
print(f"The sum of the numbers is {num_add}")
print(f"The mean of the numbers is {num_add / increment}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")

