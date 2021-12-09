from utils import *

import numpy as np

lines = read_lines(day=9)

example = (
  "2199943210",
  "3987894921",
  "9856789892",
  "8767896789",
  "9899965678"
)

box = lambda arr, y, x: arr[max(0,y-1):min(arr.shape[0],y+2), max(0,x-1):min(arr.shape[1],x+2)]

def dirs(x, y, w, h):
  if x - 1 >= 0:
    yield x - 1, y
  if x + 1 < w:
    yield x + 1, y
  if y - 1 >= 0:
    yield x, y - 1
  if y + 1 < h:
    yield x, y + 1

def main(data):
  grid = [tuple(map(int, x)) for x in data]
  # grid = np.array(*data, dtype=int)
  # grid = np.array(*data, dtype=int)

  total = 0
  h, w = len(grid), len(grid[0])
  for x in range(w):
    for y in range(h):
      z = grid[y][x]

      lowest = True
      for a, b in dirs(x, y, w, h):
        if grid[b][a] <= z:
          lowest = False
          break
      if lowest:
        total += z + 1
  print(total)

if __name__ == "__main__":
  main(lines) # answer: 570