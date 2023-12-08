
import sys
import random

temp_strint = []
tt = ''

DEBUG = 0

if DEBUG:
    stdin = open('sorted_result').readlines()

for line in sys.stdin if not DEBUG else stdin:
    try:
        temp, id = line.strip().split('\t', 1)
    except ValueError as e:
        continue
    temp_strint.append(id)
    if len(temp_strint) > 6:
        lenght_string = random.randint(1, 5)
        for i in range(0, lenght_string):
            tt += temp_strint.pop(0) + ','
        print(tt[:-1])
    tt = ''
