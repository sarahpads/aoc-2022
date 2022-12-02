import sys

elves = [0]

with open("input.txt") as input:
  for line in input:
    if not line.rstrip():
      elves.append(0)
    else:
      elves[-1] += int(line.rstrip())

print(f'Part 1: {max(elves)}')

elves.sort(reverse = True)

print(f'Part 2: {sum(elves[0:3])}')

sys.exit()