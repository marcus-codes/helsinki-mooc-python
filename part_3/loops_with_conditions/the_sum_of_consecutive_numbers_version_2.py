"""
Helsinki MOOC - Part 3: Loops With Conditions
Exercise: The sum of consecutive numbers, version 2

Task:
Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

You may assume the number typed in by the user is always equal to 2 or higher.
"""

# Write your solution here
limit = int(input("Limit: "))
current = 1
calculation = 0
print_sum = f"The consecutive sum: "

while calculation < limit:
    if calculation + current >= limit:
        print_sum += f"{current}"
    else:
        print_sum += f"{current} + "

    calculation += current
    current += 1

print(f"{print_sum} = {calculation}")
