#! /usr/bin/env python3

import sys

# 1 is local
DEBUG = 0

if DEBUG:
    stdin = open('reducer_result').readlines()
    stdout = open('mapper_2_result', 'w')

for line in sys.stdin if not DEBUG else stdin:
    words = []

    try:
        key, count, flag = line.strip().split('\t', 2)
        flag = int(flag)
    except ValueError as e:
        continue

    if flag > 0:
        continue
    else:
        if DEBUG:
            stdout.write(f'{key}\t{count}\n')
        else:
            print(f'{key}\t{count}\n')
