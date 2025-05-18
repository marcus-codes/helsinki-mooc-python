"""
Helsinki MOOC - Part 2: Combining Conditions
Exercise: Grades and points

Task:
The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!
Some examples:

Sample output
How many points [0-100]: 37
Grade: fail

Sample output
How many points [0-100]: 76
Grade: 3

Sample output
How many points [0-100]: -3
Grade: impossible!
"""

# Write your solution here
user_grade = int(input("How many points [0-100]: "))

if user_grade <= 0 or user_grade > 100:
    print("Grade: impossible!")
elif user_grade < 50:
    print("Grade: fail")
elif user_grade < 60:
    print("Grade: 1")
elif user_grade < 70:
    print("Grade: 2")
elif user_grade < 80:
    print("Grade: 3")
elif user_grade < 90:
    print("Grade: 4")
else:
    print("Grade: 5")


