import sys
from itertools import groupby, count, zip_longest

length = 4
# length = 14 # part-2

with open("input.txt") as input:
  for line in input:
    start = 0
    for i in range(0,len(line) - length):
      sequence = line[start:start + length]
      start += 1
      if len(set(sequence)) == length:
        print(start + length - 1)
        break

sys.exit()