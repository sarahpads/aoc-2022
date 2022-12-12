import sys
import re
import math
from itertools import groupby
import operator

ops = {
  "+": operator.add,
  "-": operator.sub,
  "*": operator.mul,
  "/": operator.truediv,
  "%": operator.mod,
  "^": operator.xor,
}

monkeys = []

class Monkey:
  def __init__(self, items, op, num, test, truthy, falsey):
    self.activity = 0
    self.items = items
    self.op = ops[op]
    self.num = int(num) if num.isnumeric() else None
    self.test = test
    self.truthy = truthy
    self.falsey = falsey

with open("day-11/input.txt") as input:
  for monkey in map(lambda value: list(value[1]), filter(lambda value: value[0], groupby(map(str.strip, input), key=lambda line: line != ""))):
    items = [int(item) for item in re.sub("[^0-9,]", "", monkey[1]).split(",")]
    op, num = monkey[2].split("= old ")[1].split(" ")
    test = int(monkey[3].split("divisible by")[1])
    truthy = int(monkey[4].split("monkey")[1])
    falsey = int(monkey[5].split("monkey")[1])
    monkeys.append(Monkey(items, op, num, test, truthy, falsey))

# find a common denominator amongst all of our monkeys
prime = math.prod(map(lambda monkey: monkey.test, monkeys))

for round in range(10000):
  for i, monkey in enumerate(monkeys):
    while len(monkey.items):
      monkey.activity += 1
      item = monkey.items.pop()
      # instead of storing the result of the test, we can store its modulus against the prime
      # this will prevent our numbers from becoming too big
      worry = monkey.op(item, item if monkey.num is None else monkey.num) % prime
      destinationMonkey = monkey.truthy if worry % monkey.test == 0 else monkey.falsey
      monkeys[destinationMonkey].items.append(worry)

# construct a list of items, sort them in descending order, pick the top 2, and multiply them together
print(math.prod(sorted(list(map(lambda monkey: monkey.activity, monkeys)), reverse=True)[:2]))

sys.exit()