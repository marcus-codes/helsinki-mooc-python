"""
Helsinki MOOC - Part 2: More Conditionals
Exercise: Alphabetically last

Task:
Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
only the standard English alphabet of a to z, or A to Z, is used.
Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Sample output:
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

Sample output:
Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.

Sample output:
Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
"""

# Write your solution here
word_one = input("Please type in the 1st word: ")
word_two = input("Please type in the 2nd word: ")

if word_one < word_two:
    print(f"{word_two} comes alphabetically last.")

elif word_two < word_one:
    print(f"{word_one} comes alphabetically last.")

else:
    print("You gave the same word twice.")

