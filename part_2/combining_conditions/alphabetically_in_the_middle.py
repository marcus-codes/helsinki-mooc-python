"""
Helsinki MOOC - Part 2: Combining Conditions
Exercise: Alphabetically in the middle

Task:
Please write a program which asks the user for three letters.
The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
"""

# Write your solution here
letter_one = input("1st letter: ")
letter_two = input("2nd letter: ")
letter_three = input("3rd letter: ")

middle_letter =  ""

if letter_one < letter_two and letter_one > letter_three:
    middle_letter = letter_one
elif letter_one > letter_two and letter_one < letter_three:
    middle_letter = letter_one

if letter_two < letter_one and letter_two > letter_three:
    middle_letter = letter_two
elif letter_two > letter_one and letter_two < letter_three:
    middle_letter = letter_two

if letter_three < letter_one and letter_three > letter_two:
    middle_letter = letter_three
elif letter_three > letter_one and letter_three < letter_two:
    middle_letter = letter_three

print(f"The letter in the middle is {middle_letter}")




