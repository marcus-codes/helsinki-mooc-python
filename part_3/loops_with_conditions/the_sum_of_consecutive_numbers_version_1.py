"""
Helsinki MOOC - Part 3: Loops With Conditions
Exercise: The sum of consecutive numbers, version 1

Task:
Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers
(1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

Sample output
Limit: 2
3

Sample output
Limit: 10
10

Sample output
Limit: 18
21

If you have trouble understanding how the desired output is calculated, the sample outputs in the next exercise may help.
You may assume the number typed in by the user is always equal to 2 or higher.
"""

# Write your solution here
limit = int(input("Limit: "))
current = 1
calculation = 0

while calculation < limit:
    calculation += current
    current += 1

print(calculation)




