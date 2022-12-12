import sys
import re
import math
from itertools import groupby

monkeys = []

class Monkey:
  def __init__(self, items, operation, test, truthy, falsey):
    self.activity = 0
    self.items = items
    self.operation = operation
    self.test = test
    self.truthy = truthy
    self.falsey = falsey

with open("day-11/input.txt") as input:
  for monkey in map(lambda value: list(value[1]), filter(lambda value: value[0], groupby(map(str.strip, input), key=lambda line: line != ""))):
    items = [int(item) for item in re.sub("[^0-9,]", "", monkey[1]).split(",")]
    operation = monkey[2].split("=")[1]
    test = int(monkey[3].split("divisible by")[1])
    truthy = int(monkey[4].split("monkey")[1])
    falsey = int(monkey[5].split("monkey")[1])
    monkeys.append(Monkey(items, operation, test, truthy, falsey))

  for round in range(20):
    for monkey in monkeys:
      while len(monkey.items):
        monkey.activity += 1
        old = monkey.items.pop()
        worry = math.floor(eval(monkey.operation) / 3)
        destinationMonkey = monkey.truthy if worry % monkey.test == 0 else monkey.falsey
        monkeys[destinationMonkey].items.append(worry)

# construct a list of items, sort them in descending order, pick the top 2, and multiply them together
print(math.prod(sorted(list(map(lambda monkey: monkey.activity, monkeys)), reverse=True)[:2]))

sys.exit()