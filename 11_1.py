from utils import *

import numpy as np

lines = read_lines(day=11)

example = (
  "5483143223",
  "2745854711",
  "5264556173",
  "6141336146",
  "6357385478",
  "4167524645",
  "2176841721",
  "6882881134",
  "4846848554",
  "5283751526"
)

def dirs(x, y, w, h):
  # 1, 2, 3 # y-1
  # 4, n, 5 # y
  # 6, 7, 8 # y+1
  # # # # # #
  #x-1, x, x+1

  # y - 1
  if x - 1 >= 0 and y - 1 >= 0:
    yield x - 1, y - 1
  if y - 1 >= 0:
    yield x, y - 1
  if x + 1 < w and y - 1 >= 0:
    yield x + 1, y - 1
  # y
  if x - 1 >= 0:
    yield x - 1, y
  if x + 1 < w:
    yield x + 1, y
  # y + 1
  if x - 1 >= 0 and y + 1 < h:
    yield x - 1, y + 1
  if y + 1 < h:
    yield x, y + 1
  if x + 1 < w and y + 1 < h:
    yield x + 1, y + 1

def main(data):
  data = [tuple(line) for line in data]
  grid = np.array(data, dtype=int)

  count = 0
  for _ in range(100): # steps
    grid += 1

    stack, visited = list(zip(*(grid > 9).nonzero())), set()
    while stack:
      y, x = stack.pop()
      if (y, x) in visited:
        continue
      visited.add((y, x))
      
      for dx, dy in dirs(x, y, grid.shape[1], grid.shape[0]):
        grid[dy][dx] += 1
        if grid[dy][dx] > 9 and (dy, dx) not in visited:
          stack.append((dy, dx))

    grid[(_f := (grid > 9))] = 0
    count += _f.sum()
  print(count)
  
if __name__ == "__main__":
  main(lines) # answer: 1717