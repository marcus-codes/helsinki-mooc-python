"""
Helsinki MOOC - Part 1: Arithmetic operations
Exercise: Seconds in a day

Problem Statement:

Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

The program should function as follows:

Sample output
How many days? 1
Seconds in that many days: 86400

Another example:

Sample output
How many days? 7
Seconds in that many days: 604800
"""

# Your solution here
days = input("How many days? ")
days_converted = int(days)
seconds = days_converted * 24 * 60 * 60

print(f"Seconds in that many days: {seconds}")
