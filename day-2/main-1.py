import sys
from enum import Enum

class ShapeScore(Enum):
  X = 1
  Y = 2
  Z = 3

class RoundScore(Enum):
  Win = 6
  Draw = 3
  Lose = 0

results = {
  ("A", "X"): RoundScore.Draw.value + ShapeScore.X.value,
  ("A", "Y"): RoundScore.Win.value + ShapeScore.Y.value,
  ("A", "Z"): RoundScore.Lose.value + ShapeScore.Z.value,
  ("B", "X"): RoundScore.Lose.value + ShapeScore.X.value,
  ("B", "Y"): RoundScore.Draw.value + ShapeScore.Y.value,
  ("B", "Z"): RoundScore.Win.value + ShapeScore.Z.value,
  ("C", "X"): RoundScore.Win.value + ShapeScore.X.value,
  ("C", "Y"): RoundScore.Lose.value + ShapeScore.Y.value,
  ("C", "Z"): RoundScore.Draw.value + ShapeScore.Z.value
}

score = 0

with open("input.txt") as input:
  for line in input:
    opponent, me = line.rstrip().split(" ")
    score += results[(opponent, me)]

print(score)

sys.exit()