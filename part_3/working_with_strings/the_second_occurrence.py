"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: The second occurrence

Task:
Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence,
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.
"""

# Write your solution here
word = input("Please type in a word: ")
substring = input("Please type in a character: ")

first_index = word.find(substring)
second_index = word.find(substring, first_index + len(substring))

if first_index == -1:
    print("The substring does not occur twice in the string.")
elif second_index != -1:
    print(f"The second occurrence of the substring is at index {second_index}.")
else:
    print("The substring does not occur twice in the string.")









