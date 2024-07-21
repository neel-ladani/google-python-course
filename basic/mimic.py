#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import random
import sys

def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    mimic_dict = {}
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    
    words = text.split()
    prev = ''
    for word in words:
        if prev not in mimic_dict:
            mimic_dict[prev] = [word]
        else:
            mimic_dict[prev].append(word)
        prev = word
    
    return mimic_dict

def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    output = []
    for _ in range(200):
        output.append(word)
        next_words = mimic_dict.get(word)
        if not next_words:
            next_words = mimic_dict['']  # Fallback to '' if not found
        word = random.choice(next_words)
    
    # Print output with line breaks
    line_length = 0
    for word in output:
        print(word, end=' ')
        line_length += len(word) + 1
        if line_length > 70:
            print()
            line_length = 0

def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py filename > out.txt')
        sys.exit(1)

    filename = sys.argv[1]
    mimic = mimic_dict(filename)
    print_mimic(mimic, '')

if __name__ == '__main__':
    main()
