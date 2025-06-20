"""
Helsinki MOOC - Part 3: Working With Strings
Exercise: A framed word

Task:
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Sample output
Word: testing

******************************
*          testing           *
******************************
Sample output
Word: python

******************************
*           python           *
******************************
"""

# Write your solution here

word = input("Word: ")
left_padding = (29 - len(word)) // 2
right_padding = (28 - len(word) - left_padding)
print('*' * 30)
print('*' + left_padding*' ' + word + right_padding*' ' + '*')
print('*' * 30)
