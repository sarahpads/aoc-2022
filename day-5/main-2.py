import sys
from itertools import groupby
from re import sub, split

stacks = []

# grouping function that assigns a key to each line in the file
# groupby will generate a new group everytime this key changes, so
# this only works because our file is already organized into the chunks we want
def chunk(line):
  if line.startswith('move'):
    return 'moves'
  elif '[' in line:
    return 'stacks'
  else:
    return 'junk'

with open("input.txt") as input:
  for key, section in groupby(input, chunk):
    if key == 'stacks':
      # for each line in the stacks, replace any empty values with 0, and remove any other special characters/whitespace
      lines = [sub(r"[\[\]]", '', line.replace('    ', '0').replace(' ', '')).rstrip() for line in section]
      # we need to consider the data vertically, but files read horizontally
      # use zip in order to organize our input into the appropriate stacks
      # from [0, D, 0], [N, C, 0], [Z, M, P]
      # to [0, N, Z], [D, C, M], [0, 0, P]
      # (where the first index is the top of the stack)
      # and then filter out the placeholder 0s, which are no longer necessary
      stacks = [list(filter(lambda value: value != '0', column)) for column in zip(*lines)]

    elif key == 'moves':
      for line in section:
        # strip out the words and unpack our command into three values
        amount, source, dest = list(map(int, split('move | from | to ', line)[1:]))

        # crates at the top are at the lowest index, so remove from the source and place into the dest
        value = stacks[source - 1][0:amount]
        stacks[dest - 1] = stacks[source - 1][0:amount] + stacks[dest - 1]
        del stacks[source - 1][0:amount]

  # use zip to get a tuple of all first index values
  print(list(zip(*stacks)))

sys.exit()