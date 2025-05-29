"""
Helsinki MOOC - Part 2: Simple Loops
Exercise: Story

Task:
Part 1
Please write a program which keeps asking the user for words. If the user types in end,
the program should print out the story the words formed, and finish.

Sample output
Please type in a word: Once
Please type in a word: upon
Please type in a word: a
Please type in a word: time
Please type in a word: there
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl

Part 2
Change the program so that the loop ends also if the user types in the same word twice in a row.

Sample output
Please type in a word: It
Please type in a word: was
Please type in a word: a
Please type in a word: dark
Please type in a word: and
Please type in a word: stormy
Please type in a word: night
Please type in a word: night
It was a dark and stormy night
"""

# Your solution here
# Write your solution here
first_word = input("Please type in a word: ")
prev_word = ""

while True:
    next_word = input("Please type in a word: ")

    if next_word == prev_word or next_word == first_word:
        break

    prev_word = next_word

    # checking for the end word condition
    if next_word == "end":
        break
    else:
        first_word += " " + next_word

print(first_word)
