import sys
from itertools import zip_longest

intersections = []

def elf(elf):
  return set(elf.rstrip())

with open("input.txt") as input:
  # iterate over our file in groups of three, assign each line to its own var
  for elf1, elf2, elf3 in zip_longest(*[map(elf, input)] * 3):
    # find intersections amongst all three elves and grab the first item
    shared = elf1.intersection(elf2.intersection(elf3)).pop()
    modifier = -38 if shared.isupper() else -96
    value = ord(shared) + modifier
    intersections.append(value)

  print(sum(intersections))

sys.exit()