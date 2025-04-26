"""
Helsinki MOOC - Part 1: Information from the user
Exercise: Name and address

Problem Statement: Please write a program which asks for the user's name and address.
The program should also print out the given information, as follows:

Sample output
Given name: Steve
Family name: Sanders
Street address: 91 Station Road
City and postal code: London EC05 6AW
Steve Sanders
91 Station Road
London EC05 6AW
"""

# Your solution here
name = input("Enter your name")
surname = input("Enter your surname")
address = input("Enter your address")
city = input("Enter your City and postal code")

print(name + " " + surname)
print(address)
print(city)