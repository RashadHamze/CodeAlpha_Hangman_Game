# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:06:27 2024

@author: user
"""

import random

def game():
    words = ["python", "code", "alpha", "potato", "science", "computer","football", "party", "summer"]
    word = random.choice(words)
    word_length = len(word)
    
    tries = 8
    guessed = []
    display = "_" * word_length

    while tries > 0:
        print(display)
        inp = input("Guess a letter: ").lower()

        if inp in guessed:
            print("You already guessed that letter!")
        elif inp in word:
            index = word.find(inp)
            word_list = list(display)
            word_list[index] = inp
            display = "".join(word_list)
            if not "_" in display:
                print("Well Done. You guessed the word!")
                break
        else:
            tries -= 1
            print("Incorrect guess!")
            print("Number of tries left is " + tries + "!")
            guessed.append(inp)

    if tries == 0:
        print("You lost! The word is", word)

game()