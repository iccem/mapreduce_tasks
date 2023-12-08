
import random
import sys

DEBUG = 0

if DEBUG:
    stdin = open('in/partA_1.txt').readlines()
    stdout = open('out/map_result', 'w')

for line in sys.stdin if not DEBUG else stdin:
    try:
        num = random.randint(1, 1000000)
    except ValueError as e:
        continue
    if DEBUG:
        stdout.write(str(10000000 - 1 - num) + '\t' + line)
    else:
        print(str(10000000 - 1 - num) + '\t' + line)
