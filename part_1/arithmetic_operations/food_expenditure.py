"""
Helsinki MOOC - Part 1: Arithmetic operations
Exercise: Food expenditure

Problem Statement:

Please write a program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical food expenditure both weekly and daily.

The program should function as follows:

Sample output
How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""

# Your solution here
cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
cafeteria_price = float(input("The price of a typical student lunch? "))
weekly_groceries = float(input("How much money do you spend on groceries in a week? "))

weekly_total = cafeteria * cafeteria_price + weekly_groceries

print(f"Daily: {weekly_total / 7} euros")
print(f"Weekly: {weekly_total} euros")
