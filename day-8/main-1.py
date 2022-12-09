import sys

visible = 0

# solution relies on file read cursors in order to jump around the file and
# access specific characters

with open("input.txt") as input:
  # find out how many rows and columns we're dealing with
  # also grab the totalLength of the file (total number of characters)
  rowLength = sum(1 for line in input)
  totalLength = input.tell()
  input.seek(0) # reading the input moves our cursor, need to reset
  colLength = len(input.readline())
  input.seek(0)

  def isVisible(direction, position, value):
    # depending on what way we want to look, we need to modify our cursor differently
    # if looking up, we want to go back by a full row, which is the same as -columns
    # if looking down, we want to up by a full row
    # if looking left, we just want to look to the previous character
    # if right, the next character
    modifier = (
      -colLength if direction == 'top' else
      +colLength if direction == 'bottom' else
      -1 if direction == 'left'
      else +1
    )

    # calculate the newPosition of our cursor, this is the first neighbour
    newPosition = position + modifier

    try:
      # keep going through neighbours until we find one that is taller
      # or until we try to access an invalid position, which will enter
      # the except block
      while True:
        input.seek(newPosition)
        neighbour = input.read(1)

        if int(neighbour) >= int(value):
          return False
        else:
          newPosition += modifier
    except:
      return True

    return True

  # iterate over our file until we reach the end
  while True:
    position = input.tell()
    character = input.read(1)

    if not character:
      break

    if '\n' in character:
      continue

    # find out where we are in the file
    column = position % colLength
    row = position // colLength

    # if we're at an edge, we know we're visible
    if row == 0 or row == rowLength - 1 or column == 0 or column == colLength - 2: # subtract two to account for newline character
      visible += 1

    # otherwise, we're interior trees, find out if we're visible or not
    else:
      visible += (
        1 if isVisible('top', position, character) or
        isVisible('bottom', position, character) or
        isVisible('right', position, character) or
        isVisible('left', position, character) else 0
      )
      input.seek(position + 1)

  print(visible)

sys.exit()