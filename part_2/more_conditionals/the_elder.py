"""
Helsinki MOOC - Part 2: More Conditionals
Exercise: The elder

Task:
Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

Some examples of expected behaviour:

Sample output
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Sample output
Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
"""

# Write your solution here
p1_name = input("Name: ")
p1_age = int(input("Age: "))

p2_name = input("Name: ")
p2_age = int(input("Age: "))

if p1_age > p2_age:
    print(f"The elder is {p1_name}")

elif p2_age > p1_age:
    print(f"The elder is {p2_name}")

else:
    print(f"{p1_name} and {p2_name} are the same age")

