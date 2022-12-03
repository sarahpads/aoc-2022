import sys

intersections = []

with open("input.txt") as input:
  for line in input:
    middle = int(len(line) / 2)
    compartment1 = set(line[0:middle])
    compartment2 = set(line[middle:])
    shared = compartment1.intersection(compartment2).pop()
    modifier = -38 if shared.isupper() else -96
    value = ord(shared) + modifier
    intersections.append(value)

  print(sum(intersections))

sys.exit()