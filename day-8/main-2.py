import sys
from math import prod

maxScenicScore = 0

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

  edge = 0

  def scenicFactor(direction, position, value):
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
    score = 0

    try:
      # keep going through neighbours until we find one that is taller
      # or until we try to access an invalid position, which will enter
      # the except block
      while True:
        input.seek(newPosition)
        neighbour = input.read(1)

        if int(neighbour) >= int(value):
          score += 1
          return score
        else:
          score += 1
          newPosition += modifier
    except:
      return score

    return score

  # iterate over our file until we reach the end
  while True:
    position = input.tell()
    character = input.read(1)

    if not character:
      break

    if '\n' in character:
      continue

    # multiply our scenicFactors together to get a score
    scenicScore = prod([
      scenicFactor('top', position, character),
      scenicFactor('bottom', position, character),
      scenicFactor('left', position, character),
      scenicFactor('right', position, character)
    ])

    # grab whichever one is highest - our current factor or the reigning champ
    maxScenicScore = max(maxScenicScore, scenicScore)
    input.seek(position + 1)

  print(maxScenicScore)

sys.exit()
