import sys

x = 1
cycle = 0
buffer = None

with open("day-10/input.txt") as input:
  for cycle in range(240):
    # calculate what column we're printing to
    column = cycle % 40
    # if this is the end of the line, include a newline character
    end = "\n" if column == 39 else ""

    # determine if the sprite's current position overlaps with the current column
    if column in range(x - 1, x + 2):
      print("#", end=end)
    else:
      print(".", end=end)

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

sys.exit()