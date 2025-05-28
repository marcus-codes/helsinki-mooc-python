"""
Helsinki MOOC - Part 2: Simple Loops
Exercise: The next leap year

Task:
Please write a program which asks the user for a year, and prints out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028
"""

# Write your solution here
year = int(input("Year: "))
original_year = year

# check to see if the year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    year += 4

while True:
    # check to see if the year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"The next leap year after {original_year} is {year}")
        break
    else:
        year += 1


