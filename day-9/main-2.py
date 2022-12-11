import sys

positions = set()
# reference to our current coordinates
points = [[0,0] for i in range(10)]

with open("day-9/input.txt") as input:
  for line in input:
    direction, distance = line.rstrip().split(' ')
    print(direction, distance)

    for step in range(int(distance)):
      # move our head along appropriate access in the correct direction
      for i, point in enumerate(points):
        if i == 0:
          # index 0 is our x coordinate
          axis = 0 if direction == 'R' or direction == 'L' else 1
          # find out which direction we're moving in
          modifier = 1 if direction == 'R' or direction == 'U' else -1
          point[axis] += 1 * modifier

        else:
          head = points[i - 1]
          tail = point
          # clamp our diffs between -1 and 1
          diffX = max(-1, min(head[0] - tail[0], 1))
          diffY = max(-1, min(head[1] - tail[1], 1))
          # find the absolute difference between the previous and curren tpoint; add distance between both axes
          separation = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
          isDiagonal = abs(diffX) and abs(diffY)

          if isDiagonal and abs(separation) > 2:
            # move in both directions towards head
            tail[0] += diffX
            tail[1] += diffY

          elif not isDiagonal and abs(separation) > 1:
            tail[0] += diffX
            tail[1] += diffY

        if i == 9:
          positions.add(str(tail))

print(len(positions))

sys.exit()