import sys

x = 1
cycle = 0
signals = []
buffer = None

with open("day-10/input.txt") as input:
  # our cycles start at 1
  for cycle in range(1, 221):
    # are we in a noteworthy cycle?
    if not (cycle - 20) % 40:
      print(cycle, x)
      signals.append(cycle * x)

    # is there a buffer we're waiting for?
    if buffer is not None:
      if buffer[0] == cycle:
        x += buffer[1]
        buffer = None
      continue

    line = input.readline().rstrip()

    # if this is a noop, just increment our cycle
    if "noop" in line:
      continue

    # if not a noop, this is an addx command - grab and parse the value
    value = int(line.split()[1])

    # else we need to add x to our buffer for 2 cycles from now
    buffer = (cycle + 1, value)

print(sum(signals))
sys.exit()