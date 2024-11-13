#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:31:30 2024

@author: macbookpro

Cis 256 

Florentin Popescul
"""

#guess_the_word.py

import random

# Predefined list of words
words_list = ["python", "programming", "developer", "debug", "function"]

def select_random_word():
    #Select a random word from words_list
    return random.choice(words_list)

def display_word(word, guessed_letters):
    #Display the word with guessed letters and underscores
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def play_game():
    word_to_guess = select_random_word()
    guessed_letters = set()
    attempts_left = len(word_to_guess) + 3  # Arbitrary attempts count

    print("Welcome to Guess the Word!")
    
    while attempts_left > 0:
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            attempts_left -= 1
            print("Incorrect guess.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word '{word_to_guess}'!")
            break
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    play_game()
