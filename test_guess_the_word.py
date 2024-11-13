#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:32:37 2024

@author: macbookpro

Cis 256 

Florentin Popescul
"""

# test guess the word

from guess_the_word import select_random_word, display_word

# Test if the game selects a word from the correct list
def test_select_random_word():
    word = select_random_word()
    assert word in ["python", "programming", "developer", "debug", "function"]

# Test the display function with guessed letters
def test_display_word():
    word = "developer"
    guessed_letters = {'d', 'e', 'v'}
    displayed = display_word(word, guessed_letters)
    assert displayed == "dev__o__r"

# Test display with no guessed letters
def test_display_no_guesses():
    word = "python"
    guessed_letters = set()
    displayed = display_word(word, guessed_letters)
    assert displayed == "______"
