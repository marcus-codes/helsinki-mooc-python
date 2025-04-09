"""
Helsinki MOOC - Part 1: Getting Started
Exercise: Fix the code - Seven Brothers

Problem Statement:
The program should print the names of the brothers from 'Seitsemän veljestä'
in alphabetical order, but the original code has them in incorrect order.

Original Code:
print("Simeoni")
print("Juhani")
print("Eero")
print("Lauri")
print("Aapo")
print("Tuomas")
print("Timo")
"""

# Fixed Solution
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# Alternative Solution (More Scalable)
# brothers = ["Simeoni", "Juhani", "Eero", "Lauri", "Aapo", "Tuomas", "Timo"]
# for name in sorted(brothers):
#     print(name)
