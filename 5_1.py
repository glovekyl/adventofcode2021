from utils import *

import numpy as np

lines = read_lines(day=5)

example = (
  "0,9 -> 5,9",
  "8,0 -> 0,8",
  "9,4 -> 3,4",
  "2,2 -> 2,1",
  "7,0 -> 7,4",
  "6,4 -> 2,0",
  "0,9 -> 2,9",
  "3,4 -> 1,4",
  "0,0 -> 8,8",
  "5,5 -> 8,2"
)

def main(data=None):
  grid = np.zeros((1000, 1000), dtype=int)
  for line in data:
    a, b = line.split(" -> ")
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))

    dx = ax - bx
    dy = ay - by

    if dx != 0 and dy != 0:
      continue

    x_step = np.sign(dx * -1)
    y_step = np.sign(dy * -1)
    while (ax, ay) != (bx, by):
      grid[ay, ax] += 1
      ax += x_step
      ay += y_step
    grid[ay, bx] += 1
  print((grid >= 2).sum())

if __name__ == "__main__":
  main(lines) # answer: 6267