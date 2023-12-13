#! /usr/bin/env python3

import sys
import re

# 1 is local
DEBUG = 0

if DEBUG:
    stdin = open('in/articles-sample').readlines()
    stdout = open('mapper_result', 'w')

for line in sys.stdin if not DEBUG else stdin:
    words = []
    words_cleaned = []

    try:
        words = line.strip().split()
        for i in words:
            words_cleaned.append(re.sub('[^A-Za-z\\s]', '', i))
    except ValueError as e:
        continue
    for word in words_cleaned:
        word_tail = word[1:]
        if 6 <= len(word) <= 9:
            if DEBUG:
                if word.islower():
                    stdout.write(f'{word}\t0\t1\n')
                elif (word[0].isupper()) and word_tail.islower():
                    word = word.lower()
                    stdout.write(f'{word}\t1\t0\n')
            else:
                if word.islower():
                    print(f'{word}\t0\t1\n')
                elif (word[0].isupper()) and word_tail.islower():
                    word = word.lower()
                    print(f'{word}\t1\t0\n')
