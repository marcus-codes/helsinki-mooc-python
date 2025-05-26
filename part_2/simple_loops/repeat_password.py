"""
Helsinki MOOC - Part 2: Simple Loops
Exercise: Repeat password

Task:
Please write a program which asks the user for a password. The program should then ask the user to type in the password again.
If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

Have a look at the expected behaviour below:

Sample output
Password: sekred
Repeat password: secret
They do not match!
Repeat password: cantremember
They do not match!
Repeat password: sekred
User account created!
"""

# Write your solution here
p1 = input("Password: ")
p2 = input("Repeat password: ")

while True:
    if p1 == p2:
        print("User account created!")
        break
    else:
        print("They do not match!")
        p2 = input("Repeat password: ")

