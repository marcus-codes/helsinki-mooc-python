"""
Helsinki MOOC - Part 1: Arithmetic operations
Exercise: Sum and mean

Problem Statement:

Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:

Sample output
Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""

# Your solution here
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))
number_4 = int(input("Number 4: "))

sum_of_num = number_1 + number_2 + number_3 + number_4
mean_of_num = sum_of_num / 4

print(f"The sum of the numbers is {sum_of_num} and the mean is {mean_of_num}")
