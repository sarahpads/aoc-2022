import sys
from enum import Enum

class ShapeScore(Enum):
  Rock = 1
  Paper = 2
  Sciccors = 3

class RoundScore(Enum):
  X = 0
  Y = 3
  Z = 6

results = {
  ("A", "X"): ShapeScore.Sciccors.value + RoundScore.X.value,
  ("A", "Y"): ShapeScore.Rock.value + RoundScore.Y.value,
  ("A", "Z"): ShapeScore.Paper.value + RoundScore.Z.value,
  ("B", "X"): ShapeScore.Rock.value + RoundScore.X.value,
  ("B", "Y"): ShapeScore.Paper.value + RoundScore.Y.value,
  ("B", "Z"): ShapeScore.Sciccors.value + RoundScore.Z.value,
  ("C", "X"): ShapeScore.Paper.value + RoundScore.X.value,
  ("C", "Y"): ShapeScore.Sciccors.value + RoundScore.Y.value,
  ("C", "Z"): ShapeScore.Rock.value + RoundScore.Z.value
}

score = 0

with open("input.txt") as input:
  for line in input:
    opponent, outcome = line.rstrip().split(" ")
    score += results[(opponent, outcome)]

print(score)

sys.exit()