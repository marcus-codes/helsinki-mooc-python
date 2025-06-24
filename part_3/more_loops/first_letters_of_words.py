"""
Helsinki MOOC - Part 3: More Loops
Exercise: First letters of words

Task:
Please write a program which asks the user to type in a sentence.
The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w
"""

# Write your solution here

sentence = input("Please type in a sentence: ")

for i in range(len(sentence)):
    if i == 0 or sentence[i - 1] == " ":
        print(sentence[i])
