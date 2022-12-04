import sys

count = 0

with open("input.txt") as input:
  for line in input:
    # use list comprehension to strip newlines and map each line into int arrays
    # use unpacking to assign each int pair to an elf
    elf1, elf2 = [list(map(int, elf.split('-'))) for elf in line.rstrip().split(',')]
    # construct a range out of the min/max values of each elf to find their overlap
    # if the highest start and lowest end create a valid range, we know they overlap
    # we need to add +1 to the min to make sure overlaps of a single number are counted
    # (range(7,7) has a length of 0, but in our case this counts as 1)
    overlap = len(range(max(elf1[0], elf2[0]), min(elf1[-1], elf2[-1]) + 1))

    # we know that they overlap entirely if the overlap is the same length as the smallest section
    if (overlap == min(len(range(*elf1)), len(range(*elf2))) + 1):
      count += 1

print('count', count)

sys.exit()