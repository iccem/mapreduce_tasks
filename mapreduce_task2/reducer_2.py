#! /usr/bin/env python3

import sys

# 1 is local
DEBUG = 0

current_key = None
word_sum = 0

if DEBUG:
    stdin = open('mapper_2_result').readlines()
    stdout = open('reducer_2_result', 'w')

for line in sys.stdin if not DEBUG else stdin:
    try:
        key, count = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue

    if current_key != key:
        if current_key:
            print(f'{current_key}\t{word_sum}')
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    print(f'{current_key}\t{word_sum}')
