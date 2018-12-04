#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Crossword Solver Program """

__author__ = "davidstewy"

import re


def word_find(input_word, word_list):
    altered_word = input_word.replace(' ', '.')
    regexed_word = re.compile(altered_word)
    for word in word_list:
        if len(input_word) == len(word):
            if re.match(regexed_word, word):
                print word


def main():
    words = []
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown \
        letters: ').lower()

    word_find(test_word, words)


if __name__ == '__main__':
    main()
