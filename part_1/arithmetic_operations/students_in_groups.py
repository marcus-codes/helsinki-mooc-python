"""
Helsinki MOOC - Part 1: Arithmetic operations
Exercise: Students in groups

Problem Statement:

Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

Sample output
How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

Sample output
How many students on the course? 11
Desired group size? 3
Number of groups formed: 4

Hint: the integer division operator // could come in handy here.
"""

# Write your solution here
no_of_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

full_groups = no_of_students // group_size
leftover_students = no_of_students % group_size

if leftover_students > 0:
    full_groups += 1

print(f"Number of groups formed: {full_groups}")

