#TODO-1 - Randomly choose a word from the word_list and assign to a variable called choosen_word. Then print it
#TODO-2 - Ask the user to guess a letter and assing their their answer to a variable called guess. Make guess lowercase
#TODO-3 - Check if the letter the user guessed (guess) is on of the letters in the choosen_word. Pring "Right" if it is "Wrong" if it's not

import random

word_list = ["apple", "banana", "pineapple", "berry"]

choosen_word = random.choice(word_list)

print(choosen_word)

guess = input("Please guess the letter ").lower()

for char in choosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")