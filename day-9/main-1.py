import sys

positions = set()

# reference to our current coordinates
head = [0, 0]
tail = [0, 0]

with open("input.txt") as input:
  for line in input:
    direction, distance = line.rstrip().split(' ')
    print(direction, distance)
    # index 0 is our x coordinate
    axis = 0 if direction == 'R' or direction == 'L' else 1
    # find out which direction we're moving in
    modifier = 1 if direction == 'R' or direction == 'U' else -1

    for step in range(int(distance)):
      # move our head along appropriate access in the correct direction
      head[axis] += 1 * modifier
      # find the absolute difference between the head and tail; add distance between both axes
      separation = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
      # find out if the head and tail are diagonal from each other
      isDiagonal = head[1 - axis] != tail[1 - axis]

      # if we are diagonal, we only want to move if the separation is greater than 2
      if isDiagonal and abs(separation) > 2:
        # move our tail along the appropriate axis
        tail[axis] += 1 * modifier
        # make sure our other axis is the same as head
        tail[1 - axis] = head[1 - axis]

      # otherwise, we want to move the tail if they aren't side-by-side
      elif not isDiagonal and (abs(separation) > 1):
        tail[axis] += 1 * modifier

      positions.add(str(tail))

print(len(positions))

sys.exit()