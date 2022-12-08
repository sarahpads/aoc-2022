import sys
from functools import reduce
from operator import add

directories = {}

with open("input.txt") as input:
  # keep track of our current working directory
  cwd = []

  for line in input:
    if line.startswith('$ cd'):
      # if this is a cd command, find out what directory we need to go to
      _, _, directory = line.rstrip().split(' ')
      if directory == '..':
        # if we're navigating up a level, remove the current directory from cwd
        cwd.pop()
      else:
        # if we're navigating down a level, add it to the cwd
        cwd.append(directory)

    # if this is a file listing with a size, add it to the total size of every directory
    # in our cwd hierarchy
    elif not (line.startswith('$ ls') or 'dir' in line):
      size, name = line.rstrip().split(' ')

      for i in range(len(cwd)):
        path = "".join(cwd[0:i+1])
        directories.setdefault(path, 0)
        directories[path] += int(size)

# part 1
maxFileSize = 100000
# find all of our directories that are smaller than 100000 and add them together
total = reduce(add, filter(lambda value: value <= maxFileSize, directories.values()))

# part 2
totalSpace = 70000000
requiredSpace = 30000000
remainingSpace = totalSpace - directories['/']
spaceNeeded = requiredSpace - remainingSpace
# find all of our directories that are large enough and pick the smallest amongst them
total = min(filter(lambda value: value >= spaceNeeded, directories.values()))

sys.exit()