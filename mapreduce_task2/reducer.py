#! /usr/bin/env python3

import sys

# 1 is local
DEBUG = 0

current_key = None
word_sum = 0
flag_sum = 0

if DEBUG:
    stdin = open('mapper_result').readlines()
    stdout = open('reducer_result', 'w')

for line in sys.stdin if not DEBUG else stdin:
    try:
        key, count, flag = line.strip().split('\t', 2)
        count = int(count)
        flag = int(flag)
    except ValueError as e:
        continue

    if current_key != key:
        if current_key:
            if DEBUG:
                stdout.write(f'{current_key}\t{word_sum}\t{flag_sum}\n')
            else:
                print(f'{current_key}\t{word_sum}\t{flag_sum}\n')
        word_sum = 0
        flag_sum = 0
        current_key = key
    word_sum += count
    flag_sum += flag

if current_key:
    if DEBUG:
        stdout.write(f'{current_key}\t{word_sum}\t{flag_sum}\n')
    else:
        print(f'{current_key}\t{word_sum}\t{flag_sum}\n')
